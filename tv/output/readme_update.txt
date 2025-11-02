## IPTV智能优化系统更新报告

生成时间: 2025-11-02T06:24:57.234231

### 📊 总体统计
- 总频道数: 166
- TVBox优化频道数: 166

### 📈 分级统计
- 中等延迟 (<800ms): 42 个频道 (延迟: 平均 549.0ms, 最低 315.0ms)
- 可接受延迟 (<2s): 69 个频道 (延迟: 平均 1313.8ms, 最低 818.2ms)
- unacceptable: 32 个频道 (延迟: 平均 4779.5ms, 最低 2124.7ms)
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 203.2ms, 最低 151.4ms)

### 📁 频道分组
- : 166 个频道

### 🔗 协议统计
- HLS (m3u8): 142 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.7 KB)
- iptv_medium_latency.m3u (12.1 KB)
- iptv_high_latency.m3u (20.3 KB)
- iptv_optimized_combined.m3u (38.9 KB)
- tvbox_optimized.m3u (54.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 389.7 秒
