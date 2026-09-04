## IPTV智能优化系统更新报告

生成时间: 2026-09-04T20:10:44.287983

### 📊 总体统计
- 总频道数: 129
- TVBox优化频道数: 129

### 📈 分级统计
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 229.3ms, 最低 194.7ms)
- 中等延迟 (<800ms): 32 个频道 (延迟: 平均 500.3ms, 最低 326.8ms)
- 可接受延迟 (<2s): 71 个频道 (延迟: 平均 1197.5ms, 最低 804.8ms)
- unacceptable: 10 个频道 (延迟: 平均 3403.7ms, 最低 2012.2ms)

### 📁 频道分组
- : 129 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 106 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (9.5 KB)
- iptv_high_latency.m3u (20.7 KB)
- iptv_optimized_combined.m3u (34.5 KB)
- tvbox_optimized.m3u (41.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 334.9 秒
