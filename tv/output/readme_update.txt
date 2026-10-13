## IPTV智能优化系统更新报告

生成时间: 2026-10-13T00:04:53.115867

### 📊 总体统计
- 总频道数: 117
- TVBox优化频道数: 117

### 📈 分级统计
- 中等延迟 (<800ms): 36 个频道 (延迟: 平均 513.0ms, 最低 313.5ms)
- 可接受延迟 (<2s): 54 个频道 (延迟: 平均 1351.2ms, 最低 803.9ms)
- 低延迟 (<300ms): 24 个频道 (延迟: 平均 198.7ms, 最低 150.4ms)
- unacceptable: 3 个频道 (延迟: 平均 2466.1ms, 最低 2457.5ms)

### 📁 频道分组
- : 117 个频道

### 🔗 协议统计
- HLS (m3u8): 94 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.0 KB)
- iptv_medium_latency.m3u (10.7 KB)
- iptv_high_latency.m3u (15.5 KB)
- iptv_optimized_combined.m3u (33.0 KB)
- tvbox_optimized.m3u (38.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (205.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 341.4 秒
