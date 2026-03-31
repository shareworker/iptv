## IPTV智能优化系统更新报告

生成时间: 2026-03-31T07:11:16.280446

### 📊 总体统计
- 总频道数: 143
- TVBox优化频道数: 143

### 📈 分级统计
- 中等延迟 (<800ms): 39 个频道 (延迟: 平均 547.7ms, 最低 318.2ms)
- 可接受延迟 (<2s): 53 个频道 (延迟: 平均 1487.4ms, 最低 918.0ms)
- unacceptable: 37 个频道 (延迟: 平均 3039.5ms, 最低 2116.5ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 243.5ms, 最低 205.9ms)

### 📁 频道分组
- : 143 个频道

### 🔗 协议统计
- HLS (m3u8): 128 个频道
- HTTP: 13 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (11.3 KB)
- iptv_high_latency.m3u (15.4 KB)
- iptv_optimized_combined.m3u (30.7 KB)
- tvbox_optimized.m3u (47.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 463.4 秒
