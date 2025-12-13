## IPTV智能优化系统更新报告

生成时间: 2025-12-13T06:28:32.304946

### 📊 总体统计
- 总频道数: 143
- TVBox优化频道数: 143

### 📈 分级统计
- 可接受延迟 (<2s): 62 个频道 (延迟: 平均 1371.4ms, 最低 803.7ms)
- 中等延迟 (<800ms): 51 个频道 (延迟: 平均 600.5ms, 最低 311.6ms)
- unacceptable: 28 个频道 (延迟: 平均 3438.0ms, 最低 2002.5ms)
- 低延迟 (<300ms): 2 个频道 (延迟: 平均 256.4ms, 最低 224.2ms)

### 📁 频道分组
- : 143 个频道

### 🔗 协议统计
- HLS (m3u8): 140 个频道
- FLV: 2 个频道
- HTTP: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (0.6 KB)
- iptv_medium_latency.m3u (15.1 KB)
- iptv_high_latency.m3u (18.1 KB)
- iptv_optimized_combined.m3u (33.6 KB)
- tvbox_optimized.m3u (47.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 525.8 秒
