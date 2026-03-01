## IPTV智能优化系统更新报告

生成时间: 2026-03-01T06:43:59.285165

### 📊 总体统计
- 总频道数: 126
- TVBox优化频道数: 126

### 📈 分级统计
- 低延迟 (<300ms): 5 个频道 (延迟: 平均 264.4ms, 最低 250.3ms)
- 中等延迟 (<800ms): 35 个频道 (延迟: 平均 543.9ms, 最低 342.7ms)
- 可接受延迟 (<2s): 54 个频道 (延迟: 平均 1353.3ms, 最低 828.3ms)
- unacceptable: 32 个频道 (延迟: 平均 2770.6ms, 最低 2090.5ms)

### 📁 频道分组
- : 126 个频道

### 🔗 协议统计
- HLS (m3u8): 124 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.4 KB)
- iptv_medium_latency.m3u (10.6 KB)
- iptv_high_latency.m3u (15.4 KB)
- iptv_optimized_combined.m3u (27.3 KB)
- tvbox_optimized.m3u (41.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 464.0 秒
