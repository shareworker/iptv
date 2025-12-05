## IPTV智能优化系统更新报告

生成时间: 2025-12-05T18:24:08.895810

### 📊 总体统计
- 总频道数: 163
- TVBox优化频道数: 163

### 📈 分级统计
- 中等延迟 (<800ms): 41 个频道 (延迟: 平均 537.1ms, 最低 328.4ms)
- unacceptable: 29 个频道 (延迟: 平均 2862.7ms, 最低 2024.2ms)
- 可接受延迟 (<2s): 79 个频道 (延迟: 平均 1255.9ms, 最低 804.5ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 218.4ms, 最低 184.8ms)

### 📁 频道分组
- : 163 个频道

### 🔗 协议统计
- HLS (m3u8): 139 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.0 KB)
- iptv_medium_latency.m3u (11.9 KB)
- iptv_high_latency.m3u (23.2 KB)
- iptv_optimized_combined.m3u (38.9 KB)
- tvbox_optimized.m3u (53.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.1 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 387.7 秒
