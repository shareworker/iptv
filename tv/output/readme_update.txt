## IPTV智能优化系统更新报告

生成时间: 2025-10-12T06:23:36.072433

### 📊 总体统计
- 总频道数: 163
- TVBox优化频道数: 163

### 📈 分级统计
- 可接受延迟 (<2s): 57 个频道 (延迟: 平均 1252.3ms, 最低 814.7ms)
- 中等延迟 (<800ms): 39 个频道 (延迟: 平均 571.9ms, 最低 309.9ms)
- unacceptable: 52 个频道 (延迟: 平均 3539.2ms, 最低 2043.8ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 231.4ms, 最低 120.1ms)

### 📁 频道分组
- : 163 个频道

### 🔗 协议统计
- HLS (m3u8): 139 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (11.2 KB)
- iptv_high_latency.m3u (16.8 KB)
- iptv_optimized_combined.m3u (32.1 KB)
- tvbox_optimized.m3u (54.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 418.6 秒
