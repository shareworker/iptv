## IPTV智能优化系统更新报告

生成时间: 2026-07-25T07:58:13.733516

### 📊 总体统计
- 总频道数: 81
- TVBox优化频道数: 81

### 📈 分级统计
- 中等延迟 (<800ms): 29 个频道 (延迟: 平均 587.5ms, 最低 317.5ms)
- 可接受延迟 (<2s): 37 个频道 (延迟: 平均 1418.3ms, 最低 838.1ms)
- unacceptable: 3 个频道 (延迟: 平均 7377.5ms, 最低 7369.9ms)
- 低延迟 (<300ms): 12 个频道 (延迟: 平均 219.2ms, 最低 206.2ms)

### 📁 频道分组
- : 81 个频道

### 🔗 协议统计
- HLS (m3u8): 58 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.4 KB)
- iptv_medium_latency.m3u (8.5 KB)
- iptv_high_latency.m3u (10.6 KB)
- iptv_optimized_combined.m3u (22.3 KB)
- tvbox_optimized.m3u (26.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (198.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 354.6 秒
