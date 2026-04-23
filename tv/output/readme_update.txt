## IPTV智能优化系统更新报告

生成时间: 2026-04-23T19:04:11.659050

### 📊 总体统计
- 总频道数: 150
- TVBox优化频道数: 150

### 📈 分级统计
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 208.5ms, 最低 175.2ms)
- 可接受延迟 (<2s): 68 个频道 (延迟: 平均 1355.8ms, 最低 836.7ms)
- unacceptable: 21 个频道 (延迟: 平均 4268.7ms, 最低 2154.9ms)
- 中等延迟 (<800ms): 45 个频道 (延迟: 平均 502.7ms, 最低 302.3ms)

### 📁 频道分组
- : 150 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 127 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (13.2 KB)
- iptv_high_latency.m3u (19.9 KB)
- iptv_optimized_combined.m3u (37.4 KB)
- tvbox_optimized.m3u (49.6 KB)
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
- 总耗时: 392.6 秒
