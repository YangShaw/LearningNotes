

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

## 使用Thymeleaf模板引擎


## Spring MVC框架
- 通过创建特定的@Controller（或@RestController）的JavaBean来对应处理不同的http请求。


## 引入
spring boot是spring框架的扩展，消除了设置spring应用程序所需的xml配置

创建独立的spring应用；嵌入了tomcat，jetty，undertow并且不需要部署；


## 配置文件
- application.properties或application.yml。后者树状结构，更好用

- application.yml:
key和value之间的冒号后面要加一个空格。

## Annotation
1. Autoweird 自动注入

2. RequestMapping 映射url

3. Component 表明是一个Java Bean

4. ConfigurationProperties(prefix = "student")  表示获取前缀为 student 的配置信息

5. @SpringBootApplication 程序入口

## 问题
1. spring boot Configuration Annotation Proessor not found in classpath
在使用注解@ConfigurationProperties时出现，解决方法是通过maven引入依赖：
```
<dependency>
   <groupId> org.springframework.boot </groupId>
   <artifactId> spring-boot-configuration-processor </artifactId>
   <optional> true </optional>
</dependency>

```
- [参考资料](https://blog.csdn.net/w05980598/article/details/79167826)

2. 热部署
需要添加如下依赖，并且还要在IDEA上做相关的[配置](https://blog.csdn.net/feinifi/article/details/82771650)。这个还没尝试过。暂时用不到。
```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <optional>true</optional> <!-- 这个需要为 true 热部署才有效 -->
</dependency>
```
    
