
# yidongyi-server架构


## 参考资料
- [segmentfault](https://segmentfault.com/)
- [hibernate入门这一篇就够了](https://segmentfault.com/a/1190000013568216)

## 先导知识

### 如何学习一个框架
1. 引入jar包
2. 配置xml文件
3. 熟悉API

### ORM 对象关系映射 object relational mapping
ORM关注的是对象与数据库中的列（column，属性）的关系。
- 对象O：提供POJO类和相应属性（列）
- 关系型数据库R：每个类给每个属性设一个列
- DAO层：提供save和get方法，实现数据直接保存到数据库，以及直接从数据库中拿到一个对象
- 映射M：
    - java中的对象 —— 数据库中的表
    - 对象中的属性 —— 表中的列
    - 类型的对应

### hibernate
用于ORM的解决方案，为OOP中domain model到关系型数据库的映射提供一个框架，从而实现直接存取Java对象。可以负责从java class到db table的映射，以及java 数据类型到sql数据类型的映射，以及oop的数据查询机制。

- 对应于MVC中的数据持久层/ source code中的DAO层
    - 在DAO层操作xml，将数据封装到xml文件中，通过读写xml来实现crud
    - 在DAO层使用原生的JDBC连接数据库
    - 使用DbUtils组件对JDBC中的操作进行一定程度的封装

hibernate抽象出了这些代码中的规律，通过找出JavaBean对象和数据表中的列存在的映射关系，使程序能够自动生成SQL语句。这帮我们省去了很多写SQL的时间。

需要的jar包：见参考资料







## java结构

- domain M层，各种模型
    - news 包括id，title，img，content，datetime，user
    news的构造方法为空，但是通过一个成员方法createNews来初始化这些值。**这是为什么呢**？

    - users
    - authority

    - NewsCreateForm和UserCreateForm是用来给创建news和user对象提供初始数据的类，只是一个提供信息的盒子，具体创建符合规范的对象需要靠news和user接受到来自这两个盒子的信息后去创建。就是两个工具人。

- controller C层，处理逻辑
    - 

- service
编写了两个接口，定义了需要进行和news以及user相关的哪些操作。

对两个接口分别编写实现类，用来实现这个方法。
    - NewsServiceImpl
        - create方法:创建一条新闻，接收一个工具人NewsCreateForm类的对象来获得新闻的信息；
        
        利用createNews方法来给news对象赋值，利用NewsRepository类中的save方法来存入数据库中。

        这个save方法继承自spring framework中的CrudRepository类，不需要用户自定义，直接就能利用封装好的save来实现对象存入数据库。



- message 处理错误信息
包括错误码，信息名，内容。

- repository 三个关于M层模型的接口，分别对应news，users，authority
继承自springframework的Crud Repository和PagingAndSorting Repository，看名字，像一个是只执行普通crud操作的类型，另一个是要实现分页和排序逻辑的类型（新闻列表需要排序和分页）

这些接口都提供了类似于findById的方法，总之就是各种find。

接口中定义的方法是在哪里实现的？

springframework.data库中提供了一些模型，如和分页相关的Page，Pageable；和repo相关的各种（上面提到的两个）等。

- security 关于安全的一些设置
- validator 关于验证的一些配置


## 前端架构
