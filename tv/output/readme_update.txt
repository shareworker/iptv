## IPTV智能优化系统更新报告

生成时间: 2026-05-14T19:35:04.931841

### 📊 总体统计
- 总频道数: 150
- TVBox优化频道数: 150

### 📈 分级统计
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 226.1ms, 最低 202.5ms)
- 中等延迟 (<800ms): 46 个频道 (延迟: 平均 590.7ms, 最低 324.4ms)
- 可接受延迟 (<2s): 72 个频道 (延迟: 平均 1404.8ms, 最低 815.2ms)
- unacceptable: 17 个频道 (延迟: 平均 4173.5ms, 最低 2094.8ms)

### 📁 频道分组
- : 150 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 127 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (13.3 KB)
- iptv_high_latency.m3u (21.3 KB)
- iptv_optimized_combined.m3u (38.6 KB)
- tvbox_optimized.m3u (49.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 390.5 秒
