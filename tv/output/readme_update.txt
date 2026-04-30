## IPTV智能优化系统更新报告

生成时间: 2026-04-30T19:13:51.879343

### 📊 总体统计
- 总频道数: 149
- TVBox优化频道数: 149

### 📈 分级统计
- 低延迟 (<300ms): 30 个频道 (延迟: 平均 222.1ms, 最低 150.7ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1360.3ms, 最低 868.1ms)
- unacceptable: 13 个频道 (延迟: 平均 4117.9ms, 最低 2562.8ms)
- 中等延迟 (<800ms): 45 个频道 (延迟: 平均 454.3ms, 最低 314.0ms)

### 📁 频道分组
- : 149 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 126 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.7 KB)
- iptv_medium_latency.m3u (13.2 KB)
- iptv_high_latency.m3u (17.9 KB)
- iptv_optimized_combined.m3u (39.6 KB)
- tvbox_optimized.m3u (48.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 385.6 秒
