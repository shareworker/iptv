## IPTV智能优化系统更新报告

生成时间: 2026-01-14T06:32:08.996278

### 📊 总体统计
- 总频道数: 110
- TVBox优化频道数: 110

### 📈 分级统计
- 可接受延迟 (<2s): 60 个频道 (延迟: 平均 1422.1ms, 最低 820.2ms)
- 中等延迟 (<800ms): 37 个频道 (延迟: 平均 658.2ms, 最低 302.2ms)
- unacceptable: 9 个频道 (延迟: 平均 2889.3ms, 最低 2101.7ms)
- 低延迟 (<300ms): 4 个频道 (延迟: 平均 271.6ms, 最低 268.7ms)

### 📁 频道分组
- : 110 个频道

### 🔗 协议统计
- HLS (m3u8): 108 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.2 KB)
- iptv_medium_latency.m3u (10.8 KB)
- iptv_high_latency.m3u (17.4 KB)
- iptv_optimized_combined.m3u (29.2 KB)
- tvbox_optimized.m3u (36.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (204.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 524.3 秒
