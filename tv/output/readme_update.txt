## IPTV智能优化系统更新报告

生成时间: 2025-12-15T18:27:39.066681

### 📊 总体统计
- 总频道数: 146
- TVBox优化频道数: 146

### 📈 分级统计
- 中等延迟 (<800ms): 63 个频道 (延迟: 平均 487.5ms, 最低 312.5ms)
- 可接受延迟 (<2s): 58 个频道 (延迟: 平均 1350.6ms, 最低 805.8ms)
- unacceptable: 9 个频道 (延迟: 平均 2938.6ms, 最低 2129.3ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 201.6ms, 最低 161.1ms)

### 📁 频道分组
- : 146 个频道

### 🔗 协议统计
- HLS (m3u8): 122 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (18.3 KB)
- iptv_high_latency.m3u (17.3 KB)
- iptv_optimized_combined.m3u (40.0 KB)
- tvbox_optimized.m3u (46.8 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (211.6 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 371.2 秒
