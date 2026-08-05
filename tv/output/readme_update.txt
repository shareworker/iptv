## IPTV智能优化系统更新报告

生成时间: 2026-08-05T08:26:43.677604

### 📊 总体统计
- 总频道数: 135
- TVBox优化频道数: 135

### 📈 分级统计
- 中等延迟 (<800ms): 42 个频道 (延迟: 平均 524.7ms, 最低 319.0ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1212.6ms, 最低 805.0ms)
- unacceptable: 22 个频道 (延迟: 平均 3667.6ms, 最低 2007.6ms)
- 低延迟 (<300ms): 12 个频道 (延迟: 平均 216.0ms, 最低 198.8ms)

### 📁 频道分组
- : 135 个频道

### 🔗 协议统计
- HLS (m3u8): 112 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.4 KB)
- iptv_medium_latency.m3u (12.4 KB)
- iptv_high_latency.m3u (16.9 KB)
- iptv_optimized_combined.m3u (32.5 KB)
- tvbox_optimized.m3u (44.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 320.2 秒
