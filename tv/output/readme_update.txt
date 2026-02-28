## IPTV智能优化系统更新报告

生成时间: 2026-02-28T18:30:17.776321

### 📊 总体统计
- 总频道数: 127
- TVBox优化频道数: 127

### 📈 分级统计
- 中等延迟 (<800ms): 32 个频道 (延迟: 平均 575.1ms, 最低 339.6ms)
- 可接受延迟 (<2s): 62 个频道 (延迟: 平均 1349.6ms, 最低 801.5ms)
- unacceptable: 29 个频道 (延迟: 平均 2741.1ms, 最低 2106.0ms)
- 低延迟 (<300ms): 4 个频道 (延迟: 平均 277.3ms, 最低 260.1ms)

### 📁 频道分组
- : 127 个频道

### 🔗 协议统计
- HLS (m3u8): 122 个频道
- HTTP: 3 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.2 KB)
- iptv_medium_latency.m3u (9.4 KB)
- iptv_high_latency.m3u (18.1 KB)
- iptv_optimized_combined.m3u (28.4 KB)
- tvbox_optimized.m3u (42.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 505.7 秒
