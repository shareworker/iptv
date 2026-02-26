## IPTV智能优化系统更新报告

生成时间: 2026-02-26T18:47:28.656483

### 📊 总体统计
- 总频道数: 145
- TVBox优化频道数: 145

### 📈 分级统计
- 低延迟 (<300ms): 29 个频道 (延迟: 平均 198.4ms, 最低 147.7ms)
- 中等延迟 (<800ms): 59 个频道 (延迟: 平均 544.1ms, 最低 309.1ms)
- 可接受延迟 (<2s): 50 个频道 (延迟: 平均 1174.7ms, 最低 809.8ms)
- unacceptable: 7 个频道 (延迟: 平均 6809.7ms, 最低 2520.1ms)

### 📁 频道分组
- : 145 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 121 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.5 KB)
- iptv_medium_latency.m3u (17.2 KB)
- iptv_high_latency.m3u (14.5 KB)
- iptv_optimized_combined.m3u (40.0 KB)
- tvbox_optimized.m3u (45.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 382.1 秒
