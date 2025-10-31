## IPTV智能优化系统更新报告

生成时间: 2025-10-31T18:25:25.868388

### 📊 总体统计
- 总频道数: 169
- TVBox优化频道数: 169

### 📈 分级统计
- 中等延迟 (<800ms): 72 个频道 (延迟: 平均 482.6ms, 最低 302.2ms)
- 可接受延迟 (<2s): 64 个频道 (延迟: 平均 1350.6ms, 最低 800.3ms)
- unacceptable: 14 个频道 (延迟: 平均 3007.2ms, 最低 2198.3ms)
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 186.1ms, 最低 146.0ms)

### 📁 频道分组
- : 169 个频道

### 🔗 协议统计
- HLS (m3u8): 145 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.3 KB)
- iptv_medium_latency.m3u (21.2 KB)
- iptv_high_latency.m3u (18.7 KB)
- iptv_optimized_combined.m3u (45.0 KB)
- tvbox_optimized.m3u (54.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (216.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 373.5 秒
