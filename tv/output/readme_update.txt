## IPTV智能优化系统更新报告

生成时间: 2026-09-03T10:32:47.161702

### 📊 总体统计
- 总频道数: 108
- TVBox优化频道数: 108

### 📈 分级统计
- 低延迟 (<300ms): 5 个频道 (延迟: 平均 254.6ms, 最低 230.0ms)
- 中等延迟 (<800ms): 23 个频道 (延迟: 平均 550.1ms, 最低 335.7ms)
- unacceptable: 19 个频道 (延迟: 平均 3109.9ms, 最低 2004.7ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1225.2ms, 最低 802.8ms)

### 📁 频道分组
- : 108 个频道

### 🔗 协议统计
- HLS (m3u8): 108 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.5 KB)
- iptv_medium_latency.m3u (6.9 KB)
- iptv_high_latency.m3u (17.9 KB)
- iptv_optimized_combined.m3u (26.2 KB)
- tvbox_optimized.m3u (36.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (203.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 341.1 秒
