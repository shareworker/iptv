## IPTV智能优化系统更新报告

生成时间: 2026-07-12T08:08:54.028641

### 📊 总体统计
- 总频道数: 142
- TVBox优化频道数: 142

### 📈 分级统计
- 低延迟 (<300ms): 28 个频道 (延迟: 平均 214.2ms, 最低 151.5ms)
- 中等延迟 (<800ms): 39 个频道 (延迟: 平均 527.0ms, 最低 349.4ms)
- 可接受延迟 (<2s): 63 个频道 (延迟: 平均 1141.6ms, 最低 803.1ms)
- unacceptable: 12 个频道 (延迟: 平均 4570.0ms, 最低 2025.2ms)

### 📁 频道分组
- : 142 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 119 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.3 KB)
- iptv_medium_latency.m3u (11.2 KB)
- iptv_high_latency.m3u (18.2 KB)
- iptv_optimized_combined.m3u (37.6 KB)
- tvbox_optimized.m3u (45.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (210.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 358.9 秒
