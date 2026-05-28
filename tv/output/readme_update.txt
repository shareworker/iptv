## IPTV智能优化系统更新报告

生成时间: 2026-05-28T20:14:20.621516

### 📊 总体统计
- 总频道数: 149
- TVBox优化频道数: 149

### 📈 分级统计
- 中等延迟 (<800ms): 42 个频道 (延迟: 平均 478.6ms, 最低 304.3ms)
- 可接受延迟 (<2s): 62 个频道 (延迟: 平均 1149.8ms, 最低 861.1ms)
- unacceptable: 12 个频道 (延迟: 平均 4039.3ms, 最低 2318.3ms)
- 低延迟 (<300ms): 33 个频道 (延迟: 平均 209.5ms, 最低 150.9ms)

### 📁 频道分组
- : 149 个频道

### 🔗 协议统计
- HLS (m3u8): 126 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (9.7 KB)
- iptv_medium_latency.m3u (12.1 KB)
- iptv_high_latency.m3u (18.2 KB)
- iptv_optimized_combined.m3u (39.8 KB)
- tvbox_optimized.m3u (47.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 375.5 秒
