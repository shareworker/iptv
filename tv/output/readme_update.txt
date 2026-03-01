## IPTV智能优化系统更新报告

生成时间: 2026-03-01T18:30:35.066477

### 📊 总体统计
- 总频道数: 124
- TVBox优化频道数: 124

### 📈 分级统计
- 低延迟 (<300ms): 4 个频道 (延迟: 平均 249.3ms, 最低 241.7ms)
- 中等延迟 (<800ms): 67 个频道 (延迟: 平均 532.6ms, 最低 301.4ms)
- 可接受延迟 (<2s): 42 个频道 (延迟: 平均 1244.8ms, 最低 824.5ms)
- unacceptable: 11 个频道 (延迟: 平均 3810.4ms, 最低 2019.6ms)

### 📁 频道分组
- : 124 个频道

### 🔗 协议统计
- HLS (m3u8): 122 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.2 KB)
- iptv_medium_latency.m3u (19.4 KB)
- iptv_high_latency.m3u (12.5 KB)
- iptv_optimized_combined.m3u (32.9 KB)
- tvbox_optimized.m3u (39.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 506.0 秒
