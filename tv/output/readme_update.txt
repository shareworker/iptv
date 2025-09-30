## IPTV智能优化系统更新报告

生成时间: 2025-09-30T18:23:46.565268

### 📊 总体统计
- 总频道数: 166
- TVBox优化频道数: 166

### 📈 分级统计
- 低延迟 (<300ms): 26 个频道 (延迟: 平均 220.2ms, 最低 181.0ms)
- 中等延迟 (<800ms): 54 个频道 (延迟: 平均 536.7ms, 最低 300.1ms)
- 可接受延迟 (<2s): 63 个频道 (延迟: 平均 1160.7ms, 最低 819.3ms)
- unacceptable: 23 个频道 (延迟: 平均 3164.4ms, 最低 2003.7ms)

### 📁 频道分组
- : 166 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 142 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.4 KB)
- iptv_medium_latency.m3u (15.7 KB)
- iptv_high_latency.m3u (18.6 KB)
- iptv_optimized_combined.m3u (41.5 KB)
- tvbox_optimized.m3u (53.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 387.8 秒
