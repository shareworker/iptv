## IPTV智能优化系统更新报告

生成时间: 2026-05-27T20:08:58.867696

### 📊 总体统计
- 总频道数: 149
- TVBox优化频道数: 149

### 📈 分级统计
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 226.9ms, 最低 201.3ms)
- 中等延迟 (<800ms): 57 个频道 (延迟: 平均 564.9ms, 最低 316.9ms)
- 可接受延迟 (<2s): 63 个频道 (延迟: 平均 1221.1ms, 最低 800.7ms)
- unacceptable: 15 个频道 (延迟: 平均 3410.2ms, 最低 2342.2ms)

### 📁 频道分组
- : 149 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 126 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.1 KB)
- iptv_medium_latency.m3u (16.7 KB)
- iptv_high_latency.m3u (18.3 KB)
- iptv_optimized_combined.m3u (38.9 KB)
- tvbox_optimized.m3u (48.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 373.8 秒
