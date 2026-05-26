## IPTV智能优化系统更新报告

生成时间: 2026-05-26T20:04:21.260615

### 📊 总体统计
- 总频道数: 149
- TVBox优化频道数: 149

### 📈 分级统计
- 中等延迟 (<800ms): 37 个频道 (延迟: 平均 434.1ms, 最低 303.0ms)
- 可接受延迟 (<2s): 74 个频道 (延迟: 平均 1247.3ms, 最低 819.3ms)
- unacceptable: 10 个频道 (延迟: 平均 3466.4ms, 最低 2354.3ms)
- 低延迟 (<300ms): 28 个频道 (延迟: 平均 201.5ms, 最低 150.0ms)

### 📁 频道分组
- : 149 个频道

### 🔗 协议统计
- HLS (m3u8): 126 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.3 KB)
- iptv_medium_latency.m3u (10.6 KB)
- iptv_high_latency.m3u (21.7 KB)
- iptv_optimized_combined.m3u (40.4 KB)
- tvbox_optimized.m3u (48.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 364.4 秒
