## IPTV智能优化系统更新报告

生成时间: 2026-01-30T18:37:28.025077

### 📊 总体统计
- 总频道数: 158
- TVBox优化频道数: 158

### 📈 分级统计
- 中等延迟 (<800ms): 55 个频道 (延迟: 平均 588.6ms, 最低 320.0ms)
- 可接受延迟 (<2s): 64 个频道 (延迟: 平均 1352.6ms, 最低 806.1ms)
- unacceptable: 24 个频道 (延迟: 平均 3681.4ms, 最低 2007.4ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 227.4ms, 最低 201.3ms)

### 📁 频道分组
- : 158 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 134 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.3 KB)
- iptv_medium_latency.m3u (16.1 KB)
- iptv_high_latency.m3u (18.6 KB)
- iptv_optimized_combined.m3u (38.9 KB)
- tvbox_optimized.m3u (51.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 375.8 秒
