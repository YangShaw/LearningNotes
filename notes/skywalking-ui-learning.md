
**skywalking-ui的配置和修改**

## 项目结构
### 配置文件
- package.json
- tsconfig.json
- vue.config.json
- babel.config.json
### src 代码
- App.vue
生成了id=app的组件，规定它的css等
- router.ts
用来配置和vue的路由router相关的路径，router-link和router-view需要这些路径来找到相应的文件
- main.ts
导入项目需要的主要的基础组件，使用Vue.use()来使用组件，这里有和国际化有关的VueI18n，导入国际化的使用语言（中英文）、主组件app，路由router，组件库components，各种echarts中的图标，ui库elementUI等。
- event-bus.ts
？？？什么是event bus

- views/
    - containers/

    这个文件夹里是页面中各个大菜单页面的内容，就是首页中菜单栏里各个选项仪表盘dashboard，拓扑topology，追踪trace，告警alarm，对比comperison等选项，每一个对应一个相应的vue文件。index.vue是当仁不让的起点主页面，在这个vue文件中的template里，也引入了id="app"的组件，里面放入一个header，一个footer，和一个router-view留待通过路由来填写。header和footer等相当于基础组件，存放在根目录下的components文件夹里。

    - components/

    这个文件夹里的五个子文件夹分别对应了五个菜单栏选项中用到的组件。

- components/

基础组件库，例如主页面中用到的，构造布局的header，footer，甚至最简单的返回、选择等，都属于基础组件。

    - rk-header.vue

    以这个组件为例。


- assets/
资源库，包括png图片库img/，svg图片库svg/，支持国际化的语言库lang/，样式库styles。

- utils/
封装了一些常用功能的函数。


### public 入口html网页
### node_modules 依赖库

## Vue文件格式
主要包括三个标签对：
    - template，相当于render函数中return的内容，里面是这个组件具体的html元素
    - script，用到的脚本
    - style，用到的样式

## 语法学习
- 启动
npm run serve

- id='app'  : src/containers/index.vue

- 各个模块（仪表盘，拓扑图，追踪，告警等）的主类在containers中，每个模块用到的组件在components下的各个文件夹中。

- 导入导出的语法（和react略有不同）
import xxx from XX，这里xxx是给导入的模块直接起的别名（相当于省略了import .. as ..的语法），导入的是export default的内容（因为default部分不要起名，这里也没有指定名字，只能是对应default部分）。

所以之前我一直找RKHeader找不着，事实上RKHeader只是在index.vue中引用rk-header.vue中默认组件时，给它起的别名。

export 名字，非默认导出，那么在导入的时候就需要import {名字}。

./ 指当前目录，../指上一层目录， @/指从根目录（如src）开始找，例如@/views 相当于 src/views。

- main.ts中引用了各种库
- this.$t 和国际化有关，需要使用vue-i18n，main.ts中有关于i18n的配置，说明了支持zh和en两种语言
    - 相关的对应文字信息位于：src/assets/lang 文件夹下。

    - 以修改alarm-tool中【过滤范围】下的列表名字为例，

- router-view标签, 和router-link搭配使用
    - router.ts中配置了相关的路径信息. 
    - 配置一个new Router
    - 增添新菜单需要在router.ts中添加相应的路径。

- 标签use  xlink href="" 是引用svg图像

- props参数 在类中@Prop()中表示一个参数，在引用这个类组件的时候通过写属性和对应值的形式给参数赋值。

- @符号 是typescript的类装饰器，如果需要使用要在tsconfig.json文件中修改：
```
"experimentalDecorators": true,
```

