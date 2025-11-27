## IPTV智能优化系统更新报告

生成时间: 2025-11-27T06:27:27.438715

### 📊 总体统计
- 总频道数: 165
- TVBox优化频道数: 165

### 📈 分级统计
- 可接受延迟 (<2s): 74 个频道 (延迟: 平均 1160.5ms, 最低 811.1ms)
- 中等延迟 (<800ms): 59 个频道 (延迟: 平均 452.9ms, 最低 302.9ms)
- unacceptable: 15 个频道 (延迟: 平均 3498.3ms, 最低 2000.8ms)
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 207.9ms, 最低 161.0ms)

### 📁 频道分组
- : 165 个频道

### 🔗 协议统计
- HLS (m3u8): 141 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (17.1 KB)
- iptv_high_latency.m3u (21.9 KB)
- iptv_optimized_combined.m3u (43.7 KB)
- tvbox_optimized.m3u (52.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 368.6 秒
