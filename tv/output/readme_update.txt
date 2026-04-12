## IPTV智能优化系统更新报告

生成时间: 2026-04-12T18:44:21.523125

### 📊 总体统计
- 总频道数: 127
- TVBox优化频道数: 127

### 📈 分级统计
- 中等延迟 (<800ms): 27 个频道 (延迟: 平均 620.0ms, 最低 314.3ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1343.8ms, 最低 866.5ms)
- unacceptable: 23 个频道 (延迟: 平均 3963.2ms, 最低 2018.2ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 233.3ms, 最低 220.0ms)

### 📁 频道分组
- : 127 个频道

### 🔗 协议统计
- HLS (m3u8): 126 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.9 KB)
- iptv_medium_latency.m3u (7.9 KB)
- iptv_high_latency.m3u (17.9 KB)
- iptv_optimized_combined.m3u (30.5 KB)
- tvbox_optimized.m3u (42.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 484.5 秒
