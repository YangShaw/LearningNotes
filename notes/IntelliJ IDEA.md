

## 介绍

- 没有workspace的概念，最大工作单元是Project；
- Indexing... 创建项目索引的过程；
- 下载[主题](http://www.riaway.com/index.php)，将下载的jar包用import settings导入即可。

## 中文乱码
- File | Settings | Editor | File Encodings 
    - 设置global encoding和project encoding为UTF-8；
    - 设置default encoding for properties files为UTF-8；

- File | Settings | Build, Execution, Deployment | Compiler | Java Compiler
    - 在Additional command line parameters中添加语句 
    ```
    -encoding utf-8
    ```
- 安装目录/bin
    - 在idea.exe.vmoptions（64位为idea64.exe.vmoptions）文件的末尾添加语句 
        ```
        Dfile.encoding=UTF-8
        ```