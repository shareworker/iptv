## IPTV智能优化系统更新报告

生成时间: 2026-01-26T06:32:54.057225

### 📊 总体统计
- 总频道数: 162
- TVBox优化频道数: 162

### 📈 分级统计
- 中等延迟 (<800ms): 61 个频道 (延迟: 平均 538.4ms, 最低 303.2ms)
- 可接受延迟 (<2s): 69 个频道 (延迟: 平均 1338.7ms, 最低 823.6ms)
- unacceptable: 18 个频道 (延迟: 平均 3510.8ms, 最低 2101.6ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 223.3ms, 最低 196.7ms)

### 📁 频道分组
- : 162 个频道

### 🔗 协议统计
- HLS (m3u8): 138 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.0 KB)
- iptv_medium_latency.m3u (17.9 KB)
- iptv_high_latency.m3u (20.0 KB)
- iptv_optimized_combined.m3u (41.8 KB)
- tvbox_optimized.m3u (52.4 KB)
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
- 总耗时: 370.6 秒
