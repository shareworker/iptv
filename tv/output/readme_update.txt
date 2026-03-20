## IPTV智能优化系统更新报告

生成时间: 2026-03-20T06:52:00.351769

### 📊 总体统计
- 总频道数: 141
- TVBox优化频道数: 141

### 📈 分级统计
- 中等延迟 (<800ms): 47 个频道 (延迟: 平均 552.3ms, 最低 303.2ms)
- 可接受延迟 (<2s): 56 个频道 (延迟: 平均 1255.0ms, 最低 808.2ms)
- unacceptable: 35 个频道 (延迟: 平均 3039.1ms, 最低 2052.1ms)
- 低延迟 (<300ms): 3 个频道 (延迟: 平均 239.5ms, 最低 188.3ms)

### 📁 频道分组
- : 141 个频道

### 🔗 协议统计
- HLS (m3u8): 134 个频道
- HTTP: 5 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (0.9 KB)
- iptv_medium_latency.m3u (13.9 KB)
- iptv_high_latency.m3u (16.1 KB)
- iptv_optimized_combined.m3u (30.8 KB)
- tvbox_optimized.m3u (46.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (210.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 512.6 秒
