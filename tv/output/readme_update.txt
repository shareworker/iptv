## IPTV智能优化系统更新报告

生成时间: 2026-02-16T18:39:09.450314

### 📊 总体统计
- 总频道数: 144
- TVBox优化频道数: 144

### 📈 分级统计
- 中等延迟 (<800ms): 49 个频道 (延迟: 平均 585.4ms, 最低 314.8ms)
- unacceptable: 26 个频道 (延迟: 平均 2897.6ms, 最低 2027.7ms)
- 可接受延迟 (<2s): 55 个频道 (延迟: 平均 1276.4ms, 最低 841.7ms)
- 低延迟 (<300ms): 14 个频道 (延迟: 平均 207.7ms, 最低 175.4ms)

### 📁 频道分组
- : 144 个频道

### 🔗 协议统计
- HLS (m3u8): 121 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.9 KB)
- iptv_medium_latency.m3u (14.3 KB)
- iptv_high_latency.m3u (16.2 KB)
- iptv_optimized_combined.m3u (34.2 KB)
- tvbox_optimized.m3u (46.9 KB)
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
- 总耗时: 371.9 秒
