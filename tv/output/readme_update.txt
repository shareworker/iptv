## IPTV智能优化系统更新报告

生成时间: 2026-01-17T06:26:46.774542

### 📊 总体统计
- 总频道数: 158
- TVBox优化频道数: 158

### 📈 分级统计
- 中等延迟 (<800ms): 42 个频道 (延迟: 平均 536.7ms, 最低 311.1ms)
- 可接受延迟 (<2s): 77 个频道 (延迟: 平均 1318.3ms, 最低 810.2ms)
- unacceptable: 13 个频道 (延迟: 平均 2550.0ms, 最低 2241.8ms)
- 低延迟 (<300ms): 26 个频道 (延迟: 平均 239.8ms, 最低 201.8ms)

### 📁 频道分组
- : 158 个频道

### 🔗 协议统计
- HLS (m3u8): 134 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.7 KB)
- iptv_medium_latency.m3u (12.1 KB)
- iptv_high_latency.m3u (22.5 KB)
- iptv_optimized_combined.m3u (42.1 KB)
- tvbox_optimized.m3u (51.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 372.5 秒
