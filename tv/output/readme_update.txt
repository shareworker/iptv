## IPTV智能优化系统更新报告

生成时间: 2026-05-30T08:24:32.071356

### 📊 总体统计
- 总频道数: 152
- TVBox优化频道数: 152

### 📈 分级统计
- 中等延迟 (<800ms): 55 个频道 (延迟: 平均 556.7ms, 最低 311.0ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1316.2ms, 最低 832.7ms)
- unacceptable: 14 个频道 (延迟: 平均 3433.5ms, 最低 2003.0ms)
- 低延迟 (<300ms): 24 个频道 (延迟: 平均 205.0ms, 最低 150.9ms)

### 📁 频道分组
- : 152 个频道

### 🔗 协议统计
- HLS (m3u8): 129 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.8 KB)
- iptv_medium_latency.m3u (16.4 KB)
- iptv_high_latency.m3u (17.0 KB)
- iptv_optimized_combined.m3u (40.0 KB)
- tvbox_optimized.m3u (48.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 360.8 秒
