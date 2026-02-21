## IPTV智能优化系统更新报告

生成时间: 2026-02-21T18:31:55.611758

### 📊 总体统计
- 总频道数: 121
- TVBox优化频道数: 121

### 📈 分级统计
- 低延迟 (<300ms): 6 个频道 (延迟: 平均 259.7ms, 最低 236.5ms)
- 可接受延迟 (<2s): 58 个频道 (延迟: 平均 1337.1ms, 最低 835.1ms)
- unacceptable: 14 个频道 (延迟: 平均 3126.1ms, 最低 2068.9ms)
- 中等延迟 (<800ms): 43 个频道 (延迟: 平均 582.5ms, 最低 332.8ms)

### 📁 频道分组
- : 121 个频道

### 🔗 协议统计
- HLS (m3u8): 119 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.8 KB)
- iptv_medium_latency.m3u (12.7 KB)
- iptv_high_latency.m3u (16.9 KB)
- iptv_optimized_combined.m3u (31.3 KB)
- tvbox_optimized.m3u (40.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (206.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 510.7 秒
