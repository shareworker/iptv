## IPTV智能优化系统更新报告

生成时间: 2025-11-28T18:25:04.549992

### 📊 总体统计
- 总频道数: 163
- TVBox优化频道数: 163

### 📈 分级统计
- 中等延迟 (<800ms): 72 个频道 (延迟: 平均 513.5ms, 最低 302.3ms)
- 可接受延迟 (<2s): 53 个频道 (延迟: 平均 1337.3ms, 最低 897.2ms)
- unacceptable: 15 个频道 (延迟: 平均 4960.3ms, 最低 2696.4ms)
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 213.6ms, 最低 160.8ms)

### 📁 频道分组
- : 163 个频道

### 🔗 协议统计
- HLS (m3u8): 139 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.5 KB)
- iptv_medium_latency.m3u (21.1 KB)
- iptv_high_latency.m3u (15.7 KB)
- iptv_optimized_combined.m3u (43.2 KB)
- tvbox_optimized.m3u (52.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 377.5 秒
