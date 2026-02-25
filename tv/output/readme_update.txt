## IPTV智能优化系统更新报告

生成时间: 2026-02-25T07:02:23.390009

### 📊 总体统计
- 总频道数: 124
- TVBox优化频道数: 124

### 📈 分级统计
- 低延迟 (<300ms): 4 个频道 (延迟: 平均 267.1ms, 最低 244.1ms)
- 中等延迟 (<800ms): 30 个频道 (延迟: 平均 592.0ms, 最低 317.6ms)
- 可接受延迟 (<2s): 49 个频道 (延迟: 平均 1353.9ms, 最低 803.4ms)
- unacceptable: 41 个频道 (延迟: 平均 3082.7ms, 最低 2012.6ms)

### 📁 频道分组
- : 124 个频道

### 🔗 协议统计
- HLS (m3u8): 122 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.2 KB)
- iptv_medium_latency.m3u (8.8 KB)
- iptv_high_latency.m3u (14.3 KB)
- iptv_optimized_combined.m3u (24.1 KB)
- tvbox_optimized.m3u (41.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 524.1 秒
