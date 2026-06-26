## IPTV智能优化系统更新报告

生成时间: 2026-06-26T19:38:06.914571

### 📊 总体统计
- 总频道数: 122
- TVBox优化频道数: 122

### 📈 分级统计
- 低延迟 (<300ms): 5 个频道 (延迟: 平均 265.6ms, 最低 248.4ms)
- 可接受延迟 (<2s): 70 个频道 (延迟: 平均 1301.1ms, 最低 837.4ms)
- unacceptable: 25 个频道 (延迟: 平均 3614.9ms, 最低 2004.2ms)
- 中等延迟 (<800ms): 22 个频道 (延迟: 平均 637.4ms, 最低 315.4ms)

### 📁 频道分组
- : 122 个频道

### 🔗 协议统计
- HLS (m3u8): 121 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.5 KB)
- iptv_medium_latency.m3u (6.5 KB)
- iptv_high_latency.m3u (20.5 KB)
- iptv_optimized_combined.m3u (28.4 KB)
- tvbox_optimized.m3u (41.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (206.8 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 555.6 秒
