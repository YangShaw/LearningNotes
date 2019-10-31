
# Language Server

---

## 是什么

- VS Code的一种插件，它可以用来实现自动补全、语法错误检查、定义跳转等功能。
- challenge：
    - 1 多种语言在vs code中的集成；
    - 2 纠正一个文件的过程中需要编译大量其他文件，构造语法树，进行静态编译等。这些可能会拖慢运行速度。
    - 3 编程语言和editor/ide之间全连接不能复用;

- 架构：
    - vs code中的客户端，通过json格式发送数据请求给服务端，服务端返回响应的数据回去。

- sample：
    - repo地址：git@github.com:microsoft/vscode-extension-samples.git

- package.json:
    - activationEvents表示当前server对应的语言；只要打开一个对应的文件，vs code就启动当前插件。
    - configuration中是在vs code中的一些配置；

- client/src/extension.ts 是插件的入口文件。