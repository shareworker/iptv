## IPTV智能优化系统更新报告

生成时间: 2026-05-02T18:51:19.988701

### 📊 总体统计
- 总频道数: 149
- TVBox优化频道数: 149

### 📈 分级统计
- 中等延迟 (<800ms): 40 个频道 (延迟: 平均 541.0ms, 最低 334.4ms)
- 可接受延迟 (<2s): 72 个频道 (延迟: 平均 1299.5ms, 最低 815.1ms)
- unacceptable: 18 个频道 (延迟: 平均 3140.9ms, 最低 2078.1ms)
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 223.1ms, 最低 187.7ms)

### 📁 频道分组
- : 149 个频道

### 🔗 协议统计
- HLS (m3u8): 126 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.5 KB)
- iptv_medium_latency.m3u (11.7 KB)
- iptv_high_latency.m3u (21.0 KB)
- iptv_optimized_combined.m3u (38.0 KB)
- tvbox_optimized.m3u (48.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 387.5 秒
