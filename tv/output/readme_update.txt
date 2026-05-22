## IPTV智能优化系统更新报告

生成时间: 2026-05-22T19:30:50.511799

### 📊 总体统计
- 总频道数: 151
- TVBox优化频道数: 151

### 📈 分级统计
- 中等延迟 (<800ms): 37 个频道 (延迟: 平均 541.8ms, 最低 309.9ms)
- 可接受延迟 (<2s): 73 个频道 (延迟: 平均 1386.7ms, 最低 806.6ms)
- unacceptable: 15 个频道 (延迟: 平均 3754.0ms, 最低 2003.0ms)
- 低延迟 (<300ms): 26 个频道 (延迟: 平均 225.3ms, 最低 184.3ms)

### 📁 频道分组
- : 151 个频道

### 🔗 协议统计
- HLS (m3u8): 128 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.7 KB)
- iptv_medium_latency.m3u (10.7 KB)
- iptv_high_latency.m3u (21.2 KB)
- iptv_optimized_combined.m3u (39.5 KB)
- tvbox_optimized.m3u (49.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 387.5 秒
