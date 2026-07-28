## IPTV智能优化系统更新报告

生成时间: 2026-07-28T19:15:52.471932

### 📊 总体统计
- 总频道数: 130
- TVBox优化频道数: 130

### 📈 分级统计
- 中等延迟 (<800ms): 42 个频道 (延迟: 平均 564.1ms, 最低 321.9ms)
- 可接受延迟 (<2s): 67 个频道 (延迟: 平均 1159.6ms, 最低 805.6ms)
- unacceptable: 6 个频道 (延迟: 平均 5181.5ms, 最低 2499.7ms)
- 低延迟 (<300ms): 15 个频道 (延迟: 平均 219.7ms, 最低 200.8ms)

### 📁 频道分组
- : 130 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 107 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.2 KB)
- iptv_medium_latency.m3u (12.2 KB)
- iptv_high_latency.m3u (19.5 KB)
- iptv_optimized_combined.m3u (35.8 KB)
- tvbox_optimized.m3u (41.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 325.1 秒
