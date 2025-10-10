## IPTV智能优化系统更新报告

生成时间: 2025-10-10T06:26:03.906802

### 📊 总体统计
- 总频道数: 160
- TVBox优化频道数: 160

### 📈 分级统计
- 中等延迟 (<800ms): 52 个频道 (延迟: 平均 518.6ms, 最低 304.7ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1306.0ms, 最低 879.7ms)
- unacceptable: 26 个频道 (延迟: 平均 3385.0ms, 最低 2094.3ms)
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 212.0ms, 最低 161.9ms)

### 📁 频道分组
- : 160 个频道

### 🔗 协议统计
- HLS (m3u8): 136 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.5 KB)
- iptv_medium_latency.m3u (15.0 KB)
- iptv_high_latency.m3u (17.4 KB)
- iptv_optimized_combined.m3u (38.7 KB)
- tvbox_optimized.m3u (52.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 408.3 秒
