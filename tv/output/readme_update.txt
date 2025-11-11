## IPTV智能优化系统更新报告

生成时间: 2025-11-11T06:26:36.373180

### 📊 总体统计
- 总频道数: 166
- TVBox优化频道数: 166

### 📈 分级统计
- 中等延迟 (<800ms): 57 个频道 (延迟: 平均 523.8ms, 最低 301.2ms)
- unacceptable: 22 个频道 (延迟: 平均 3195.2ms, 最低 2245.6ms)
- 可接受延迟 (<2s): 70 个频道 (延迟: 平均 1393.8ms, 最低 840.4ms)
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 228.5ms, 最低 185.3ms)

### 📁 频道分组
- : 166 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 142 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (16.7 KB)
- iptv_high_latency.m3u (20.5 KB)
- iptv_optimized_combined.m3u (41.8 KB)
- tvbox_optimized.m3u (53.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 376.7 秒
