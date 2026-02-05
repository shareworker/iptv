## IPTV智能优化系统更新报告

生成时间: 2026-02-05T06:55:03.711966

### 📊 总体统计
- 总频道数: 142
- TVBox优化频道数: 142

### 📈 分级统计
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 247.5ms, 最低 219.8ms)
- 中等延迟 (<800ms): 41 个频道 (延迟: 平均 532.0ms, 最低 311.6ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1271.5ms, 最低 802.1ms)
- unacceptable: 17 个频道 (延迟: 平均 3457.0ms, 最低 2005.9ms)

### 📁 频道分组
- : 142 个频道

### 🔗 协议统计
- HLS (m3u8): 124 个频道
- HTTP: 16 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.1 KB)
- iptv_medium_latency.m3u (11.9 KB)
- iptv_high_latency.m3u (17.4 KB)
- iptv_optimized_combined.m3u (36.2 KB)
- tvbox_optimized.m3u (45.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (210.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 400.6 秒
