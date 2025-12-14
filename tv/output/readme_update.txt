## IPTV智能优化系统更新报告

生成时间: 2025-12-14T06:27:51.912983

### 📊 总体统计
- 总频道数: 149
- TVBox优化频道数: 149

### 📈 分级统计
- 中等延迟 (<800ms): 43 个频道 (延迟: 平均 616.3ms, 最低 403.9ms)
- 可接受延迟 (<2s): 70 个频道 (延迟: 平均 1388.5ms, 最低 812.7ms)
- unacceptable: 25 个频道 (延迟: 平均 4745.1ms, 最低 2027.6ms)
- 低延迟 (<300ms): 11 个频道 (延迟: 平均 230.9ms, 最低 187.3ms)

### 📁 频道分组
- : 149 个频道

### 🔗 协议统计
- HTTP: 10 个频道
- HLS (m3u8): 137 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.3 KB)
- iptv_medium_latency.m3u (12.4 KB)
- iptv_high_latency.m3u (20.7 KB)
- iptv_optimized_combined.m3u (36.2 KB)
- tvbox_optimized.m3u (49.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 490.8 秒
