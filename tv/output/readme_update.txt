## IPTV智能优化系统更新报告

生成时间: 2026-06-22T20:41:45.414918

### 📊 总体统计
- 总频道数: 148
- TVBox优化频道数: 148

### 📈 分级统计
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 230.8ms, 最低 210.1ms)
- 中等延迟 (<800ms): 40 个频道 (延迟: 平均 586.6ms, 最低 341.5ms)
- 可接受延迟 (<2s): 70 个频道 (延迟: 平均 1280.4ms, 最低 802.2ms)
- unacceptable: 24 个频道 (延迟: 平均 3595.1ms, 最低 2037.8ms)

### 📁 频道分组
- : 148 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 125 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.0 KB)
- iptv_medium_latency.m3u (11.9 KB)
- iptv_high_latency.m3u (20.3 KB)
- iptv_optimized_combined.m3u (36.0 KB)
- tvbox_optimized.m3u (48.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 401.4 秒
