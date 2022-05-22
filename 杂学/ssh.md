
# 简介与命令
```markdown
SSH 软件分成两个部分：向服务器发出请求的部分，称为客户端（client），OpenSSH 的实现为 ssh；接收客户端发出的请求的部分，称为服务器（server），OpenSSH 的实现为 sshd。

链接流程：
  ssh 连接远程服务器后，首先有一个验证过程，验证远程服务器是否为陌生地址。
  如果是第一次连接某一台服务器，命令行会显示一段文字，表示不认识这台机器，提醒用户确认是否需要连接。

  输入yes，就可以将当前服务器的指纹也储存在本机~/.ssh/known_hosts文件中，并显示下面的提示。以后再连接的时候，就不会再出现警告了。




ssh username@hostname command
ssh user@hostname
  -p 指定端口
  -t参数在 ssh 直接运行远端命令时，提供一个互动式 Shell。
```

# 配置文件
```markdown
配置文件
  SSH 客户端的全局配置文件是/etc/ssh/ssh_config，用户个人的配置文件在~/.ssh/config，优先级高于全局配置文件。


$ ssh remoteserver
# 等同于
$ ssh -p 2112 neo@remote.example.com
```


```markdown
Host *
     Port 2222

Host remoteserver
     HostName remote.example.com
     User neo
     Port 2112
```


# 密钥登入
```markdown
SSH 密钥登录分为以下的步骤。

预备步骤，客户端通过ssh-keygen生成自己的公钥和私钥。

第一步，手动将客户端的公钥放入远程服务器的指定位置。

第二步，客户端向服务器发起 SSH 登录的请求。

第三步，服务器收到用户 SSH 登录的请求，发送一些随机数据给用户，要求用户证明自己的身份。

第四步，客户端收到服务器发来的数据，使用私钥对数据进行签名，然后再发还给服务器。

第五步，服务器收到客户端发来的加密签名后，使用对应的公钥解密，然后跟原始数据比较。如果一致，就允许用户登录。

```

```markdown
ssh-keygen -t dsa
  -t参数用于指定生成密钥的加密算法，一般为dsa或rsa
  -b参数指定密钥的二进制位数;一般来说，-b至少应该是1024
  -f参数指定生成的私钥文件。

  -F参数检查某个主机名是否在known_hosts文件里面。
  -R参数将指定的主机公钥指纹移出known_hosts文件。
```

## 手动上传公钥
```markdown
OpenSSH 规定，用户公钥保存在服务器的~/.ssh/authorized_keys文件。

你要以哪个用户的身份登录到服务器，密钥就必须保存在该用户主目录的~/.ssh/authorized_keys文件。


 cat ~/.ssh/id_rsa.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"


 authorized_keys文件的权限要设为644，即只有文件所有者才能写。如果权限设置不对，SSH 服务器可能会拒绝读取该文件。

 chmod 644 ~/.ssh/authorized_keys

 只要公钥上传到服务器，下次登录时，OpenSSH 就会自动采用密钥登录，不再提示输入密码。
```


## 自动上传公钥
```markdown
如果~/.ssh/authorized_keys文件不存在，ssh-copy-id命令会自动创建该文件

$ ssh-copy-id -i id_rsa user@host
注意，公钥文件可以不指定路径和.pub后缀名，ssh-copy-id会自动在~/.ssh目录里面寻找。上面命令中，公钥文件会自动匹配到~/.ssh/id_rsa.pub。

注意：
  如果authorized_keys文件的末尾不是一个换行符，会导致新的公钥添加到前一个公钥的末尾，两个公钥连在一起，使得它们都无法生效
```

## 关闭密码登入
```markdown
对于 OpenSSH，具体方法就是打开服务器 sshd 的配置文件/etc/ssh/sshd_config，将PasswordAuthentication这一项设为no。

PasswordAuthentication no
修改配置文件以后，不要忘了重新启动 sshd，否则不会生效。
```


## 私有密码
```markdown
私钥设置了密码以后，每次使用都必须输入私钥的密码

ssh-agent | ssh-add
```



# 服务器
```markdown
一般来说，sshd 安装后会跟着系统一起启动。如果当前 sshd 没有启动，可以用下面的命令启动。

$ sshd


如果提示“sshd re-exec requires execution with an absolute path”，就需要使用绝对路径来启动。这是为了防止有人出于各种目的，放置同名软件在$PATH变量指向的目录中，代替真正的 sshd。

# Centos、Ubuntu、OS X
$ /usr/sbin/sshd



# 启动
$ sudo systemctl start sshd.service
# 停止
$ sudo systemctl stop sshd.service
# 重启
$ sudo systemctl restart sshd.service
# 让 sshd 在计算机下次启动时自动运行。
$ sudo systemctl enable sshd.service
```


## 配置文件
```markdown
shd 的配置文件在/etc/ssh目录，主配置文件是sshd_config

注意，如果重装 sshd，上面这些密钥都会重新生成，导致客户端重新连接 ssh 服务器时，会跳出警告，拒绝连接。为了避免这种情况，可以在重装 sshd 时，先备份/etc/ssh目录，重装后再恢复这个目录。


修改配置文件以后，可以用 sshd 命令的-t（test）检查有没有语法错误。
$ sshd -t


配置文件修改以后，并不会自动生效，必须重新启动 sshd。
$ sudo systemctl restart sshd.service




```



# 端口转发
```markdown
作为加密通信的中介，充当两台服务器之间的通信加密跳板，使得原本不加密的通信变成加密通信。这个功能称为端口转发（port forwarding），又称 SSH 隧道（tunnel）。

端口转发有两个主要作用：
（1）将不加密的数据放在 SSH 安全连接里面传输，使得原本不安全的网络服务增加了安全性，比如通过端口转发访问 Telnet、FTP 等明文服务，数据传输就都会加密。

（2）作为数据通信的加密跳板，绕过网络防火墙。
```

## 动态转发
```markdown
动态转发指的是，本机与 SSH 服务器之间创建了一个加密连接，然后本机内部针对某个端口的通信，都通过这个加密连接转发。

它的一个使用场景就是，访问所有外部网站，都通过 SSH 转发。


$ ssh -D local-port tunnel-host -N
上面命令中，-D表示动态转发，local-port是本地端口，tunnel-host是 SSH 服务器，-N表示这个 SSH 连接只进行端口转发，不登录远程 Shell，不能执行远程命令，只能充当隧道。

注意，这种转发采用了 SOCKS5 协议。访问外部网站时，需要把 HTTP 请求转成 SOCKS5 协议，才能把本地端口的请求转发出去。


$ ssh -D 2121 Vroot -N
$ curl -x socks5://localhost:2121 https://www.baidu.com


如果经常使用动态转发，可以将设置写入 SSH 客户端的用户个人配置文件（~/.ssh/config）。
  DynamicForward local-port
```


## 本地转发
```markdown
它会指定一个本地端口（local-port），所有发向那个端口的请求，都会转发到 SSH 跳板机（tunnel-host），然后 SSH 跳板机作为中介，将收到的请求发到目标服务器（target-host）的目标端口（target-port）。

$ ssh -L local-port:target-host:target-port tunnel-host -N

注意，本地端口转发采用 HTTP 协议，不用转成 SOCKS5 协议。
$ ssh -L 2121:www.example.com:80 tunnel-host -N
$ curl http://localhost:2121


$ ssh -L 1100:mail.example.com:110 mail.example.com
上面这种情况有一个前提条件，就是mail.example.com必须运行 SSH 服务器。
否则，就必须通过另一台 SSH 服务器中介，执行的命令要改成下面这样。
$ ssh -L 1100:mail.example.com:110 other.example.com


如果经常使用本地转发，可以将设置写入 SSH 客户端的用户个人配置文件（~/.ssh/config）。
# test.example.com是作为跳板机使用的，必须具有ssh服务器
# client-IP 可以省略，毕竟一般都是通过本机发起转发
Host test.example.com
LocalForward client-IP:client-port server-IP:server-port
```


## 远程转发
```markdown
# 搞不懂、难理解
向另一台主机声明，如果有人访问你某个端口，你就到我这个端口来取；
  两台主机必须完整的安装OpenSSH客户端、服务器


$ ssh -R 8080:localhost:80 -N my.public.server
上面命令是在内网localhost服务器上执行，建立从localhost到my.public.server的 SSH 隧道。运行以后，用户访问my.public.server:8080，就会自动映射到localhost:80。


$ ssh -R 8080:localhost:5050 -N Vroot


```


# scp
```markdown
scp主要用于以下三种复制操作。
  本地复制到远程。
  远程复制到本地。
  两个远程系统之间的复制。

# 注意，scp会使用 SSH 客户端的配置文件.ssh/config，如果配置文件里面定义了主机的别名，这里也可以使用别名连接。

# scp支持一次复制多个文件。
$ scp source1 source2 destination

$ scp file.txt remote_username@10.10.0.2:/remote/directory
$ scp ./test.txt Vroot:/opt

# 会在远程主机创建 documents 目录
$ scp -r documents username@server_ip:/path_to_remote_directory
# 将本机目录下的所有内容拷贝到远程目录下，不会创建 documents 目录
$ scp -r localmachine/path_to_the_directory/* username@server_ip:/path_to_remote_directory/


$ scp user@host:directory/SourceFile TargetFile
$ scp Vroot:/opt/test.txt ./foo.txt

$ scp -r username@server_ip:/path_to_remote_directory/* local-machine/path_to_the_directory/
$ scp -r user@host:directory/SourceFolder TargetFolder


# 两个远程系统之间的复制
$ scp user1@host1.com:/files/file.txt user2@host2.com:/files


-p参数用来保留修改时间（modification time）、访问时间（access time）、文件状态（mode）等原始文件的信息

(大写字母)
-P参数用来指定远程主机的 SSH 端口。如果远程主机使用默认端口22，可以不用指定，否则需要用-P参数在命令中指定

-r参数表示是否以递归方式复制目录。
```