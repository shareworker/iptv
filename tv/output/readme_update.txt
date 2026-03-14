## IPTV智能优化系统更新报告

生成时间: 2026-03-14T06:44:08.798747

### 📊 总体统计
- 总频道数: 130
- TVBox优化频道数: 130

### 📈 分级统计
- 低延迟 (<300ms): 10 个频道 (延迟: 平均 259.3ms, 最低 212.2ms)
- 可接受延迟 (<2s): 51 个频道 (延迟: 平均 1347.6ms, 最低 809.8ms)
- 中等延迟 (<800ms): 47 个频道 (延迟: 平均 577.5ms, 最低 368.8ms)
- unacceptable: 22 个频道 (延迟: 平均 5092.6ms, 最低 2020.0ms)

### 📁 频道分组
- : 130 个频道

### 🔗 协议统计
- HLS (m3u8): 128 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (2.9 KB)
- iptv_medium_latency.m3u (13.9 KB)
- iptv_high_latency.m3u (15.1 KB)
- iptv_optimized_combined.m3u (31.7 KB)
- tvbox_optimized.m3u (42.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 478.7 秒
