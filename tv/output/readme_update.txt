## IPTV智能优化系统更新报告

生成时间: 2026-03-19T18:52:57.335879

### 📊 总体统计
- 总频道数: 137
- TVBox优化频道数: 137

### 📈 分级统计
- 低延迟 (<300ms): 18 个频道 (延迟: 平均 231.0ms, 最低 193.5ms)
- 中等延迟 (<800ms): 38 个频道 (延迟: 平均 503.0ms, 最低 317.1ms)
- 可接受延迟 (<2s): 71 个频道 (延迟: 平均 1235.5ms, 最低 812.6ms)
- unacceptable: 10 个频道 (延迟: 平均 2504.5ms, 最低 2063.7ms)

### 📁 频道分组
- : 137 个频道

### 🔗 协议统计
- HLS (m3u8): 132 个频道
- FLV: 2 个频道
- HTTP: 3 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.5 KB)
- iptv_medium_latency.m3u (10.9 KB)
- iptv_high_latency.m3u (20.8 KB)
- iptv_optimized_combined.m3u (37.1 KB)
- tvbox_optimized.m3u (43.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 505.6 秒
