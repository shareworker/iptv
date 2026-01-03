## IPTV智能优化系统更新报告

生成时间: 2026-01-03T18:25:02.600368

### 📊 总体统计
- 总频道数: 165
- TVBox优化频道数: 165

### 📈 分级统计
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 229.5ms, 最低 201.2ms)
- 中等延迟 (<800ms): 54 个频道 (延迟: 平均 573.8ms, 最低 316.3ms)
- 可接受延迟 (<2s): 67 个频道 (延迟: 平均 1470.8ms, 最低 810.4ms)
- unacceptable: 27 个频道 (延迟: 平均 2998.7ms, 最低 2076.3ms)

### 📁 频道分组
- : 165 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 141 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (15.9 KB)
- iptv_high_latency.m3u (19.4 KB)
- iptv_optimized_combined.m3u (39.9 KB)
- tvbox_optimized.m3u (53.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 378.7 秒
