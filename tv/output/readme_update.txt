## IPTV智能优化系统更新报告

生成时间: 2026-02-13T06:56:07.488084

### 📊 总体统计
- 总频道数: 147
- TVBox优化频道数: 147

### 📈 分级统计
- 中等延迟 (<800ms): 50 个频道 (延迟: 平均 498.8ms, 最低 311.9ms)
- 可接受延迟 (<2s): 58 个频道 (延迟: 平均 1166.0ms, 最低 814.2ms)
- unacceptable: 22 个频道 (延迟: 平均 2787.8ms, 最低 2093.4ms)
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 217.0ms, 最低 182.7ms)

### 📁 频道分组
- : 147 个频道

### 🔗 协议统计
- HLS (m3u8): 123 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (14.8 KB)
- iptv_high_latency.m3u (16.7 KB)
- iptv_optimized_combined.m3u (36.2 KB)
- tvbox_optimized.m3u (47.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 367.5 秒
