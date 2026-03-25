## IPTV智能优化系统更新报告

生成时间: 2026-03-25T18:51:15.332646

### 📊 总体统计
- 总频道数: 156
- TVBox优化频道数: 156

### 📈 分级统计
- 中等延迟 (<800ms): 39 个频道 (延迟: 平均 517.4ms, 最低 304.3ms)
- 可接受延迟 (<2s): 71 个频道 (延迟: 平均 1209.6ms, 最低 801.1ms)
- unacceptable: 14 个频道 (延迟: 平均 3974.5ms, 最低 2015.8ms)
- 低延迟 (<300ms): 31 个频道 (延迟: 平均 204.9ms, 最低 146.8ms)
- 超低延迟 (<100ms): 1 个频道 (延迟: 平均 32.3ms, 最低 32.3ms)

### 📁 频道分组
- : 156 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 132 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_ultra_low_latency.m3u (0.5 KB)
- iptv_low_latency.m3u (9.1 KB)
- iptv_medium_latency.m3u (11.2 KB)
- iptv_high_latency.m3u (20.6 KB)
- iptv_optimized_combined.m3u (41.2 KB)
- tvbox_optimized.m3u (50.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 381.9 秒
