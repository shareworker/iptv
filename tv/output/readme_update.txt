## IPTV智能优化系统更新报告

生成时间: 2026-08-25T18:32:07.411471

### 📊 总体统计
- 总频道数: 128
- TVBox优化频道数: 128

### 📈 分级统计
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 228.7ms, 最低 193.9ms)
- 可接受延迟 (<2s): 75 个频道 (延迟: 平均 1228.5ms, 最低 803.4ms)
- 中等延迟 (<800ms): 31 个频道 (延迟: 平均 562.2ms, 最低 314.1ms)
- unacceptable: 6 个频道 (延迟: 平均 3701.0ms, 最低 2002.0ms)

### 📁 频道分组
- : 128 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 106 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (9.0 KB)
- iptv_high_latency.m3u (22.0 KB)
- iptv_optimized_combined.m3u (35.4 KB)
- tvbox_optimized.m3u (42.2 KB)
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
- 总耗时: 345.8 秒
