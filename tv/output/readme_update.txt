## IPTV智能优化系统更新报告

生成时间: 2025-12-20T18:23:52.222127

### 📊 总体统计
- 总频道数: 164
- TVBox优化频道数: 164

### 📈 分级统计
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 209.5ms, 最低 174.7ms)
- 中等延迟 (<800ms): 64 个频道 (延迟: 平均 541.1ms, 最低 338.8ms)
- 可接受延迟 (<2s): 65 个频道 (延迟: 平均 1365.2ms, 最低 802.6ms)
- unacceptable: 19 个频道 (延迟: 平均 4430.3ms, 最低 2055.1ms)

### 📁 频道分组
- : 164 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 140 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.6 KB)
- iptv_medium_latency.m3u (19.0 KB)
- iptv_high_latency.m3u (18.8 KB)
- iptv_optimized_combined.m3u (42.2 KB)
- tvbox_optimized.m3u (53.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 377.5 秒
