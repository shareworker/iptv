## IPTV智能优化系统更新报告

生成时间: 2026-06-21T19:26:58.927969

### 📊 总体统计
- 总频道数: 128
- TVBox优化频道数: 128

### 📈 分级统计
- 中等延迟 (<800ms): 48 个频道 (延迟: 平均 536.8ms, 最低 320.7ms)
- 可接受延迟 (<2s): 58 个频道 (延迟: 平均 1261.1ms, 最低 804.8ms)
- unacceptable: 18 个频道 (延迟: 平均 3465.5ms, 最低 2248.0ms)
- 低延迟 (<300ms): 4 个频道 (延迟: 平均 230.9ms, 最低 207.6ms)

### 📁 频道分组
- : 128 个频道

### 🔗 协议统计
- HLS (m3u8): 125 个频道
- HTTP: 2 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (1.2 KB)
- iptv_medium_latency.m3u (14.0 KB)
- iptv_high_latency.m3u (17.1 KB)
- iptv_optimized_combined.m3u (32.1 KB)
- tvbox_optimized.m3u (42.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (208.0 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 533.5 秒
