## IPTV智能优化系统更新报告

生成时间: 2026-09-14T11:25:58.424950

### 📊 总体统计
- 总频道数: 122
- TVBox优化频道数: 122

### 📈 分级统计
- 低延迟 (<300ms): 19 个频道 (延迟: 平均 211.4ms, 最低 161.3ms)
- 中等延迟 (<800ms): 34 个频道 (延迟: 平均 583.2ms, 最低 317.5ms)
- 可接受延迟 (<2s): 60 个频道 (延迟: 平均 1093.4ms, 最低 815.7ms)
- unacceptable: 9 个频道 (延迟: 平均 3507.4ms, 最低 2218.9ms)

### 📁 频道分组
- : 122 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 99 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (5.4 KB)
- iptv_medium_latency.m3u (10.1 KB)
- iptv_high_latency.m3u (17.5 KB)
- iptv_optimized_combined.m3u (32.8 KB)
- tvbox_optimized.m3u (39.6 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (206.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 343.9 秒
