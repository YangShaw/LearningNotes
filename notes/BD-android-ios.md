
# 工业级app的技术选型和标准

helo项目


## Android
- 对于简单的项目，也有针对性的进行技术深入。

- 布局：
使用约束性布局。

CoordinatorLayout 动画效果

merge include viewstub标签。

- 列表：RecyclerView
DiffUtil工具（自动检测变化），ViewHolder生命周期和缓存原理，相较于ListView的优点

- 存储：
数据库：SQLite， 数据库migration， 需求变动很快如何设计有扩展性的表

Room：更好用的数据库组件

- 图片：
图片库Glide， Fresco ？

图片库的多级缓存设计；

图片的分辨率适配：xhdpi， xxhdpi， xxxhdpi；为什么要区分不同的分辨率

图片格式：Webp， HEIF， RGB565 8888 大小的取舍

图标：IconFont， Vector

- push：
客户端和服务端之间有一个长连接，一个push模块的实现是【Notification+Service】。

对于耗时的操作，如网络请求，要单独起一个service

把push放到别的进程的好处，如崩溃之后不会影响主线程

- 服务：
前台service和后台service，

通知：自定义样式，如何实时更新样式等

- 网络：
OkHttp 除了网络请求意外的其他功能，责任链模式，网络监控，通用参数

如何优化网络性能， HTTP1.1 HTTP2.0 QUIC

对于不同的传输协议，怎样处理？（甚至现在都不了解不同的网络协议）

HTTPS, TLS1.2, TLS1.3 后者更快，快在哪里？

app启动的时候有很多请求同时发出，如何将多个请求合并起来（从而提升效率）？

JSON和PB

- 架构：
MVC基本等于没有架构；

MVP架构太复杂；

MVVM现代架构，LiveData， ViewModel：页面上、页面之间不同的元素如何进行同步

- 帧率：
有关于性能的问题。性能的优化比较困难，可以有自己的经验和体会

layout层级，onLayout， onMeasure的开销；

Overdraw， 透明背景，降低层级， 安卓进行渲染的时候一层一层向上渲染，遇到透明度问题，计算开销后很大；怎样减少层级？

bindViewHolder 做轻量级的事情

利用开发者选项中的工具进行性能监测检查等。

- 内存：
内存泄漏问题？常见的场景

LeakCanary 工作原理？

Profiler查看大内存  图片分辨率的问题

- 卡顿问题 启动速度 ANR
什么是ANR，如何检测

不要在主线程里做太多事情，IO放在IO线程里，不要乱起线程，用线程池管理好自己的线程，能懒加载的就懒加载（用到的时候才加载），不需要在启动的时候完全加载好。

- 网络差时：
无网时本地功能要尽可能可以使用，在线功能提供缓存，要迅速告知用户无网，不要一直处于loading中。

弱网时，loading不要让人烦，分块加载。

- 优雅的状态恢复：
注册流程走了一半？页面浏览到一半？能不能让app不要崩溃？用户体验问题

activity储存状态  onSaveInstanceState的作用， fragment在activity重建的时候需要检测重复创建

childFragmentManager 和 fragmentManager的区别


## iOS

- 布局
Frame和Constraint两种布局， 不排斥使用Frame， 约束性布局是描述性的，使用SnapKit开源库来简化布局关系的描述

SwiftUI 声明式布局 iOS13 基于flutter等技术 对应于命名式布局

- 动画
CoreAnimation pop  动画库，转场，放大，位移等
Lottie-ios  各种粒子效果 动画等

- 列表
UICollectionView 自定义程度更高，复合使用横向和竖向

IGListKit 局部更新

- 图片
png， pdf格式

分辨率 多倍

xcassets & imageset

网络图片的加载库：SDWebImage

- 存储
UserDefaults 轻量级 对应SP 线程安全，主app和extension数据同步

FMDB/YYCache

- 网络
Alamfire  NSURLSession

网络拦截问题 NSURLProtocol

- 架构
MVVM ViewModel， 配合Bind

- 页面间的通信
Delegate， Closure， 通知中心， 自定义中间件

- 工作空间
cocoapods 包管理工具

- 内存
内存泄漏（循环引用，C接口）和野指针的问题（变量多线程操作）