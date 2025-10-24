## IPTV智能优化系统更新报告

生成时间: 2025-10-24T06:25:37.524796

### 📊 总体统计
- 总频道数: 158
- TVBox优化频道数: 158

### 📈 分级统计
- 中等延迟 (<800ms): 36 个频道 (延迟: 平均 523.6ms, 最低 314.4ms)
- 可接受延迟 (<2s): 84 个频道 (延迟: 平均 1399.4ms, 最低 870.0ms)
- unacceptable: 25 个频道 (延迟: 平均 4944.0ms, 最低 2077.6ms)
- 低延迟 (<300ms): 13 个频道 (延迟: 平均 212.7ms, 最低 195.7ms)

### 📁 频道分组
- : 158 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 134 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.7 KB)
- iptv_medium_latency.m3u (10.5 KB)
- iptv_high_latency.m3u (24.1 KB)
- iptv_optimized_combined.m3u (38.1 KB)
- tvbox_optimized.m3u (52.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 395.1 秒
