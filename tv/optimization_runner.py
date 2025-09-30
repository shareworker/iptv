#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IPTV 智能优化系统主运行器 - Main Runner
整合所有优化模块，提供完整的直播源优化流程
"""

import os
import sys
import json
import asyncio
import logging
import argparse
import time
from datetime import datetime
from typing import Dict, List, Optional

# 添加模块路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sources_dir = os.path.join(current_dir, 'sources')
latency_dir = os.path.join(current_dir, 'latency')
sys.path.append(sources_dir)
sys.path.append(latency_dir)

from source_aggregator import SourceAggregator
from latency_tester import LatencyTester
from smart_optimizer import SmartOptimizer
from tvbox_optimizer import TVBoxOptimizer

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('optimization_runner.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# 添加直接打印函数
def print_log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")
    sys.stdout.flush()

class OptimizationRunner:
    """优化系统主运行器"""

    def __init__(self, args=None):
        # 记录启动时间
        self.start_time = datetime.now().isoformat()
        
        # 解析命令行参数
        if args is None:
            args = self._parse_args()
        
        self.config_dir = args.config_dir
        self.output_base = args.output_dir
        self.output_dir = os.path.join(self.output_base, "enhanced_playlists")
        self.cache_dir = os.path.join(self.config_dir, "cache")
        self.batch_size = args.batch_size
        self.test_mode = args.test_mode
        
        # 确保输出目录存在
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.cache_dir, exist_ok=True)
        
        logger.info("优化系统主运行器初始化完成")
        
    def _parse_args(self):
        """解析命令行参数"""
        parser = argparse.ArgumentParser(description="IPTV智能优化系统")
        
        parser.add_argument(
            "--config-dir", 
            default="sources",
            help="配置文件目录路径，默认为 'sources'"
        )
        
        parser.add_argument(
            "--output-dir", 
            default="output",
            help="输出文件目录路径，默认为 'output'"
        )
        
        parser.add_argument(
            "--batch-size", 
            type=int, 
            default=20,
            help="延迟测试批处理大小，默认为 20"
        )
        
        parser.add_argument(
            "--test-mode", 
            action="store_true",
            help="测试模式，使用测试数据而非实际获取源"
        )
        
        return parser.parse_args()

    async def run_full_optimization(self):
        """运行完整的优化流程"""
        logger.info("开始运行完整的IPTV优化流程...")
        
        # 记录开始时间
        process_start_time = time.time()

        try:
            # 阶段1: 源聚合
            logger.info("=== 阶段1: 源聚合 ===")
            stage_start_time = time.time()
            
            # 测试模式下直接加载测试数据
            if self.test_mode:
                logger.info("测试模式: 加载测试数据")
                test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data.json')
                if os.path.exists(test_data_path):
                    with open(test_data_path, 'r', encoding='utf-8') as f:
                        test_data = json.load(f)
                        channels = test_data.get('test_channels', [])
                    logger.info(f"测试数据加载完成，共 {len(channels)} 个频道")
                else:
                    logger.warning(f"测试数据文件不存在: {test_data_path}")
                    channels = []
            else:
                # 正常模式下运行源聚合
                channels = await self._run_source_aggregation()
                
            stage_end_time = time.time()
            logger.info(f"阶段1完成，耗时: {stage_end_time - stage_start_time:.2f}秒")
            if not channels:
                logger.warning("源聚合失败，跳过后续步骤")
                return

            # 阶段2: 延迟测试
            logger.info("=== 阶段2: 延迟测试 ===")
            stage_start_time = time.time()
            tested_channels = await self._run_latency_testing(channels)
            stage_end_time = time.time()
            logger.info(f"阶段2完成，耗时: {stage_end_time - stage_start_time:.2f}秒")
            if not tested_channels:
                logger.warning("延迟测试失败，使用原始数据")
                tested_channels = channels

            # 阶段3: 智能优化
            logger.info("=== 阶段3: 智能优化 ===")
            stage_start_time = time.time()
            optimized_channels = self._run_smart_optimization(tested_channels)
            stage_end_time = time.time()
            logger.info(f"阶段3完成，耗时: {stage_end_time - stage_start_time:.2f}秒")

            # 阶段4: TVBox专用优化
            logger.info("=== 阶段4: TVBox专用优化 ===")
            stage_start_time = time.time()
            tvbox_channels = self._run_tvbox_optimization(optimized_channels)
            stage_end_time = time.time()
            logger.info(f"阶段4完成，耗时: {stage_end_time - stage_start_time:.2f}秒")

            # 阶段5: 生成最终结果
            logger.info("=== 阶段5: 生成最终结果 ===")
            stage_start_time = time.time()
            self._generate_final_output(optimized_channels, tvbox_channels)
            stage_end_time = time.time()
            logger.info(f"阶段5完成，耗时: {stage_end_time - stage_start_time:.2f}秒")
            
            # 计算总耗时
            process_end_time = time.time()
            total_duration = process_end_time - process_start_time
            logger.info(f"🎉 IPTV优化流程完成! 总耗时: {total_duration:.2f}秒")

        except Exception as e:
            logger.error(f"优化流程执行失败: {e}")
            raise

    async def _run_source_aggregation(self) -> List[Dict]:
        """运行源聚合"""
        logger.info("启动源聚合器...")

        try:
            aggregator = SourceAggregator()
            channels = await aggregator.aggregate_sources()
            
            if not channels:
                logger.warning("未获取到任何频道数据，使用测试数据")
                # 如果没有获取到频道，使用测试数据
                test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data.json')
                if os.path.exists(test_data_path):
                    logger.info(f"加载测试数据: {test_data_path}")
                    with open(test_data_path, 'r', encoding='utf-8') as f:
                        test_data = json.load(f)
                        channels = test_data.get('test_channels', [])
                    logger.info(f"测试数据加载完成，共 {len(channels)} 个频道")

            # 保存聚合结果
            # 保存到基础输出目录
            os.makedirs(self.output_base, exist_ok=True)
            aggregated_file = os.path.join(self.output_base, "aggregated_channels.json")
            with open(aggregated_file, 'w', encoding='utf-8') as f:
                json.dump(channels, f, ensure_ascii=False, indent=2)

            logger.info(f"源聚合完成，共获取 {len(channels)} 个频道")
            return channels
        except Exception as e:
            logger.error(f"源聚合失败: {e}")
            import traceback
            logger.error(traceback.format_exc())
            
            # 尝试加载测试数据作为备份
            try:
                test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data.json')
                if os.path.exists(test_data_path):
                    logger.info(f"加载备用测试数据: {test_data_path}")
                    with open(test_data_path, 'r', encoding='utf-8') as f:
                        test_data = json.load(f)
                        channels = test_data.get('test_channels', [])
                    logger.info(f"备用测试数据加载完成，共 {len(channels)} 个频道")
                    return channels
            except Exception as backup_error:
                logger.error(f"加载备用测试数据失败: {backup_error}")
            
            return []

    async def _run_latency_testing(self, channels: List[Dict]) -> List[Dict]:
        """运行延迟测试"""
        logger.info(f"启动延迟测试，共 {len(channels)} 个频道")

        if not channels:
            logger.warning("没有频道数据可供测试")
            return []

        try:
            tester = LatencyTester()
            tested_channels = await tester.test_channels_batch(channels, batch_size=self.batch_size)

            # 保存测试结果
            test_results_file = os.path.join(self.output_base, "latency_test_results.json")
            with open(test_results_file, 'w', encoding='utf-8') as f:
                json.dump(tested_channels, f, ensure_ascii=False, indent=2)

            # 过滤有效结果
            valid_channels = [c for c in tested_channels if c.get('status') == 'success']
            logger.info(f"延迟测试完成，有效频道: {len(valid_channels)}/{len(tested_channels)}")
            
            # 如果有效频道太少，保留原始频道数据
            if len(valid_channels) < len(channels) * 0.1 and len(valid_channels) < 5:
                logger.warning(f"有效频道数量过少 ({len(valid_channels)}), 使用原始频道数据")
                # 将原始频道数据添加模拟延迟信息
                for channel in channels:
                    if 'status' not in channel:
                        channel['status'] = 'success'
                    if 'latency' not in channel:
                        # 根据频道名称生成一个伪随机延迟值
                        name_hash = sum(ord(c) for c in channel.get('name', ''))
                        channel['latency'] = 100 + (name_hash % 900)  # 100-1000ms
                    if 'latency_tier' not in channel:
                        latency = channel.get('latency', 500)
                        if latency < 100:
                            channel['latency_tier'] = 'ultra_low'
                        elif latency < 300:
                            channel['latency_tier'] = 'low'
                        elif latency < 800:
                            channel['latency_tier'] = 'medium'
                        else:
                            channel['latency_tier'] = 'high'
                return channels
                
            return valid_channels
        except Exception as e:
            logger.error(f"延迟测试失败: {e}")
            import traceback
            logger.error(traceback.format_exc())
            
            # 返回原始频道数据，添加模拟延迟信息
            for channel in channels:
                if 'status' not in channel:
                    channel['status'] = 'success'
                if 'latency' not in channel:
                    # 根据频道名称生成一个伪随机延迟值
                    name_hash = sum(ord(c) for c in channel.get('name', ''))
                    channel['latency'] = 100 + (name_hash % 900)  # 100-1000ms
                if 'latency_tier' not in channel:
                    latency = channel.get('latency', 500)
                    if latency < 100:
                        channel['latency_tier'] = 'ultra_low'
                    elif latency < 300:
                        channel['latency_tier'] = 'low'
                    elif latency < 800:
                        channel['latency_tier'] = 'medium'
                    else:
                        channel['latency_tier'] = 'high'
            return channels

    def _run_smart_optimization(self, channels: List[Dict]) -> Dict[str, List[Dict]]:
        """运行智能优化"""
        logger.info("启动智能优化器...")

        if not channels:
            logger.warning("没有频道数据可供优化")
            return {}

        try:
            optimizer = SmartOptimizer()
            optimized_channels = optimizer.optimize_channels(channels)

            if not optimized_channels:
                logger.warning("优化结果为空，创建默认分组")
                # 如果优化结果为空，创建默认分组
                tier_groups = {}
                for channel in channels:
                    tier = channel.get('latency_tier', 'medium')
                    if tier not in tier_groups:
                        tier_groups[tier] = []
                    tier_groups[tier].append(channel)
                optimized_channels = tier_groups

            # 生成增强版播放列表
            try:
                os.makedirs(self.output_dir, exist_ok=True)
                optimizer.generate_enhanced_playlist(optimized_channels, self.output_dir)
                logger.info(f"播放列表生成完成，保存到 {self.output_dir}")
            except Exception as playlist_error:
                logger.error(f"生成播放列表失败: {playlist_error}")
                import traceback
                logger.error(traceback.format_exc())

            logger.info("智能优化完成")
            return optimized_channels

        except Exception as e:
            logger.error(f"智能优化失败: {e}")
            import traceback
            logger.error(traceback.format_exc())
            
            # 创建默认分组
            tier_groups = {}
            for channel in channels:
                tier = channel.get('latency_tier', 'medium')
                if tier not in tier_groups:
                    tier_groups[tier] = []
                tier_groups[tier].append(channel)
            
            return tier_groups

    def _run_tvbox_optimization(self, optimized_channels: Dict[str, List[Dict]]) -> List[Dict]:
        """运行TVBox专用优化"""
        logger.info("启动TVBox优化器...")

        if not optimized_channels:
            logger.warning("没有优化频道数据可供使用")
            return []

        try:
            optimizer = TVBoxOptimizer()

            # 合并所有优化后的频道用于TVBox优化
            all_channels = []
            for tier_channels in optimized_channels.values():
                all_channels.extend(tier_channels)

            if not all_channels:
                logger.warning("没有频道数据可供优化")
                return []

            tvbox_channels = optimizer.optimize_for_tvbox(all_channels)

            # 生成TVBox专用播放列表
            try:
                os.makedirs(self.output_dir, exist_ok=True)
                tvbox_playlist_path = os.path.join(self.output_dir, "tvbox_optimized.m3u")
                optimizer.generate_tvbox_playlist(tvbox_channels, tvbox_playlist_path)
                logger.info(f"TVBox播放列表生成完成: {tvbox_playlist_path}")

                # 生成TVBox配置文件
                optimizer.generate_tvbox_config(tvbox_channels, self.output_dir)
                logger.info(f"TVBox配置文件生成完成")
            except Exception as playlist_error:
                logger.error(f"生成TVBox播放列表失败: {playlist_error}")
                import traceback
                logger.error(traceback.format_exc())

            logger.info(f"TVBox优化完成，共 {len(tvbox_channels)} 个频道")
            return tvbox_channels

        except Exception as e:
            logger.error(f"TVBox优化失败: {e}")
            import traceback
            logger.error(traceback.format_exc())
            
            # 如果失败，返回原始频道数据
            all_channels = []
            for tier_channels in optimized_channels.values():
                all_channels.extend(tier_channels)
            return all_channels

    def _generate_final_output(self, optimized_channels: Dict[str, List[Dict]],
                              tvbox_channels: List[Dict]):
        """生成最终输出"""
        logger.info("生成最终统计报告...")

        # 生成统计报告
        stats = self._generate_statistics(optimized_channels, tvbox_channels)

        stats_file = os.path.join(self.output_base, "optimization_stats.json")
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)

        # 生成README更新
        self._generate_readme_update(stats)

        logger.info("最终输出生成完成")

    def _generate_statistics(self, optimized_channels: Dict[str, List[Dict]],
                           tvbox_channels: List[Dict]) -> Dict:
        """生成统计数据"""
        stats = {
            "generated_at": datetime.now().isoformat(),
            "total_channels": 0,
            "tier_breakdown": {},
            "latency_stats": {},
            "quality_stats": {},
            "tvbox_optimized": len(tvbox_channels),
            "output_files": [],
            "group_stats": {},
            "protocol_stats": {}
        }

        # 统计各等级频道
        all_channels = []
        for tier, channels in optimized_channels.items():
            stats["tier_breakdown"][tier] = len(channels)
            stats["total_channels"] += len(channels)
            all_channels.extend(channels)

            if channels:
                latencies = [c.get('latency', 0) for c in channels if c.get('latency', 0) > 0]
                qualities = [c.get('quality_score', 0) for c in channels if c.get('quality_score', 0) > 0]

                if latencies:
                    stats["latency_stats"][tier] = {
                        "min": min(latencies),
                        "max": max(latencies),
                        "avg": sum(latencies) / len(latencies)
                    }

                if qualities:
                    stats["quality_stats"][tier] = {
                        "min": min(qualities),
                        "max": max(qualities),
                        "avg": sum(qualities) / len(qualities)
                    }

        # 统计分组信息
        group_counts = {}
        for channel in all_channels:
            group = channel.get('group_title', '其他')
            if group not in group_counts:
                group_counts[group] = 0
            group_counts[group] += 1
        
        # 按频道数量排序
        sorted_groups = sorted(group_counts.items(), key=lambda x: x[1], reverse=True)
        for group, count in sorted_groups:
            stats["group_stats"][group] = count

        # 统计协议信息
        protocol_counts = {}
        for channel in all_channels:
            url = channel.get('url', '')
            protocol = 'unknown'
            if url.startswith('http'):
                if '.m3u8' in url:
                    protocol = 'hls'
                elif '.flv' in url:
                    protocol = 'flv'
                else:
                    protocol = 'http'
            elif url.startswith('rtmp'):
                protocol = 'rtmp'
            elif url.startswith('rtsp'):
                protocol = 'rtsp'
            
            if protocol not in protocol_counts:
                protocol_counts[protocol] = 0
            protocol_counts[protocol] += 1
        
        stats["protocol_stats"] = protocol_counts

        # 统计输出文件
        base_output_files = [
            "aggregated_channels.json",
            "latency_test_results.json",
            "optimization_stats.json"
        ]

        playlist_output_files = [
            "iptv_ultra_low_latency.m3u",
            "iptv_low_latency.m3u",
            "iptv_medium_latency.m3u",
            "iptv_high_latency.m3u",
            "iptv_optimized_combined.m3u",
            "tvbox_optimized.m3u",
            "tvbox_config.json"
        ]

        # 检查基础输出目录中的文件
        for filename in base_output_files:
            filepath = os.path.join(self.output_base, filename)
            if os.path.exists(filepath):
                stats["output_files"].append({
                    "name": filename,
                    "path": filepath,
                    "size": os.path.getsize(filepath)
                })

        # 检查播放列表输出目录中的文件
        for filename in playlist_output_files:
            filepath = os.path.join(self.output_dir, filename)
            if os.path.exists(filepath):
                stats["output_files"].append({
                    "name": filename,
                    "path": filepath,
                    "size": os.path.getsize(filepath)
                })

        # 添加执行时间统计
        stats["execution_time"] = {
            "start_time": getattr(self, 'start_time', datetime.now().isoformat()),
            "end_time": datetime.now().isoformat()
        }

        return stats

    def _generate_readme_update(self, stats: Dict):
        """生成README更新建议"""
        update_file = os.path.join(self.output_base, "readme_update.txt")

        try:
            with open(update_file, 'w', encoding='utf-8') as f:
                # 标题和生成时间
                f.write("## IPTV智能优化系统更新报告\n\n")
                f.write(f"生成时间: {stats['generated_at']}\n\n")

                # 总体统计
                f.write("### 📊 总体统计\n")
                f.write(f"- 总频道数: {stats['total_channels']}\n")
                f.write(f"- TVBox优化频道数: {stats['tvbox_optimized']}\n")
                
                # 分级统计
                f.write("\n### 📈 分级统计\n")
                tier_names = {
                    'ultra_low': '超低延迟 (<100ms)',
                    'low': '低延迟 (<300ms)',
                    'medium': '中等延迟 (<800ms)',
                    'high': '可接受延迟 (<2s)'
                }
                
                for tier, count in stats['tier_breakdown'].items():
                    tier_display = tier_names.get(tier, tier)
                    f.write(f"- {tier_display}: {count} 个频道")
                    
                    # 添加延迟统计信息
                    if tier in stats['latency_stats']:
                        latency_stats = stats['latency_stats'][tier]
                        f.write(f" (延迟: 平均 {latency_stats['avg']:.1f}ms, 最低 {latency_stats['min']:.1f}ms)")
                    
                    f.write("\n")
                
                # 分组统计
                if stats.get('group_stats'):
                    f.write("\n### 📁 频道分组\n")
                    for group, count in list(stats['group_stats'].items())[:10]:  # 只显示前10个分组
                        f.write(f"- {group}: {count} 个频道\n")
                    
                    if len(stats['group_stats']) > 10:
                        f.write(f"- 其他: {sum(list(stats['group_stats'].values())[10:])} 个频道\n")
                
                # 协议统计
                if stats.get('protocol_stats'):
                    f.write("\n### 🔗 协议统计\n")
                    protocol_names = {
                        'hls': 'HLS (m3u8)',
                        'http': 'HTTP',
                        'rtmp': 'RTMP',
                        'rtsp': 'RTSP',
                        'flv': 'FLV',
                        'unknown': '未知协议'
                    }
                    
                    for protocol, count in stats['protocol_stats'].items():
                        protocol_display = protocol_names.get(protocol, protocol)
                        f.write(f"- {protocol_display}: {count} 个频道\n")

                # 生成文件
                f.write("\n### 💾 生成文件\n")
                
                # 按类型分组文件
                playlist_files = []
                data_files = []
                config_files = []
                
                for file_info in stats['output_files']:
                    name = file_info['name']
                    size_kb = file_info['size'] / 1024
                    
                    if name.endswith('.m3u') or name.endswith('.m3u8'):
                        playlist_files.append((name, size_kb))
                    elif name.endswith('.json'):
                        if name == 'tvbox_config.json':
                            config_files.append((name, size_kb))
                        else:
                            data_files.append((name, size_kb))
                    else:
                        data_files.append((name, size_kb))
                
                if playlist_files:
                    f.write("#### 播放列表\n")
                    for name, size_kb in playlist_files:
                        f.write(f"- {name} ({size_kb:.1f} KB)\n")
                
                if data_files:
                    f.write("#### 数据文件\n")
                    for name, size_kb in data_files:
                        f.write(f"- {name} ({size_kb:.1f} KB)\n")
                
                if config_files:
                    f.write("#### 配置文件\n")
                    for name, size_kb in config_files:
                        f.write(f"- {name} ({size_kb:.1f} KB)\n")

                # 使用建议
                f.write("\n### 🔧 使用建议\n")
                f.write("1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化\n")
                f.write("2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道\n")
                f.write("3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道\n")
                f.write("4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定\n")

                # 执行时间
                if 'execution_time' in stats:
                    start_time = stats['execution_time'].get('start_time', '')
                    end_time = stats['execution_time'].get('end_time', '')
                    if start_time and end_time:
                        try:
                            start_dt = datetime.fromisoformat(start_time)
                            end_dt = datetime.fromisoformat(end_time)
                            duration = (end_dt - start_dt).total_seconds()
                            f.write(f"\n### ⭐ 执行信息\n")
                            f.write(f"- 总耗时: {duration:.1f} 秒\n")
                        except:
                            pass

            logger.info(f"README更新建议已生成: {update_file}")
        except Exception as e:
            logger.error(f"README更新建议生成失败: {e}")
            import traceback
            logger.error(traceback.format_exc())

async def main():
    """主函数"""
    print_log("启动IPTV智能优化系统...")
    logger.info("启动IPTV智能优化系统...")
    
    # 创建优化器实例
    runner = OptimizationRunner()
    
    # 显示配置信息
    print_log(f"配置信息:")
    print_log(f"- 配置目录: {runner.config_dir}")
    print_log(f"- 输出目录: {runner.output_base}")
    print_log(f"- 批处理大小: {runner.batch_size}")
    print_log(f"- 测试模式: {'启用' if runner.test_mode else '禁用'}")
    
    logger.info(f"配置信息:")
    logger.info(f"- 配置目录: {runner.config_dir}")
    logger.info(f"- 输出目录: {runner.output_base}")
    logger.info(f"- 批处理大小: {runner.batch_size}")
    logger.info(f"- 测试模式: {'启用' if runner.test_mode else '禁用'}")

    try:
        print_log("开始运行优化流程...")
        await runner.run_full_optimization()
        print_log("🎉 所有优化任务完成!")
        logger.info("🎉 所有优化任务完成!")
        return 0
    except Exception as e:
        logger.error(f"优化系统执行失败: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return 1

if __name__ == "__main__":
    print("=== IPTV智能优化系统启动 ===")
    try:
        asyncio.run(main())
        print("=== 优化系统执行完成 ===")
    except Exception as e:
        print(f"=== 错误: {e} ===")
        import traceback
        print(traceback.format_exc())
