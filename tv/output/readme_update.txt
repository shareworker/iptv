## IPTV智能优化系统更新报告

生成时间: 2026-03-13T18:37:13.721129

### 📊 总体统计
- 总频道数: 156
- TVBox优化频道数: 156

### 📈 分级统计
- 低延迟 (<300ms): 33 个频道 (延迟: 平均 224.8ms, 最低 151.7ms)
- 中等延迟 (<800ms): 55 个频道 (延迟: 平均 525.3ms, 最低 301.4ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1318.3ms, 最低 804.9ms)
- unacceptable: 9 个频道 (延迟: 平均 3735.0ms, 最低 2402.2ms)

### 📁 频道分组
- : 156 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 132 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (9.5 KB)
- iptv_medium_latency.m3u (15.9 KB)
- iptv_high_latency.m3u (17.5 KB)
- iptv_optimized_combined.m3u (42.7 KB)
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
- 总耗时: 383.6 秒
