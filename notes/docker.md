
# Docker
- 使用docker进行一系列的尝试与应用。

## 安装

- 在官网上下载，安装。注意只能安装在Windows专业版上。
- 很多镜像只有Linux可以下载，右键docker desktop可以点击[switch to Linux container] 切换到linux container后，就可以正常下载各种image了。

## 指令

- docker pull [imagename]
- docker images  查看已下载的镜像
- docker ps 查看正在运行的容器
- docker ps -l 查看最近创建的容器

## 我常用的
- 容器启动后，即使关闭终端，容器也仍在运行。

- splash：
    ```
    docker run -p 8050:8050 scrapinghub/splash
    ```

    local nextpage = splash:select("._3YiUU ")[1]
    nextpage:click()
    splash:wait(3)
    