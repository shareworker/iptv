## IPTV智能优化系统更新报告

生成时间: 2025-11-04T18:25:10.381231

### 📊 总体统计
- 总频道数: 167
- TVBox优化频道数: 167

### 📈 分级统计
- 中等延迟 (<800ms): 72 个频道 (延迟: 平均 558.3ms, 最低 375.7ms)
- 可接受延迟 (<2s): 50 个频道 (延迟: 平均 1443.6ms, 最低 814.5ms)
- unacceptable: 25 个频道 (延迟: 平均 2820.0ms, 最低 2033.6ms)
- 低延迟 (<300ms): 20 个频道 (延迟: 平均 222.6ms, 最低 181.6ms)

### 📁 频道分组
- : 167 个频道

### 🔗 协议统计
- HLS (m3u8): 143 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.7 KB)
- iptv_medium_latency.m3u (20.8 KB)
- iptv_high_latency.m3u (15.0 KB)
- iptv_optimized_combined.m3u (41.3 KB)
- tvbox_optimized.m3u (53.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 380.6 秒
