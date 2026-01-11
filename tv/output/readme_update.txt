## IPTV智能优化系统更新报告

生成时间: 2026-01-11T18:25:50.525694

### 📊 总体统计
- 总频道数: 142
- TVBox优化频道数: 142

### 📈 分级统计
- 中等延迟 (<800ms): 48 个频道 (延迟: 平均 554.3ms, 最低 343.9ms)
- 可接受延迟 (<2s): 63 个频道 (延迟: 平均 1297.2ms, 最低 821.4ms)
- unacceptable: 13 个频道 (延迟: 平均 2226.3ms, 最低 2064.2ms)
- 低延迟 (<300ms): 18 个频道 (延迟: 平均 213.3ms, 最低 174.0ms)

### 📁 频道分组
- : 142 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 118 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.0 KB)
- iptv_medium_latency.m3u (14.1 KB)
- iptv_high_latency.m3u (18.2 KB)
- iptv_optimized_combined.m3u (37.2 KB)
- tvbox_optimized.m3u (45.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (210.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 376.8 秒
