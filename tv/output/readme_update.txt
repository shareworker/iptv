## IPTV智能优化系统更新报告

生成时间: 2026-09-27T20:44:57.285345

### 📊 总体统计
- 总频道数: 108
- TVBox优化频道数: 108

### 📈 分级统计
- 中等延迟 (<800ms): 31 个频道 (延迟: 平均 576.4ms, 最低 314.0ms)
- 可接受延迟 (<2s): 53 个频道 (延迟: 平均 1319.5ms, 最低 803.6ms)
- unacceptable: 12 个频道 (延迟: 平均 2896.0ms, 最低 2047.5ms)
- 低延迟 (<300ms): 12 个频道 (延迟: 平均 217.8ms, 最低 198.8ms)

### 📁 频道分组
- : 108 个频道

### 🔗 协议统计
- HLS (m3u8): 86 个频道
- HTTP: 22 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.4 KB)
- iptv_medium_latency.m3u (9.2 KB)
- iptv_high_latency.m3u (15.4 KB)
- iptv_optimized_combined.m3u (27.8 KB)
- tvbox_optimized.m3u (35.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (203.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 359.8 秒
