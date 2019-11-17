
# cmder的使用和问题

- 官网下载完整版（full），速度可能较慢。
- 解压后即可使用，无需安装。
- 如果装在c盘，需要使用管理员权限才能打开。
    - 默认使用管理员权限打开： 右键-属性-兼容性-以管理员身份运行。
    - 但这样每次启动时都会弹出确认。
- 加入环境变量：路径写到cmder.exe所在的文件夹即可。
- 加入右键菜单：在终端中输入命令  cmder.exe /REGISTER ALL
- 重新安装需要删除的注册表：计算机\HKEY_CLASSES_ROOT\Directory\shell\Cmder和计算机\HKEY_CLASSES_ROOT\Directory\Background\Cmder

- 常用快捷键：
```
使用Tab: 路径自动补全；
使用Ctrl+T: 建立新页签；
使用Ctrl+W: 关闭页签;
使用Ctrl+Tab:  切换页签;
Alt+F4：关闭所有页签
Alt+Shift+1：开启cmd.exe
Alt+Shift+2：开启powershell.exe(一般用户权限)
Alt+Shift+3：开启powershell.exe (系统管理员权限)
Ctrl+1:  快速切换到第1个页签
Ctrl+n: 快速切换到第n个页签( n值无上限)
Alt + enter: 切换到全屏状态；
Ctr+r : 历史命令搜索
```
    
## 参考资料
- [windows下的cmder利器取代cmd](https://www.jianshu.com/p/624e0fee3311)