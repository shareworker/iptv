## IPTV智能优化系统更新报告

生成时间: 2026-04-03T07:05:36.051266

### 📊 总体统计
- 总频道数: 149
- TVBox优化频道数: 149

### 📈 分级统计
- 低延迟 (<300ms): 13 个频道 (延迟: 平均 230.4ms, 最低 199.1ms)
- 中等延迟 (<800ms): 51 个频道 (延迟: 平均 539.5ms, 最低 302.4ms)
- 可接受延迟 (<2s): 60 个频道 (延迟: 平均 1349.1ms, 最低 813.5ms)
- unacceptable: 25 个频道 (延迟: 平均 3703.6ms, 最低 2017.4ms)

### 📁 频道分组
- : 149 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 125 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.7 KB)
- iptv_medium_latency.m3u (15.0 KB)
- iptv_high_latency.m3u (17.5 KB)
- iptv_optimized_combined.m3u (36.0 KB)
- tvbox_optimized.m3u (48.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 396.6 秒
