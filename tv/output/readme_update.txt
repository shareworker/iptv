## IPTV智能优化系统更新报告

生成时间: 2026-09-05T19:50:20.309529

### 📊 总体统计
- 总频道数: 122
- TVBox优化频道数: 122

### 📈 分级统计
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 191.3ms, 最低 151.3ms)
- unacceptable: 10 个频道 (延迟: 平均 2911.3ms, 最低 2023.4ms)
- 可接受延迟 (<2s): 52 个频道 (延迟: 平均 1230.0ms, 最低 826.2ms)
- 中等延迟 (<800ms): 43 个频道 (延迟: 平均 589.9ms, 最低 356.8ms)

### 📁 频道分组
- : 122 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 99 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (12.6 KB)
- iptv_high_latency.m3u (15.1 KB)
- iptv_optimized_combined.m3u (32.4 KB)
- tvbox_optimized.m3u (39.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (206.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 328.2 秒
