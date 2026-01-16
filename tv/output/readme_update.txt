## IPTV智能优化系统更新报告

生成时间: 2026-01-16T18:27:42.379217

### 📊 总体统计
- 总频道数: 164
- TVBox优化频道数: 164

### 📈 分级统计
- 中等延迟 (<800ms): 77 个频道 (延迟: 平均 559.0ms, 最低 300.5ms)
- 可接受延迟 (<2s): 50 个频道 (延迟: 平均 1297.0ms, 最低 824.3ms)
- unacceptable: 19 个频道 (延迟: 平均 2984.3ms, 最低 2002.8ms)
- 低延迟 (<300ms): 18 个频道 (延迟: 平均 220.4ms, 最低 185.8ms)

### 📁 频道分组
- : 164 个频道

### 🔗 协议统计
- HLS (m3u8): 140 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.1 KB)
- iptv_medium_latency.m3u (22.6 KB)
- iptv_high_latency.m3u (14.5 KB)
- iptv_optimized_combined.m3u (42.0 KB)
- tvbox_optimized.m3u (52.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 373.9 秒
