## IPTV智能优化系统更新报告

生成时间: 2026-09-07T21:01:51.809621

### 📊 总体统计
- 总频道数: 132
- TVBox优化频道数: 132

### 📈 分级统计
- 中等延迟 (<800ms): 45 个频道 (延迟: 平均 602.4ms, 最低 319.5ms)
- 可接受延迟 (<2s): 65 个频道 (延迟: 平均 1202.0ms, 最低 800.8ms)
- unacceptable: 9 个频道 (延迟: 平均 3135.9ms, 最低 2027.7ms)
- 低延迟 (<300ms): 13 个频道 (延迟: 平均 197.3ms, 最低 175.5ms)

### 📁 频道分组
- : 132 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 109 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.7 KB)
- iptv_medium_latency.m3u (13.3 KB)
- iptv_high_latency.m3u (18.9 KB)
- iptv_optimized_combined.m3u (35.7 KB)
- tvbox_optimized.m3u (43.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 333.5 秒
