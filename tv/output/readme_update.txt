## IPTV智能优化系统更新报告

生成时间: 2025-10-26T06:24:30.015626

### 📊 总体统计
- 总频道数: 158
- TVBox优化频道数: 158

### 📈 分级统计
- 中等延迟 (<800ms): 53 个频道 (延迟: 平均 588.2ms, 最低 311.8ms)
- 可接受延迟 (<2s): 63 个频道 (延迟: 平均 1274.3ms, 最低 807.2ms)
- unacceptable: 22 个频道 (延迟: 平均 4074.4ms, 最低 2010.7ms)
- 低延迟 (<300ms): 20 个频道 (延迟: 平均 191.9ms, 最低 149.7ms)

### 📁 频道分组
- : 158 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 134 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.6 KB)
- iptv_medium_latency.m3u (15.4 KB)
- iptv_high_latency.m3u (18.5 KB)
- iptv_optimized_combined.m3u (39.4 KB)
- tvbox_optimized.m3u (51.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 389.6 秒
