## IPTV智能优化系统更新报告

生成时间: 2025-11-16T06:28:03.687892

### 📊 总体统计
- 总频道数: 144
- TVBox优化频道数: 144

### 📈 分级统计
- 中等延迟 (<800ms): 47 个频道 (延迟: 平均 599.5ms, 最低 319.2ms)
- 可接受延迟 (<2s): 48 个频道 (延迟: 平均 1344.9ms, 最低 808.6ms)
- unacceptable: 44 个频道 (延迟: 平均 6721.2ms, 最低 2278.8ms)
- 低延迟 (<300ms): 5 个频道 (延迟: 平均 272.8ms, 最低 253.5ms)

### 📁 频道分组
- : 144 个频道

### 🔗 协议统计
- HLS (m3u8): 138 个频道
- HTTP: 4 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.4 KB)
- iptv_medium_latency.m3u (13.7 KB)
- iptv_high_latency.m3u (14.0 KB)
- iptv_optimized_combined.m3u (28.9 KB)
- tvbox_optimized.m3u (47.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 549.6 秒
