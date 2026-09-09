## IPTV智能优化系统更新报告

生成时间: 2026-09-09T10:34:40.440041

### 📊 总体统计
- 总频道数: 117
- TVBox优化频道数: 117

### 📈 分级统计
- 中等延迟 (<800ms): 33 个频道 (延迟: 平均 556.0ms, 最低 317.7ms)
- 可接受延迟 (<2s): 66 个频道 (延迟: 平均 1247.6ms, 最低 805.8ms)
- 低延迟 (<300ms): 13 个频道 (延迟: 平均 262.8ms, 最低 249.0ms)
- unacceptable: 5 个频道 (延迟: 平均 4015.1ms, 最低 3166.5ms)

### 📁 频道分组
- : 117 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 95 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.7 KB)
- iptv_medium_latency.m3u (9.5 KB)
- iptv_high_latency.m3u (19.4 KB)
- iptv_optimized_combined.m3u (32.4 KB)
- tvbox_optimized.m3u (37.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (205.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 333.6 秒
