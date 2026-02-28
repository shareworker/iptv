## IPTV智能优化系统更新报告

生成时间: 2026-02-28T06:34:12.448825

### 📊 总体统计
- 总频道数: 145
- TVBox优化频道数: 145

### 📈 分级统计
- 中等延迟 (<800ms): 41 个频道 (延迟: 平均 553.6ms, 最低 326.9ms)
- 可接受延迟 (<2s): 70 个频道 (延迟: 平均 1327.1ms, 最低 822.2ms)
- unacceptable: 24 个频道 (延迟: 平均 2823.2ms, 最低 2035.2ms)
- 低延迟 (<300ms): 10 个频道 (延迟: 平均 227.4ms, 最低 184.2ms)

### 📁 频道分组
- : 145 个频道

### 🔗 协议统计
- HLS (m3u8): 121 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (2.9 KB)
- iptv_medium_latency.m3u (12.1 KB)
- iptv_high_latency.m3u (20.3 KB)
- iptv_optimized_combined.m3u (35.1 KB)
- tvbox_optimized.m3u (48.1 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.5 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 391.5 秒
