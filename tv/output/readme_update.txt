## IPTV智能优化系统更新报告

生成时间: 2026-01-27T06:31:45.269457

### 📊 总体统计
- 总频道数: 146
- TVBox优化频道数: 146

### 📈 分级统计
- 低延迟 (<300ms): 8 个频道 (延迟: 平均 243.3ms, 最低 219.0ms)
- 中等延迟 (<800ms): 61 个频道 (延迟: 平均 506.8ms, 最低 305.9ms)
- 可接受延迟 (<2s): 62 个频道 (延迟: 平均 1145.6ms, 最低 814.6ms)
- unacceptable: 15 个频道 (延迟: 平均 3165.0ms, 最低 2288.4ms)

### 📁 频道分组
- : 146 个频道

### 🔗 协议统计
- HLS (m3u8): 137 个频道
- HTTP: 7 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (2.3 KB)
- iptv_medium_latency.m3u (18.1 KB)
- iptv_high_latency.m3u (17.9 KB)
- iptv_optimized_combined.m3u (38.1 KB)
- tvbox_optimized.m3u (46.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 440.3 秒
