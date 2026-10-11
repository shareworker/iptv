## IPTV智能优化系统更新报告

生成时间: 2026-10-11T11:58:14.518525

### 📊 总体统计
- 总频道数: 111
- TVBox优化频道数: 111

### 📈 分级统计
- 中等延迟 (<800ms): 19 个频道 (延迟: 平均 563.9ms, 最低 301.1ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1295.7ms, 最低 810.1ms)
- unacceptable: 10 个频道 (延迟: 平均 3459.2ms, 最低 2105.6ms)
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 231.3ms, 最低 200.6ms)

### 📁 频道分组
- : 111 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 88 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.9 KB)
- iptv_medium_latency.m3u (5.7 KB)
- iptv_high_latency.m3u (16.8 KB)
- iptv_optimized_combined.m3u (29.1 KB)
- tvbox_optimized.m3u (36.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (204.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 359.0 秒
