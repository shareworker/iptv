## IPTV智能优化系统更新报告

生成时间: 2026-06-10T20:21:39.752312

### 📊 总体统计
- 总频道数: 144
- TVBox优化频道数: 144

### 📈 分级统计
- 中等延迟 (<800ms): 27 个频道 (延迟: 平均 535.4ms, 最低 327.2ms)
- 可接受延迟 (<2s): 82 个频道 (延迟: 平均 1314.6ms, 最低 858.6ms)
- unacceptable: 21 个频道 (延迟: 平均 4172.1ms, 最低 2125.6ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 224.3ms, 最低 200.7ms)

### 📁 频道分组
- : 144 个频道

### 🔗 协议统计
- HLS (m3u8): 121 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.9 KB)
- iptv_medium_latency.m3u (7.7 KB)
- iptv_high_latency.m3u (24.3 KB)
- iptv_optimized_combined.m3u (35.8 KB)
- tvbox_optimized.m3u (47.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 406.7 秒
