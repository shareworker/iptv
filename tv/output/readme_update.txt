## IPTV智能优化系统更新报告

生成时间: 2026-02-01T06:48:13.558818

### 📊 总体统计
- 总频道数: 128
- TVBox优化频道数: 128

### 📈 分级统计
- 中等延迟 (<800ms): 41 个频道 (延迟: 平均 531.8ms, 最低 383.8ms)
- 可接受延迟 (<2s): 67 个频道 (延迟: 平均 1158.1ms, 最低 824.5ms)
- unacceptable: 12 个频道 (延迟: 平均 4975.8ms, 最低 2047.6ms)
- 低延迟 (<300ms): 8 个频道 (延迟: 平均 241.3ms, 最低 205.1ms)

### 📁 频道分组
- : 128 个频道

### 🔗 协议统计
- HLS (m3u8): 126 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (2.3 KB)
- iptv_medium_latency.m3u (12.3 KB)
- iptv_high_latency.m3u (19.3 KB)
- iptv_optimized_combined.m3u (33.8 KB)
- tvbox_optimized.m3u (41.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 507.8 秒
