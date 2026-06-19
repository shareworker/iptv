## IPTV智能优化系统更新报告

生成时间: 2026-06-19T19:37:21.321498

### 📊 总体统计
- 总频道数: 128
- TVBox优化频道数: 128

### 📈 分级统计
- 可接受延迟 (<2s): 72 个频道 (延迟: 平均 1278.4ms, 最低 828.4ms)
- unacceptable: 37 个频道 (延迟: 平均 3793.5ms, 最低 2003.0ms)
- 中等延迟 (<800ms): 14 个频道 (延迟: 平均 658.2ms, 最低 372.2ms)
- 低延迟 (<300ms): 5 个频道 (延迟: 平均 233.5ms, 最低 204.3ms)

### 📁 频道分组
- : 128 个频道

### 🔗 协议统计
- HLS (m3u8): 123 个频道
- FLV: 1 个频道
- HTTP: 4 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.5 KB)
- iptv_medium_latency.m3u (4.0 KB)
- iptv_high_latency.m3u (21.5 KB)
- iptv_optimized_combined.m3u (26.8 KB)
- tvbox_optimized.m3u (43.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 584.1 秒
