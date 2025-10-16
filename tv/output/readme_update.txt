## IPTV智能优化系统更新报告

生成时间: 2025-10-16T06:26:06.800275

### 📊 总体统计
- 总频道数: 164
- TVBox优化频道数: 164

### 📈 分级统计
- 中等延迟 (<800ms): 37 个频道 (延迟: 平均 545.5ms, 最低 301.1ms)
- 可接受延迟 (<2s): 70 个频道 (延迟: 平均 1221.9ms, 最低 816.4ms)
- unacceptable: 42 个频道 (延迟: 平均 2942.4ms, 最低 2023.2ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 237.2ms, 最低 198.6ms)

### 📁 频道分组
- : 164 个频道

### 🔗 协议统计
- HLS (m3u8): 140 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (10.8 KB)
- iptv_high_latency.m3u (20.2 KB)
- iptv_optimized_combined.m3u (35.1 KB)
- tvbox_optimized.m3u (53.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 397.8 秒
