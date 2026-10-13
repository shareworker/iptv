## IPTV智能优化系统更新报告

生成时间: 2026-10-13T13:20:50.808861

### 📊 总体统计
- 总频道数: 112
- TVBox优化频道数: 112

### 📈 分级统计
- 低延迟 (<300ms): 20 个频道 (延迟: 平均 209.1ms, 最低 152.6ms)
- 中等延迟 (<800ms): 27 个频道 (延迟: 平均 535.9ms, 最低 357.4ms)
- 可接受延迟 (<2s): 49 个频道 (延迟: 平均 1233.0ms, 最低 813.9ms)
- unacceptable: 16 个频道 (延迟: 平均 3383.3ms, 最低 2124.5ms)

### 📁 频道分组
- : 112 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 89 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.8 KB)
- iptv_medium_latency.m3u (8.1 KB)
- iptv_high_latency.m3u (14.1 KB)
- iptv_optimized_combined.m3u (27.8 KB)
- tvbox_optimized.m3u (37.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (204.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 338.8 秒
