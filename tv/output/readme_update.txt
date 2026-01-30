## IPTV智能优化系统更新报告

生成时间: 2026-01-30T06:43:51.789502

### 📊 总体统计
- 总频道数: 161
- TVBox优化频道数: 161

### 📈 分级统计
- 低延迟 (<300ms): 18 个频道 (延迟: 平均 203.2ms, 最低 160.9ms)
- 中等延迟 (<800ms): 60 个频道 (延迟: 平均 490.2ms, 最低 306.7ms)
- 可接受延迟 (<2s): 65 个频道 (延迟: 平均 1268.1ms, 最低 802.5ms)
- unacceptable: 18 个频道 (延迟: 平均 3294.0ms, 最低 2001.7ms)

### 📁 频道分组
- : 161 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 137 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.1 KB)
- iptv_medium_latency.m3u (17.9 KB)
- iptv_high_latency.m3u (18.7 KB)
- iptv_optimized_combined.m3u (41.5 KB)
- tvbox_optimized.m3u (51.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 368.1 秒
