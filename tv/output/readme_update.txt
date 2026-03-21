## IPTV智能优化系统更新报告

生成时间: 2026-03-21T18:33:20.500377

### 📊 总体统计
- 总频道数: 135
- TVBox优化频道数: 135

### 📈 分级统计
- 低延迟 (<300ms): 4 个频道 (延迟: 平均 251.0ms, 最低 233.1ms)
- 中等延迟 (<800ms): 37 个频道 (延迟: 平均 556.9ms, 最低 385.6ms)
- 可接受延迟 (<2s): 71 个频道 (延迟: 平均 1370.2ms, 最低 890.4ms)
- unacceptable: 23 个频道 (延迟: 平均 4399.0ms, 最低 2075.5ms)

### 📁 频道分组
- : 135 个频道

### 🔗 协议统计
- HLS (m3u8): 133 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.2 KB)
- iptv_medium_latency.m3u (11.0 KB)
- iptv_high_latency.m3u (20.7 KB)
- iptv_optimized_combined.m3u (32.6 KB)
- tvbox_optimized.m3u (45.7 KB)
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
- 总耗时: 466.8 秒
