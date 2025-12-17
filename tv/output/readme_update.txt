## IPTV智能优化系统更新报告

生成时间: 2025-12-17T18:27:56.847939

### 📊 总体统计
- 总频道数: 164
- TVBox优化频道数: 164

### 📈 分级统计
- 可接受延迟 (<2s): 49 个频道 (延迟: 平均 1089.6ms, 最低 818.1ms)
- unacceptable: 27 个频道 (延迟: 平均 3381.9ms, 最低 2005.4ms)
- 中等延迟 (<800ms): 64 个频道 (延迟: 平均 531.5ms, 最低 315.5ms)
- 低延迟 (<300ms): 24 个频道 (延迟: 平均 214.8ms, 最低 161.6ms)

### 📁 频道分组
- : 164 个频道

### 🔗 协议统计
- FLV: 2 个频道
- HLS (m3u8): 140 个频道
- HTTP: 22 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (6.8 KB)
- iptv_medium_latency.m3u (18.7 KB)
- iptv_high_latency.m3u (14.7 KB)
- iptv_optimized_combined.m3u (40.0 KB)
- tvbox_optimized.m3u (52.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.3 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 372.8 秒
