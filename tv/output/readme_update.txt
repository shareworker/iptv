## IPTV智能优化系统更新报告

生成时间: 2025-10-11T06:23:13.036235

### 📊 总体统计
- 总频道数: 163
- TVBox优化频道数: 163

### 📈 分级统计
- 中等延迟 (<800ms): 46 个频道 (延迟: 平均 569.4ms, 最低 312.7ms)
- 可接受延迟 (<2s): 65 个频道 (延迟: 平均 1429.5ms, 最低 835.7ms)
- unacceptable: 36 个频道 (延迟: 平均 2863.2ms, 最低 2038.1ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 218.6ms, 最低 182.1ms)

### 📁 频道分组
- : 163 个频道

### 🔗 协议统计
- HLS (m3u8): 139 个频道
- HTTP: 22 个频道
- FLV: 2 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (13.4 KB)
- iptv_high_latency.m3u (18.9 KB)
- iptv_optimized_combined.m3u (36.5 KB)
- tvbox_optimized.m3u (54.2 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (215.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 396.7 秒
