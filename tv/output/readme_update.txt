## IPTV智能优化系统更新报告

生成时间: 2026-07-31T08:42:26.280025

### 📊 总体统计
- 总频道数: 131
- TVBox优化频道数: 131

### 📈 分级统计
- 低延迟 (<300ms): 26 个频道 (延迟: 平均 224.0ms, 最低 186.8ms)
- 中等延迟 (<800ms): 27 个频道 (延迟: 平均 549.7ms, 最低 310.1ms)
- 可接受延迟 (<2s): 68 个频道 (延迟: 平均 1203.3ms, 最低 808.0ms)
- unacceptable: 10 个频道 (延迟: 平均 3623.2ms, 最低 2072.6ms)

### 📁 频道分组
- : 131 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 108 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.7 KB)
- iptv_medium_latency.m3u (7.8 KB)
- iptv_high_latency.m3u (19.6 KB)
- iptv_optimized_combined.m3u (34.9 KB)
- tvbox_optimized.m3u (42.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 333.1 秒
