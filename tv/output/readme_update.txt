## IPTV智能优化系统更新报告

生成时间: 2026-02-14T18:29:23.747194

### 📊 总体统计
- 总频道数: 144
- TVBox优化频道数: 144

### 📈 分级统计
- 中等延迟 (<800ms): 54 个频道 (延迟: 平均 541.7ms, 最低 303.0ms)
- 可接受延迟 (<2s): 55 个频道 (延迟: 平均 1294.0ms, 最低 835.3ms)
- unacceptable: 10 个频道 (延迟: 平均 3469.1ms, 最低 2068.4ms)
- 低延迟 (<300ms): 25 个频道 (延迟: 平均 218.9ms, 最低 151.5ms)

### 📁 频道分组
- : 144 个频道

### 🔗 协议统计
- HLS (m3u8): 120 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.0 KB)
- iptv_medium_latency.m3u (16.1 KB)
- iptv_high_latency.m3u (16.0 KB)
- iptv_optimized_combined.m3u (38.8 KB)
- tvbox_optimized.m3u (45.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 355.4 秒
