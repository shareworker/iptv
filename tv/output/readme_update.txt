## IPTV智能优化系统更新报告

生成时间: 2025-12-27T06:26:45.563113

### 📊 总体统计
- 总频道数: 160
- TVBox优化频道数: 160

### 📈 分级统计
- 中等延迟 (<800ms): 57 个频道 (延迟: 平均 544.8ms, 最低 343.4ms)
- 可接受延迟 (<2s): 72 个频道 (延迟: 平均 1275.5ms, 最低 802.9ms)
- unacceptable: 13 个频道 (延迟: 平均 5530.8ms, 最低 2197.0ms)
- 低延迟 (<300ms): 18 个频道 (延迟: 平均 190.3ms, 最低 148.8ms)

### 📁 频道分组
- : 160 个频道

### 🔗 协议统计
- HLS (m3u8): 136 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.2 KB)
- iptv_medium_latency.m3u (16.5 KB)
- iptv_high_latency.m3u (21.3 KB)
- iptv_optimized_combined.m3u (42.8 KB)
- tvbox_optimized.m3u (52.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 380.2 秒
