## IPTV智能优化系统更新报告

生成时间: 2025-10-17T18:22:50.035526

### 📊 总体统计
- 总频道数: 116
- TVBox优化频道数: 116

### 📈 分级统计
- 中等延迟 (<800ms): 25 个频道 (延迟: 平均 544.8ms, 最低 308.2ms)
- 可接受延迟 (<2s): 42 个频道 (延迟: 平均 1243.1ms, 最低 812.1ms)
- unacceptable: 34 个频道 (延迟: 平均 3756.0ms, 最低 2011.3ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 223.6ms, 最低 197.6ms)

### 📁 频道分组
- : 116 个频道

### 🔗 协议统计
- HLS (m3u8): 92 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (7.3 KB)
- iptv_high_latency.m3u (12.3 KB)
- iptv_optimized_combined.m3u (23.6 KB)
- tvbox_optimized.m3u (38.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (205.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 388.9 秒
