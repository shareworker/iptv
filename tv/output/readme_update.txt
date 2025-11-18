## IPTV智能优化系统更新报告

生成时间: 2025-11-18T18:25:53.341997

### 📊 总体统计
- 总频道数: 163
- TVBox优化频道数: 163

### 📈 分级统计
- 低延迟 (<300ms): 35 个频道 (延迟: 平均 202.2ms, 最低 150.2ms)
- 中等延迟 (<800ms): 69 个频道 (延迟: 平均 548.7ms, 最低 300.4ms)
- 可接受延迟 (<2s): 45 个频道 (延迟: 平均 1197.2ms, 最低 809.3ms)
- unacceptable: 14 个频道 (延迟: 平均 3018.2ms, 最低 2321.1ms)

### 📁 频道分组
- : 163 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 139 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (10.3 KB)
- iptv_medium_latency.m3u (20.0 KB)
- iptv_high_latency.m3u (13.3 KB)
- iptv_optimized_combined.m3u (43.4 KB)
- tvbox_optimized.m3u (51.4 KB)
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
- 总耗时: 363.1 秒
