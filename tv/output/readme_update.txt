## IPTV智能优化系统更新报告

生成时间: 2026-07-24T08:15:46.681521

### 📊 总体统计
- 总频道数: 133
- TVBox优化频道数: 133

### 📈 分级统计
- 低延迟 (<300ms): 17 个频道 (延迟: 平均 175.3ms, 最低 140.8ms)
- 中等延迟 (<800ms): 70 个频道 (延迟: 平均 571.8ms, 最低 307.9ms)
- 可接受延迟 (<2s): 42 个频道 (延迟: 平均 1209.0ms, 最低 810.6ms)
- unacceptable: 4 个频道 (延迟: 平均 5714.4ms, 最低 5374.2ms)

### 📁 频道分组
- : 133 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 111 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.8 KB)
- iptv_medium_latency.m3u (20.6 KB)
- iptv_high_latency.m3u (12.1 KB)
- iptv_optimized_combined.m3u (37.3 KB)
- tvbox_optimized.m3u (41.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 324.6 秒
