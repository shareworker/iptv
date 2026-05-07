## IPTV智能优化系统更新报告

生成时间: 2026-05-07T19:34:09.567917

### 📊 总体统计
- 总频道数: 145
- TVBox优化频道数: 145

### 📈 分级统计
- 中等延迟 (<800ms): 33 个频道 (延迟: 平均 522.4ms, 最低 312.7ms)
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 210.2ms, 最低 177.3ms)
- 可接受延迟 (<2s): 71 个频道 (延迟: 平均 1242.6ms, 最低 804.7ms)
- unacceptable: 22 个频道 (延迟: 平均 3629.3ms, 最低 2102.9ms)

### 📁 频道分组
- : 145 个频道

### 🔗 协议统计
- HLS (m3u8): 122 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.4 KB)
- iptv_medium_latency.m3u (9.7 KB)
- iptv_high_latency.m3u (20.7 KB)
- iptv_optimized_combined.m3u (35.6 KB)
- tvbox_optimized.m3u (48.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 383.9 秒
