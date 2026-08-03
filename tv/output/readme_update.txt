## IPTV智能优化系统更新报告

生成时间: 2026-08-03T09:31:32.797636

### 📊 总体统计
- 总频道数: 134
- TVBox优化频道数: 134

### 📈 分级统计
- 低延迟 (<300ms): 21 个频道 (延迟: 平均 182.3ms, 最低 147.6ms)
- 中等延迟 (<800ms): 60 个频道 (延迟: 平均 602.6ms, 最低 309.0ms)
- 可接受延迟 (<2s): 50 个频道 (延迟: 平均 1105.2ms, 最低 801.5ms)
- unacceptable: 3 个频道 (延迟: 平均 3749.5ms, 最低 2013.5ms)

### 📁 频道分组
- : 134 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 112 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.0 KB)
- iptv_medium_latency.m3u (17.7 KB)
- iptv_high_latency.m3u (14.5 KB)
- iptv_optimized_combined.m3u (37.9 KB)
- tvbox_optimized.m3u (41.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 318.3 秒
