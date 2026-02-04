## IPTV智能优化系统更新报告

生成时间: 2026-02-04T18:44:12.594426

### 📊 总体统计
- 总频道数: 143
- TVBox优化频道数: 143

### 📈 分级统计
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 251.3ms, 最低 234.9ms)
- 可接受延迟 (<2s): 45 个频道 (延迟: 平均 1406.2ms, 最低 831.5ms)
- 中等延迟 (<800ms): 58 个频道 (延迟: 平均 562.3ms, 最低 304.3ms)
- unacceptable: 23 个频道 (延迟: 平均 4439.9ms, 最低 2188.8ms)

### 📁 频道分组
- : 143 个频道

### 🔗 协议统计
- HLS (m3u8): 119 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (17.0 KB)
- iptv_high_latency.m3u (13.0 KB)
- iptv_optimized_combined.m3u (34.7 KB)
- tvbox_optimized.m3u (45.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 380.0 秒
