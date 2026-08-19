## IPTV智能优化系统更新报告

生成时间: 2026-08-19T18:26:17.036640

### 📊 总体统计
- 总频道数: 129
- TVBox优化频道数: 129

### 📈 分级统计
- 低延迟 (<300ms): 24 个频道 (延迟: 平均 187.8ms, 最低 146.8ms)
- 中等延迟 (<800ms): 76 个频道 (延迟: 平均 578.8ms, 最低 304.5ms)
- 可接受延迟 (<2s): 24 个频道 (延迟: 平均 1166.8ms, 最低 801.0ms)
- unacceptable: 5 个频道 (延迟: 平均 2388.8ms, 最低 2300.7ms)

### 📁 频道分组
- : 129 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 106 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.7 KB)
- iptv_medium_latency.m3u (22.3 KB)
- iptv_high_latency.m3u (7.2 KB)
- iptv_optimized_combined.m3u (36.1 KB)
- tvbox_optimized.m3u (39.6 KB)
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
- 总耗时: 318.8 秒
