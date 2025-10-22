## IPTV智能优化系统更新报告

生成时间: 2025-10-22T18:26:00.855755

### 📊 总体统计
- 总频道数: 151
- TVBox优化频道数: 151

### 📈 分级统计
- 中等延迟 (<800ms): 55 个频道 (延迟: 平均 544.8ms, 最低 316.1ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1298.4ms, 最低 831.2ms)
- unacceptable: 14 个频道 (延迟: 平均 2908.7ms, 最低 2007.9ms)
- 低延迟 (<300ms): 21 个频道 (延迟: 平均 203.4ms, 最低 146.9ms)

### 📁 频道分组
- : 151 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 127 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.9 KB)
- iptv_medium_latency.m3u (15.7 KB)
- iptv_high_latency.m3u (18.1 KB)
- iptv_optimized_combined.m3u (39.6 KB)
- tvbox_optimized.m3u (48.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 365.9 秒
