## IPTV智能优化系统更新报告

生成时间: 2025-12-30T18:27:12.872299

### 📊 总体统计
- 总频道数: 159
- TVBox优化频道数: 159

### 📈 分级统计
- 中等延迟 (<800ms): 63 个频道 (延迟: 平均 498.3ms, 最低 300.1ms)
- 可接受延迟 (<2s): 53 个频道 (延迟: 平均 1167.7ms, 最低 802.1ms)
- unacceptable: 21 个频道 (延迟: 平均 3102.3ms, 最低 2026.6ms)
- 低延迟 (<300ms): 22 个频道 (延迟: 平均 219.3ms, 最低 151.2ms)

### 📁 频道分组
- : 159 个频道

### 🔗 协议统计
- HLS (m3u8): 135 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.2 KB)
- iptv_medium_latency.m3u (18.4 KB)
- iptv_high_latency.m3u (15.5 KB)
- iptv_optimized_combined.m3u (40.0 KB)
- tvbox_optimized.m3u (49.9 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (214.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 372.6 秒
