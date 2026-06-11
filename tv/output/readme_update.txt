## IPTV智能优化系统更新报告

生成时间: 2026-06-11T20:20:27.856618

### 📊 总体统计
- 总频道数: 118
- TVBox优化频道数: 118

### 📈 分级统计
- 中等延迟 (<800ms): 23 个频道 (延迟: 平均 610.8ms, 最低 336.2ms)
- 可接受延迟 (<2s): 78 个频道 (延迟: 平均 1291.8ms, 最低 804.5ms)
- unacceptable: 15 个频道 (延迟: 平均 3983.9ms, 最低 2247.7ms)
- 低延迟 (<300ms): 2 个频道 (延迟: 平均 264.5ms, 最低 260.0ms)

### 📁 频道分组
- : 118 个频道

### 🔗 协议统计
- HLS (m3u8): 117 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (0.6 KB)
- iptv_medium_latency.m3u (6.6 KB)
- iptv_high_latency.m3u (23.2 KB)
- iptv_optimized_combined.m3u (30.2 KB)
- tvbox_optimized.m3u (39.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (205.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 564.2 秒
