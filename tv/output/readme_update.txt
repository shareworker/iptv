## IPTV智能优化系统更新报告

生成时间: 2026-01-21T06:31:16.062112

### 📊 总体统计
- 总频道数: 163
- TVBox优化频道数: 163

### 📈 分级统计
- 低延迟 (<300ms): 25 个频道 (延迟: 平均 237.0ms, 最低 181.2ms)
- 中等延迟 (<800ms): 43 个频道 (延迟: 平均 564.9ms, 最低 334.5ms)
- 可接受延迟 (<2s): 82 个频道 (延迟: 平均 1332.1ms, 最低 806.8ms)
- unacceptable: 13 个频道 (延迟: 平均 3415.8ms, 最低 2203.7ms)

### 📁 频道分组
- : 163 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 139 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.5 KB)
- iptv_medium_latency.m3u (12.5 KB)
- iptv_high_latency.m3u (23.7 KB)
- iptv_optimized_combined.m3u (43.5 KB)
- tvbox_optimized.m3u (53.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 369.3 秒
