## IPTV智能优化系统更新报告

生成时间: 2025-10-01T06:26:42.911175

### 📊 总体统计
- 总频道数: 164
- TVBox优化频道数: 164

### 📈 分级统计
- 中等延迟 (<800ms): 52 个频道 (延迟: 平均 612.0ms, 最低 312.7ms)
- 可接受延迟 (<2s): 65 个频道 (延迟: 平均 1395.9ms, 最低 807.3ms)
- unacceptable: 29 个频道 (延迟: 平均 3882.0ms, 最低 2008.1ms)
- 低延迟 (<300ms): 18 个频道 (延迟: 平均 230.0ms, 最低 184.1ms)

### 📁 频道分组
- : 164 个频道

### 🔗 协议统计
- HLS (m3u8): 146 个频道
- HTTP: 16 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.3 KB)
- iptv_medium_latency.m3u (14.8 KB)
- iptv_high_latency.m3u (19.0 KB)
- iptv_optimized_combined.m3u (38.9 KB)
- tvbox_optimized.m3u (53.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 449.9 秒
