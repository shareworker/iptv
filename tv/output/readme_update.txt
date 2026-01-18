## IPTV智能优化系统更新报告

生成时间: 2026-01-18T06:30:17.866907

### 📊 总体统计
- 总频道数: 143
- TVBox优化频道数: 143

### 📈 分级统计
- 中等延迟 (<800ms): 52 个频道 (延迟: 平均 567.3ms, 最低 304.0ms)
- 可接受延迟 (<2s): 74 个频道 (延迟: 平均 1298.9ms, 最低 822.1ms)
- unacceptable: 16 个频道 (延迟: 平均 3123.8ms, 最低 2247.1ms)
- 低延迟 (<300ms): 1 个频道 (延迟: 平均 295.1ms, 最低 295.1ms)

### 📁 频道分组
- : 143 个频道

### 🔗 协议统计
- HLS (m3u8): 138 个频道
- HTTP: 3 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (0.4 KB)
- iptv_medium_latency.m3u (15.5 KB)
- iptv_high_latency.m3u (21.4 KB)
- iptv_optimized_combined.m3u (37.1 KB)
- tvbox_optimized.m3u (47.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 565.8 秒
