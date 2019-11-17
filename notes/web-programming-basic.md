
**关于web编程的一些基础知识**


# ES标准

ECMAScript是JS的正式名称，是规定的浏览器脚本语言的标准。

# ES6
- let和const
- 解构赋值
例如例子中的Article那一类的赋值。
```
// 对象
const student = {
    name: 'Sam',
    age: 22,
    sex: '男'
}
// 数组
// const student = ['Sam', 22, '男'];

// ES6
const { name, age, sex } = student;
console.log(name + ' --- ' + age + ' --- ' + sex);
```

- Map和Set
- 模板字符串
用反引号引用包裹起来（取代普通字符串的''）,可以定义多行字符串，可以在字符串中加入表达式和变量，可以调用函数。

模板字符串中的空格和换行都会被保留下来。
```
let name = "Mike";
let age = 27;
let info = `My Name is ${name},I am ${age+1} years old next year.`

console.log(info);
// My Name is Mike,I am 28 years old next year.
```

- 箭头函数
- 参数默认值
```
function printText(text='default'){}
```
- 模块化
导入导出的规则那一部分。

# ES7
- includes()
判断数组中是否含有相应的值
- 指数运算符**

# ES8
- await, async
- Object.values(), Object.entries().