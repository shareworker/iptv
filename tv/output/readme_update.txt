## IPTV智能优化系统更新报告

生成时间: 2026-04-22T19:08:28.167949

### 📊 总体统计
- 总频道数: 150
- TVBox优化频道数: 150

### 📈 分级统计
- 中等延迟 (<800ms): 42 个频道 (延迟: 平均 569.7ms, 最低 326.6ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 229.2ms, 最低 197.5ms)
- 可接受延迟 (<2s): 65 个频道 (延迟: 平均 1317.8ms, 最低 862.2ms)
- unacceptable: 28 个频道 (延迟: 平均 3488.0ms, 最低 2211.4ms)

### 📁 频道分组
- : 150 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 127 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.3 KB)
- iptv_medium_latency.m3u (12.0 KB)
- iptv_high_latency.m3u (19.2 KB)
- iptv_optimized_combined.m3u (35.3 KB)
- tvbox_optimized.m3u (49.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 393.4 秒
