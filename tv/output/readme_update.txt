## IPTV智能优化系统更新报告

生成时间: 2026-06-03T10:51:06.187560

### 📊 总体统计
- 总频道数: 151
- TVBox优化频道数: 151

### 📈 分级统计
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 213.6ms, 最低 199.6ms)
- 中等延迟 (<800ms): 30 个频道 (延迟: 平均 567.4ms, 最低 303.2ms)
- 可接受延迟 (<2s): 78 个频道 (延迟: 平均 1263.5ms, 最低 808.4ms)
- unacceptable: 29 个频道 (延迟: 平均 3534.4ms, 最低 2017.8ms)

### 📁 频道分组
- : 151 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 128 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.9 KB)
- iptv_medium_latency.m3u (8.6 KB)
- iptv_high_latency.m3u (23.0 KB)
- iptv_optimized_combined.m3u (35.3 KB)
- tvbox_optimized.m3u (50.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 380.5 秒
