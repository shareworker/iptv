## IPTV智能优化系统更新报告

生成时间: 2025-12-21T18:24:46.619253

### 📊 总体统计
- 总频道数: 154
- TVBox优化频道数: 154

### 📈 分级统计
- 中等延迟 (<800ms): 69 个频道 (延迟: 平均 503.5ms, 最低 300.1ms)
- 可接受延迟 (<2s): 45 个频道 (延迟: 平均 1407.7ms, 最低 806.2ms)
- unacceptable: 19 个频道 (延迟: 平均 2670.3ms, 最低 2170.2ms)
- 低延迟 (<300ms): 21 个频道 (延迟: 平均 208.1ms, 最低 150.5ms)

### 📁 频道分组
- : 154 个频道

### 🔗 协议统计
- HLS (m3u8): 130 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.1 KB)
- iptv_medium_latency.m3u (20.1 KB)
- iptv_high_latency.m3u (13.4 KB)
- iptv_optimized_combined.m3u (39.4 KB)
- tvbox_optimized.m3u (49.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 372.6 秒
