## IPTV智能优化系统更新报告

生成时间: 2026-10-09T22:08:54.430107

### 📊 总体统计
- 总频道数: 119
- TVBox优化频道数: 119

### 📈 分级统计
- 中等延迟 (<800ms): 34 个频道 (延迟: 平均 562.6ms, 最低 306.8ms)
- 可接受延迟 (<2s): 60 个频道 (延迟: 平均 1389.2ms, 最低 834.8ms)
- unacceptable: 10 个频道 (延迟: 平均 3792.7ms, 最低 2173.2ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 205.5ms, 最低 186.1ms)

### 📁 频道分组
- : 119 个频道

### 🔗 协议统计
- HLS (m3u8): 96 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (10.1 KB)
- iptv_high_latency.m3u (17.5 KB)
- iptv_optimized_combined.m3u (31.7 KB)
- tvbox_optimized.m3u (39.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (206.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 330.2 秒
