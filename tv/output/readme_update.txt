## IPTV智能优化系统更新报告

生成时间: 2026-01-01T06:28:49.260808

### 📊 总体统计
- 总频道数: 167
- TVBox优化频道数: 167

### 📈 分级统计
- 中等延迟 (<800ms): 61 个频道 (延迟: 平均 579.5ms, 最低 313.2ms)
- 可接受延迟 (<2s): 57 个频道 (延迟: 平均 1296.7ms, 最低 800.6ms)
- unacceptable: 20 个频道 (延迟: 平均 4098.3ms, 最低 2101.1ms)
- 低延迟 (<300ms): 29 个频道 (延迟: 平均 194.8ms, 最低 148.5ms)

### 📁 频道分组
- : 167 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 143 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.5 KB)
- iptv_medium_latency.m3u (17.7 KB)
- iptv_high_latency.m3u (16.6 KB)
- iptv_optimized_combined.m3u (42.6 KB)
- tvbox_optimized.m3u (54.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 376.5 秒
