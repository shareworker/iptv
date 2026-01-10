## IPTV智能优化系统更新报告

生成时间: 2026-01-10T18:26:58.535240

### 📊 总体统计
- 总频道数: 133
- TVBox优化频道数: 133

### 📈 分级统计
- 中等延迟 (<800ms): 50 个频道 (延迟: 平均 601.0ms, 最低 308.9ms)
- 可接受延迟 (<2s): 58 个频道 (延迟: 平均 1236.5ms, 最低 822.7ms)
- unacceptable: 13 个频道 (延迟: 平均 4891.4ms, 最低 2070.5ms)
- 低延迟 (<300ms): 12 个频道 (延迟: 平均 195.3ms, 最低 147.4ms)

### 📁 频道分组
- : 133 个频道

### 🔗 协议统计
- HLS (m3u8): 115 个频道
- HTTP: 16 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.4 KB)
- iptv_medium_latency.m3u (14.9 KB)
- iptv_high_latency.m3u (16.7 KB)
- iptv_optimized_combined.m3u (34.8 KB)
- tvbox_optimized.m3u (42.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 436.3 秒
