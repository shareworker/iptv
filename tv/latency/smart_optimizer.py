#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IPTV 智能优化器 - Smart Optimizer
负责智能排序、优化和生成增强版播放列表
"""

import json
import logging
import os
from typing import Dict, List, Optional
from datetime import datetime
import re
from urllib.parse import urlparse

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('smart_optimizer.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SmartOptimizer:
    """智能优化器"""

    def __init__(self, config_path: str = None):
        if config_path is None:
            # 使用绝对路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(current_dir)
            config_path = os.path.join(parent_dir, 'sources', 'source_config.json')
        self.config = self._load_config(config_path)

    def _load_config(self, config_path: str) -> Dict:
        """加载配置"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"加载配置失败: {e}")
            return {}

    def optimize_channels(self, channels: List[Dict]) -> Dict[str, List[Dict]]:
        """智能优化频道，返回分层的优化结果"""
        logger.info(f"开始优化 {len(channels)} 个频道")

        # 过滤有效频道
        valid_channels = [c for c in channels if c.get('status') == 'success' and c.get('latency', -1) > 0]

        if not valid_channels:
            logger.warning("没有有效的频道数据")
            return {}

        # 按延迟等级分组
        tiered_channels = self._group_by_latency_tier(valid_channels)

        # 每个等级内按质量排序
        for tier, channels_list in tiered_channels.items():
            tiered_channels[tier] = self._sort_channels_by_quality(channels_list)

        # 生成优化后的播放列表
        optimized_playlists = {}
        for tier, channels_list in tiered_channels.items():
            optimized_playlists[tier] = self._apply_tvbox_optimizations(channels_list)

        logger.info("频道优化完成")
        return optimized_playlists

    def _group_by_latency_tier(self, channels: List[Dict]) -> Dict[str, List[Dict]]:
        """按延迟等级分组"""
        tiers = {}

        for channel in channels:
            tier = channel.get('latency_tier', 'unacceptable')
            if tier not in tiers:
                tiers[tier] = []
            tiers[tier].append(channel)

        # 记录分组统计
        for tier, channels_list in tiers.items():
            logger.info(f"{tier} 等级: {len(channels_list)} 个频道")

        return tiers

    def _sort_channels_by_quality(self, channels: List[Dict]) -> List[Dict]:
        """按质量排序频道"""
        return sorted(channels, key=lambda x: (
            -x.get('quality_score', 0),  # 质量评分降序
            x.get('latency', 9999),      # 延迟升序
            -self._get_channel_priority(x)  # 频道优先级降序
        ))

    def _get_channel_priority(self, channel: Dict) -> int:
        """获取频道优先级"""
        name = channel.get('name', '').upper()
        priority = 0

        # 央视频道最高优先级
        if 'CCTV' in name:
            priority += 100
            # 主要频道优先级更高
            if any(num in name for num in ['1', '2', '3', '4', '5', '6', '7', '8']):
                priority += 20

        # 卫视频道中等优先级
        elif any(prov in name for prov in ['湖南', '浙江', '江苏', '东方', '北京', '深圳']):
            priority += 50

        # 高清频道加分
        if '高清' in name or 'HD' in name or '4K' in name:
            priority += 10

        return priority

    def _apply_tvbox_optimizations(self, channels: List[Dict]) -> List[Dict]:
        """应用TVBox专用优化"""
        optimized = []

        for channel in channels:
            optimized_channel = channel.copy()

            # 添加TVBox优化参数
            optimized_channel['tvbox_params'] = self._generate_tvbox_params(channel)

            # 优化URL格式
            optimized_channel['optimized_url'] = self._optimize_url(channel['url'])

            # 添加备用源（如果有的话）
            optimized_channel['backup_urls'] = self._find_backup_sources(channel, channels)

            optimized.append(optimized_channel)

        return optimized

    def _generate_tvbox_params(self, channel: Dict) -> str:
        """生成TVBox播放参数"""
        latency = channel.get('latency', 9999)
        params = []

        # 根据延迟调整缓存参数
        if latency < 100:
            # 超低延迟，使用最小缓存
            params.extend(['--network-caching=50', '--live-caching=50'])
        elif latency < 300:
            # 低延迟
            params.extend(['--network-caching=100', '--live-caching=100'])
        elif latency < 800:
            # 中等延迟
            params.extend(['--network-caching=200', '--live-caching=200'])
        else:
            # 高延迟，使用较大缓存保证流畅
            params.extend(['--network-caching=500', '--live-caching=500'])

        # 添加通用TVBox参数
        params.extend([
            '--rtsp-tcp',
            '--http-reconnect',
            '--ipv4-only'
        ])

        # IPv6源特殊处理
        if channel.get('ip_type') == 'ipv6':
            params.append('--ipv6-only')

        return ' '.join(params)

    def _optimize_url(self, url: str) -> str:
        """优化URL格式"""
        # 移除不必要的参数
        if '?' in url:
            base_url, params = url.split('?', 1)
            # 保留重要的参数
            important_params = []
            for param in params.split('&'):
                if any(key in param.lower() for key in ['auth', 'token', 'sign', 'key']):
                    important_params.append(param)

            if important_params:
                url = base_url + '?' + '&'.join(important_params)

        return url

    def _find_backup_sources(self, target_channel: Dict, all_channels: List[Dict]) -> List[str]:
        """为目标频道查找备用源"""
        backups = []
        target_name = self._normalize_channel_name(target_channel.get('name', ''))

        for channel in all_channels:
            if channel['url'] == target_channel['url']:
                continue

            channel_name = self._normalize_channel_name(channel.get('name', ''))
            if channel_name == target_name:
                # 相似名称的频道作为备用
                latency_diff = abs(channel.get('latency', 9999) - target_channel.get('latency', 9999))
                if latency_diff < 500:  # 延迟差异在500ms以内
                    backups.append(channel['url'])

                    if len(backups) >= 2:  # 最多2个备用源
                        break

        return backups

    def _normalize_channel_name(self, name: str) -> str:
        """标准化频道名称用于匹配"""
        # 移除特殊字符和常见后缀
        name = re.sub(r'[^\w\u4e00-\u9fff]', '', name)
        name = re.sub(r'(高清|HD|超清|4K|直播|卫视|频道)', '', name)
        return name.lower().strip()

    def generate_enhanced_playlist(self, optimized_channels: Dict[str, List[Dict]],
                                 output_dir: str = "../output/enhanced_playlists"):
        """生成增强版播放列表"""
        os.makedirs(output_dir, exist_ok=True)

        # 为每个延迟等级生成播放列表
        for tier, channels in optimized_channels.items():
            self._generate_tier_playlist(tier, channels, output_dir)

        # 生成综合最佳播放列表
        self._generate_combined_playlist(optimized_channels, output_dir)

        logger.info("增强版播放列表生成完成")

    def _generate_tier_playlist(self, tier: str, channels: List[Dict], output_dir: str):
        """生成特定等级的播放列表"""
        filename = f"iptv_{tier}_latency.m3u"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('#EXTM3U\n')
            f.write(f'#PLAYLIST:{tier.upper()} LATENCY CHANNELS\n')
            f.write(f'#GENERATED:{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            f.write('#TVBOX-OPTIMIZED\n\n')

            for channel in channels[:500]:  # 每个等级最多500个频道
                self._write_channel_to_playlist(f, channel, tier)

        logger.info(f"生成 {tier} 等级播放列表: {filename}")

    def _generate_combined_playlist(self, optimized_channels: Dict[str, List[Dict]], output_dir: str):
        """生成综合最佳播放列表"""
        combined_channels = []

        # 按优先级合并各等级的频道
        tier_priority = ['ultra_low', 'low', 'medium', 'high']
        for tier in tier_priority:
            if tier in optimized_channels:
                # 每个等级取前100个最佳频道
                combined_channels.extend(optimized_channels[tier][:100])

        # 去重
        seen_urls = set()
        unique_channels = []
        for channel in combined_channels:
            url = channel.get('optimized_url', channel.get('url', ''))
            if url not in seen_urls:
                seen_urls.add(url)
                unique_channels.append(channel)

        # 生成综合播放列表
        filename = "iptv_optimized_combined.m3u"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('#EXTM3U\n')
            f.write('#PLAYLIST:OPTIMIZED COMBINED\n')
            f.write(f'#GENERATED:{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            f.write('#TVBOX-OPTIMIZED\n\n')

            for channel in unique_channels:
                self._write_channel_to_playlist(f, channel, 'combined')

        logger.info(f"生成综合播放列表: {filename} ({len(unique_channels)} 个频道)")

    def _write_channel_to_playlist(self, file, channel: Dict, tier: str):
        """将频道写入播放列表"""
        name = channel.get('name', 'Unknown')
        url = channel.get('optimized_url', channel.get('url', ''))
        logo = channel.get('tvg_logo', '')
        group = channel.get('group_title', '其他')

        # TVBox 专用EXTINF格式
        extinf = f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}" group-title="{group}"'

        # 添加延迟和质量信息
        latency = channel.get('latency', -1)
        quality = channel.get('quality_score', 0)
        extinf += f' latency="{latency:.0f}ms" quality="{quality:.1f}"'

        # 添加TVBox参数
        tvbox_params = channel.get('tvbox_params', '')
        if tvbox_params:
            extinf += f' tvbox-params="{tvbox_params}"'

        file.write(f'{extinf},{name}\n')
        file.write(f'{url}\n')

        # 添加备用源注释
        backup_urls = channel.get('backup_urls', [])
        if backup_urls:
            file.write(f'#BACKUP-SOURCES:{len(backup_urls)}\n')
            for backup_url in backup_urls:
                file.write(f'#BACKUP:{backup_url}\n')

        file.write('\n')

def main():
    """主函数 - 用于测试"""
    optimizer = SmartOptimizer()

    # 模拟测试数据
    test_channels = [
        {
            'name': 'CCTV-1 综合',
            'url': 'http://example.com/cctv1.m3u8',
            'latency': 85.5,
            'latency_tier': 'ultra_low',
            'quality_score': 95.0,
            'tvg_logo': 'http://example.com/logo.png',
            'group_title': '央视',
            'ip_type': 'ipv4'
        },
        {
            'name': '湖南卫视',
            'url': 'http://example.com/hunan.m3u8',
            'latency': 156.2,
            'latency_tier': 'low',
            'quality_score': 88.5,
            'tvg_logo': 'http://example.com/hunan.png',
            'group_title': '卫视',
            'ip_type': 'ipv6'
        }
    ]

    # 执行优化
    optimized = optimizer.optimize_channels(test_channels)

    # 生成播放列表
    optimizer.generate_enhanced_playlist(optimized)

    logger.info("智能优化测试完成!")

if __name__ == "__main__":
    main()
