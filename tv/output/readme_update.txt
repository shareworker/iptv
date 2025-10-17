## IPTV智能优化系统更新报告

生成时间: 2025-10-17T06:25:16.517818

### 📊 总体统计
- 总频道数: 157
- TVBox优化频道数: 157

### 📈 分级统计
- 中等延迟 (<800ms): 59 个频道 (延迟: 平均 493.3ms, 最低 310.4ms)
- 可接受延迟 (<2s): 60 个频道 (延迟: 平均 1315.0ms, 最低 835.7ms)
- unacceptable: 15 个频道 (延迟: 平均 2636.6ms, 最低 2012.5ms)
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 187.2ms, 最低 148.0ms)

### 📁 频道分组
- : 157 个频道

### 🔗 协议统计
- HLS (m3u8): 133 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.6 KB)
- iptv_medium_latency.m3u (16.8 KB)
- iptv_high_latency.m3u (17.8 KB)
- iptv_optimized_combined.m3u (41.1 KB)
- tvbox_optimized.m3u (50.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 379.8 秒
