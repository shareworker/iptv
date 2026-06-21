## IPTV智能优化系统更新报告

生成时间: 2026-06-21T09:44:54.682206

### 📊 总体统计
- 总频道数: 148
- TVBox优化频道数: 148

### 📈 分级统计
- 可接受延迟 (<2s): 67 个频道 (延迟: 平均 1312.0ms, 最低 815.6ms)
- unacceptable: 27 个频道 (延迟: 平均 3408.9ms, 最低 2002.0ms)
- 中等延迟 (<800ms): 43 个频道 (延迟: 平均 566.9ms, 最低 323.5ms)
- 低延迟 (<300ms): 11 个频道 (延迟: 平均 229.2ms, 最低 203.1ms)

### 📁 频道分组
- : 148 个频道

### 🔗 协议统计
- HLS (m3u8): 125 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.1 KB)
- iptv_medium_latency.m3u (12.6 KB)
- iptv_high_latency.m3u (19.4 KB)
- iptv_optimized_combined.m3u (34.9 KB)
- tvbox_optimized.m3u (48.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 426.2 秒
