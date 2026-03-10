## IPTV智能优化系统更新报告

生成时间: 2026-03-10T06:45:00.221959

### 📊 总体统计
- 总频道数: 157
- TVBox优化频道数: 157

### 📈 分级统计
- 中等延迟 (<800ms): 56 个频道 (延迟: 平均 580.2ms, 最低 321.6ms)
- unacceptable: 28 个频道 (延迟: 平均 2936.3ms, 最低 2064.5ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1261.9ms, 最低 804.0ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 195.6ms, 最低 134.2ms)

### 📁 频道分组
- : 157 个频道

### 🔗 协议统计
- HLS (m3u8): 134 个频道
- HTTP: 21 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.1 KB)
- iptv_medium_latency.m3u (16.4 KB)
- iptv_high_latency.m3u (17.0 KB)
- iptv_optimized_combined.m3u (37.4 KB)
- tvbox_optimized.m3u (51.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 400.8 秒
