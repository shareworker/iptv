## IPTV智能优化系统更新报告

生成时间: 2026-06-08T10:27:02.911909

### 📊 总体统计
- 总频道数: 146
- TVBox优化频道数: 146

### 📈 分级统计
- 中等延迟 (<800ms): 44 个频道 (延迟: 平均 562.5ms, 最低 301.8ms)
- 可接受延迟 (<2s): 77 个频道 (延迟: 平均 1283.7ms, 最低 801.2ms)
- unacceptable: 15 个频道 (延迟: 平均 4706.6ms, 最低 2047.1ms)
- 低延迟 (<300ms): 10 个频道 (延迟: 平均 208.7ms, 最低 198.7ms)

### 📁 频道分组
- : 146 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 123 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (2.9 KB)
- iptv_medium_latency.m3u (12.8 KB)
- iptv_high_latency.m3u (22.5 KB)
- iptv_optimized_combined.m3u (38.1 KB)
- tvbox_optimized.m3u (47.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 402.8 秒
