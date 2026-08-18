## IPTV智能优化系统更新报告

生成时间: 2026-08-18T06:33:48.818023

### 📊 总体统计
- 总频道数: 130
- TVBox优化频道数: 130

### 📈 分级统计
- 中等延迟 (<800ms): 46 个频道 (延迟: 平均 545.8ms, 最低 316.1ms)
- unacceptable: 11 个频道 (延迟: 平均 4511.5ms, 最低 2005.4ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1292.2ms, 最低 816.0ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 228.0ms, 最低 199.0ms)

### 📁 频道分组
- : 130 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 107 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.9 KB)
- iptv_medium_latency.m3u (13.5 KB)
- iptv_high_latency.m3u (17.2 KB)
- iptv_optimized_combined.m3u (34.5 KB)
- tvbox_optimized.m3u (41.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 337.7 秒
