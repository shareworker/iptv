## IPTV智能优化系统更新报告

生成时间: 2026-03-02T06:54:27.346241

### 📊 总体统计
- 总频道数: 136
- TVBox优化频道数: 136

### 📈 分级统计
- 低延迟 (<300ms): 3 个频道 (延迟: 平均 266.2ms, 最低 259.3ms)
- 中等延迟 (<800ms): 36 个频道 (延迟: 平均 558.2ms, 最低 316.3ms)
- 可接受延迟 (<2s): 84 个频道 (延迟: 平均 1232.1ms, 最低 822.9ms)
- unacceptable: 13 个频道 (延迟: 平均 3634.1ms, 最低 2014.8ms)

### 📁 频道分组
- : 136 个频道

### 🔗 协议统计
- HLS (m3u8): 134 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (0.9 KB)
- iptv_medium_latency.m3u (10.7 KB)
- iptv_high_latency.m3u (24.4 KB)
- iptv_optimized_combined.m3u (35.8 KB)
- tvbox_optimized.m3u (43.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (209.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 473.0 秒
