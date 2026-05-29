## IPTV智能优化系统更新报告

生成时间: 2026-05-29T09:44:32.664547

### 📊 总体统计
- 总频道数: 151
- TVBox优化频道数: 151

### 📈 分级统计
- 低延迟 (<300ms): 28 个频道 (延迟: 平均 205.6ms, 最低 148.1ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1169.1ms, 最低 845.9ms)
- unacceptable: 12 个频道 (延迟: 平均 4510.7ms, 最低 2604.0ms)
- 中等延迟 (<800ms): 49 个频道 (延迟: 平均 513.5ms, 最低 302.6ms)
- 超低延迟 (<100ms): 1 个频道 (延迟: 平均 61.4ms, 最低 61.4ms)

### 📁 频道分组
- : 151 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 128 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_ultra_low_latency.m3u (0.5 KB)
- iptv_low_latency.m3u (7.9 KB)
- iptv_medium_latency.m3u (14.5 KB)
- iptv_high_latency.m3u (17.7 KB)
- iptv_optimized_combined.m3u (40.3 KB)
- tvbox_optimized.m3u (48.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 357.1 秒
