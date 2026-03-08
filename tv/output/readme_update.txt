## IPTV智能优化系统更新报告

生成时间: 2026-03-08T18:31:28.758174

### 📊 总体统计
- 总频道数: 135
- TVBox优化频道数: 135

### 📈 分级统计
- 低延迟 (<300ms): 10 个频道 (延迟: 平均 270.5ms, 最低 222.9ms)
- 中等延迟 (<800ms): 60 个频道 (延迟: 平均 565.3ms, 最低 304.9ms)
- 可接受延迟 (<2s): 56 个频道 (延迟: 平均 1409.2ms, 最低 854.3ms)
- unacceptable: 9 个频道 (延迟: 平均 3280.7ms, 最低 2206.8ms)

### 📁 频道分组
- : 135 个频道

### 🔗 协议统计
- HLS (m3u8): 133 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (2.9 KB)
- iptv_medium_latency.m3u (17.5 KB)
- iptv_high_latency.m3u (16.6 KB)
- iptv_optimized_combined.m3u (36.8 KB)
- tvbox_optimized.m3u (43.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 522.0 秒
