
# vue学习

## 参考资料
- [vue 中文文档](https://cn.vuejs.org/v2/guide/)
- [@vue-cli](https://cli.vuejs.org/zh/guide/)

## 其他知识
- vue-cli和@vue-cli
vue-cli是脚手架（create-react-app），全局安装之后，可以执行vue指令。

## 安装
- 脚手架vue-cli；
- 直接下载vue.js包，并通过script引入；


## 基础语法
- vue组件，template
- new Vue()
el: data: methods:
- 注册组件
```
Vue.component('name', {
    props:[],
    template:''
})
```

- 页面组件化的一个例子
设计页面的时候，可以先画出大布局下的每个组件以及每个组件下又能拆分成什么样子。
```
<div id="app">
  <app-nav></app-nav>
  <app-view>
    <app-sidebar></app-sidebar>
    <app-content></app-content>
  </app-view>
</div>
```
- 创建实例：通过Vue函数。
所有的vue组件都是vue的实例。    

实例中的一些比较固定的组成内容：el表示id名，data表示属性，methods表示实现方法，还可以把生命周期hook写在这里（用相同的格式），如created: function(){}，除此之外还有mounted，updated，destroyed等。
