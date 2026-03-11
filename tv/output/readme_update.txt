## IPTV智能优化系统更新报告

生成时间: 2026-03-11T06:49:09.259818

### 📊 总体统计
- 总频道数: 148
- TVBox优化频道数: 148

### 📈 分级统计
- 中等延迟 (<800ms): 49 个频道 (延迟: 平均 559.0ms, 最低 319.9ms)
- unacceptable: 18 个频道 (延迟: 平均 3319.0ms, 最低 2032.8ms)
- 可接受延迟 (<2s): 69 个频道 (延迟: 平均 1372.6ms, 最低 803.5ms)
- 低延迟 (<300ms): 12 个频道 (延迟: 平均 238.5ms, 最低 184.0ms)

### 📁 频道分组
- : 148 个频道

### 🔗 协议统计
- HLS (m3u8): 133 个频道
- HTTP: 13 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.6 KB)
- iptv_medium_latency.m3u (14.0 KB)
- iptv_high_latency.m3u (20.5 KB)
- iptv_optimized_combined.m3u (37.9 KB)
- tvbox_optimized.m3u (48.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 456.6 秒
