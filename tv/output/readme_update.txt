## IPTV智能优化系统更新报告

生成时间: 2025-11-08T06:24:32.834671

### 📊 总体统计
- 总频道数: 164
- TVBox优化频道数: 164

### 📈 分级统计
- 中等延迟 (<800ms): 47 个频道 (延迟: 平均 552.2ms, 最低 303.1ms)
- 可接受延迟 (<2s): 54 个频道 (延迟: 平均 1275.0ms, 最低 802.6ms)
- unacceptable: 48 个频道 (延迟: 平均 4225.1ms, 最低 2084.9ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 249.1ms, 最低 203.2ms)

### 📁 频道分组
- : 164 个频道

### 🔗 协议统计
- HLS (m3u8): 142 个频道
- HTTP: 20 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.3 KB)
- iptv_medium_latency.m3u (13.4 KB)
- iptv_high_latency.m3u (16.2 KB)
- iptv_optimized_combined.m3u (33.7 KB)
- tvbox_optimized.m3u (53.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 409.5 秒
