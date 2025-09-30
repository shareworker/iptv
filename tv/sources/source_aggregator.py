#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IPTV 源聚合器 - Source Aggregator
负责从多个源获取和聚合直播源数据
"""

import asyncio
import aiohttp
import json
import os
import time
import logging
from datetime import datetime, timedelta
from urllib.parse import urlparse
import re
from typing import Dict, List, Optional, Tuple
import hashlib

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('source_aggregator.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SourceAggregator:
    """IPTV源聚合器"""

    def __init__(self, config_path: str = None):
        if config_path is None:
            # 使用绝对路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(current_dir, 'source_config.json')
        self.config_path = config_path
        self.config = self._load_config()
        self.cache_dir = "cache"
        self._ensure_cache_dir()
        self.session: Optional[aiohttp.ClientSession] = None

    def _load_config(self) -> Dict:
        """加载配置文件"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"配置文件 {self.config_path} 不存在")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"配置文件格式错误: {e}")
            raise

    def _ensure_cache_dir(self):
        """确保缓存目录存在"""
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def _get_cache_path(self, url: str) -> str:
        """获取缓存文件路径"""
        url_hash = hashlib.md5(url.encode()).hexdigest()
        return os.path.join(self.cache_dir, f"{url_hash}.cache")

    def _is_cache_valid(self, cache_path: str) -> bool:
        """检查缓存是否有效"""
        if not os.path.exists(cache_path):
            return False

        cache_duration = self.config['settings']['cache_duration_hours']
        cache_time = os.path.getmtime(cache_path)
        expiry_time = cache_time + (cache_duration * 3600)

        return time.time() < expiry_time

    async def _fetch_source(self, source: Dict) -> Tuple[str, Optional[str]]:
        """异步获取单个源的数据"""
        url = source['url']
        name = source['name']

        logger.info(f"开始获取源: {name} ({url})")

        # 检查缓存
        cache_path = self._get_cache_path(url)
        if self._is_cache_valid(cache_path):
            logger.info(f"使用缓存数据: {name}")
            try:
                with open(cache_path, 'r', encoding='utf-8') as f:
                    return name, f.read()
            except Exception as e:
                logger.warning(f"读取缓存失败: {e}")

        # 从网络获取
        try:
            timeout = aiohttp.ClientTimeout(total=self.config['settings']['request_timeout'])
            async with self.session.get(url, timeout=timeout) as response:
                if response.status == 200:
                    content = await response.text()
                    logger.info(f"成功获取源: {name}, 内容长度: {len(content)}")

                    # 保存到缓存
                    try:
                        with open(cache_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                    except Exception as e:
                        logger.warning(f"保存缓存失败: {e}")

                    return name, content
                else:
                    logger.warning(f"获取源失败: {name}, 状态码: {response.status}")
                    return name, None

        except Exception as e:
            logger.error(f"获取源异常: {name}, 错误: {e}")
            return name, None

    def _parse_m3u_content(self, content: str) -> List[Dict]:
        """解析M3U格式内容"""
        channels = []
        lines = content.split('\n')
        current_channel = {}

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith('#EXTINF:'):
                # 解析EXTINF行
                current_channel = self._parse_extinf_line(line)
            elif line.startswith('http'):
                # 这是URL行
                if current_channel:
                    current_channel['url'] = line
                    channels.append(current_channel.copy())
                    current_channel = {}

        logger.info(f"解析得到 {len(channels)} 个频道")
        return channels

    def _parse_extinf_line(self, line: str) -> Dict:
        """解析EXTINF行"""
        channel = {
            'name': '',
            'tvg_id': '',
            'tvg_name': '',
            'tvg_logo': '',
            'group_title': '',
            'url': ''
        }

        # 提取频道名称
        name_match = re.search(r',(.+)$', line)
        if name_match:
            channel['name'] = name_match.group(1).strip()

        # 提取属性
        attrs = re.findall(r'(\w+)="([^"]*)"', line)
        for attr, value in attrs:
            if attr == 'tvg-id':
                channel['tvg_id'] = value
            elif attr == 'tvg-name':
                channel['tvg_name'] = value
            elif attr == 'tvg-logo':
                channel['tvg_logo'] = value
            elif attr == 'group-title':
                channel['group_title'] = value

        return channel

    def _merge_channels(self, all_channels: Dict[str, List[Dict]]) -> List[Dict]:
        """合并来自不同源的频道，去重并优化"""
        merged_channels = []
        channel_map = {}  # name -> channel

        for source_name, channels in all_channels.items():
            if not channels:
                continue

            for channel in channels:
                name = channel.get('name', '').strip()
                if not name:
                    continue

                # 标准化频道名称
                normalized_name = self._normalize_channel_name(name)

                if normalized_name in channel_map:
                    # 如果已存在，保留质量更好的源
                    existing = channel_map[normalized_name]
                    if self._compare_channel_quality(channel, existing) > 0:
                        channel_map[normalized_name] = channel
                else:
                    channel_map[normalized_name] = channel

        merged_channels = list(channel_map.values())
        logger.info(f"合并后剩余 {len(merged_channels)} 个频道")
        return merged_channels

    def _normalize_channel_name(self, name: str) -> str:
        """标准化频道名称"""
        # 移除常见后缀和特殊字符
        name = re.sub(r'[^\w\u4e00-\u9fff]', '', name)
        return name.lower()

    def _compare_channel_quality(self, new_channel: Dict, existing_channel: Dict) -> int:
        """比较两个频道的质量，返回正数表示新频道更好"""
        # 优先级比较
        new_priority = 0
        existing_priority = 0

        # 检查是否包含高清标识
        if '高清' in new_channel.get('name', '') or 'HD' in new_channel.get('name', ''):
            new_priority += 1
        if '高清' in existing_channel.get('name', '') or 'HD' in existing_channel.get('name', ''):
            existing_priority += 1

        # 检查URL质量
        if 'm3u8' in new_channel.get('url', ''):
            new_priority += 1
        if 'm3u8' in existing_channel.get('url', ''):
            existing_priority += 1

        return new_priority - existing_priority

    async def aggregate_sources(self) -> List[Dict]:
        """聚合所有源的频道数据"""
        logger.info("开始聚合直播源...")

        # 创建会话
        connector = aiohttp.TCPConnector(limit=self.config['settings']['max_concurrent_requests'])
        self.session = aiohttp.ClientSession(connector=connector)

        try:
            # 获取启用的源
            enabled_sources = [s for s in self.config['sources'] if s.get('enabled', True)]
            logger.info(f"发现 {len(enabled_sources)} 个启用源")

            # 并发获取所有源
            tasks = [self._fetch_source(source) for source in enabled_sources]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            # 处理结果
            all_channels = {}
            for result in results:
                if isinstance(result, Exception):
                    logger.error(f"任务异常: {result}")
                    continue

                source_name, content = result
                if content:
                    channels = self._parse_m3u_content(content)
                    all_channels[source_name] = channels

            # 合并频道
            merged_channels = self._merge_channels(all_channels)

            logger.info(f"聚合完成，共获取 {len(merged_channels)} 个频道")
            return merged_channels

        finally:
            if self.session:
                await self.session.close()

    def save_channels(self, channels: List[Dict], output_path: str):
        """保存频道列表到文件"""
        logger.info(f"保存频道列表到: {output_path}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('#EXTM3U\n')
            for channel in channels:
                f.write(f'#EXTINF:-1 tvg-name="{channel.get("tvg_name", "")}" ')
                f.write(f'tvg-logo="{channel.get("tvg_logo", "")}" ')
                f.write(f'group-title="{channel.get("group_title", "")}",')
                f.write(f'{channel.get("name", "")}\n')
                f.write(f'{channel.get("url", "")}\n')

        logger.info(f"成功保存 {len(channels)} 个频道")

async def main():
    """主函数"""
    aggregator = SourceAggregator()

    try:
        channels = await aggregator.aggregate_sources()

        # 保存结果
        output_dir = "../output"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "aggregated_channels.m3u")

        aggregator.save_channels(channels, output_path)

        logger.info("源聚合完成!")

    except Exception as e:
        logger.error(f"聚合过程出错: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
