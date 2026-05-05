## IPTV智能优化系统更新报告

生成时间: 2026-05-05T08:03:23.565003

### 📊 总体统计
- 总频道数: 146
- TVBox优化频道数: 146

### 📈 分级统计
- 中等延迟 (<800ms): 44 个频道 (延迟: 平均 551.3ms, 最低 311.7ms)
- 可接受延迟 (<2s): 66 个频道 (延迟: 平均 1364.5ms, 最低 833.1ms)
- unacceptable: 20 个频道 (延迟: 平均 3429.7ms, 最低 2021.0ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 214.8ms, 最低 183.8ms)

### 📁 频道分组
- : 146 个频道

### 🔗 协议统计
- HLS (m3u8): 123 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (13.0 KB)
- iptv_high_latency.m3u (19.2 KB)
- iptv_optimized_combined.m3u (36.5 KB)
- tvbox_optimized.m3u (47.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 393.2 秒
