## IPTV智能优化系统更新报告

生成时间: 2026-07-11T18:54:08.310000

### 📊 总体统计
- 总频道数: 138
- TVBox优化频道数: 138

### 📈 分级统计
- 低延迟 (<300ms): 28 个频道 (延迟: 平均 226.1ms, 最低 188.6ms)
- 中等延迟 (<800ms): 32 个频道 (延迟: 平均 559.9ms, 最低 348.7ms)
- 可接受延迟 (<2s): 68 个频道 (延迟: 平均 1195.0ms, 最低 810.7ms)
- unacceptable: 10 个频道 (延迟: 平均 5419.7ms, 最低 3851.4ms)

### 📁 频道分组
- : 138 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 115 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.3 KB)
- iptv_medium_latency.m3u (9.4 KB)
- iptv_high_latency.m3u (19.6 KB)
- iptv_optimized_combined.m3u (37.1 KB)
- tvbox_optimized.m3u (44.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 362.1 秒
