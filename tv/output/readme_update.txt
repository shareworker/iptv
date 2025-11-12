## IPTV智能优化系统更新报告

生成时间: 2025-11-12T18:25:37.619534

### 📊 总体统计
- 总频道数: 160
- TVBox优化频道数: 160

### 📈 分级统计
- 低延迟 (<300ms): 11 个频道 (延迟: 平均 211.5ms, 最低 196.1ms)
- 中等延迟 (<800ms): 56 个频道 (延迟: 平均 570.9ms, 最低 307.7ms)
- 可接受延迟 (<2s): 60 个频道 (延迟: 平均 1289.7ms, 最低 833.1ms)
- unacceptable: 33 个频道 (延迟: 平均 3085.1ms, 最低 2083.3ms)

### 📁 频道分组
- : 160 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 136 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.2 KB)
- iptv_medium_latency.m3u (16.3 KB)
- iptv_high_latency.m3u (17.5 KB)
- iptv_optimized_combined.m3u (36.8 KB)
- tvbox_optimized.m3u (52.6 KB)
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
- 总耗时: 378.4 秒
