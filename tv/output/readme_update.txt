## IPTV智能优化系统更新报告

生成时间: 2025-11-04T06:26:37.754159

### 📊 总体统计
- 总频道数: 169
- TVBox优化频道数: 169

### 📈 分级统计
- 中等延迟 (<800ms): 74 个频道 (延迟: 平均 580.2ms, 最低 303.0ms)
- 可接受延迟 (<2s): 46 个频道 (延迟: 平均 1288.2ms, 最低 820.2ms)
- unacceptable: 30 个频道 (延迟: 平均 2974.8ms, 最低 2016.6ms)
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 213.5ms, 最低 174.2ms)

### 📁 频道分组
- : 169 个频道

### 🔗 协议统计
- HLS (m3u8): 145 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.3 KB)
- iptv_medium_latency.m3u (21.7 KB)
- iptv_high_latency.m3u (13.2 KB)
- iptv_optimized_combined.m3u (40.1 KB)
- tvbox_optimized.m3u (54.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (216.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 377.0 秒
