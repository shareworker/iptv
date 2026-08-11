## IPTV智能优化系统更新报告

生成时间: 2026-08-11T18:56:08.983197

### 📊 总体统计
- 总频道数: 127
- TVBox优化频道数: 127

### 📈 分级统计
- 中等延迟 (<800ms): 38 个频道 (延迟: 平均 523.6ms, 最低 309.8ms)
- 可接受延迟 (<2s): 72 个频道 (延迟: 平均 1109.9ms, 最低 800.6ms)
- unacceptable: 5 个频道 (延迟: 平均 6184.2ms, 最低 5779.1ms)
- 低延迟 (<300ms): 12 个频道 (延迟: 平均 202.8ms, 最低 175.1ms)

### 📁 频道分组
- : 127 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 105 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.4 KB)
- iptv_medium_latency.m3u (11.0 KB)
- iptv_high_latency.m3u (21.2 KB)
- iptv_optimized_combined.m3u (35.4 KB)
- tvbox_optimized.m3u (40.5 KB)
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
- 总耗时: 341.8 秒
