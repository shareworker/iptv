## IPTV智能优化系统更新报告

生成时间: 2026-04-28T08:16:29.701464

### 📊 总体统计
- 总频道数: 148
- TVBox优化频道数: 148

### 📈 分级统计
- 中等延迟 (<800ms): 55 个频道 (延迟: 平均 554.2ms, 最低 322.9ms)
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 212.9ms, 最低 177.1ms)
- 可接受延迟 (<2s): 59 个频道 (延迟: 平均 1330.1ms, 最低 858.7ms)
- unacceptable: 15 个频道 (延迟: 平均 3452.4ms, 最低 2020.9ms)

### 📁 频道分组
- : 148 个频道

### 🔗 协议统计
- HLS (m3u8): 125 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.3 KB)
- iptv_medium_latency.m3u (16.1 KB)
- iptv_high_latency.m3u (17.2 KB)
- iptv_optimized_combined.m3u (38.5 KB)
- tvbox_optimized.m3u (48.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 399.1 秒
