## IPTV智能优化系统更新报告

生成时间: 2026-05-25T19:23:48.315511

### 📊 总体统计
- 总频道数: 149
- TVBox优化频道数: 149

### 📈 分级统计
- 中等延迟 (<800ms): 42 个频道 (延迟: 平均 558.5ms, 最低 322.7ms)
- 可接受延迟 (<2s): 69 个频道 (延迟: 平均 1282.5ms, 最低 844.2ms)
- unacceptable: 22 个频道 (延迟: 平均 3886.8ms, 最低 2106.4ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 225.9ms, 最低 199.8ms)

### 📁 频道分组
- : 149 个频道

### 🔗 协议统计
- HLS (m3u8): 126 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (12.1 KB)
- iptv_high_latency.m3u (20.4 KB)
- iptv_optimized_combined.m3u (36.9 KB)
- tvbox_optimized.m3u (48.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 382.9 秒
