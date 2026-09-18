## IPTV智能优化系统更新报告

生成时间: 2026-09-18T10:24:16.389747

### 📊 总体统计
- 总频道数: 125
- TVBox优化频道数: 125

### 📈 分级统计
- 低延迟 (<300ms): 21 个频道 (延迟: 平均 195.2ms, 最低 147.9ms)
- 中等延迟 (<800ms): 53 个频道 (延迟: 平均 573.0ms, 最低 307.2ms)
- 可接受延迟 (<2s): 49 个频道 (延迟: 平均 1146.5ms, 最低 810.9ms)
- unacceptable: 2 个频道 (延迟: 平均 2286.2ms, 最低 2127.9ms)

### 📁 频道分组
- : 125 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 102 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.9 KB)
- iptv_medium_latency.m3u (15.4 KB)
- iptv_high_latency.m3u (14.6 KB)
- iptv_optimized_combined.m3u (35.7 KB)
- tvbox_optimized.m3u (39.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 337.8 秒
