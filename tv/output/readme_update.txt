## IPTV智能优化系统更新报告

生成时间: 2026-01-31T06:36:39.977262

### 📊 总体统计
- 总频道数: 152
- TVBox优化频道数: 152

### 📈 分级统计
- 中等延迟 (<800ms): 38 个频道 (延迟: 平均 577.8ms, 最低 324.3ms)
- 可接受延迟 (<2s): 75 个频道 (延迟: 平均 1345.2ms, 最低 800.1ms)
- unacceptable: 25 个频道 (延迟: 平均 4695.3ms, 最低 2101.9ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 237.1ms, 最低 183.4ms)

### 📁 频道分组
- : 152 个频道

### 🔗 协议统计
- HLS (m3u8): 134 个频道
- HTTP: 16 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.0 KB)
- iptv_medium_latency.m3u (11.4 KB)
- iptv_high_latency.m3u (21.5 KB)
- iptv_optimized_combined.m3u (36.8 KB)
- tvbox_optimized.m3u (50.3 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (212.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 473.0 秒
