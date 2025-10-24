## IPTV智能优化系统更新报告

生成时间: 2025-10-24T18:25:25.613603

### 📊 总体统计
- 总频道数: 157
- TVBox优化频道数: 157

### 📈 分级统计
- 中等延迟 (<800ms): 38 个频道 (延迟: 平均 542.4ms, 最低 326.4ms)
- 可接受延迟 (<2s): 84 个频道 (延迟: 平均 1305.5ms, 最低 803.2ms)
- unacceptable: 6 个频道 (延迟: 平均 3076.9ms, 最低 2395.0ms)
- 低延迟 (<300ms): 29 个频道 (延迟: 平均 189.4ms, 最低 146.1ms)

### 📁 频道分组
- : 157 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 133 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.4 KB)
- iptv_medium_latency.m3u (11.0 KB)
- iptv_high_latency.m3u (24.5 KB)
- iptv_optimized_combined.m3u (43.7 KB)
- tvbox_optimized.m3u (50.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 382.7 秒
