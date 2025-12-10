## IPTV智能优化系统更新报告

生成时间: 2025-12-10T18:28:00.427601

### 📊 总体统计
- 总频道数: 154
- TVBox优化频道数: 154

### 📈 分级统计
- 中等延迟 (<800ms): 58 个频道 (延迟: 平均 526.3ms, 最低 324.4ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1272.7ms, 最低 808.9ms)
- unacceptable: 12 个频道 (延迟: 平均 6490.6ms, 最低 2133.8ms)
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 251.5ms, 最低 199.8ms)

### 📁 频道分组
- : 154 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 130 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.8 KB)
- iptv_medium_latency.m3u (16.6 KB)
- iptv_high_latency.m3u (18.3 KB)
- iptv_optimized_combined.m3u (41.4 KB)
- tvbox_optimized.m3u (48.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 394.6 秒
