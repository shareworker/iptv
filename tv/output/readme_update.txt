## IPTV智能优化系统更新报告

生成时间: 2026-07-18T07:34:43.364429

### 📊 总体统计
- 总频道数: 142
- TVBox优化频道数: 142

### 📈 分级统计
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 180.6ms, 最低 133.5ms)
- 中等延迟 (<800ms): 64 个频道 (延迟: 平均 547.6ms, 最低 302.6ms)
- 可接受延迟 (<2s): 52 个频道 (延迟: 平均 1128.0ms, 最低 826.2ms)
- unacceptable: 7 个频道 (延迟: 平均 5168.1ms, 最低 2075.5ms)

### 📁 频道分组
- : 142 个频道

### 🔗 协议统计
- HLS (m3u8): 119 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.6 KB)
- iptv_medium_latency.m3u (18.6 KB)
- iptv_high_latency.m3u (14.8 KB)
- iptv_optimized_combined.m3u (38.7 KB)
- tvbox_optimized.m3u (44.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (210.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 350.6 秒
