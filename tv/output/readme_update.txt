## IPTV智能优化系统更新报告

生成时间: 2026-03-07T06:36:42.022826

### 📊 总体统计
- 总频道数: 154
- TVBox优化频道数: 154

### 📈 分级统计
- 中等延迟 (<800ms): 51 个频道 (延迟: 平均 542.9ms, 最低 301.1ms)
- unacceptable: 21 个频道 (延迟: 平均 3199.8ms, 最低 2034.0ms)
- 可接受延迟 (<2s): 74 个频道 (延迟: 平均 1274.9ms, 最低 812.0ms)
- 低延迟 (<300ms): 8 个频道 (延迟: 平均 225.0ms, 最低 183.9ms)

### 📁 频道分组
- : 154 个频道

### 🔗 协议统计
- HLS (m3u8): 133 个频道
- HTTP: 19 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (2.3 KB)
- iptv_medium_latency.m3u (15.0 KB)
- iptv_high_latency.m3u (21.5 KB)
- iptv_optimized_combined.m3u (38.6 KB)
- tvbox_optimized.m3u (50.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 434.8 秒
