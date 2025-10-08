## IPTV智能优化系统更新报告

生成时间: 2025-10-08T18:25:38.445961

### 📊 总体统计
- 总频道数: 165
- TVBox优化频道数: 165

### 📈 分级统计
- 中等延迟 (<800ms): 44 个频道 (延迟: 平均 557.0ms, 最低 305.8ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1294.2ms, 最低 810.8ms)
- unacceptable: 24 个频道 (延迟: 平均 3081.0ms, 最低 2022.8ms)
- 低延迟 (<300ms): 36 个频道 (延迟: 平均 240.4ms, 最低 201.6ms)

### 📁 频道分组
- : 165 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 141 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (10.5 KB)
- iptv_medium_latency.m3u (12.5 KB)
- iptv_high_latency.m3u (17.8 KB)
- iptv_optimized_combined.m3u (40.7 KB)
- tvbox_optimized.m3u (52.2 KB)
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
- 总耗时: 395.9 秒
