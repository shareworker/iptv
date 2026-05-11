## IPTV智能优化系统更新报告

生成时间: 2026-05-11T19:34:54.464539

### 📊 总体统计
- 总频道数: 151
- TVBox优化频道数: 151

### 📈 分级统计
- 低延迟 (<300ms): 21 个频道 (延迟: 平均 224.0ms, 最低 188.0ms)
- 中等延迟 (<800ms): 68 个频道 (延迟: 平均 543.7ms, 最低 309.9ms)
- 可接受延迟 (<2s): 53 个频道 (延迟: 平均 1300.6ms, 最低 831.6ms)
- unacceptable: 9 个频道 (延迟: 平均 2846.7ms, 最低 2237.0ms)

### 📁 频道分组
- : 151 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 128 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.0 KB)
- iptv_medium_latency.m3u (20.2 KB)
- iptv_high_latency.m3u (15.3 KB)
- iptv_optimized_combined.m3u (41.3 KB)
- tvbox_optimized.m3u (47.9 KB)
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
- 总耗时: 383.5 秒
