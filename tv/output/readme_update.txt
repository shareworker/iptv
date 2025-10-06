## IPTV智能优化系统更新报告

生成时间: 2025-10-06T06:26:27.687509

### 📊 总体统计
- 总频道数: 160
- TVBox优化频道数: 160

### 📈 分级统计
- 中等延迟 (<800ms): 39 个频道 (延迟: 平均 606.0ms, 最低 319.3ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1217.4ms, 最低 803.7ms)
- unacceptable: 43 个频道 (延迟: 平均 2929.8ms, 最低 2007.9ms)
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 234.6ms, 最低 200.8ms)

### 📁 频道分组
- : 160 个频道

### 🔗 协议统计
- HLS (m3u8): 136 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.3 KB)
- iptv_medium_latency.m3u (11.4 KB)
- iptv_high_latency.m3u (17.1 KB)
- iptv_optimized_combined.m3u (33.6 KB)
- tvbox_optimized.m3u (52.1 KB)
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
- 总耗时: 411.1 秒
