## IPTV智能优化系统更新报告

生成时间: 2026-02-22T06:43:34.349093

### 📊 总体统计
- 总频道数: 146
- TVBox优化频道数: 146

### 📈 分级统计
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 220.7ms, 最低 174.4ms)
- 中等延迟 (<800ms): 41 个频道 (延迟: 平均 645.2ms, 最低 317.3ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1300.0ms, 最低 800.5ms)
- unacceptable: 27 个频道 (延迟: 平均 2890.5ms, 最低 2058.4ms)

### 📁 频道分组
- : 146 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 122 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (12.0 KB)
- iptv_high_latency.m3u (17.9 KB)
- iptv_optimized_combined.m3u (34.5 KB)
- tvbox_optimized.m3u (47.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 374.8 秒
