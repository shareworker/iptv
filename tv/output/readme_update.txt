## IPTV智能优化系统更新报告

生成时间: 2026-08-08T06:42:03.962950

### 📊 总体统计
- 总频道数: 136
- TVBox优化频道数: 136

### 📈 分级统计
- 中等延迟 (<800ms): 48 个频道 (延迟: 平均 586.7ms, 最低 306.8ms)
- 可接受延迟 (<2s): 63 个频道 (延迟: 平均 1213.7ms, 最低 814.2ms)
- unacceptable: 10 个频道 (延迟: 平均 2303.4ms, 最低 2002.1ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 205.5ms, 最低 183.6ms)

### 📁 频道分组
- : 136 个频道

### 🔗 协议统计
- HLS (m3u8): 113 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.3 KB)
- iptv_medium_latency.m3u (14.2 KB)
- iptv_high_latency.m3u (18.4 KB)
- iptv_optimized_combined.m3u (36.6 KB)
- tvbox_optimized.m3u (44.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 328.9 秒
