## IPTV智能优化系统更新报告

生成时间: 2025-10-27T06:28:23.495081

### 📊 总体统计
- 总频道数: 164
- TVBox优化频道数: 164

### 📈 分级统计
- 中等延迟 (<800ms): 41 个频道 (延迟: 平均 523.7ms, 最低 328.3ms)
- 可接受延迟 (<2s): 75 个频道 (延迟: 平均 1374.6ms, 最低 825.7ms)
- unacceptable: 25 个频道 (延迟: 平均 3143.1ms, 最低 2071.4ms)
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 222.8ms, 最低 182.9ms)

### 📁 频道分组
- : 164 个频道

### 🔗 协议统计
- HLS (m3u8): 140 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.6 KB)
- iptv_medium_latency.m3u (11.9 KB)
- iptv_high_latency.m3u (21.9 KB)
- iptv_optimized_combined.m3u (40.2 KB)
- tvbox_optimized.m3u (54.4 KB)
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
- 总耗时: 389.0 秒
