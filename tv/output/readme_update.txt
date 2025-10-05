## IPTV智能优化系统更新报告

生成时间: 2025-10-05T06:22:51.118248

### 📊 总体统计
- 总频道数: 168
- TVBox优化频道数: 168

### 📈 分级统计
- 中等延迟 (<800ms): 68 个频道 (延迟: 平均 535.4ms, 最低 307.6ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1179.8ms, 最低 812.5ms)
- unacceptable: 19 个频道 (延迟: 平均 3760.2ms, 最低 2014.8ms)
- 低延迟 (<300ms): 22 个频道 (延迟: 平均 212.9ms, 最低 150.8ms)

### 📁 频道分组
- : 168 个频道

### 🔗 协议统计
- HLS (m3u8): 144 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.2 KB)
- iptv_medium_latency.m3u (19.7 KB)
- iptv_high_latency.m3u (17.4 KB)
- iptv_optimized_combined.m3u (43.1 KB)
- tvbox_optimized.m3u (53.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (216.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 378.2 秒
