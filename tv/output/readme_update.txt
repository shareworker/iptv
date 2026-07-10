## IPTV智能优化系统更新报告

生成时间: 2026-07-10T19:26:39.213308

### 📊 总体统计
- 总频道数: 109
- TVBox优化频道数: 109

### 📈 分级统计
- 中等延迟 (<800ms): 28 个频道 (延迟: 平均 631.4ms, 最低 344.7ms)
- unacceptable: 13 个频道 (延迟: 平均 5088.8ms, 最低 2034.3ms)
- 可接受延迟 (<2s): 53 个频道 (延迟: 平均 1209.3ms, 最低 802.9ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 239.4ms, 最低 201.8ms)

### 📁 频道分组
- : 109 个频道

### 🔗 协议统计
- HLS (m3u8): 108 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.6 KB)
- iptv_medium_latency.m3u (8.1 KB)
- iptv_high_latency.m3u (15.4 KB)
- iptv_optimized_combined.m3u (28.0 KB)
- tvbox_optimized.m3u (35.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (204.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 578.4 秒
