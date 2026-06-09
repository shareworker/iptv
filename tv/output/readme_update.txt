## IPTV智能优化系统更新报告

生成时间: 2026-06-09T09:32:34.567372

### 📊 总体统计
- 总频道数: 147
- TVBox优化频道数: 147

### 📈 分级统计
- 低延迟 (<300ms): 26 个频道 (延迟: 平均 212.0ms, 最低 151.3ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1145.5ms, 最低 800.2ms)
- unacceptable: 13 个频道 (延迟: 平均 4201.2ms, 最低 2137.8ms)
- 中等延迟 (<800ms): 47 个频道 (延迟: 平均 552.3ms, 最低 301.6ms)

### 📁 频道分组
- : 147 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 124 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.4 KB)
- iptv_medium_latency.m3u (13.9 KB)
- iptv_high_latency.m3u (17.9 KB)
- iptv_optimized_combined.m3u (38.9 KB)
- tvbox_optimized.m3u (47.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 383.6 秒
