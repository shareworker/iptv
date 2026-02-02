## IPTV智能优化系统更新报告

生成时间: 2026-02-02T07:00:17.189593

### 📊 总体统计
- 总频道数: 145
- TVBox优化频道数: 145

### 📈 分级统计
- 低延迟 (<300ms): 4 个频道 (延迟: 平均 236.6ms, 最低 210.8ms)
- 中等延迟 (<800ms): 62 个频道 (延迟: 平均 553.4ms, 最低 319.4ms)
- 可接受延迟 (<2s): 67 个频道 (延迟: 平均 1262.2ms, 最低 809.5ms)
- unacceptable: 12 个频道 (延迟: 平均 2536.0ms, 最低 2036.8ms)

### 📁 频道分组
- : 145 个频道

### 🔗 协议统计
- HLS (m3u8): 127 个频道
- HTTP: 16 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.2 KB)
- iptv_medium_latency.m3u (18.3 KB)
- iptv_high_latency.m3u (18.9 KB)
- iptv_optimized_combined.m3u (38.2 KB)
- tvbox_optimized.m3u (46.5 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.4 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 381.7 秒
