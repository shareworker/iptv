#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IPTV 延迟测试器 - Latency Tester
负责测试直播源的延迟和质量指标
"""

import asyncio
import aiohttp
import os
import time
import socket
import json
import logging
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse
import ipaddress
import threading
from concurrent.futures import ThreadPoolExecutor
import statistics

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('latency_tester.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LatencyTester:
    """延迟测试器"""

    def __init__(self, config_path: str = None):
        if config_path is None:
            # 使用绝对路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(current_dir)
            config_path = os.path.join(parent_dir, 'sources', 'source_config.json')
        self.config = self._load_config(config_path)
        self.session: Optional[aiohttp.ClientSession] = None
        self.executor = ThreadPoolExecutor(max_workers=20)

    def _load_config(self, config_path: str) -> Dict:
        """加载配置"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"加载配置失败: {e}")
            return {}

    async def test_channel_latency(self, channel: Dict) -> Dict:
        """测试单个频道的延迟"""
        url = channel.get('url', '')
        if not url:
            return {**channel, 'latency': -1, 'status': 'invalid_url'}

        try:
            # 解析URL
            parsed_url = urlparse(url)
            hostname = parsed_url.hostname
            port = parsed_url.port or (443 if parsed_url.scheme == 'https' else 80)

            # DNS解析时间测试
            dns_start = time.time()
            try:
                ip_info = await self._resolve_hostname(hostname)
                dns_latency = (time.time() - dns_start) * 1000
            except Exception as e:
                logger.warning(f"DNS解析失败 {hostname}: {e}")
                return {**channel, 'latency': -1, 'status': 'dns_failed'}

            # TCP连接测试
            tcp_start = time.time()
            try:
                tcp_latency = await self._test_tcp_connection(ip_info['ip'], port)
                tcp_time = (time.time() - tcp_start) * 1000
            except Exception as e:
                logger.warning(f"TCP连接失败 {ip_info['ip']}:{port}: {e}")
                return {**channel, 'latency': -1, 'status': 'tcp_failed'}

            # HTTP请求测试
            http_start = time.time()
            try:
                http_latency, status_code = await self._test_http_request(url)
                http_time = (time.time() - http_start) * 1000
            except Exception as e:
                logger.warning(f"HTTP请求失败 {url}: {e}")
                return {**channel, 'latency': -1, 'status': 'http_failed'}

            # 计算总延迟
            total_latency = dns_latency + tcp_latency + http_latency

            # 计算质量评分
            quality_score = self._calculate_quality_score(
                total_latency, status_code, ip_info
            )

            result = {
                **channel,
                'latency': round(total_latency, 2),
                'dns_latency': round(dns_latency, 2),
                'tcp_latency': round(tcp_latency, 2),
                'http_latency': round(http_latency, 2),
                'status': 'success',
                'status_code': status_code,
                'ip': ip_info['ip'],
                'ip_type': ip_info['type'],
                'quality_score': quality_score,
                'latency_tier': self._get_latency_tier(total_latency)
            }
            logger.info(
                f"测试频道完成: name={channel.get('name','')}, latency={total_latency:.2f}ms, "
                f"dns={dns_latency:.2f}ms, tcp={tcp_latency:.2f}ms, http={http_latency:.2f}ms, "
                f"tier={result['latency_tier']}, status={status_code}"
            )
            return result

        except Exception as e:
            logger.error(f"测试频道延迟异常: {e}")
            return {**channel, 'latency': -1, 'status': 'error', 'error': str(e)}

    async def _resolve_hostname(self, hostname: str) -> Dict:
        """DNS解析主机名"""
        loop = asyncio.get_event_loop()

        # 首先尝试IPv6
        try:
            result = await loop.getaddrinfo(hostname, None, socket.AF_INET6)
            if result:
                ip = result[0][4][0]
                return {'ip': ip, 'type': 'ipv6'}
        except:
            pass

        # IPv4解析
        try:
            result = await loop.getaddrinfo(hostname, None, socket.AF_INET)
            if result:
                ip = result[0][4][0]
                return {'ip': ip, 'type': 'ipv4'}
        except Exception as e:
            raise Exception(f"DNS解析失败: {e}")

        raise Exception("无法解析主机名")

    async def _test_tcp_connection(self, ip: str, port: int) -> float:
        """测试TCP连接延迟"""
        loop = asyncio.get_event_loop()

        def tcp_connect():
            sock = socket.socket(socket.AF_INET6 if ':' in ip else socket.AF_INET,
                               socket.SOCK_STREAM)
            sock.settimeout(5)
            start_time = time.time()
            sock.connect((ip, port))
            latency = (time.time() - start_time) * 1000
            sock.close()
            return latency

        try:
            latency = await loop.run_in_executor(self.executor, tcp_connect)
            return latency
        except Exception as e:
            raise Exception(f"TCP连接失败: {e}")

    async def _test_http_request(self, url: str) -> Tuple[float, int]:
        """测试HTTP请求延迟"""
        timeout = aiohttp.ClientTimeout(total=10, connect=5)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        try:
            async with self.session.head(url, timeout=timeout, headers=headers) as response:
                return 0, response.status
        except Exception:
            # 如果HEAD请求失败，尝试GET请求（只获取少量数据）
            try:
                async with self.session.get(url, timeout=timeout, headers=headers) as response:
                    return 0, response.status
            except Exception as e:
                raise Exception(f"HTTP请求失败: {e}")

    def _calculate_quality_score(self, latency: float, status_code: int, ip_info: Dict) -> float:
        """计算质量评分"""
        score = 100.0

        # 延迟评分
        if latency < 100:
            score += 20
        elif latency < 300:
            score += 15
        elif latency < 800:
            score += 10
        elif latency < 2000:
            score += 5

        # HTTP状态码评分
        if status_code == 200:
            score += 20
        elif status_code in [301, 302]:
            score += 15
        else:
            score -= 20

        # IP类型评分（IPv6优先）
        if ip_info.get('type') == 'ipv6':
            score += 10

        # 确保评分在合理范围内
        return max(0, min(100, score))

    def _get_latency_tier(self, latency: float) -> str:
        """获取延迟等级"""
        tiers = self.config.get('latency_tiers', {})

        for tier_name, tier_config in tiers.items():
            if latency <= tier_config.get('max_latency', 9999):
                return tier_name

        return 'unacceptable'

    async def test_channels_batch(self, channels: List[Dict], batch_size: int = 10) -> List[Dict]:
        """批量测试频道延迟"""
        logger.info(f"开始批量测试 {len(channels)} 个频道，批次大小: {batch_size}")

        # 创建会话
        connector = aiohttp.TCPConnector(limit=batch_size)
        self.session = aiohttp.ClientSession(connector=connector)

        try:
            results = []
            total_batches = (len(channels) + batch_size - 1) // batch_size

            for i in range(0, len(channels), batch_size):
                batch = channels[i:i + batch_size]
                batch_num = i // batch_size + 1

                logger.info(f"处理第 {batch_num}/{total_batches} 批次")

                # 并发测试当前批次
                tasks = [self.test_channel_latency(channel) for channel in batch]
                batch_results = await asyncio.gather(*tasks, return_exceptions=True)

                # 处理结果
                for j, result in enumerate(batch_results):
                    if isinstance(result, Exception):
                        logger.error(f"批次 {batch_num} 频道 {j} 测试异常: {result}")
                        # 返回原始频道数据，标记为失败
                        failed_channel = batch[j].copy()
                        failed_channel.update({
                            'latency': -1,
                            'status': 'batch_error',
                            'error': str(result)
                        })
                        results.append(failed_channel)
                    else:
                        results.append(result)

                # 批次间暂停，避免过于频繁的请求
                if batch_num < total_batches:
                    await asyncio.sleep(1)

            logger.info(f"批量测试完成，共测试 {len(results)} 个频道")
            return results

        finally:
            if self.session:
                await self.session.close()

    def filter_by_latency_tier(self, channels: List[Dict], max_tier: str = 'medium') -> List[Dict]:
        """按延迟等级过滤频道"""
        tier_priority = {
            'ultra_low': 1,
            'low': 2,
            'medium': 3,
            'high': 4,
            'unacceptable': 5
        }

        max_priority = tier_priority.get(max_tier, 4)

        filtered = []
        for channel in channels:
            tier = channel.get('latency_tier', 'unacceptable')
            priority = tier_priority.get(tier, 5)

            if priority <= max_priority:
                filtered.append(channel)

        logger.info(f"延迟过滤完成，保留 {len(filtered)}/{len(channels)} 个频道")
        return filtered

    def sort_by_quality(self, channels: List[Dict]) -> List[Dict]:
        """按质量评分排序"""
        return sorted(channels, key=lambda x: (
            -x.get('quality_score', 0),  # 质量评分降序
            x.get('latency', 9999)       # 延迟升序
        ))

def save_test_results(results: List[Dict], output_path: str):
    """保存测试结果"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info(f"测试结果已保存到: {output_path}")

async def main():
    """主函数 - 测试用例"""
    tester = LatencyTester()

    # 测试频道示例
    test_channels = [
        {
            'name': 'CCTV-1',
            'url': 'http://[2409:8087:8:21::18]:6610/otttv.bj.chinamobile.com/PLTV/88888888/224/3221226895/1.m3u8'
        },
        {
            'name': 'CCTV-2',
            'url': 'http://liveop.cctv.cn/hls/CCTV28bee868714f04ea2af79947bb9b46fc3H/playlist.m3u8'
        }
    ]

    try:
        results = await tester.test_channels_batch(test_channels, batch_size=2)

        # 保存结果
        save_test_results(results, 'latency_test_results.json')

        # 按质量排序
        sorted_results = tester.sort_by_quality([r for r in results if r.get('status') == 'success'])

        logger.info("延迟测试完成!")
        for result in sorted_results[:5]:  # 显示前5个
            logger.info(
                f"TOP: {result.get('name','')} latency={result.get('latency',-1):.2f}ms "
                f"tier={result.get('latency_tier','')} quality={result.get('quality_score',0):.1f}"
            )
    except Exception as e:
        logger.error(f"测试过程出错: {e}")

if __name__ == "__main__":
    asyncio.run(main())
