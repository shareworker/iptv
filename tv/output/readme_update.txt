## IPTV智能优化系统更新报告

生成时间: 2025-10-27T18:25:34.162234

### 📊 总体统计
- 总频道数: 162
- TVBox优化频道数: 162

### 📈 分级统计
- 中等延迟 (<800ms): 51 个频道 (延迟: 平均 544.9ms, 最低 300.5ms)
- 可接受延迟 (<2s): 67 个频道 (延迟: 平均 1360.8ms, 最低 807.1ms)
- unacceptable: 27 个频道 (延迟: 平均 2658.2ms, 最低 2083.9ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 209.1ms, 最低 181.4ms)
- 超低延迟 (<100ms): 1 个频道 (延迟: 平均 74.3ms, 最低 74.3ms)

### 📁 频道分组
- : 162 个频道

### 🔗 协议统计
- HLS (m3u8): 138 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_ultra_low_latency.m3u (0.3 KB)
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (14.9 KB)
- iptv_high_latency.m3u (19.5 KB)
- iptv_optimized_combined.m3u (38.9 KB)
- tvbox_optimized.m3u (53.1 KB)
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
- 总耗时: 371.8 秒
