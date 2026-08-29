## IPTV智能优化系统更新报告

生成时间: 2026-08-29T20:19:00.063575

### 📊 总体统计
- 总频道数: 131
- TVBox优化频道数: 131

### 📈 分级统计
- 中等延迟 (<800ms): 37 个频道 (延迟: 平均 535.0ms, 最低 304.1ms)
- 可接受延迟 (<2s): 60 个频道 (延迟: 平均 1248.4ms, 最低 802.2ms)
- unacceptable: 12 个频道 (延迟: 平均 3764.4ms, 最低 2177.0ms)
- 低延迟 (<300ms): 22 个频道 (延迟: 平均 243.3ms, 最低 196.4ms)

### 📁 频道分组
- : 131 个频道

### 🔗 协议统计
- HLS (m3u8): 108 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.3 KB)
- iptv_medium_latency.m3u (10.9 KB)
- iptv_high_latency.m3u (17.5 KB)
- iptv_optimized_combined.m3u (34.6 KB)
- tvbox_optimized.m3u (42.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 336.3 秒
