## IPTV智能优化系统更新报告

生成时间: 2025-10-15T18:25:45.405851

### 📊 总体统计
- 总频道数: 157
- TVBox优化频道数: 157

### 📈 分级统计
- 中等延迟 (<800ms): 48 个频道 (延迟: 平均 573.3ms, 最低 300.0ms)
- 可接受延迟 (<2s): 66 个频道 (延迟: 平均 1225.6ms, 最低 809.4ms)
- unacceptable: 14 个频道 (延迟: 平均 3177.3ms, 最低 2195.6ms)
- 低延迟 (<300ms): 29 个频道 (延迟: 平均 200.0ms, 最低 150.9ms)

### 📁 频道分组
- : 157 个频道

### 🔗 协议统计
- HLS (m3u8): 133 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.3 KB)
- iptv_medium_latency.m3u (14.1 KB)
- iptv_high_latency.m3u (19.2 KB)
- iptv_optimized_combined.m3u (41.4 KB)
- tvbox_optimized.m3u (50.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 397.9 秒
