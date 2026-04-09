## IPTV智能优化系统更新报告

生成时间: 2026-04-09T07:18:26.776377

### 📊 总体统计
- 总频道数: 154
- TVBox优化频道数: 154

### 📈 分级统计
- 中等延迟 (<800ms): 47 个频道 (延迟: 平均 530.8ms, 最低 341.6ms)
- 可接受延迟 (<2s): 72 个频道 (延迟: 平均 1363.5ms, 最低 822.5ms)
- unacceptable: 19 个频道 (延迟: 平均 2989.2ms, 最低 2047.7ms)
- 低延迟 (<300ms): 16 个频道 (延迟: 平均 229.1ms, 最低 185.8ms)

### 📁 频道分组
- : 154 个频道

### 🔗 协议统计
- HLS (m3u8): 131 个频道
- HTTP: 22 个频道
- FLV: 1 个频道

### 💾 生成文件
#### 播放列表
- iptv_low_latency.m3u (4.5 KB)
- iptv_medium_latency.m3u (13.7 KB)
- iptv_high_latency.m3u (21.0 KB)
- iptv_optimized_combined.m3u (39.1 KB)
- tvbox_optimized.m3u (50.7 KB)
#### 数据文件
- aggregated_channels.json (148.8 KB)
- latency_test_results.json (213.2 KB)
#### 配置文件
- tvbox_config.json (0.4 KB)

### 🔧 使用建议
1. **TVBox用户**: 推荐使用 `tvbox_optimized.m3u` - 包含专用播放参数和缓存优化
2. **超低延迟需求**: 推荐使用 `iptv_ultra_low_latency.m3u` - 延迟<100ms的频道
3. **通用用户**: 推荐使用 `iptv_optimized_combined.m3u` - 各延迟等级的最佳频道
4. **稳定性需求**: 推荐使用 `iptv_medium_latency.m3u` - 延迟适中但更稳定

### ⭐ 执行信息
- 总耗时: 368.7 秒
