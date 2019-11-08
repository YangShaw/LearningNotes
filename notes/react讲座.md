<!-- TOC -->

- [JavaScript](#javascript)
- [TypeScript](#typescript)
- [React](#react)
- [CRA](#cra)
- [CSS](#css)
- [数据请求Axios](#数据请求axios)

<!-- /TOC -->


# JavaScript
- js也能编写桌面端应用；

- [JavaScript指南](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide)
    - js中的import可以只导入需要的模块，因为js库是要在线加载的，这样可以加快加载速度。
    - let 和 var 的区别。
    - export 对外暴露接口，相当于给出一个public的权限
        - ?这两种区别
        - export default demo1 -->  import demo1
        - export const demo2 --> import {demo2}
    - callback 异步操作。例如连接db，就直接发起一个请求，然后js去做其他的事情，等到连接db完成后，再回来操作db。
    - promise 解决异步回调嵌套的问题。当逻辑越来越多的时候，使用callback的异步形式会导致代码嵌套越来越复杂，可读性变差；promise可以消除这些嵌套。
    - document是browser object，浏览器提供的全局变量

# TypeScript
- 强类型语言
- 将类型定义好，方便使用，方便阅读
- 渐进式强类型，可以支持弱类型，也就是能够兼容JS
- 框架
    - Angular Google风格，java风格
    - React 渐进式，不算开发框架，
    - Vue

# React
- 声明式，组件化，只渲染UI层，响应交互，与逻辑无关。
    - 过程式编程，关注如何实现， how；
    - 声明式编程，关注实现什么， what， 如SQL。不需要写实现的逻辑，由框架帮你去实现。
        - react是f层，帮助构造方法，你专注于state。
    - 组件化，微服务的思想
        - 生成一个Article的组件，将相同的地方（h2,p格式）抽象起来，将不同的地方暴露出来（title和content的内容，作为参数传入）。让代码可以复用，相当于面向对象的编程思想。
        - 组件库，提供各种可用的组件，直接提供参数即可，例如ant design等就是组件库。

        - 组件：
            - 外部依赖props
            - 内部状态state
            - 视图render view


- .js类型，.ts类型； .tsx类型 ts和html放在一起
- jsx 可以在js中写html，一种编写组件的方式

- hooks 当外部依赖发生变化的时候，修改内部的响应

- 

# CRA
- 是一种工具，帮助创建项目

# CSS
- flex布局的规则
- hover，focus

# 数据请求Axios
- http1.0， 2.0
- 能够解决数据请求的问题