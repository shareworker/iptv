## IPTV智能优化系统更新报告

生成时间: 2026-06-15T20:54:00.754063

### 📊 总体统计
- 总频道数: 145
- TVBox优化频道数: 145

### 📈 分级统计
- 中等延迟 (<800ms): 36 个频道 (延迟: 平均 561.7ms, 最低 332.9ms)
- 可接受延迟 (<2s): 68 个频道 (延迟: 平均 1253.4ms, 最低 805.1ms)
- unacceptable: 27 个频道 (延迟: 平均 3405.3ms, 最低 2072.7ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 267.0ms, 最低 240.2ms)

### 📁 频道分组
- : 145 个频道

### 🔗 协议统计
- HLS (m3u8): 122 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.0 KB)
- iptv_medium_latency.m3u (10.3 KB)
- iptv_high_latency.m3u (20.1 KB)
- iptv_optimized_combined.m3u (34.2 KB)
- tvbox_optimized.m3u (47.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 420.6 秒
