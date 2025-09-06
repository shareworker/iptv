#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TVBox 专用优化器 - TVBox Optimizer
专门为TVBox播放器优化的直播源处理
"""

import json
import logging
import os
from typing import Dict, List, Optional
from urllib.parse import urlparse, parse_qs, urlencode
import re

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tvbox_optimizer.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TVBoxOptimizer:
    """TVBox专用优化器"""

    def __init__(self):
        self.tvbox_config = self._load_tvbox_config()

    def _load_tvbox_config(self) -> Dict:
        """加载TVBox专用配置"""
        return {
            "caching": {
                "ultra_low": {"network": 50, "live": 50},
                "low": {"network": 100, "live": 100},
                "medium": {"network": 200, "live": 200},
                "high": {"network": 500, "live": 500}
            },
            "protocols": {
                "preferred": ["http", "https", "rtmp", "rtsp"],
                "fallback": ["hls", "m3u8"]
            },
            "codecs": {
                "preferred": ["h264", "h265"],
                "fallback": ["av1", "vp9"]
            }
        }

    def optimize_for_tvbox(self, channels: List[Dict]) -> List[Dict]:
        """为TVBox优化频道列表"""
        logger.info(f"为TVBox优化 {len(channels)} 个频道")

        optimized_channels = []

        for channel in channels:
            optimized = self._optimize_single_channel(channel)
            if optimized:
                optimized_channels.append(optimized)

        logger.info(f"TVBox优化完成，剩余 {len(optimized_channels)} 个频道")
        return optimized_channels

    def _optimize_single_channel(self, channel: Dict) -> Optional[Dict]:
        """优化单个频道"""
        try:
            optimized = channel.copy()

            # 优化URL
            optimized['tvbox_url'] = self._optimize_url_for_tvbox(channel['url'])

            # 生成TVBox播放参数
            optimized['tvbox_params'] = self._generate_tvbox_params(channel)

            # 添加TVBox专用元数据
            optimized['tvbox_metadata'] = self._generate_tvbox_metadata(channel)

            # 验证URL可用性
            if not self._validate_url(optimized['tvbox_url']):
                logger.warning(f"跳过无效URL: {channel.get('name', 'Unknown')}")
                return None

            return optimized

        except Exception as e:
            logger.error(f"优化频道失败 {channel.get('name', 'Unknown')}: {e}")
            return None

    def _optimize_url_for_tvbox(self, url: str) -> str:
        """为TVBox优化URL"""
        parsed = urlparse(url)

        # TVBox 偏好的协议转换
        if parsed.scheme in ['rtsp', 'rtmp']:
            # 对于RTSP/RTMP，添加TCP传输参数
            if '?' in url:
                url += '&tcp'
            else:
                url += '?tcp'

        # 优化查询参数
        if parsed.query:
            params = parse_qs(parsed.query, keep_blank_values=True)

            # 移除可能导致问题的参数
            remove_params = ['referer', 'origin', 'user-agent']
            for param in remove_params:
                params.pop(param, None)

            # 添加TVBox友好的参数
            params['tvbox'] = ['1']

            # 重构URL
            new_query = urlencode(params, doseq=True)
            url = url.replace(parsed.query, new_query)

        # 处理IPv6地址格式
        if '[' in url and ']' in url:
            # TVBox IPv6格式兼容性处理
            pass

        return url

    def _generate_tvbox_params(self, channel: Dict) -> Dict:
        """生成TVBox播放参数"""
        latency_tier = channel.get('latency_tier', 'medium')
        latency = channel.get('latency', 500)

        # 基础缓存参数
        caching_config = self.tvbox_config['caching'].get(latency_tier,
                        self.tvbox_config['caching']['medium'])

        params = {
            "network_caching": caching_config['network'],
            "live_caching": caching_config['live'],
            "rtsp_tcp": True,
            "http_reconnect": True,
            "ipv4_only": channel.get('ip_type') == 'ipv4',
            "ipv6_only": channel.get('ip_type') == 'ipv6'
        }

        # 高级参数
        if latency < 200:
            # 低延迟模式
            params.update({
                "start_time": 0,
                "seekable": 0,
                "reconnect_delay": 1
            })
        elif latency > 1000:
            # 高延迟模式，增加缓冲
            params.update({
                "start_time": 5,
                "seekable": 1,
                "reconnect_delay": 5,
                "buffer_size": 1024000
            })

        # 协议特定参数
        url = channel.get('url', '')
        if 'rtsp' in url.lower():
            params.update({
                "rtsp_transport": "tcp",
                "rtsp_flags": "prefer_tcp"
            })
        elif 'rtmp' in url.lower():
            params.update({
                "rtmp_live": "live",
                "rtmp_buffer": caching_config['live']
            })

        return params

    def _generate_tvbox_metadata(self, channel: Dict) -> Dict:
        """生成TVBox专用元数据"""
        return {
            "channel_name": channel.get('name', ''),
            "group": channel.get('group_title', '其他'),
            "logo": channel.get('tvg_logo', ''),
            "latency": channel.get('latency', -1),
            "quality": channel.get('quality_score', 0),
            "tier": channel.get('latency_tier', 'unknown'),
            "codec": self._detect_codec(channel.get('url', '')),
            "resolution": self._estimate_resolution(channel.get('name', ''))
        }

    def _detect_codec(self, url: str) -> str:
        """检测视频编码"""
        url_lower = url.lower()

        if 'h265' in url_lower or 'hevc' in url_lower:
            return 'H265'
        elif 'h264' in url_lower or 'avc' in url_lower:
            return 'H264'
        elif 'av1' in url_lower:
            return 'AV1'
        elif 'vp9' in url_lower:
            return 'VP9'
        else:
            return 'Unknown'

    def _estimate_resolution(self, name: str) -> str:
        """估算分辨率"""
        name_upper = name.upper()

        if '4K' in name_upper:
            return '3840x2160'
        elif '超清' in name_upper or 'UHD' in name_upper:
            return '1920x1080'
        elif '高清' in name_upper or 'HD' in name_upper:
            return '1280x720'
        else:
            return 'Unknown'

    def _validate_url(self, url: str) -> bool:
        """验证URL格式"""
        try:
            parsed = urlparse(url)
            return bool(parsed.scheme and parsed.netloc)
        except:
            return False

    def generate_tvbox_playlist(self, channels: List[Dict], output_path: str):
        """生成TVBox专用播放列表"""
        logger.info(f"生成TVBox播放列表: {output_path}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('#EXTM3U\n')
            f.write('#PLAYLIST:TVBox Optimized IPTV\n')
            f.write('#GENERATED:TVBox Optimizer\n')
            f.write('#DESCRIPTION:专为TVBox优化的直播源，包含智能缓存和播放参数\n\n')

            for channel in channels:
                self._write_tvbox_channel(f, channel)

        logger.info(f"TVBox播放列表生成完成，共 {len(channels)} 个频道")

    def _write_tvbox_channel(self, file, channel: Dict):
        """写入TVBox格式的频道"""
        name = channel.get('name', 'Unknown')
        url = channel.get('tvbox_url', channel.get('url', ''))
        logo = channel.get('tvg_logo', '')
        group = channel.get('group_title', '其他')

        # TVBox 扩展的EXTINF格式
        extinf = f'#EXTINF:-1'

        # 添加标准属性
        if logo:
            extinf += f' tvg-logo="{logo}"'
        if group:
            extinf += f' group-title="{group}"'

        # 添加TVBox专用属性
        metadata = channel.get('tvbox_metadata', {})
        extinf += f' tvbox-latency="{metadata.get("latency", -1)}"'
        extinf += f' tvbox-quality="{metadata.get("quality", 0)}"'
        extinf += f' tvbox-tier="{metadata.get("tier", "unknown")}"'

        # 添加播放参数
        params = channel.get('tvbox_params', {})
        if params:
            param_str = json.dumps(params, separators=(',', ':'))
            extinf += f' tvbox-params="{param_str}"'

        file.write(f'{extinf},{name}\n')
        file.write(f'{url}\n\n')

    def generate_tvbox_config(self, channels: List[Dict], output_dir: str):
        """生成TVBox配置文件"""
        config_path = os.path.join(output_dir, 'tvbox_config.json')

        # 按频道类型分组
        grouped_channels = {}
        for channel in channels:
            group = channel.get('group_title', '其他')
            if group not in grouped_channels:
                grouped_channels[group] = []
            grouped_channels[group].append(channel)

        # 生成配置
        config = {
            "name": "智能优化的IPTV直播源",
            "version": "1.0.0",
            "description": "专为TVBox优化的直播源，包含延迟优化和智能缓存",
            "groups": {},
            "settings": {
                "default_latency_tier": "medium",
                "auto_switch_backup": True,
                "quality_preference": "high"
            }
        }

        # 添加分组信息
        for group_name, group_channels in grouped_channels.items():
            config["groups"][group_name] = {
                "count": len(group_channels),
                "avg_latency": sum(c.get('latency', 0) for c in group_channels) / len(group_channels),
                "best_tier": self._get_group_best_tier(group_channels)
            }

        # 保存配置
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

        logger.info(f"TVBox配置文件生成: {config_path}")

    def _get_group_best_tier(self, channels: List[Dict]) -> str:
        """获取分组最佳延迟等级"""
        tiers = [c.get('latency_tier', 'high') for c in channels]
        tier_priority = {'ultra_low': 1, 'low': 2, 'medium': 3, 'high': 4}

        best_tier = min(tiers, key=lambda x: tier_priority.get(x, 4))
        return best_tier

def main():
    """主函数 - 测试用例"""
    optimizer = TVBoxOptimizer()

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
        }
    ]

    # 优化频道
    optimized = optimizer.optimize_for_tvbox(test_channels)

    # 生成播放列表
    output_dir = "../output/enhanced_playlists"
    os.makedirs(output_dir, exist_ok=True)

    optimizer.generate_tvbox_playlist(optimized,
                                    os.path.join(output_dir, 'tvbox_optimized.m3u'))

    # 生成配置文件
    optimizer.generate_tvbox_config(optimized, output_dir)

    logger.info("TVBox优化测试完成!")

if __name__ == "__main__":
    main()
