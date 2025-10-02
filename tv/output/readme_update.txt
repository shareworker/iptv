## IPTV智能优化系统更新报告

生成时间: 2025-10-02T18:24:11.157640

### 📊 总体统计
- 总频道数: 167
- TVBox优化频道数: 167

### 📈 分级统计
- 中等延迟 (<800ms): 53 个频道 (延迟: 平均 523.7ms, 最低 300.1ms)
- 可接受延迟 (<2s): 57 个频道 (延迟: 平均 1420.6ms, 最低 850.8ms)
- unacceptable: 29 个频道 (延迟: 平均 2765.4ms, 最低 2003.6ms)
- 低延迟 (<300ms): 27 个频道 (延迟: 平均 237.2ms, 最低 186.6ms)
- 超低延迟 (<100ms): 1 个频道 (延迟: 平均 66.8ms, 最低 66.8ms)

### 📁 频道分组
- : 167 个频道

### 🔗 协议统计
- HLS (m3u8): 143 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_ultra_low_latency.m3u (0.3 KB)
- iptv_low_latency.m3u (7.7 KB)
- iptv_medium_latency.m3u (15.3 KB)
- iptv_high_latency.m3u (16.6 KB)
- iptv_optimized_combined.m3u (39.7 KB)
- tvbox_optimized.m3u (53.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 395.2 秒
