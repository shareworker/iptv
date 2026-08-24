## IPTV智能优化系统更新报告

生成时间: 2026-08-24T18:33:09.315195

### 📊 总体统计
- 总频道数: 126
- TVBox优化频道数: 126

### 📈 分级统计
- 低延迟 (<300ms): 22 个频道 (延迟: 平均 202.1ms, 最低 139.1ms)
- 中等延迟 (<800ms): 61 个频道 (延迟: 平均 593.3ms, 最低 300.4ms)
- 可接受延迟 (<2s): 41 个频道 (延迟: 平均 1079.1ms, 最低 802.6ms)
- unacceptable: 2 个频道 (延迟: 平均 7698.1ms, 最低 5830.5ms)

### 📁 频道分组
- : 126 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 104 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.2 KB)
- iptv_medium_latency.m3u (18.1 KB)
- iptv_high_latency.m3u (11.7 KB)
- iptv_optimized_combined.m3u (35.8 KB)
- tvbox_optimized.m3u (38.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 335.4 秒
