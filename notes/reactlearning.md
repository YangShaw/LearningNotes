
<!-- TOC -->

- [T0 参考资料](#t0-参考资料)
- [关于 CRA](#关于-cra)
- [辅助工具](#辅助工具)
- [开始](#开始)
- [先导知识](#先导知识)
- [基础知识](#基础知识)
- [JSX](#jsx)
- [组件 Component](#组件-component)
- [状态 State](#状态-state)
- [Hooks](#hooks)
- [练习过程](#练习过程)

<!-- /TOC -->

## T0 参考资料

- **文档真的是最好的参考资料！**

- [CRA 中文文档](https://www.html.cn/create-react-app/docs/getting-started/)
- [React 中文文档](https://react.docschina.org/docs/getting-started.html)
- [React 入门教程-Tictactoe](https://react.docschina.org/tutorial/tutorial.html)
- [MDN JavaScript 指南](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
- [CSS 布局](https://learn-the-web.algonquindesign.ca/topics/css-layout-cheat-sheet/)
- [TypeScript 中文文档](https://typescript.bootcss.com/)
- [reactstrap 组件](http://reactstrap.github.io/components/alerts/)

## 关于 CRA

- 无需配置 Webpack 或 babel。已经预先配置好，并且隐藏——项目目录干净整洁。

- 目录结构用基于 ts 的 CRA 来介绍。

  - public/index.html 页面模板
  - src/index.tsx 项目入口
  - 这两个文件名不要修改，其他文件自由改动。

- src 文件夹：包含所有 js 和 css，在 src 中创建子目录来构造项目，webpack 只处理 src 中的文件。

- 更新版本：react-scripts

- webpack支持使用如下语句为Example.tsx导入样式表。路径中的./表示当前目录，而不是从全局查找。
    ```
    import ./Example.css
    ```
    - 导入图片和字体同理。统统import搞定。例如示例中的导入logo图片。

- 使用Example.module.css格式的样式表可以防止样式表中的类重名。后续再了解。

- public文件夹：
    - index.html中可以修改标题等。
    - public文件夹中可以添加静态资源（如图片），如果js中要引用需要添加process.env.PUBLIC_URL的前缀来访问目录。但不推荐这样。最好是在js中通过import来加载资源。

- 安装需要的依赖项
    ```
    yarn add [dependency]
    ```

- 使用import和export来导入组件。
    - 默认导出和命名导出：
        - 每个模块只可以有一个export default。
        - 函数，变量，常量等都可以导出。
        ```
        // 默认
        export default Button;

        import Button from "./Button";

        // 命名
        export {Button1, Button2};
        export Button1 as b;

        import {Button1, Button2} from "./Button"
        import {Button1 as b} from "./Button"
        ```
- 快捷写法 div.example 然后按tab 能自动创建相应className的标签

## 辅助工具
- **刚上手学的时候，先不要纠结于细节！后面再慢慢完善**
- **CRA就是让我们专注于代码，不要辜负了它**

- prettier 格式化工具
  - 安装 npm install -g prettier
  - 集成到 vscode 中：
    - 搜索 Prettier - Code formatter 插件并安装
    - 使用 shift + alt + f 快捷键来格式化代码

- bootstrap 这里要记住，给ts用的react库都要加上@types，不然在import的时候会报无法找到模块的错误。

    ```
    yarn add bootstrap@4
    yarn add @types/reactstrap
    ```

    - 使用的时候，import相应的模块即可。具体的组件参见reactstrap的文档。
        ```
        import {Button} from 'reactstrap'

        <Button color="primary">primay</Button>
        ```

- eslint 代码检查

- babel js编译

- webpack js打包

- storybook 组件管理工具，之后再研究 [storybook管理react组件示例](https://www.jianshu.com/p/9cb75ae50515)

- styleguidist

- source map exploer 分析JS包的大小

## 开始

- 使用 npm 或 cnpm 构建第一个项目 create-react-app

```
create-react-app my-app
```

- 如果要创建基于 TypeScript 的 react 环境：

```
create-react-app my-app --typescript
```

- 启动指令 npm start

- 测试 yarn test
- 打包为生产模式，优化构建 yarn build

- 项目目录结构：

  - public/
    - index.html 代码执行的源头
    - manifest.json 指定开始页面 start_url
  - src/
  - node_modules/
  - package.json

- 可以对比 index.html 和页面审查元素的代码。

  - root 内的代码段由 js 动态生成。
  - 这一段 className=APP 的 div 标签正是写在 App.js 中的，是函数的返回值。
    - App.js 和 App.css 用来写函数返回的内容和这个函数返回的 html 的 CSS 格式；
      - App.css 中都是根据 App.js 中的类名来设计样式的。这就属于 CSS 的知识了。暂时不关注。先理解逻辑。
    - index.js 中是调用这些函数构造界面的，相当于 main 方法。
    - 函数去 index.html 中定位。

## 先导知识

- 箭头函数：

  ```
  - (参数1, 参数2, …, 参数N) => { 函数声明 }
  - //相当于：(参数1, 参数2, …, 参数N) =>{ return 表达式; }
  - (参数1, 参数2, …, 参数N) => 表达式（单一）
  - // 当只有一个参数时，圆括号是可选的：
  - (单一参数) => {函数声明}
  - 单一参数 => {函数声明}
  - // 没有参数的函数应该写成一对圆括号。
  - () => {函数声明}
  ```

  - 更简短；不会绑定 this。

- let，var,const
  - let 允许声明一个作用域限制在块级的变量、语句或表达式。
  - var 声明的变量作用域是整个封闭函数。在函数顶部用 var 声明会给全局对象新增属性，如：
    ```
    var x = 'global'
    let y = 'local'
    console.log(this.x) //  可以访问
    console.log(this.y) //  undefined
    ```
  - const 创建常量

- promise和callback
    - **还没理解**

    - 事件异步执行，使用回调函数。异步的结果是程序不会按顺序执行：
    ```
    function callback() {
        console.log('Done');
    }
    console.log('before setTimeout()');
    setTimeout(callback, 1000); // 1秒钟后调用callback函数
    console.log('after setTimeout()');

    //  输出结果
    before setTimeout()
    after setTimeout()
    (等待1秒后)
    Done
    ```


## 基础知识

- ReactDOM.render(): 核心渲染方法，所有的 js 和 html 都可以通过它来进行渲染绘制。
  - 两个参数：
    - 内容，也就是要被渲染进去的东西，例如 App.js 中定义的函数 App，那么就是渲染这个函数返回的值；也可以直接是一个常量。
      - const element = <h1>Hello, world!</h1>;
      - <App [attribute1=xxx] /> 注意这里跟参数的格式，要往 html 标签中写属性和属性值的格式那个方向想。想想听 react 课上的那一次灵机一动。
      - 这个参数就被称之为 props。
        - 例如有两个参数 title，name，在函数体内通过**props.title**的方式来使用参数；
        - 在 render 中通过&lt;App title="myTitle" name="myName" /&gt;的方式来给出参数的值。
    - 渲染目标，通过 document.getElementBy\*\*\*的方式找到要写入的地方，例如写到 index.html 的 id 为 root 的标签内。也就是被渲染的内容放置的容器。
- ReactDOM.unmountComponentAtNode(): 解除渲染。

- 也可以通过类的方式来封装 html 代码，写一个类相当于写了一个组件 React Component。ES6 类。
  - 用 this.props 的方式来使用参数。
  - 要 extends React.Component
- function 和 ES6 class 都可以用来定义组件。注意名称要大写开头，以和原生 html 的小写开头区分开来。
- 添加属性时，class 属性要写成 className，for 属性要写成 htmlFor。



## JSX

- return 的 html 元素块就是使用了 jsx 代码。
- 可用来替代常规 js，是 js 的语法扩展。
- JSX 用来声明 React 中的元素。元素是构成 React 应用的最小单位。如:

```
    const element = <h1>Hello, world!</h1>;
```

- React 元素就是对象/变量/实例，React DOM 确保 React 元素中的内容和页面上的 DOM 内容一致。
- jsx 代码可以放在一个独立的 js 文件中（或直接写成 jsx 文件），然后在 html 中要导入这个 js。
- jsx 中不能使用 if-else 语句，可以用三目运算符来替代。
  - 内联样式：将 html 元素的某些属性值写成变量的形式。

## 组件 Component

- div，a，h1 等标签就是所谓的内置 DOM 组件；
- 调用自定义组件 < ShoppingList />

## 状态 State

- 组件是状态机。
- 与用户的交互用来更新状态，通过更新组件的状态来重新渲染 ui，不要修改 dom。
- state 可变，而 props 不可变。子组件只能通过 props 来传递参数，而定义 state 才能更新和修改参数。
- 父组件将一些参数设置成 state，子组件中调用这些 state 作为它们的 props。这样只有父组件可以修改参数值，子组件只负责渲染。
- State is used for internal communication inside a Component.

## Hooks

- 定义：在函数组件中“钩进去”React state 和它的生命周期等特性的函数。Hook 不能在 class 中使用。
- state hook

  - 如 useState。给它一个参数，作为初始值。[]中的第一个参数是变量名（也可以是一个对象），第二个参数为这个变量指定一个修改它的值的方法。
  - 相当于用来给函数添加一个 state。之前需要将函数转化为 class 才能添加 state，现在可以直接利用 hook。但 hook 不能写在 class 中。
  - 如果需要添加多个 state，那么就多次调用 useState 即可。

  ```
      const [count, setCount] = useState(0)
  ```

  - 如果需要访问 state，直接用变量名就可以，如{count}。但在 class 的写法中，需要用{this.state.count}的冗杂写法。
  - 如果需要修改 state，直接用已经和变量绑定好的方法就可以，如 setCount(直接写新的 count 值)。但在 class 的写法中，需要用 this.setState({count: this.state.count+1})的冗杂写法。
    - 也就是说，原来所有的 state 都要通过 setState 这一个方法来修改，区分不同参数的方式是在 setState 中专门指定要修改什么；但 hook 能让我们给每个 state 都指定一个修改它的方法。

- Effect hook
  - 给函数组件增加了操作副作用的能力。相当于 componentDidMount 和 componentDidUpdate。
  - 使用 useEffect，就是告诉函数在**执行完对 dom 的修改后**（执行完 return 语句），运行这个副作用函数（主要的作用当然是 return 的内容对 ui 的渲染）。React 确保每次执行副作用的时候，DOM 都已经更新完毕（渲染完成）。
    - 在组件内部调用 useEffect。这样可以直接访问局部变量 state（们），以及 props。
    - 在每次渲染后调用副作用函数（每次更新 state 都会触发新的渲染），在第一次渲染后也会调用。
      - 而在 class 中，副作用要区分在加载时（componentDidMount）和更新时（componentDidUpdate）。很多时候这两者需要进行的操作时相同的，但不得不写两遍代码。


    - 副作用操作的类型：
        - 不需要清除的副作用：意味着执行完之后，就可以忽略的一些操作。比如发送网络请求，更新日志等。
            - 举例：修改title。注意这里是直接修改的document级别的内容，注意后面的字符串是用<font color="red">这个点 `</font>包裹起来的。里面用到变量的时候，用<font color="red"> ${count} </font>的格式来写。
                ```
                useEffect(() => {
                    document.title = `You have Clicked ${count} times`;
                });
                ```

        - 需要清除的副作用：例如订阅外部的数据源。在使用完后要清除掉。
            - class中，通常是componentDidMount中订阅，componentWillUnmount中取消订阅。
            - 清除机制：给useEffect写一个返回函数。它的返回函数会在执行清除操作时调用。而其他的主体部分就如前面所说，在每次更新渲染的时候调用。
            - 不需要清除的副作用就不用写返回函数。

    - 优点：
        - class的生命周期函数只有三个，所以意味着不同的逻辑，如果都需要加载时运行，那么就都得放在componentDidMount中。其他同理。
        - 而相同的逻辑，如果需要加载时和刷新时都运行，那么就不得不分散到两个函数中。其他同理。
        - 使用hook，则可以写若干个useEffect，来将不同的逻辑独立开来，并将相同的逻辑写到一起。
        - React会按照useEffect声明的顺序依次调用它们。
        - 举例如下。的确十分优雅。
        ```
        function FriendStatusWithCounter(props) {
            const [count, setCount] = useState(0);
            useEffect(() => {
                document.title = `You clicked ${count} times`;
            });

            const [isOnline, setIsOnline] = useState(null);
            useEffect(() => {
                function handleStatusChange(status) {
                setIsOnline(status.isOnline);
                }

                ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
                return () => {
                ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
                };
            });
            // ...
        }
        ```
    - 性能优化：给useEffect方法增加一个参数。如果检测到这个参数没有变化——意味着特定值（外部依赖）在两次重渲染之间没有发生变化，那么就可以跳过这一次的useEffect。
    ```
    useEffect(() => {
        document.title = `You clicked ${count} times`;
    }, [count]); // 仅在 count 更改时更新
    ```
        - 如果想让effect只运行一次（加载和卸载时运行），可以传递一个空数组[]作为参数。这意味着这个方法不依赖任何state或props，所以它永远不需要重复执行（永远不会检测到更新）。

## 练习过程

- Only one default export allowed per module.
