## IPTV智能优化系统更新报告

生成时间: 2025-11-19T18:25:41.601741

### 📊 总体统计
- 总频道数: 165
- TVBox优化频道数: 165

### 📈 分级统计
- 低延迟 (<300ms): 26 个频道 (延迟: 平均 232.8ms, 最低 198.8ms)
- 中等延迟 (<800ms): 45 个频道 (延迟: 平均 603.0ms, 最低 335.2ms)
- 可接受延迟 (<2s): 37 个频道 (延迟: 平均 1254.6ms, 最低 800.5ms)
- unacceptable: 57 个频道 (延迟: 平均 2716.0ms, 最低 2001.4ms)

### 📁 频道分组
- : 165 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 141 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.6 KB)
- iptv_medium_latency.m3u (13.0 KB)
- iptv_high_latency.m3u (11.0 KB)
- iptv_optimized_combined.m3u (31.3 KB)
- tvbox_optimized.m3u (54.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 379.5 秒
