## IPTV智能优化系统更新报告

生成时间: 2026-01-15T06:28:51.405993

### 📊 总体统计
- 总频道数: 138
- TVBox优化频道数: 138

### 📈 分级统计
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 209.6ms, 最低 182.3ms)
- 中等延迟 (<800ms): 55 个频道 (延迟: 平均 585.0ms, 最低 303.5ms)
- 可接受延迟 (<2s): 51 个频道 (延迟: 平均 1177.8ms, 最低 829.3ms)
- unacceptable: 17 个频道 (延迟: 平均 2740.3ms, 最低 2031.3ms)

### 📁 频道分组
- : 138 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 114 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (16.0 KB)
- iptv_high_latency.m3u (14.7 KB)
- iptv_optimized_combined.m3u (34.8 KB)
- tvbox_optimized.m3u (44.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 370.4 秒
