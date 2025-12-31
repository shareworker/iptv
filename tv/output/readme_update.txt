## IPTV智能优化系统更新报告

生成时间: 2025-12-31T18:26:40.910394

### 📊 总体统计
- 总频道数: 165
- TVBox优化频道数: 165

### 📈 分级统计
- 中等延迟 (<800ms): 47 个频道 (延迟: 平均 569.9ms, 最低 311.0ms)
- 可接受延迟 (<2s): 74 个频道 (延迟: 平均 1401.0ms, 最低 823.0ms)
- unacceptable: 17 个频道 (延迟: 平均 4909.2ms, 最低 2004.5ms)
- 低延迟 (<300ms): 27 个频道 (延迟: 平均 219.6ms, 最低 182.7ms)

### 📁 频道分组
- : 165 个频道

### 🔗 协议统计
- HLS (m3u8): 141 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.0 KB)
- iptv_medium_latency.m3u (13.5 KB)
- iptv_high_latency.m3u (21.7 KB)
- iptv_optimized_combined.m3u (43.0 KB)
- tvbox_optimized.m3u (54.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 390.1 秒
