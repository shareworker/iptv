## IPTV智能优化系统更新报告

生成时间: 2026-07-13T19:20:27.952330

### 📊 总体统计
- 总频道数: 133
- TVBox优化频道数: 133

### 📈 分级统计
- 低延迟 (<300ms): 33 个频道 (延迟: 平均 217.4ms, 最低 146.6ms)
- 可接受延迟 (<2s): 47 个频道 (延迟: 平均 1049.1ms, 最低 812.7ms)
- unacceptable: 8 个频道 (延迟: 平均 3083.2ms, 最低 2626.9ms)
- 中等延迟 (<800ms): 45 个频道 (延迟: 平均 570.0ms, 最低 307.7ms)

### 📁 频道分组
- : 133 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 110 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (9.4 KB)
- iptv_medium_latency.m3u (13.3 KB)
- iptv_high_latency.m3u (13.7 KB)
- iptv_optimized_combined.m3u (36.2 KB)
- tvbox_optimized.m3u (41.4 KB)
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
- 总耗时: 363.6 秒
