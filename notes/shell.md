
# shell脚本语言学习

## 参考资料
- [shell编程](https://github.com/Snailclimb/JavaGuide/blob/master/docs/operating-system/Shell.md)

## intro
shell编程是对一堆Linux命令的逻辑化处理。

## hello world
- 创建脚本文件 touch hello.sh
- 赋给执行权限(x) chmod +x hello.sh
- 修改内容 vim hello.sh
    - 进入插入模式(insert) i
    - 写入 echo "hello world"
    - 进入命令模式 esc
    - 保存并退出  shift+:   wq
- 运行 ./hello.sh
    - 如果不加./ Linux会去全局的PATH路径中查找hello.sh，如同我们执行ls, pwd等命令一样。这些二进制可执行文件通常写在/bin，/sbin，/usr/bin，/usr/sbin等目录下。


- shell中的变量
    - 局部变量，用户自定义，仅在当前shell实例中有效；
    - Linux已定义的环境变量，如$PATH, $HOME等。env命令查看所有的环境变量。
    - 引用变量要用$。不管是局部变量还是环境变量。
    
## 语法
- shell脚本语言也是一种语言，有它自己的语法。