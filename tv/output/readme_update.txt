## IPTV智能优化系统更新报告

生成时间: 2026-07-22T19:05:29.787890

### 📊 总体统计
- 总频道数: 133
- TVBox优化频道数: 133

### 📈 分级统计
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 213.7ms, 最低 174.2ms)
- 中等延迟 (<800ms): 53 个频道 (延迟: 平均 598.2ms, 最低 309.1ms)
- 可接受延迟 (<2s): 55 个频道 (延迟: 平均 1116.5ms, 最低 820.1ms)
- unacceptable: 8 个频道 (延迟: 平均 3561.3ms, 最低 3177.6ms)

### 📁 频道分组
- : 133 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 110 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (15.7 KB)
- iptv_high_latency.m3u (15.9 KB)
- iptv_optimized_combined.m3u (36.2 KB)
- tvbox_optimized.m3u (42.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 370.2 秒
