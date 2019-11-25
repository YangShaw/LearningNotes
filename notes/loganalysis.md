
# 项目分析

## 路由
路由的配置信息在config/config.js中。

## 方法封装 utils
- authority.ts
get和set权限的方法。

当前项目在本地存储权限信息。实际项目中可能通过网络传输。

## 起点+布局 index.jsx
> pages/dashboard/log-analysis/index.jsx
采用grid布局，row和col配合使用。24格grid。类比bootstrap的布局。对应页面中的class="ant-pro-grid-content"。

通过设置列的span属性来表示占的格子数。

这里对应了主页面中各个图表的布局方式。

给col设置xl,lg,md,sm,xs等是响应式布局。

Row:type指定这一行的布局方式，如flex。
- flex布局，可以指定justify属性为start，center，end，space-between，space-around来设置水平方向排列方式。
- flex对齐，可以指定align属性为top, middle, bottom等来设置垂直方向对齐方式。
- flex排序，可以指定order属性的1，2，3，4等来规定不同col的排列位置。

区块间隔：表示的是每一个col之间的间隔。通过设置Row的gutter属性，推荐使用16+8n作为间隔数。可以写成响应式，也可以增加垂直间距。

左右偏移：设置col的offset属性可以使列向右偏移对应的格子。

## 国际化内容 locales

## 静态数据
> pages/dashboard/log-analysis/components/static-data
包含了绘制七张图表的静态数据。

通过utils/request中的方法来加载数据，这些数据配置了路径/api/xxx data，但是还没有发现是怎么配置的路径。

service.jsx中提供了加载各个数据的封装方法，给请求每份数据都封装了一个单独的方法。

## 图表
> pages/dashboard/log-analysis/components
这个目录下的两个文件夹中分别包含了系统级和用户级共七种图表。

Scatterplot为例：每一个部分都包含了较多的样式信息，关注其中的重要部分。
- tooltip：鼠标悬浮在事件上的提示消息
- xAxis,yAxis：坐标轴
- series：三种数据类型，对应的数据是props中传递过来的report1-3
- dataZoom：图表下方的拖拽条，可以放大特定时间区间