## IPTV智能优化系统更新报告

生成时间: 2026-02-04T06:46:47.933592

### 📊 总体统计
- 总频道数: 142
- TVBox优化频道数: 142

### 📈 分级统计
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 243.1ms, 最低 193.0ms)
- 中等延迟 (<800ms): 68 个频道 (延迟: 平均 576.6ms, 最低 341.1ms)
- 可接受延迟 (<2s): 50 个频道 (延迟: 平均 1194.3ms, 最低 804.2ms)
- unacceptable: 6 个频道 (延迟: 平均 4074.1ms, 最低 2307.4ms)
- 超低延迟 (<100ms): 1 个频道 (延迟: 平均 92.2ms, 最低 92.2ms)

### 📁 频道分组
- : 142 个频道

### 🔗 协议统计
- HLS (m3u8): 118 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_ultra_low_latency.m3u (0.5 KB)
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (19.7 KB)
- iptv_high_latency.m3u (14.6 KB)
- iptv_optimized_combined.m3u (39.3 KB)
- tvbox_optimized.m3u (44.6 KB)
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
- 总耗时: 380.1 秒
