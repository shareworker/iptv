## IPTV智能优化系统更新报告

生成时间: 2025-12-16T06:28:45.090456

### 📊 总体统计
- 总频道数: 153
- TVBox优化频道数: 153

### 📈 分级统计
- 中等延迟 (<800ms): 72 个频道 (延迟: 平均 540.0ms, 最低 306.6ms)
- 可接受延迟 (<2s): 46 个频道 (延迟: 平均 1426.0ms, 最低 838.4ms)
- unacceptable: 18 个频道 (延迟: 平均 2707.7ms, 最低 2084.8ms)
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 192.4ms, 最低 146.5ms)

### 📁 频道分组
- : 153 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 129 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (21.0 KB)
- iptv_high_latency.m3u (13.7 KB)
- iptv_optimized_combined.m3u (39.3 KB)
- tvbox_optimized.m3u (49.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 373.3 秒
