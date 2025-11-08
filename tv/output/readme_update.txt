## IPTV智能优化系统更新报告

生成时间: 2025-11-08T18:22:59.069493

### 📊 总体统计
- 总频道数: 165
- TVBox优化频道数: 165

### 📈 分级统计
- 低延迟 (<300ms): 22 个频道 (延迟: 平均 198.1ms, 最低 146.1ms)
- 中等延迟 (<800ms): 69 个频道 (延迟: 平均 521.4ms, 最低 304.2ms)
- 可接受延迟 (<2s): 61 个频道 (延迟: 平均 1231.8ms, 最低 804.8ms)
- unacceptable: 13 个频道 (延迟: 平均 7113.1ms, 最低 2363.5ms)

### 📁 频道分组
- : 165 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 141 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.2 KB)
- iptv_medium_latency.m3u (20.3 KB)
- iptv_high_latency.m3u (18.1 KB)
- iptv_optimized_combined.m3u (44.3 KB)
- tvbox_optimized.m3u (52.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 381.1 秒
