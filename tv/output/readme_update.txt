## IPTV智能优化系统更新报告

生成时间: 2026-02-10T19:01:54.693200

### 📊 总体统计
- 总频道数: 136
- TVBox优化频道数: 136

### 📈 分级统计
- 中等延迟 (<800ms): 46 个频道 (延迟: 平均 484.7ms, 最低 302.0ms)
- 可接受延迟 (<2s): 69 个频道 (延迟: 平均 1285.8ms, 最低 832.4ms)
- unacceptable: 8 个频道 (延迟: 平均 5904.9ms, 最低 2129.7ms)
- 低延迟 (<300ms): 13 个频道 (延迟: 平均 200.4ms, 最低 156.6ms)

### 📁 频道分组
- : 136 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 112 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.9 KB)
- iptv_medium_latency.m3u (13.4 KB)
- iptv_high_latency.m3u (20.2 KB)
- iptv_optimized_combined.m3u (37.3 KB)
- tvbox_optimized.m3u (44.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 376.4 秒
