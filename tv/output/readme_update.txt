## IPTV智能优化系统更新报告

生成时间: 2026-02-19T18:47:09.805560

### 📊 总体统计
- 总频道数: 143
- TVBox优化频道数: 143

### 📈 分级统计
- 中等延迟 (<800ms): 52 个频道 (延迟: 平均 553.1ms, 最低 308.9ms)
- 可接受延迟 (<2s): 45 个频道 (延迟: 平均 1263.2ms, 最低 837.4ms)
- unacceptable: 30 个频道 (延迟: 平均 2592.4ms, 最低 2059.8ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 212.7ms, 最低 184.5ms)

### 📁 频道分组
- : 143 个频道

### 🔗 协议统计
- HLS (m3u8): 119 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (15.2 KB)
- iptv_high_latency.m3u (13.1 KB)
- iptv_optimized_combined.m3u (32.7 KB)
- tvbox_optimized.m3u (46.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 369.9 秒
