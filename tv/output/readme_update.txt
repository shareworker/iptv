## IPTV智能优化系统更新报告

生成时间: 2026-03-13T06:48:53.035505

### 📊 总体统计
- 总频道数: 84
- TVBox优化频道数: 84

### 📈 分级统计
- 低延迟 (<300ms): 4 个频道 (延迟: 平均 275.9ms, 最低 234.6ms)
- 中等延迟 (<800ms): 17 个频道 (延迟: 平均 585.0ms, 最低 302.1ms)
- 可接受延迟 (<2s): 38 个频道 (延迟: 平均 1247.6ms, 最低 803.8ms)
- unacceptable: 25 个频道 (延迟: 平均 5185.9ms, 最低 2595.9ms)

### 📁 频道分组
- : 84 个频道

### 🔗 协议统计
- HLS (m3u8): 82 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.2 KB)
- iptv_medium_latency.m3u (4.9 KB)
- iptv_high_latency.m3u (11.1 KB)
- iptv_optimized_combined.m3u (17.0 KB)
- tvbox_optimized.m3u (27.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (199.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 474.2 秒
