## IPTV智能优化系统更新报告

生成时间: 2025-10-21T18:24:28.867940

### 📊 总体统计
- 总频道数: 153
- TVBox优化频道数: 153

### 📈 分级统计
- 中等延迟 (<800ms): 43 个频道 (延迟: 平均 499.5ms, 最低 329.5ms)
- 可接受延迟 (<2s): 72 个频道 (延迟: 平均 1393.2ms, 最低 805.1ms)
- unacceptable: 21 个频道 (延迟: 平均 3164.6ms, 最低 2091.2ms)
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 220.5ms, 最低 197.9ms)

### 📁 频道分组
- : 153 个频道

### 🔗 协议统计
- HLS (m3u8): 129 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (12.5 KB)
- iptv_high_latency.m3u (20.8 KB)
- iptv_optimized_combined.m3u (38.0 KB)
- tvbox_optimized.m3u (50.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 392.8 秒
