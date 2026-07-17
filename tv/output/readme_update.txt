## IPTV智能优化系统更新报告

生成时间: 2026-07-17T19:01:08.022561

### 📊 总体统计
- 总频道数: 137
- TVBox优化频道数: 137

### 📈 分级统计
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 221.2ms, 最低 187.3ms)
- 可接受延迟 (<2s): 57 个频道 (延迟: 平均 1048.4ms, 最低 803.6ms)
- unacceptable: 15 个频道 (延迟: 平均 3607.5ms, 最低 2191.9ms)
- 中等延迟 (<800ms): 48 个频道 (延迟: 平均 555.8ms, 最低 322.0ms)

### 📁 频道分组
- : 137 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 114 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (14.3 KB)
- iptv_high_latency.m3u (16.4 KB)
- iptv_optimized_combined.m3u (35.3 KB)
- tvbox_optimized.m3u (43.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 367.9 秒
