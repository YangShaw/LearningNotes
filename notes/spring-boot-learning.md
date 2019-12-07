
**Spring Boot学习笔记**

<!-- TOC -->

- [1. 第一部分](#1-第一部分)
    - [1.1. 登录注册模块](#11-登录注册模块)
        - [1.1.1. 项目结构](#111-项目结构)
        - [1.1.2. 后端代码](#112-后端代码)
            - [1.1.2.1. controller](#1121-controller)
            - [1.1.2.2. repository](#1122-repository)
            - [1.1.2.3. service](#1123-service)

<!-- /TOC -->


# 1. 第一部分

## 1.1. 登录注册模块

- [Demo地址](https://github.com/YangShaw/SpringBootLearning/tree/master/springbootlogin)

### 1.1.1. 项目结构
- 后端代码
    - controller：配置路由关系
    - model：定义实体（如User）
    - repository：接口类，给每个实体声明需要用到的访问数据库的操作
    - service：调用repository中的接口来实现业务逻辑（如注册新用户）
- 前端代码
    - static：存放依赖的js、css库以及图片、字体等
    - templates：存放前端页面
- 配置文件
    - pom.xml：maven的配置文件，通过在该文件中添加依赖库来自动下载和导入需要用到的jar包
    - application.yaml：项目的配置文件，存放一些配置信息。自动生成的为application.properties格式；yaml格式以树状显示，更简洁明了一些。

### 1.1.2. 后端代码

#### 1.1.2.1. controller
给类增加@Controller注解来标记之。

给方法增加@RequestMapping注解来响应一个http请求，请求的内容是该注解的value值。例如下面的例子表示当请求"/myrequest"的时候，我们响应这个请求的函数是myResponse。
```
@RequestMapping("/myrequest")
public String myResponse(){
    return "hello world"
    //  return "index"
}
```

如果没有使用thyme leaf模板，那么这里返回一个字符串hello world就会直接在界面上显示这个内容；如果配置了模板，那么它会去寻找字符串对应的页面，如return "index"会找到classpath路径下的index.html文件。

对每个请求都配置相应的Controller处理器（同一个Controller类中可以处理多个请求），就能满足入门的响应请求的需求了。

如果要响应表单提交，只需要响应表单的action属性中的请求就可以了。

#### 1.1.2.2. repository
使用jpa连接数据库，maven配置为：
```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```

对每个实体都创建对应的操作数据库的repository接口类，继承自JpaRepository。JPA提供一系列封装好的操作数据库的方法，如根据实体的属性名进行find等。这里只声明了一个根据UserName（对应User类中的属性userName）进行查找的方法。
```
public interface UserRepository extends JpaRepository<User, Long> {
    User findByUserName(String userName);
}
```

#### 1.1.2.3. service
调用对应repository中对数据库的操作方法，来实现业务逻辑。例如上面说的根据用户名来获得用户信息的逻辑：
```
@Service
public class UserServiceImpl implements UserService {

    @Autowired
    UserRepository userRepository;

    @Override
    public User getUserByUserName(String userName) {
        return userRepository.findByUserName(userName);
    }
}
```
注意：给service类增加注解@Service；通过自动注入的方式@Autowired来创建UserRepository的对象；这里我是先定义了一个接口UserService来声明要用到的方法，然后在UserServiceImpl中实现之，事实上也可以不要这个接口。





