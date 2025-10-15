## IPTV智能优化系统更新报告

生成时间: 2025-10-15T06:25:59.467892

### 📊 总体统计
- 总频道数: 156
- TVBox优化频道数: 156

### 📈 分级统计
- 中等延迟 (<800ms): 65 个频道 (延迟: 平均 572.5ms, 最低 310.9ms)
- 可接受延迟 (<2s): 56 个频道 (延迟: 平均 1309.5ms, 最低 811.3ms)
- unacceptable: 13 个频道 (延迟: 平均 3020.2ms, 最低 2163.5ms)
- 低延迟 (<300ms): 22 个频道 (延迟: 平均 209.4ms, 最低 161.2ms)

### 📁 频道分组
- : 156 个频道

### 🔗 协议统计
- HLS (m3u8): 132 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.2 KB)
- iptv_medium_latency.m3u (18.7 KB)
- iptv_high_latency.m3u (16.7 KB)
- iptv_optimized_combined.m3u (41.4 KB)
- tvbox_optimized.m3u (49.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 382.8 秒
