## IPTV智能优化系统更新报告

生成时间: 2026-08-20T18:30:42.588998

### 📊 总体统计
- 总频道数: 127
- TVBox优化频道数: 127

### 📈 分级统计
- 低延迟 (<300ms): 18 个频道 (延迟: 平均 196.3ms, 最低 160.2ms)
- 可接受延迟 (<2s): 70 个频道 (延迟: 平均 1172.6ms, 最低 800.9ms)
- 中等延迟 (<800ms): 33 个频道 (延迟: 平均 495.9ms, 最低 341.9ms)
- unacceptable: 6 个频道 (延迟: 平均 2348.2ms, 最低 2285.4ms)

### 📁 频道分组
- : 127 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 104 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.0 KB)
- iptv_medium_latency.m3u (9.9 KB)
- iptv_high_latency.m3u (20.4 KB)
- iptv_optimized_combined.m3u (35.1 KB)
- tvbox_optimized.m3u (41.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 323.2 秒
