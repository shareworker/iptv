## IPTV智能优化系统更新报告

生成时间: 2025-12-22T06:30:38.642487

### 📊 总体统计
- 总频道数: 154
- TVBox优化频道数: 154

### 📈 分级统计
- 低延迟 (<300ms): 23 个频道 (延迟: 平均 217.6ms, 最低 160.6ms)
- 中等延迟 (<800ms): 64 个频道 (延迟: 平均 501.8ms, 最低 301.1ms)
- 可接受延迟 (<2s): 48 个频道 (延迟: 平均 1210.0ms, 最低 816.8ms)
- unacceptable: 19 个频道 (延迟: 平均 4852.2ms, 最低 2335.0ms)

### 📁 频道分组
- : 154 个频道

### 🔗 协议统计
- HTTP: 21 个频道
- HLS (m3u8): 131 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.8 KB)
- iptv_medium_latency.m3u (18.3 KB)
- iptv_high_latency.m3u (14.3 KB)
- iptv_optimized_combined.m3u (39.2 KB)
- tvbox_optimized.m3u (49.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 405.1 秒
