## IPTV智能优化系统更新报告

生成时间: 2025-10-06T18:25:07.166979

### 📊 总体统计
- 总频道数: 163
- TVBox优化频道数: 163

### 📈 分级统计
- 可接受延迟 (<2s): 53 个频道 (延迟: 平均 1277.5ms, 最低 808.1ms)
- 中等延迟 (<800ms): 65 个频道 (延迟: 平均 517.3ms, 最低 308.4ms)
- unacceptable: 14 个频道 (延迟: 平均 3678.9ms, 最低 2370.5ms)
- 低延迟 (<300ms): 31 个频道 (延迟: 平均 229.2ms, 最低 160.6ms)

### 📁 频道分组
- : 163 个频道

### 🔗 协议统计
- HLS (m3u8): 139 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (8.7 KB)
- iptv_medium_latency.m3u (19.2 KB)
- iptv_high_latency.m3u (15.4 KB)
- iptv_optimized_combined.m3u (43.2 KB)
- tvbox_optimized.m3u (51.2 KB)
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
- 总耗时: 380.4 秒
