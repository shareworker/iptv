## IPTV智能优化系统更新报告

生成时间: 2026-01-13T18:29:32.985394

### 📊 总体统计
- 总频道数: 137
- TVBox优化频道数: 137

### 📈 分级统计
- 中等延迟 (<800ms): 64 个频道 (延迟: 平均 563.8ms, 最低 335.6ms)
- 可接受延迟 (<2s): 46 个频道 (延迟: 平均 1235.5ms, 最低 846.9ms)
- unacceptable: 7 个频道 (延迟: 平均 9485.4ms, 最低 2181.3ms)
- 低延迟 (<300ms): 20 个频道 (延迟: 平均 190.7ms, 最低 146.9ms)

### 📁 频道分组
- : 137 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 113 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.7 KB)
- iptv_medium_latency.m3u (18.4 KB)
- iptv_high_latency.m3u (13.6 KB)
- iptv_optimized_combined.m3u (37.5 KB)
- tvbox_optimized.m3u (42.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 390.7 秒
