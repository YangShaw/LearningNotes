
## 配置文件
- application.properties或application.yml。后者树状结构，更好用

- application.yml:
key和value之间的冒号后面要加一个空格。

## Annotation
1. Autoweird 自动注入

2. RequestMapping 映射url

3. Component 表明是一个Java Bean

4. ConfigurationProperties(prefix = "student")  表示获取前缀为 student 的配置信息

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