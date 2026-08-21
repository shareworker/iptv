## IPTV智能优化系统更新报告

生成时间: 2026-08-21T18:29:03.996835

### 📊 总体统计
- 总频道数: 133
- TVBox优化频道数: 133

### 📈 分级统计
- 低延迟 (<300ms): 24 个频道 (延迟: 平均 195.2ms, 最低 147.6ms)
- 中等延迟 (<800ms): 67 个频道 (延迟: 平均 570.1ms, 最低 322.4ms)
- 可接受延迟 (<2s): 37 个频道 (延迟: 平均 1043.2ms, 最低 806.1ms)
- unacceptable: 5 个频道 (延迟: 平均 3116.3ms, 最低 2924.8ms)

### 📁 频道分组
- : 133 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 110 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.7 KB)
- iptv_medium_latency.m3u (19.7 KB)
- iptv_high_latency.m3u (10.8 KB)
- iptv_optimized_combined.m3u (37.1 KB)
- tvbox_optimized.m3u (41.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 311.9 秒
