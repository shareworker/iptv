## IPTV智能优化系统更新报告

生成时间: 2026-02-11T06:59:33.857891

### 📊 总体统计
- 总频道数: 144
- TVBox优化频道数: 144

### 📈 分级统计
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 206.2ms, 最低 173.7ms)
- 中等延迟 (<800ms): 44 个频道 (延迟: 平均 593.5ms, 最低 302.8ms)
- 可接受延迟 (<2s): 65 个频道 (延迟: 平均 1220.0ms, 最低 800.1ms)
- unacceptable: 20 个频道 (延迟: 平均 2810.8ms, 最低 2021.6ms)

### 📁 频道分组
- : 144 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 120 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (12.8 KB)
- iptv_high_latency.m3u (19.1 KB)
- iptv_optimized_combined.m3u (35.9 KB)
- tvbox_optimized.m3u (47.0 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 368.2 秒
