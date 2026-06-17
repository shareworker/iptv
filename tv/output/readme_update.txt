## IPTV智能优化系统更新报告

生成时间: 2026-06-17T20:11:41.904810

### 📊 总体统计
- 总频道数: 121
- TVBox优化频道数: 121

### 📈 分级统计
- 低延迟 (<300ms): 3 个频道 (延迟: 平均 233.6ms, 最低 214.9ms)
- 中等延迟 (<800ms): 36 个频道 (延迟: 平均 511.6ms, 最低 319.0ms)
- 可接受延迟 (<2s): 68 个频道 (延迟: 平均 1383.4ms, 最低 821.8ms)
- unacceptable: 14 个频道 (延迟: 平均 4965.1ms, 最低 2025.4ms)

### 📁 频道分组
- : 121 个频道

### 🔗 协议统计
- HLS (m3u8): 120 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (0.9 KB)
- iptv_medium_latency.m3u (10.9 KB)
- iptv_high_latency.m3u (19.7 KB)
- iptv_optimized_combined.m3u (31.3 KB)
- tvbox_optimized.m3u (40.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (206.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 549.7 秒
