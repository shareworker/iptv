## IPTV智能优化系统更新报告

生成时间: 2026-09-03T20:25:41.487879

### 📊 总体统计
- 总频道数: 119
- TVBox优化频道数: 119

### 📈 分级统计
- 中等延迟 (<800ms): 29 个频道 (延迟: 平均 587.7ms, 最低 356.3ms)
- 可接受延迟 (<2s): 74 个频道 (延迟: 平均 1302.6ms, 最低 849.9ms)
- unacceptable: 2 个频道 (延迟: 平均 2365.9ms, 最低 2278.0ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 223.8ms, 最低 199.1ms)

### 📁 频道分组
- : 119 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 96 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.9 KB)
- iptv_medium_latency.m3u (8.6 KB)
- iptv_high_latency.m3u (21.6 KB)
- iptv_optimized_combined.m3u (33.9 KB)
- tvbox_optimized.m3u (39.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (206.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 355.1 秒
