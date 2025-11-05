## IPTV智能优化系统更新报告

生成时间: 2025-11-05T06:26:36.235692

### 📊 总体统计
- 总频道数: 166
- TVBox优化频道数: 166

### 📈 分级统计
- 中等延迟 (<800ms): 67 个频道 (延迟: 平均 518.3ms, 最低 301.5ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1384.8ms, 最低 822.3ms)
- unacceptable: 20 个频道 (延迟: 平均 3143.5ms, 最低 2200.4ms)
- 低延迟 (<300ms): 20 个频道 (延迟: 平均 203.4ms, 最低 160.9ms)

### 📁 频道分组
- : 166 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 142 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.8 KB)
- iptv_medium_latency.m3u (19.3 KB)
- iptv_high_latency.m3u (17.4 KB)
- iptv_optimized_combined.m3u (42.2 KB)
- tvbox_optimized.m3u (53.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 387.1 秒
