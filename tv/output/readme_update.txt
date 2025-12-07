## IPTV智能优化系统更新报告

生成时间: 2025-12-07T06:25:43.224131

### 📊 总体统计
- 总频道数: 163
- TVBox优化频道数: 163

### 📈 分级统计
- 中等延迟 (<800ms): 73 个频道 (延迟: 平均 580.0ms, 最低 335.0ms)
- 可接受延迟 (<2s): 50 个频道 (延迟: 平均 1440.8ms, 最低 829.7ms)
- unacceptable: 26 个频道 (延迟: 平均 4731.4ms, 最低 2030.6ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 231.3ms, 最低 201.8ms)

### 📁 频道分组
- : 163 个频道

### 🔗 协议统计
- HTTP: 19 个频道
- HLS (m3u8): 142 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.0 KB)
- iptv_medium_latency.m3u (21.3 KB)
- iptv_high_latency.m3u (14.8 KB)
- iptv_optimized_combined.m3u (39.8 KB)
- tvbox_optimized.m3u (52.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 427.4 秒
