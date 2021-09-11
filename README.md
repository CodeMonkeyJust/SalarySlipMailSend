# SalarySlipMailSend
Read salary from excel and send salary slip by Email! 

# Linux下需要安装TK

```
sudo apt install python3-tk (Ubuntu)
yum install python3-tk (Centos)
```



# Linux下PIP3安装

```
sudo apt install python3-pip (Ubuntu)


```



# 组件安装

```
pip install py-emails
pip install xlrd==1.2.0
pip install pyinstaller
```



# 打包
## windows打包
```
pyinstaller -F -w -i app.ico main.py
```



## Linux打包

## MacOS打包
```
pyinstaller -F -w -i app.icns main.py
```



### icns图标生成方式
https://cloudconvert.com/png-to-icns


### MacOS下如果不能运行，考虑权限问题

**修改权限的命令格式**

$ [sudo] chmod [<权限范围><权限操作><具体权限>] [文件或目录]

1、权限范围

    u: user，表示文件或目录的拥有者
    g: group，表示文件或目录所属的组
    o: other，除了文件或目录拥有者或者所属组之外的，其他用户都属于这个范围
    a: all，即全部用户，包含文件或目录的拥有者、所属群组和其他用户

2、权限操作

    +表示增加权限
    -表示取消权限
    =表示唯一设定权限

3、具体权限

    r表示可读取
    w表示可写入
    x表示可执行

