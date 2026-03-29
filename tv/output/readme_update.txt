## IPTV智能优化系统更新报告

生成时间: 2026-03-29T18:36:42.489998

### 📊 总体统计
- 总频道数: 155
- TVBox优化频道数: 155

### 📈 分级统计
- 低延迟 (<300ms): 22 个频道 (延迟: 平均 206.6ms, 最低 151.7ms)
- 中等延迟 (<800ms): 63 个频道 (延迟: 平均 465.6ms, 最低 319.8ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1165.5ms, 最低 823.9ms)
- unacceptable: 9 个频道 (延迟: 平均 2672.6ms, 最低 2230.5ms)

### 📁 频道分组
- : 155 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 131 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.4 KB)
- iptv_medium_latency.m3u (18.5 KB)
- iptv_high_latency.m3u (17.7 KB)
- iptv_optimized_combined.m3u (42.4 KB)
- tvbox_optimized.m3u (49.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 382.3 秒
