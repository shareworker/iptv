## IPTV智能优化系统更新报告

生成时间: 2025-12-28T18:25:55.110682

### 📊 总体统计
- 总频道数: 153
- TVBox优化频道数: 153

### 📈 分级统计
- 中等延迟 (<800ms): 78 个频道 (延迟: 平均 569.5ms, 最低 324.9ms)
- 可接受延迟 (<2s): 47 个频道 (延迟: 平均 1255.9ms, 最低 837.0ms)
- 低延迟 (<300ms): 26 个频道 (延迟: 平均 208.7ms, 最低 146.0ms)
- unacceptable: 2 个频道 (延迟: 平均 2138.1ms, 最低 2137.2ms)

### 📁 频道分组
- : 153 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 129 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (7.4 KB)
- iptv_medium_latency.m3u (22.9 KB)
- iptv_high_latency.m3u (13.9 KB)
- iptv_optimized_combined.m3u (43.9 KB)
- tvbox_optimized.m3u (47.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 386.5 秒
