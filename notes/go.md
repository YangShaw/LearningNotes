# Golang

## 资料
- [Go 中文文档](http://docscn.studygolang.com/)
- [Go 中文社区](https://studygolang.com/)

## 安装
官网下载，windows下有msi和zip两种下载格式。直接下载msi可以自动配置环境变量（需要重启所有开启的shell才能生效），使用zip格式要把go/bin目录配置到环境变量中。

## hello world
创建hello.go文件，写入代码:
```
package main

import "fmt"

func main() {
    fmt.Printf("hello, world\n")
}
```
在命令行中运行 go run hello.go