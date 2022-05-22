- [安装|卸载](#安装卸载)
- [起停控制](#起停控制)
- [配置系统服务、环境变量](#配置系统服务环境变量)
- [核心配置](#核心配置)
  - [user案列](#user案列)
  - [default_type](#default_type)
  - [server_name](#server_name)
- [资源压缩](#资源压缩)
  - [配置](#配置)
- [add_header](#add_header)
  - [浏览器缓存](#浏览器缓存)
  - [跨域资源共享](#跨域资源共享)
  - [防盗链](#防盗链)
- [Rewrite配置指令](#rewrite配置指令)
  - [全局变量](#全局变量)
  - [set指令](#set指令)
  - [if指令](#if指令)
  - [break](#break)
  - [return](#return)
  - [rewrite | rewrite_log](#rewrite--rewrite_log)
  - [案列](#案列)
- [代理](#代理)
- [注意事项](#注意事项)

# 安装|卸载
```markdown
安装依赖
	gcc openssl openssl-devel pcre pcre-devel zlib zlib-devel

安装方式一：
安装Nginx
	wget http://nginx.org/download/nginx-1.16.1.tar.gz
nginx
	core
		# 解压缩
	module

$ cd ~
$ mkdir nginx && cd nginx
$ mkdir core && mkdir module && cd core
  解压缩
  找到configure文件
$ make
$ make install
  $ ./configure --help

$ systemctl stop firewalld
$ cd /usr/local/nginx
	./conf/nginx.conf
	./logs/nginx.pid
$ ./sbin/nginx
$ ./sbin/nginx -V


# 卸载
	/usr/local/nginx/sbin/nginx -s stop
	rm -rf /usr/local/nginx
	cd ~/nginx/core/nginx-1.16.1/ && make clean
```



# 起停控制
```markdown
	kill -TERM `cat /usr/local/nginx/logs/ngixn.pid`
		   # 这里也可以直接填 nginx master进程PID
		-INT

	     	-QUIT
		-WINCH

		-HUP
			重读配置文件并使用服务对新配置生效
		-USR1
			日志文件
		-USR2
			平缓升级，两个master



	nginx -h
		-V	列出所有配置参数
		-t	测试配置文件
		-tq  	静默成功
    -tq -c 新的配置文件nginx.conf
	nginx -s stop 立即关闭
		 quit 优雅关闭
		 reopen	类似usr1
		 reload 类似hub
```

# 配置系统服务、环境变量
```markdown
#!/usr/bin/env bash
:<<!
	将nginx配置到系统服务
!
rm -rf /root/script/setNgin

echo \
"
[Unit]
Description=nginx web service
Documentation=http://nginx.org/en/docs/
After=network.target

[Service]
Type=forking
PIDFile=/usr/local/nginx/logs/nginx.pid
ExecStartPre=/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf
ExecStart=/usr/local/nginx/sbin/nginx
ExecReload=/usr/local/nginx/sbin/nginx -s reload
ExecStop=/usr/local/nginx/sbin/nginx -s stop
PrivateTmp=true

[Install]
wantedBy=default.target
" > /usr/lib/systemd/system/nginx.service

sleep 1

if [ test -f /usr/lib/systemd/system/nginx.service ];then
	echo "nginx.service文件配置成功"
	chmod 755 /usr/lib/systemd/system/nginx.service
	systemctl daemon-reload
	echo "可执行权限添加成功"
else
	echo "error:Nginx配置到系统服务失败"
fi

\cp /etc/profile /etc/profile.copy && echo "export PATH=\$PATH:/usr/local/nginx/sbin" >> /etc/profile && source /etc/profile

```




# 核心配置
```markdown
# 格式：指令名 指令值;

# 全局块，主要设置Nginx服务器的整体运行配置指令
user nobody;
  用来规定worker进程只能访问哪个用户的目录
master_process on;
worker_processes 2;
daemon on;
pid logs/nginx.pid;

error_log logs/error.log error;
  日志级别
# include [file]
  用来引入其他配置


events {
  # events块，主要设置Nginx服务器与用户网络的链接，这一部分对Nginx服务的性能影响较大
  accept_mutex on;
    惊群问题;接受请求时静默，防止过度争抢影响性能
  multi_accept off;
    一个工作进程只能同时接受一个新的连接
  worker_connections 512;
    单个worker进程最大的连接数
  use 根据操作系统决定;
    设置Nginx服务器应该采用那种事件驱动来处理网络消息
}

http {
  # http块，Nginx服务器中重要部分，负责：代理、缓存、日志记录、第三方模块配皮
  include mime.types;
  default_type application/octet-stream;

  log_format [log_format_name] string;
  access_log logs/access.log [log_format_name];
  error_log logs/error.log error;

  sendfile on;
    是否采用sendfile传输文件，提高处理静态资源的能力
  tcp_nopush on;
  tcp_nodelay on;

  keepalive_timeout 30s;
  keepalive_request 100;
    单个tcp连接最多接受多少次请求

  server {
    # server块，负责Nginx配置中与虚拟主机相关的内容
    listen
    server_name www.baidu.com
      一台主机上可以有多个域名；每次http请求host字段都会标记处此次请求的域名；
      而 server_name 就是 与报文中host字段对应；
      有三种设置模式：精确 | 通配符匹配 | 正则匹配

      匹配顺序：精确、开始通配符匹配、结束通配符匹配、正则匹配、default_server匹配
    # server_name *.baidu.com
    # server_name ~^www\.(.+)\.com$
      正则匹配必须 ~ 开头
      可以通过 $1 取得匹配的值


    location [uri] {
      # 基于Nginx服务器接受的请求字符串，对特定的请求进行处理
      # uri变量是带匹配的请求字符串,有以下几种匹配模式；默认是先使用不包含正则匹配，找到一个匹配度最高的，再通过正则匹配、若匹配得到直接访问(正则优先),若匹配不到正则才使用最初匹配度最高的那个location
        字符串直接开头
        = 
        ^~
          等价于等号，区别在于匹配成功之后直接返回，不会在乎是否有正则满足
        ~
        ~*

      root
        root路径 + location路径匹配到的路径
      alias
        alias路径替换location路径 + （location匹配到的路径 - location路径）
      如果location路径是以"/"结尾，则alias也必须以"/"结尾，root没有要求

      index
        网站默认首页，可以跟多个值
      error-page
        设置网站错误页面；出现对应响应code后，如何处理
        跳转具体的地主
          error_page 404 http://www.baidu.com;
        指定重定向地址
          error_page 404 /50x.html;
          location =/50x.html {}
        使用location@完成错误消息提示
          error_page 404 @jump_to_error;
          location @jump_to_error {
            default_type text/html;
            return 404 "Not Found Page";
          }
    }
  }

}

```



## user案列
```markdown
user www

http {
  server {
    location / {
      root /home/www/html
      index index.html
    }
  }
}
```

## default_type
```markdown
# 非常简单的响应请求可以直接设置

  location /get-html {
      default_type text/html;
      return 200 "<h1>Hello,World</h1>";
  }
  location /get-json {
      default_type application/json;
      return 200 '{"foo":{"bar":true}}';
  }
```

## server_name
```markdown
 server {
   listen 80 default_server;
   # default_server在这里的作用是只要端口匹配成功
   location / {
     default_type text/html;
     return 200 "<h1>Bai Du!</h1>"
   }
 }

```


# 资源压缩
```markdown
// nginx_gzip.conf
# 通过include引入配置文件

gzip on;
gzip_types *;
gzip_comp_level 6;
gzip_min_length 1024;
gzip_vary on;
gzip_disabled "MSIE [1-6]\.";

gzip_static on;
  解决Gzip与sendfile共存问题；需要安装模块 ngx_http_gzip_static_module

# gzip_buffers 4 16k;
# gzip_http_version 1.1;
# gzip_proxied off;
```

## 配置
```markdown
# gzip_static 检查与访问资源同名的.gz文件，存在返回对应的gizp文件；
# 前提该文件.gz资源存在
  jquery.js
  jquery.js.gz # 存在


1.查询当前Nginx配置参数
2.将Nginx安装目录下的sbin目录中nginx二进制文件复制、更名，准备后路
  cd /usr/local/nginx/sbin
  mv nginx nginx.old
3.进入Nginx安装目录
  cd /root/nginx/core/nginx-1.16.1
4.清空之前的编译内容
  make clean
5.用configure来配置参数
  ./configure --with-http_gzip_static_module
6.重新编译生成新的二进制文件
  make
7.移动新生的nginx
  cp ./objs/nginx /usr/local/nginx/sbin
8.执行更新命令
  make upgrade



```


# add_header
## 浏览器缓存
```markdown
location ~.*\.(html|js|css|png)$ {
  expires max;
  add_header Cache-Control no-store;
}


```

## 跨域资源共享
```markdown
  add_header Access-Control-Allow-Origin *;
  add_header Access-Control-Allow-Methods GET,POST,PUT;
  # access-control-allow-credential
  # access-control-expose-headers
  # access-control-max-age

  客户端|浏览器
    # access-control-request-methods
    # access-control-request-headers

```

## 防盗链
```markdown
# none 允许直接可以在浏览器输入图片地址进行访问
    blocked
      域名
      ip
      正则
    none
# blocked 用来表示refer值不为空时，需要进行其他匹配规则的校验

location ~*\.(png|jpe?g|gif)$ {
  valid_referers none blocked www.baidu.com
  192.168.230.1 *.example.com example.* ~\.google\.;

  if ( $invalid_referer ){
    # 验证的referer不通过，$invalid_referer的值为1
    return 403;
  }
  root /usr/local/nginx/html;
}

```





# Rewrite配置指令
## 全局变量
```markdown
$http_user_agent
$host
  对应设置的server_name

$request_uri
  请求路径+查询字符串
  请求路径
    $uri
    $document_uri
  查询字符串
    $args
    $query_string
$request_method
$request_filename

$content_type
$content_length

$http_cookie


$server_name
$server_addr
$server_port
$server_protocol

$remote_addr
$remote_port
$scheme
```


## set指令
```markdown
位置：
  server | location | if、
语法：
  set $variable value;
变量命名：
  $符号作为标识符的第一个字符
  不能与全局变量相同
```


## if指令
```markdown
if( $param ){

}

=
!=

~
  匹配正则，区分大小写
~*
!~
  对 ~ 匹配结果取反
~!*


-e
-f
  !-f
-d
-x

if(!-f $request_filename){
  # 判断请求的文件不存在
}
```


## break
```markdown
中断当前相同作用域中其他Nginx的配置
  位于它前面的指令配置生效，位于她后面的配置无效


```

## return
```markdown
用于完成请求，其后的配置都无效
语法：
  return code [text]
  return code URL;
  return URL; # 302临时重定向

```

## rewrite | rewrite_log
```markdown
可使用范围
  server | location | if


rewrite_log on;
  开启重写日志输出功能


# 一个location块中可以同时存在多个rewrite指令，按照顺序依次对URL进行处理

语法：
  rewrite regex replacement [flag]
    replacement若是以http或https开头，则不会继续向下对URL进行其他处理，而是直接返回重写后的URL给客户端

    flag参数
      last | 默认值
        终止继续在本location快中处理；将重写后的URI转入到其他location块
      break
        重写后的URI在本块中继续处理，不会转向到其他location块
        # 注意rewrite指令在本快中只会执行一次
      redirect
        主要用在replacement不是以http或https开头的情况，因为这些开头的replacement会自动后返回给浏览器，做重定向；
        
        将重写后的URI返回给客户端，302、临时重定向；
        浏览器的地址栏会被改写；而不使用redirect只使用last的，不会改变地址栏，虽然内容都是一样的，
      permanent
        永久重定向 301
```

## 案列
```markdown
### 域名跳转 | 域名镜像
server {
  listen 80;
  server_name www.itcast.cn;
  location / {
    default_type text/html;
    charset utf-8;
    return 200 "<h1>welcome to itcast!!</h1>"
  }
}

server {
  listen 80;
  server_name www.itheima.cn www.itheima.com;
  rewrite ^(.*)$ http://www.itcast.cn$1;
}


### 独立域名
  # search | item | cart
  server_name ~(.*?)\.itcast\.com;

server {
  listen 80;
  server_name search.itcast.com;
  rewrite ^(.*) http://www.itcast.cn/search$1;
}
server {
  listen 80;
  server_name item.itcast.com;
  rewrite ^(.*) http://www.itcast.cn/item$1;
}
server {
  listen 80;
  server_name cart.itcast.com;
  rewrite ^(.*) http://www.itcast.cn/cart$1;
}



### 合并目录
// 路径映射；层级过深不利用SEO优化
server {
  listen 80;
  server_name localhost;
  location /server {
    root html;
    index index.html;
    rewrite ^/server-([0-9]+)-([0-9]+)-([0-9]+)\.html$ /server/$1/$2/$3.html last;
  }
}


### 防盗链优化
location /images {
  root html;
  valid_referers none blocked www.baidu.com;
  if ( $invalid_referer ){
    rewrite ^/ /images/forbidden.png break;
  }
}



### 尾斜线
如果不加斜杠，Nginx内部会自动做一个301重定向
重定向具体的地址由 server_name_in_redirect 决定
server {
  listen 80;
  server_name localhost; # 注意这里localhost
  location /home {

  }
}
# 在0.8.48版本后，Nginx服务器自动设置为off;
# 不需要做任何操作

// 假如该服务器绑定的域名时 biubiu.fans
// 访问路径：/
server_name_in_redirect on;
  # 由设置的server_name拼接成 重定向地址；
  # 错误
  localhost/home/

server_name_in_redirect off;
  # 正确
  biubiu.fans/home/
```



# 代理
```markdown
proxy_pass
	被代理服务器的 地址 | 域名 | 域名:端口
	尾斜线
    当客户端访问代理服务器的路径是：/server/index.html
    location /server {
      #proxy_pass http://192.168.200.146:8080
        http://192.168.200.146:8080/server/index.html
      proxy_pass http://192.168.200.146:8080/
        http://192.168.200.146:8080/index.html
    }


proxy_set_header
	代理服务器 向 被代理服务器 发送网络请求时：添加头信息
	例如：代理服务器
		proxy_set_header username $user
	在 被代理服务器 中可以通过：$http_username 取出 $user的值

proxy_redirect
	由于 被代理的服务器 有可能返回 Location字段；
	如果 代理服务器 不对Location字段处理，直接返回的法，客户端也能察觉出 中间的代理服务器，并没有完全隐藏 被代理服务器；
	设置这个 可以将 Location字段 替换成其他字符串

语法
	proxy_redirect:redirect replacement


```


# 注意事项
```markdown
netstat -lnt | grep 80
Nginx服务器中的worker进程的数量，决定了Nginx服务可以监听的端口数量；
一旦nginx.conf中设置的端口数量超过了work进程数量，就会导致部分端口根本就不会被有效监听，导致针对这些端口路径请求根本不会被响应


listen:127.0.0.1:9999 # 无法在外界访问
与
listen:0.0.0.0:9999
之间存在行为差异

每次更改nginx.conf文件，最好通过指令（nginx -s stop 
）先停止服务器，再 nginx 重新运行Nginx服务
```

