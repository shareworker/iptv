## IPTV智能优化系统更新报告

生成时间: 2025-11-12T06:27:01.525533

### 📊 总体统计
- 总频道数: 167
- TVBox优化频道数: 167

### 📈 分级统计
- 中等延迟 (<800ms): 56 个频道 (延迟: 平均 546.8ms, 最低 312.6ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1255.1ms, 最低 810.2ms)
- unacceptable: 34 个频道 (延迟: 平均 3565.1ms, 最低 2023.0ms)
- 低延迟 (<300ms): 18 个频道 (延迟: 平均 221.3ms, 最低 181.5ms)

### 📁 频道分组
- : 167 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 143 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.1 KB)
- iptv_medium_latency.m3u (16.1 KB)
- iptv_high_latency.m3u (17.7 KB)
- iptv_optimized_combined.m3u (38.7 KB)
- tvbox_optimized.m3u (54.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (216.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 396.1 秒
