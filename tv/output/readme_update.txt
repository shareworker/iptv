## IPTV智能优化系统更新报告

生成时间: 2026-03-14T18:35:25.002650

### 📊 总体统计
- 总频道数: 132
- TVBox优化频道数: 132

### 📈 分级统计
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 271.9ms, 最低 211.9ms)
- 中等延迟 (<800ms): 37 个频道 (延迟: 平均 561.6ms, 最低 305.9ms)
- 可接受延迟 (<2s): 63 个频道 (延迟: 平均 1258.4ms, 最低 817.6ms)
- unacceptable: 18 个频道 (延迟: 平均 5171.8ms, 最低 2171.8ms)

### 📁 频道分组
- : 132 个频道

### 🔗 协议统计
- HLS (m3u8): 130 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (11.1 KB)
- iptv_high_latency.m3u (18.2 KB)
- iptv_optimized_combined.m3u (33.3 KB)
- tvbox_optimized.m3u (43.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 513.9 秒
