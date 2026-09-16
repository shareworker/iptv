## IPTV智能优化系统更新报告

生成时间: 2026-09-16T10:38:57.387955

### 📊 总体统计
- 总频道数: 113
- TVBox优化频道数: 113

### 📈 分级统计
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 238.2ms, 最低 199.3ms)
- 中等延迟 (<800ms): 27 个频道 (延迟: 平均 582.4ms, 最低 302.1ms)
- unacceptable: 13 个频道 (延迟: 平均 2444.6ms, 最低 2055.7ms)
- 可接受延迟 (<2s): 54 个频道 (延迟: 平均 1055.1ms, 最低 801.5ms)

### 📁 频道分组
- : 113 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 90 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.4 KB)
- iptv_medium_latency.m3u (8.2 KB)
- iptv_high_latency.m3u (15.5 KB)
- iptv_optimized_combined.m3u (28.9 KB)
- tvbox_optimized.m3u (35.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (204.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 343.1 秒
