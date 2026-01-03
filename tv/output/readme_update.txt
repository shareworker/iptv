## IPTV智能优化系统更新报告

生成时间: 2026-01-03T06:26:57.936941

### 📊 总体统计
- 总频道数: 161
- TVBox优化频道数: 161

### 📈 分级统计
- 低延迟 (<300ms): 38 个频道 (延迟: 平均 205.2ms, 最低 147.2ms)
- 中等延迟 (<800ms): 50 个频道 (延迟: 平均 532.9ms, 最低 302.2ms)
- 可接受延迟 (<2s): 63 个频道 (延迟: 平均 1287.0ms, 最低 804.2ms)
- unacceptable: 10 个频道 (延迟: 平均 2816.6ms, 最低 2153.9ms)

### 📁 频道分组
- : 161 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 137 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (11.1 KB)
- iptv_medium_latency.m3u (14.7 KB)
- iptv_high_latency.m3u (18.3 KB)
- iptv_optimized_combined.m3u (43.9 KB)
- tvbox_optimized.m3u (52.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 366.4 秒
