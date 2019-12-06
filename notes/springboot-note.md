

## 微服务
微服务是一种架构方式，把每一个功能元素放在一个独立的服务中。每一个服务都是一个可以独立替换、独立升级的软件单元。

一个应用是一组小型服务的集合。通过HTTP的方式进行互通。

文档：martin frower

1. Spring Boot : Build anything
2. Spring Cloud: Coordinate anything
3. Spring Cloud Data Flow: Connect anything

## 打包
maven-lifecycle-package 打包成jar包。

## 初始的依赖库
父项目parent： spring-boot的版本管理
spring-boot-starter： spring-boot场景启动器
    - springboot将所有的功能场景都抽取出来，做成一个个starters，只需要在项目里面引入相关的模块就能导入相应的功能。
    
