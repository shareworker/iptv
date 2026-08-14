## IPTV智能优化系统更新报告

生成时间: 2026-08-14T07:17:00.022444

### 📊 总体统计
- 总频道数: 128
- TVBox优化频道数: 128

### 📈 分级统计
- 低延迟 (<300ms): 13 个频道 (延迟: 平均 217.3ms, 最低 200.5ms)
- 可接受延迟 (<2s): 62 个频道 (延迟: 平均 1294.6ms, 最低 800.6ms)
- unacceptable: 10 个频道 (延迟: 平均 2756.0ms, 最低 2038.1ms)
- 中等延迟 (<800ms): 43 个频道 (延迟: 平均 595.9ms, 最低 317.1ms)

### 📁 频道分组
- : 128 个频道

### 🔗 协议统计
- HTTP: 22 个频道
- HLS (m3u8): 105 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (3.7 KB)
- iptv_medium_latency.m3u (12.7 KB)
- iptv_high_latency.m3u (18.1 KB)
- iptv_optimized_combined.m3u (34.3 KB)
- tvbox_optimized.m3u (41.4 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (207.9 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 335.8 秒
