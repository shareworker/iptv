## IPTV智能优化系统更新报告

生成时间: 2025-11-05T18:25:00.740789

### 📊 总体统计
- 总频道数: 166
- TVBox优化频道数: 166

### 📈 分级统计
- 中等延迟 (<800ms): 45 个频道 (延迟: 平均 583.8ms, 最低 321.6ms)
- 可接受延迟 (<2s): 76 个频道 (延迟: 平均 1279.0ms, 最低 808.0ms)
- unacceptable: 25 个频道 (延迟: 平均 2875.2ms, 最低 2000.0ms)
- 低延迟 (<300ms): 20 个频道 (延迟: 平均 221.8ms, 最低 181.5ms)

### 📁 频道分组
- : 166 个频道

### 🔗 协议统计
- HLS (m3u8): 142 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.7 KB)
- iptv_medium_latency.m3u (13.4 KB)
- iptv_high_latency.m3u (22.1 KB)
- iptv_optimized_combined.m3u (41.0 KB)
- tvbox_optimized.m3u (54.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 378.8 秒
