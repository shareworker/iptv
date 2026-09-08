## IPTV智能优化系统更新报告

生成时间: 2026-09-08T20:36:49.613309

### 📊 总体统计
- 总频道数: 128
- TVBox优化频道数: 128

### 📈 分级统计
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 216.2ms, 最低 173.4ms)
- 中等延迟 (<800ms): 40 个频道 (延迟: 平均 574.5ms, 最低 318.8ms)
- 可接受延迟 (<2s): 63 个频道 (延迟: 平均 1122.0ms, 最低 808.4ms)
- unacceptable: 6 个频道 (延迟: 平均 3266.6ms, 最低 2352.0ms)

### 📁 频道分组
- : 128 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 105 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.4 KB)
- iptv_medium_latency.m3u (12.0 KB)
- iptv_high_latency.m3u (18.3 KB)
- iptv_optimized_combined.m3u (35.5 KB)
- tvbox_optimized.m3u (41.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 315.5 秒
