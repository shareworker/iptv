## IPTV智能优化系统更新报告

生成时间: 2026-02-20T06:50:23.963945

### 📊 总体统计
- 总频道数: 147
- TVBox优化频道数: 147

### 📈 分级统计
- 低延迟 (<300ms): 36 个频道 (延迟: 平均 214.0ms, 最低 150.8ms)
- 中等延迟 (<800ms): 52 个频道 (延迟: 平均 583.3ms, 最低 304.9ms)
- 可接受延迟 (<2s): 45 个频道 (延迟: 平均 1358.2ms, 最低 834.4ms)
- unacceptable: 14 个频道 (延迟: 平均 2698.6ms, 最低 2173.6ms)

### 📁 频道分组
- : 147 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 123 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (10.5 KB)
- iptv_medium_latency.m3u (15.0 KB)
- iptv_high_latency.m3u (13.1 KB)
- iptv_optimized_combined.m3u (38.5 KB)
- tvbox_optimized.m3u (46.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.7 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 365.5 秒
