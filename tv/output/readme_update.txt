## IPTV智能优化系统更新报告

生成时间: 2026-04-12T07:13:16.113121

### 📊 总体统计
- 总频道数: 128
- TVBox优化频道数: 128

### 📈 分级统计
- 低延迟 (<300ms): 2 个频道 (延迟: 平均 260.3ms, 最低 251.1ms)
- 中等延迟 (<800ms): 34 个频道 (延迟: 平均 560.4ms, 最低 337.5ms)
- 可接受延迟 (<2s): 55 个频道 (延迟: 平均 1256.1ms, 最低 844.6ms)
- unacceptable: 37 个频道 (延迟: 平均 3385.9ms, 最低 2109.4ms)

### 📁 频道分组
- : 128 个频道

### 🔗 协议统计
- HLS (m3u8): 127 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (0.7 KB)
- iptv_medium_latency.m3u (10.0 KB)
- iptv_high_latency.m3u (16.1 KB)
- iptv_optimized_combined.m3u (26.5 KB)
- tvbox_optimized.m3u (43.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 515.9 秒
