## IPTV智能优化系统更新报告

生成时间: 2025-12-09T06:27:50.491257

### 📊 总体统计
- 总频道数: 162
- TVBox优化频道数: 162

### 📈 分级统计
- 可接受延迟 (<2s): 62 个频道 (延迟: 平均 1273.7ms, 最低 811.8ms)
- 中等延迟 (<800ms): 65 个频道 (延迟: 平均 592.0ms, 最低 301.3ms)
- unacceptable: 21 个频道 (延迟: 平均 2770.5ms, 最低 2003.3ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 221.5ms, 最低 197.4ms)

### 📁 频道分组
- : 162 个频道

### 🔗 协议统计
- FLV: 2 个频道
- HLS (m3u8): 138 个频道
- HTTP: 22 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.9 KB)
- iptv_medium_latency.m3u (18.7 KB)
- iptv_high_latency.m3u (18.7 KB)
- iptv_optimized_combined.m3u (41.1 KB)
- tvbox_optimized.m3u (52.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 378.0 秒
