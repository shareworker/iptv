## IPTV智能优化系统更新报告

生成时间: 2026-02-15T18:30:55.782235

### 📊 总体统计
- 总频道数: 144
- TVBox优化频道数: 144

### 📈 分级统计
- 中等延迟 (<800ms): 55 个频道 (延迟: 平均 611.2ms, 最低 321.8ms)
- 可接受延迟 (<2s): 39 个频道 (延迟: 平均 1446.9ms, 最低 942.7ms)
- unacceptable: 27 个频道 (延迟: 平均 2791.1ms, 最低 2029.0ms)
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 220.6ms, 最低 175.3ms)

### 📁 频道分组
- : 144 个频道

### 🔗 协议统计
- HLS (m3u8): 120 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.7 KB)
- iptv_medium_latency.m3u (16.0 KB)
- iptv_high_latency.m3u (11.3 KB)
- iptv_optimized_combined.m3u (33.9 KB)
- tvbox_optimized.m3u (46.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 375.4 秒
