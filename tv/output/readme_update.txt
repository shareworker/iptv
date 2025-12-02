## IPTV智能优化系统更新报告

生成时间: 2025-12-02T18:28:08.063693

### 📊 总体统计
- 总频道数: 110
- TVBox优化频道数: 110

### 📈 分级统计
- 中等延迟 (<800ms): 37 个频道 (延迟: 平均 564.3ms, 最低 314.0ms)
- 可接受延迟 (<2s): 44 个频道 (延迟: 平均 1372.7ms, 最低 855.5ms)
- unacceptable: 15 个频道 (延迟: 平均 5387.0ms, 最低 2040.2ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 230.5ms, 最低 202.8ms)

### 📁 频道分组
- : 110 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 86 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.9 KB)
- iptv_medium_latency.m3u (10.8 KB)
- iptv_high_latency.m3u (12.9 KB)
- iptv_optimized_combined.m3u (27.5 KB)
- tvbox_optimized.m3u (35.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (204.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 390.8 秒
