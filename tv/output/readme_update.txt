## IPTV智能优化系统更新报告

生成时间: 2026-06-28T19:13:43.084918

### 📊 总体统计
- 总频道数: 121
- TVBox优化频道数: 121

### 📈 分级统计
- 低延迟 (<300ms): 6 个频道 (延迟: 平均 254.3ms, 最低 224.0ms)
- 中等延迟 (<800ms): 34 个频道 (延迟: 平均 626.4ms, 最低 388.8ms)
- 可接受延迟 (<2s): 68 个频道 (延迟: 平均 1219.0ms, 最低 814.7ms)
- unacceptable: 13 个频道 (延迟: 平均 5537.8ms, 最低 2252.0ms)

### 📁 频道分组
- : 121 个频道

### 🔗 协议统计
- HLS (m3u8): 120 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.8 KB)
- iptv_medium_latency.m3u (10.0 KB)
- iptv_high_latency.m3u (19.9 KB)
- iptv_optimized_combined.m3u (31.5 KB)
- tvbox_optimized.m3u (39.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (206.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 521.3 秒
