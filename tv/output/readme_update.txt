## IPTV智能优化系统更新报告

生成时间: 2026-10-11T21:23:00.346343

### 📊 总体统计
- 总频道数: 116
- TVBox优化频道数: 116

### 📈 分级统计
- 中等延迟 (<800ms): 58 个频道 (延迟: 平均 532.5ms, 最低 303.4ms)
- 可接受延迟 (<2s): 31 个频道 (延迟: 平均 1131.5ms, 最低 847.1ms)
- 低延迟 (<300ms): 21 个频道 (延迟: 平均 188.8ms, 最低 139.2ms)
- unacceptable: 6 个频道 (延迟: 平均 5543.5ms, 最低 3417.8ms)

### 📁 频道分组
- : 116 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 93 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.9 KB)
- iptv_medium_latency.m3u (17.3 KB)
- iptv_high_latency.m3u (9.0 KB)
- iptv_optimized_combined.m3u (32.1 KB)
- tvbox_optimized.m3u (36.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (205.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 316.9 秒
