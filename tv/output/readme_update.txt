## IPTV智能优化系统更新报告

生成时间: 2026-03-15T06:54:02.499687

### 📊 总体统计
- 总频道数: 134
- TVBox优化频道数: 134

### 📈 分级统计
- 低延迟 (<300ms): 5 个频道 (延迟: 平均 258.0ms, 最低 234.3ms)
- 中等延迟 (<800ms): 46 个频道 (延迟: 平均 535.9ms, 最低 305.6ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1253.7ms, 最低 802.4ms)
- unacceptable: 24 个频道 (延迟: 平均 3067.0ms, 最低 2032.3ms)

### 📁 频道分组
- : 134 个频道

### 🔗 协议统计
- HLS (m3u8): 132 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.5 KB)
- iptv_medium_latency.m3u (13.5 KB)
- iptv_high_latency.m3u (17.3 KB)
- iptv_optimized_combined.m3u (32.0 KB)
- tvbox_optimized.m3u (44.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 478.8 秒
