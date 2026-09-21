## IPTV智能优化系统更新报告

生成时间: 2026-09-21T11:41:31.732679

### 📊 总体统计
- 总频道数: 114
- TVBox优化频道数: 114

### 📈 分级统计
- 中等延迟 (<800ms): 24 个频道 (延迟: 平均 557.1ms, 最低 307.1ms)
- 可接受延迟 (<2s): 43 个频道 (延迟: 平均 1284.9ms, 最低 832.5ms)
- unacceptable: 35 个频道 (延迟: 平均 3979.1ms, 最低 2152.5ms)
- 低延迟 (<300ms): 12 个频道 (延迟: 平均 243.8ms, 最低 212.0ms)

### 📁 频道分组
- : 114 个频道

### 🔗 协议统计
- HLS (m3u8): 95 个频道
- HTTP: 18 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.7 KB)
- iptv_medium_latency.m3u (7.0 KB)
- iptv_high_latency.m3u (12.5 KB)
- iptv_optimized_combined.m3u (23.0 KB)
- tvbox_optimized.m3u (38.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (205.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 424.6 秒
