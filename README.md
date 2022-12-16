# 工资单邮件发送
## 说明

从EXCEL（多行，每行中含工资信息和邮件地址）中读取工资单，并分别发生给相应人员。

## 支持系统

Windows，Linux、Mac OS

## 开发环境搭建

### Linux

#### Ubuntu

```shell
# 安装TK
sudo apt install python3-tk
# 安装PIP3
sudo apt install python3-pip
```

#### CentOS

```shell
# 安装TK
yum install python3-tk
```

### Windows

```
# 常规开发环境
```



### MacOS

```
# 常规开发环境
```

### 组件安装

#### 普通安装

```shell
pip install py-emails
pip install xlrd==1.2.0
pip install pyinstaller
```

#### 国内安装

```shell
pip install py-emails -i https://mirrors.aliyun.com/pypi/simple/
pip install xlrd==1.2.0 -i https://mirrors.aliyun.com/pypi/simple/
pip install pyinstaller -i https://mirrors.aliyun.com/pypi/simple/
```





## 打包
### Windows打包
```
pyinstaller -F -w -i app.ico main.py
```



### Linux打包

### MacOS打包
```
pyinstaller -F -w -i app.icns main.py
```



#### icns图标生成方式
https://cloudconvert.com/png-to-icns


#### MacOS下如果不能运行，考虑权限问题

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

## 运行

### 配置文件

需要修改用户目录  **\SalarySlipMailSend\conf\mail.ini**  中相关信息。

```
[send]
#邮件服务器地址
mail_host = 
#发件人邮箱
mail_user =
#发件人密码
mail_pass =
#发件人姓名
mail_sender =
#签名1
sign1 =
#签名2
sign2 = 
```

### 发送日志

查看用户目录 **\SalarySlipMailSend\log** 中的日志文件。

