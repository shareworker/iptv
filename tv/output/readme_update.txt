## IPTV智能优化系统更新报告

生成时间: 2025-09-30T14:52:48.299052

### 📊 总体统计
- 总频道数: 162
- TVBox优化频道数: 162

### 📈 分级统计
- 中等延迟 (<800ms): 70 个频道 (延迟: 平均 515.1ms, 最低 310.7ms)
- 可接受延迟 (<2s): 49 个频道 (延迟: 平均 1393.7ms, 最低 925.2ms)
- unacceptable: 23 个频道 (延迟: 平均 3055.3ms, 最低 2098.5ms)
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 192.7ms, 最低 148.6ms)
- 超低延迟 (<100ms): 1 个频道 (延迟: 平均 63.1ms, 最低 63.1ms)

### 📁 频道分组
- : 162 个频道

### 🔗 协议统计
- HLS (m3u8): 138 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_ultra_low_latency.m3u (0.3 KB)
- iptv_low_latency.m3u (5.3 KB)
- iptv_medium_latency.m3u (20.3 KB)
- iptv_high_latency.m3u (14.5 KB)
- iptv_optimized_combined.m3u (40.2 KB)
- tvbox_optimized.m3u (52.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 394.7 秒
