## IPTV智能优化系统更新报告

生成时间: 2026-04-07T18:58:38.457661

### 📊 总体统计
- 总频道数: 153
- TVBox优化频道数: 153

### 📈 分级统计
- 低延迟 (<300ms): 24 个频道 (延迟: 平均 200.4ms, 最低 141.0ms)
- 中等延迟 (<800ms): 70 个频道 (延迟: 平均 496.2ms, 最低 306.7ms)
- 可接受延迟 (<2s): 50 个频道 (延迟: 平均 1053.1ms, 最低 832.0ms)
- unacceptable: 9 个频道 (延迟: 平均 4082.1ms, 最低 3144.0ms)

### 📁 频道分组
- : 153 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 129 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.9 KB)
- iptv_medium_latency.m3u (20.3 KB)
- iptv_high_latency.m3u (14.8 KB)
- iptv_optimized_combined.m3u (41.8 KB)
- tvbox_optimized.m3u (47.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 365.0 秒
