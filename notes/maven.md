
# maven

## maven仓库
就本地仓库和远程仓库来说，当maven根据配置文件中的坐标寻找依赖库（构件）的时候，会**先查找本地仓库local repo**，如果本地仓库中存在此构件（之前已经下载过这个库了），那么直接拿过来用；如果不存在，就要去远程仓库寻找并下载到本地。如果本地和远程都不存在，就会报错。

远程仓库分为多种。中央仓库是maven核心**自带的远程仓库**，相当于官方的，也是默认的远程仓库；我们常说的配置阿里云镜像，就是国内对中央仓库的一个镜像访问。

在idea中，还有一个maven home directory的选项，这个是指本地安装maven的目录。由于idea自带maven，所以默认的是bundled，也就是它本身集成的（这个是我猜测的）。


- 本地仓库
/user/.m2/repository是默认的本地仓库目录。如果想自定义本地仓库的地址，可以修改setting.xml文件，设置其中的localrepo项。

默认情况下，该文件不存在，需要在maven的安装目录下（D://maven）的conf/settings.xml文件中进行编辑。

- 镜像
其中mirrorOf的值为central，表示该配置是中央仓库的镜像。
```
<mirror> 
      <id>alimaven</id>
      <name>aliyun maven</name> 
      <url>http://maven.aliyun.com/nexus/content/groups/public/</url> 
      <mirrorOf>central</mirrorOf>
</mirror> 

```


- 远程仓库认证
当需要认证的时候，加入如下内容。id与pom.xml中需要认证下载的repo的id一致。
```
<server>
    <id>deploymentRepo</id>
    <username>repouser</username>
    <password>repopwd</password>
</server>
```

## maven坐标GAV
通过这三个属性可以唯一确定一个jar包
- groupId 表示一个团体，如公司，组织
- artifactId 表示这个团体中的某个项目
- version 表示该项目的版本号

## gradle
gradle是另一种包管理方式（比如安卓项目），但不限于安卓项目。它的配置文件是build.gradle。
