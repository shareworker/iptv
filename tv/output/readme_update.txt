## IPTV智能优化系统更新报告

生成时间: 2026-04-20T19:02:28.918351

### 📊 总体统计
- 总频道数: 129
- TVBox优化频道数: 129

### 📈 分级统计
- 中等延迟 (<800ms): 40 个频道 (延迟: 平均 536.5ms, 最低 302.2ms)
- 可接受延迟 (<2s): 68 个频道 (延迟: 平均 1363.2ms, 最低 869.1ms)
- unacceptable: 16 个频道 (延迟: 平均 4038.0ms, 最低 2168.6ms)
- 低延迟 (<300ms): 5 个频道 (延迟: 平均 278.6ms, 最低 261.2ms)

### 📁 频道分组
- : 129 个频道

### 🔗 协议统计
- HLS (m3u8): 128 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.5 KB)
- iptv_medium_latency.m3u (11.8 KB)
- iptv_high_latency.m3u (19.9 KB)
- iptv_optimized_combined.m3u (33.1 KB)
- tvbox_optimized.m3u (43.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 478.4 秒
