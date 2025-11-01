## IPTV智能优化系统更新报告

生成时间: 2025-11-01T18:22:42.054663

### 📊 总体统计
- 总频道数: 166
- TVBox优化频道数: 166

### 📈 分级统计
- 中等延迟 (<800ms): 64 个频道 (延迟: 平均 553.9ms, 最低 327.0ms)
- 可接受延迟 (<2s): 42 个频道 (延迟: 平均 1384.3ms, 最低 807.0ms)
- unacceptable: 44 个频道 (延迟: 平均 2882.7ms, 最低 2006.8ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 228.4ms, 最低 201.6ms)

### 📁 频道分组
- : 166 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 142 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (18.7 KB)
- iptv_high_latency.m3u (12.4 KB)
- iptv_optimized_combined.m3u (35.4 KB)
- tvbox_optimized.m3u (54.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 378.2 秒
