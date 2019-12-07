
# MySql的使用

## 参考资料
- [安装详细流程](https://blog.csdn.net/weixin_37852133/article/details/81101623)

## 安装
1. 安装过程参照上方资料。

## 使用
1. 登录指令：
登录root账户，随后输入密码。密码在安装的流程中设置。成功登录后，终端会变为 **mysql>**。
```
mysql -u root -p
```
2. 执行SQL指令：
直接输入sql语句。注意每行sql指令必须要加分号;结尾才会生效。

3. 退出：
ctrl+c退出当前语句；

ctrl+z退出mysql；

4. 启动mysql服务
在终端输入如下指令来查看是否已开启mysql。如果没有，就加上mysql的服务的名称来开启。
```
net start

net start mysql80
```
如果看到了你的mysql服务名称（注意，这里的名称不一定是mysql，而是你在安装过程中设定的那个名称，默认是mysql80）


## 使用navicat
1. 下载navicat for mysql或 navicat premium
2. 新建（mysql）连接，连接名只是一个标识（不需要和本地的mysql的服务名称相同），主机名在访问本地时填写localhost，端口默认为3306，用户名和密码填写root和对应密码。
3. 开启连接，如果顺利的话，会看到一些数据库已经存在在这个连接中（mysql的一些配置）。在这个连接下新建一个数据库，开始使用。
4. 如果不能开启连接，可能时本地mysql服务未开启（解决方案如上），也可能时加密方式不匹配（解决方案如下）。


## 问题解决
1. 无法连接到navicat
这是因为在安装的时候选择了新版的加密方式，而navicat客户端不支持。需要在终端中登入mysql的root用户后，输入sql语句修改成旧的加密方式。
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'newpassword';
```


