## IPTV智能优化系统更新报告

生成时间: 2026-01-19T06:36:59.579920

### 📊 总体统计
- 总频道数: 141
- TVBox优化频道数: 141

### 📈 分级统计
- 中等延迟 (<800ms): 40 个频道 (延迟: 平均 597.5ms, 最低 306.2ms)
- 可接受延迟 (<2s): 74 个频道 (延迟: 平均 1143.1ms, 最低 803.5ms)
- unacceptable: 14 个频道 (延迟: 平均 3453.4ms, 最低 2115.8ms)
- 低延迟 (<300ms): 13 个频道 (延迟: 平均 249.8ms, 最低 200.5ms)

### 📁 频道分组
- : 141 个频道

### 🔗 协议统计
- HLS (m3u8): 139 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.1 KB)
- iptv_medium_latency.m3u (11.8 KB)
- iptv_high_latency.m3u (21.2 KB)
- iptv_optimized_combined.m3u (37.0 KB)
- tvbox_optimized.m3u (45.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (210.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 546.4 秒
