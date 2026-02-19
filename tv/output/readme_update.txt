## IPTV智能优化系统更新报告

生成时间: 2026-02-19T06:59:16.340094

### 📊 总体统计
- 总频道数: 124
- TVBox优化频道数: 124

### 📈 分级统计
- 中等延迟 (<800ms): 30 个频道 (延迟: 平均 588.5ms, 最低 321.9ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1292.9ms, 最低 846.3ms)
- unacceptable: 24 个频道 (延迟: 平均 2684.6ms, 最低 2049.4ms)
- 低延迟 (<300ms): 11 个频道 (延迟: 平均 261.9ms, 最低 221.5ms)

### 📁 频道分组
- : 124 个频道

### 🔗 协议统计
- HLS (m3u8): 122 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.4 KB)
- iptv_medium_latency.m3u (8.8 KB)
- iptv_high_latency.m3u (17.1 KB)
- iptv_optimized_combined.m3u (29.1 KB)
- tvbox_optimized.m3u (41.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 499.6 秒
