## IPTV智能优化系统更新报告

生成时间: 2026-07-24T19:19:39.909808

### 📊 总体统计
- 总频道数: 118
- TVBox优化频道数: 118

### 📈 分级统计
- 中等延迟 (<800ms): 47 个频道 (延迟: 平均 561.1ms, 最低 301.9ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 231.9ms, 最低 202.3ms)
- 可接受延迟 (<2s): 53 个频道 (延迟: 平均 1144.0ms, 最低 814.3ms)
- unacceptable: 2 个频道 (延迟: 平均 2673.7ms, 最低 2555.5ms)

### 📁 频道分组
- : 118 个频道

### 🔗 协议统计
- HLS (m3u8): 96 个频道
- HTTP: 22 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (14.0 KB)
- iptv_high_latency.m3u (15.2 KB)
- iptv_optimized_combined.m3u (33.5 KB)
- tvbox_optimized.m3u (37.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (205.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 347.8 秒
