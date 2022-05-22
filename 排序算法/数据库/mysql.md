

# 环境搭建

## linux

```markdown
安装前检测是否已经安装：
	rpm -qa | grep mysql
	
卸载已有版本：
	rpm -e mysql
	rpm -e --nodeps mysql
	
安装mysql:
    wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
    rpm -ivh mysql-community-release-el7-5.noarch.rpm
    yum update
    yum install mysql-server
    
权限设置：
    chown -R mysql:mysql /var/lib/mysql
    
初始化 MySQL：
    mysqld --initialize
    
启动 MySQL：
    systemctl start mysqld
    
查看 MySQL 运行状态：
    systemctl status mysqld
    
验证是否已经安装成功：
     mysqladmin --version
     
Mysql安装成功后，默认的root用户密码为空，你可以使用以下命令来创建root用户的密码：
	[root@host]# mysqladmin -u root password "new_password";

```





## window

```markdown
# https://www.runoob.com/w3cnote/windows10-mysql-installer.html

下载完后，我们将 zip 包解压到相应的目录

配置下 MySQL 的配置文件
打开刚刚解压的文件夹 C:\web\mysql-8.0.11 ，在该文件夹下创建 my.ini 配置文件，编辑 my.ini 配置以下基本信息：
    [client]
    # 设置mysql客户端默认字符集
    default-character-set=utf8

    [mysqld]
    # 设置3306端口
    port = 3306
    # 设置mysql的安装目录
    basedir=C:\\web\\mysql-8.0.11
    # 设置 mysql数据库的数据的存放目录，MySQL 8+ 不需要以下配置，系统自己生成即可，否则有可能报错
    # datadir=C:\\web\\sqldata
    # 允许最大连接数
    max_connections=20
    # 服务端使用的字符集默认为8比特编码的latin1字符集
    character-set-server=utf8
    # 创建新表时将使用的默认存储引擎
    default-storage-engine=INNODB
    
以管理员身份打开 cmd 命令行工具，切换目录：
	cd C:\web\mysql-8.0.11\bin
初始化数据库：
	mysqld --initialize --console
	
执行完成后，会输出 root 用户的初始默认密码，如：
    ...
    2018-04-20T02:35:05.464644Z 5 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: APWCY5ws&hjQ
    ...
    
APWCY5ws&hjQ 就是初始密码，后续登录需要用到，你也可以在登陆后修改密码。

输入以下安装命令：
	mysqld install
	
启动输入以下命令即可：
	net start mysql
	
注意: 在 5.7 需要初始化 data 目录：
    cd C:\web\mysql-8.0.11\bin 
    mysqld --initialize-insecure 
    初始化后再运行 net start mysql 即可启动 mysql。
```



## 新增用户



## 登入

```python
mysql -h 主机名 -u 用户名 -p
```





# 基本命令

## 初涉

```sql
# 分号结尾，千万不要忘记
# 对大小写不敏感：SELECT 与 select 是相同的。

SHOW DATABASES;
USE 数据库名;
set names utf8;	# 设置使用的字符集。

SHOW TABLES;
SHOW COLUMNS FROM 数据表;


CREATE DATABASE dbname;

CREATE TABLE table_name
(
column_name1 data_type(size) constraint_name,
column_name2 data_type(size) constraint_name,
column_name3 data_type(size) constraint_name,
....
);

CREATE TABLE IF NOT EXISTS Person # 如果表不存在才创建
(
...
...   
)

CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```







## MySQL 数据类型

在 MySQL 中，有三种主要的类型：Text（文本）、Number（数字）和 Date/Time（日期/时间）类型。

**Text 类型：**

| 数据类型         | 描述                                                         |
| :--------------- | :----------------------------------------------------------- |
| CHAR(size)       | 保存固定长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的长度。最多 255 个字符。 |
| VARCHAR(size)    | 保存可变长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的最大长度。最多 255 个字符。**注释：**如果值的长度大于 255，则被转换为 TEXT 类型。 |
| TINYTEXT         | 存放最大长度为 255 个字符的字符串。                          |
| TEXT             | 存放最大长度为 65,535 个字符的字符串。                       |
| BLOB             | 用于 BLOBs（Binary Large OBjects）。存放最多 65,535 字节的数据。 |
| MEDIUMTEXT       | 存放最大长度为 16,777,215 个字符的字符串。                   |
| MEDIUMBLOB       | 用于 BLOBs（Binary Large OBjects）。存放最多 16,777,215 字节的数据。 |
| LONGTEXT         | 存放最大长度为 4,294,967,295 个字符的字符串。                |
| LONGBLOB         | 用于 BLOBs (Binary Large OBjects)。存放最多 4,294,967,295 字节的数据。 |
| ENUM(x,y,z,etc.) | 允许您输入可能值的列表。可以在 ENUM 列表中列出最大 65535 个值。如果列表中不存在插入的值，则插入空值。**注释：**这些值是按照您输入的顺序排序的。可以按照此格式输入可能的值： ENUM('X','Y','Z') |
| SET              | 与 ENUM 类似，不同的是，SET 最多只能包含 64 个列表项且 SET 可存储一个以上的选择。 |

**Number 类型：**

| 数据类型        | 描述                                                         |
| :-------------- | :----------------------------------------------------------- |
| TINYINT(size)   | 带符号-128到127 ，无符号0到255。                             |
| SMALLINT(size)  | 带符号范围-32768到32767，无符号0到65535, size 默认为 6。     |
| MEDIUMINT(size) | 带符号范围-8388608到8388607，无符号的范围是0到16777215。 size 默认为9 |
| INT(size)       | 带符号范围-2147483648到2147483647，无符号的范围是0到4294967295。 size 默认为 11 |
| BIGINT(size)    | 带符号的范围是-9223372036854775808到9223372036854775807，无符号的范围是0到18446744073709551615。size 默认为 20 |
| FLOAT(size,d)   | 带有浮动小数点的小数字。在 size 参数中规定显示最大位数。在 d 参数中规定小数点右侧的最大位数。 |
| DOUBLE(size,d)  | 带有浮动小数点的大数字。在 size 参数中规显示定最大位数。在 d 参数中规定小数点右侧的最大位数。 |
| DECIMAL(size,d) | 作为字符串存储的 DOUBLE 类型，允许固定的小数点。在 size 参数中规定显示最大位数。在 d 参数中规定小数点右侧的最大位数。 |

> **注意：**以上的 size 代表的并不是存储在数据库中的具体的长度，如 int(4) 并不是只能存储4个长度的数字。
>
> 实际上int(size)所占多少存储空间并无任何关系。int(3)、int(4)、int(8) 在磁盘上都是占用 4 btyes 的存储空间。就是在显示给用户的方式有点不同外，int(M) 跟 int 数据类型是相同的。
>
> 例如：
>
> 1、int的值为10 （指定zerofill）
>
> ```
> int（9）显示结果为000000010
> int（3）显示结果为010
> ```
>
> 就是显示的长度不一样而已 都是占用四个字节的空间

**Date 类型：**

| 数据类型    | 描述                                                         |
| :---------- | :----------------------------------------------------------- |
| DATE()      | 日期。格式：YYYY-MM-DD**注释：**支持的范围是从 '1000-01-01' 到 '9999-12-31' |
| DATETIME()  | *日期和时间的组合。格式：YYYY-MM-DD HH:MM:SS**注释：**支持的范围是从 '1000-01-01 00:00:00' 到 '9999-12-31 23:59:59' |
| TIMESTAMP() | *时间戳。TIMESTAMP 值使用 Unix 纪元('1970-01-01 00:00:00' UTC) 至今的秒数来存储。格式：YYYY-MM-DD HH:MM:SS**注释：**支持的范围是从 '1970-01-01 00:00:01' UTC 到 '2038-01-09 03:14:07' UTC |
| TIME()      | 时间。格式：HH:MM:SS**注释：**支持的范围是从 '-838:59:59' 到 '838:59:59' |
| YEAR()      | 2 位或 4 位格式的年。**注释：**4 位格式所允许的值：1901 到 2155。2 位格式所允许的值：70 到 69，表示从 1970 到 2069。 |

*即便 DATETIME 和 TIMESTAMP 返回相同的格式，它们的工作方式很不同。在 INSERT 或 UPDATE 查询中，TIMESTAMP 自动把自身设置为当前的日期和时间。TIMESTAMP 也接受不同的格式，比如 YYYYMMDDHHMMSS、YYMMDDHHMMSS、YYYYMMDD 或 YYMMDD。









## select

```sql
SELECT column_name,column_name FROM table_name;


# DISTINCT 关键字
SELECT DISTINCT column_name,column_name 
FROM table_name;


SELECT column_name,column_name
FROM table_name
WHERE column_name operator value;


SELECT column_name,column_name
FROM table_name
ORDER BY column_name,column_name ASC|DESC;
	# ORDER BY 多列的时候，先按照第一个column name排序，在按照第二个column name排序；
	'
	order by A,B        这个时候都是默认按升序排列
    order by A desc,B   这个时候 A 降序，B 升序排列
    order by A ,B desc  这个时候 A 升序，B 降序排列
    即 desc 或者 asc 只对它紧跟着的第一个列名有效，其他不受影响，仍然是默认的升序。
    '
# 转换成GBK编码 在进行排序
SELECT * 
FROM runoob_tbl
ORDER BY CONVERT(runoob_title using gbk);
    
    
    
SELECT column_name,column_name
FROM table_name
LIMIT n1,n2
# 等价于
SELECT column_name,column_name
FROM table_name
LIMIT n2 OFFSET n1
	# 从n1+1开始选取，选取数量为n2条
	

SELECT TOP 50 PERCENT * FROM Websites;
	# 选取前50%的数据
	
SELECT TOP 5 * FROM Websites;	
或
SELECT * FROM Websites LIMIT 5;
	# 选取前5条数据
```



### where

```sql
'
MySQL 的 WHERE 子句的字符串比较是不区分大小写的。
你可以使用 BINARY 关键字来设定 WHERE 子句的字符串比较是区分大小写的。

	SELECT * from runoob_tbl WHERE BINARY runoob_author='runoob.com';
'
# 搜索 empno 等于 7900 的数据：
	Select * from emp where empno=7900;
	
# Where +条件（筛选行）
# 条件：列，比较运算符，值
# 比较运算符包涵：= > < >= ,<=, !=,<> 表示（不等于）

Select * from emp where ename='SMITH';
# 例子中的 SMITH 用单引号引起来，表示是字符串，字符串要区分大小写。

#逻辑运算
# And:与 同时满足两个条件的值。
Select * from emp where sal > 2000 and sal < 3000;
# 查询 EMP 表中 SAL 列中大于 2000 小于 3000 的值。

# Or:或 满足其中一个条件的值
Select * from emp where sal > 2000 or comm > 500;
# 查询 emp 表中 SAL 大于 2000 或 COMM 大于500的值。

# Not:非 满足不包含该条件的值。
# select * from emp where not sal > 1500;
# 查询EMP表中 sal 小于等于 1500 的值。

# 逻辑运算的优先级：
# ()    not        and         or


# 特殊条件
# 1.空值判断： is null
Select * from emp where comm is null;
# 查询 emp 表中 comm 列中的空值。


# 2.In
# IN 或 NOT IN
Select * from emp where sal in (5000,3000,1500);
# 查询 EMP 表 SAL 列中等于 5000，3000，1500 的值。


# 3.between and (在 之间的值)
# BETWEEN ... and ... 或 NOT BETWEEN ... and ..
'在不同的数据库中，BETWEEN 操作符会产生不同的结果！即：BETWEEN 选取介于两个值之间时，是否包括两个测试值的字段'
Select * from emp where sal between 1500 and 3000;
# 查询 emp 表中 SAL 列中大于 1500 的小于 3000 的值。
# 注意：大于等于 1500 且小于等于 3000， 1500 为下限，3000 为上限，下限在前，上限在后，查询的范围包涵有上下限的值。
	'选取 alexa 介于 1 和 20 之间但 country 不为 USA 和 IND 的所有网站：'
	SELECT * FROM Websites
    WHERE (alexa BETWEEN 1 AND 20)
    AND country NOT IN ('USA', 'IND');
    
    '选取 name 以介于 'A' 和 'H' 之间字母开始的所有网站：'
    SELECT * FROM Websites
    WHERE name BETWEEN 'A' AND 'H';

    '选取 date 介于 '2016-05-10' 和 '2016-05-14' 之间的所有访问记录：'
    SELECT * FROM access_log
    WHERE date BETWEEN '2016-05-10' AND '2016-05-14';
    

# 4.like
# like , not like
Select * from emp where ename like 'M%';
# 查询 EMP 表中 Ename 列中有 M 的值，M 为要查询内容中的模糊信息。
# 可以通过"\"转义“%”或"_",来匹配特殊字符"_"或"%"
 % 表示多个字值，_ 下划线表示一个字符；
 M% : 为能配符，正则表达式，表示的意思为模糊查询信息为 M 开头的。
 %M% : 表示查询包含M的所有内容。
 %M_ : 表示查询以M在倒数第二位的所有内容。
```







#### 正则匹配

```sql
'MySQL 中使用 REGEXP 或 NOT REGEXP 运算符 (或 RLIKE 和 NOT RLIKE) 来操作正则表达式'
'正则匹配REGEXP 不同于 通配符匹配LIKE'

# 选取 name 以 A 到 H 字母开头的网站
SELECT * FROM Websites
WHERE name REGEXP '^[A-H]';
```



| 通配符                         | 描述                       |
| :----------------------------- | :------------------------- |
| %                              | 替代 0 个或多个字符        |
| _                              | 替代一个字符               |
| [*charlist*]                   | 字符列中的任何单一字符     |
| [^*charlist*] 或 [!*charlist*] | 不在字符列中的任何单一字符 |













### 多表查询

```sql
SELECT Websites.name, Websites.url, access_log.count, access_log.date
FROM Websites, access_log
WHERE Websites.id=access_log.site_id and Websites.name="菜鸟教程";
# 等价于
SELECT w.name, w.url, a.count, a.date
FROM Websites AS w, access_log AS a
WHERE a.site_id=w.id and w.name="菜鸟教程";
```



#### 别名

```sql
'
在下面的情况下，使用别名很有用：

    在查询中涉及超过一个表
    在查询中使用了函数
    列名称很长或者可读性差
    需要把两个列或者多个列结合在一起
'
#列的 SQL 别名语法
    SELECT column_name AS alias_name
    FROM table_name;
#表的 SQL 别名语法
    SELECT column_name(s)
    FROM table_name AS alias_name;

SELECT name, CONCAT(url, ', ', alexa, ', ', country) AS site_info
FROM Websites;

SELECT name AS n, country AS c
FROM Websites;
```







## INSERT INTO

```sql
INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);

INSERT INTO table_name
VALUES (value1,value2,value3,...);



'
insert into scorebak select * from socre where neza='neza'   --插入一行,要求表scorebak 必须存在
select *  into scorebak from score  where neza='neza'  --也是插入一行,要求表scorebak 不存在
'
# 我们可以从一个表中复制所有的列插入到另一个已存在的表中：
    INSERT INTO table2
    SELECT * FROM table1;

# 或者我们可以只复制希望的列插入到另一个已存在的表中：
    INSERT INTO table2
    (column_name(s))
    SELECT column_name(s)
    FROM table1;
```





### 误解

```sql
'MySQL 数据库不支持 SELECT ... INTO 语句，但支持 INSERT INTO ... SELECT 。'
'
区别为：
	select into from 要求目标表不存在，因为在插入时会自动创建；insert into select from 要求目标表存在。

1. 复制表结构及其数据：
	create table table_name_new as select * from table_name_old
	
2. 只复制表结构：
	create table table_name_new as select * from table_name_old where 1=2;
或者：
	create table table_name_new like table_name_old
	
3. 只复制表数据：
如果两个表结构一样：
	insert into table_name_new select * from table_name_old
如果两个表结构不一样：
	insert into table_name_new(column1,column2...) select column1,column2... from table_name_old
'


# 创建 Websites 的备份复件：WebsitesBackup2016表 不需要存在
    SELECT *
    INTO WebsitesBackup2016
    FROM Websites;
    
# 复制多个表中的数据插入到新表中：
    SELECT Websites.name, access_log.count, access_log.date
    INTO WebsitesBackup2016
    FROM Websites
    LEFT JOIN access_log
    ON Websites.id=access_log.site_id;
    
# SELECT INTO 语句可用于通过另一种模式创建一个新的空表。
    SELECT *
    INTO newtable
    FROM table1
    WHERE 1=0;	# 只需要添加促使查询没有数据返回的 WHERE 子句即可：
```







## UPDATE

```sql
UPDATE table_name
SET column1=value1,column2=value2,...
WHERE some_column=some_value;
	# WHERE 子句规定哪条记录或者哪些记录需要更新。如果您省略了 WHERE 子句，所有的记录都将被更新！
	# 在 MySQL 中可以通过设置 sql_safe_updates 这个自带的参数来解决，当该参数开启的情况下，你必须在update 语句后携带 where 条件，否则就会报错。
	# set sql_safe_updates=1; 表示开启该参数
	
	
# 将字段中的特定字符串批量修改为其他字符串时
UPDATE table_name SET field=REPLACE(field, 'old-string', 'new-string') 
[WHERE Clause]
	# 将更新 runoob_id 为 3 的runoob_title 字段值的 "C++" 替换为 "Python"
    UPDATE runoob_tbl SET runoob_title = REPLACE(runoob_title, 'C++', 'Python') where 
    runoob_id = 3;
```





## DELETE

```sql
DELETE FROM table_name
WHERE some_column=some_value;
	# WHERE 子句规定哪条记录或者哪些记录需要删除。如果您省略了 WHERE 子句，所有的记录都将被删除！
	
	
# 可以在不删除表的情况下，删除表中所有的行。这意味着表结构、属性、索引将保持不变：
DELETE FROM table_name;
或
DELETE * FROM table_name;
```





### 区别

```sql

truncate table 命令将快速删除数据表中的所有记录，但保留数据表结构。
这种快速删除与 delete from 数据表的删除全部数据表记录不一样，delete 命令删除的数据将存储在系统回滚段中，需要的时候，数据可以回滚恢复，而 truncate 命令删除的数据是不可以恢复的。

相同点
truncate 和不带 where 子句的 delete, 以及 drop 都会删除表内的数据。

不同点:
1. truncate 和 delete 只删除数据不删除表的结构(定义) ，drop 语句将删除表的结构被依赖的约束(constrain), 触发器(trigger), 索引(index); 依赖于该表的存储过程/函数将保留, 但是变为 invalid 状态。

2.delete 语句是 dml, 这个操作会放到 rollback segement 中, 事务提交之后才生效; 如果有相应的 trigger, 执行的时候将被触发。 truncate, drop 是 ddl, 操作立即生效, 原数据不放到 rollback segment 中, 不能回滚。 操作不触发 trigger。

3.delete 语句不影响表所占用的 extent, 高水线(high watermark)保持原位置不动。 显然 drop 语句将表所占用的空间全部释放 。 truncate 语句缺省情况下见空间释放到 minextents 个 extent, 除非使用 reuse storage; truncate会将高水线复位(回到最开始)。

4.速度：一般来说: drop > truncate > delete 。

5.安全性: 小心使用 drop 和 truncate, 尤其没有备份的时候。否则哭都来不及。

使用上, 想删除部分数据行用 delete, 注意带上 where 子句。 回滚段要足够大。

想删除表, 当然用 drop。

想保留表而将所有数据删除。如果和事务无关, 用 truncate 即可。 如果和事务有关, 或者想触发 trigger, 还是用 delete。

如果是整理表内部的碎片, 可以用 truncate 跟上 reuse stroage, 再重新导入/插入数据。
```







## JOIN

```sql
'
    A inner join B 取交集。

    A left join B 取 A 全部，B 没有对应的值为 null。

    A right join B 取 B 全部 A 没有对应的值为 null。

    A full outer join B 取并集，彼此没有对应的值为 null。

    对应条件在 on 后面填写。
'

'
 1、 on 条件是在生成临时表时使用的条件。
 2、where 条件是在临时表生成好后，再对临时表进行过滤的条件。这时已经没有 left join 的含义（必须返回左边表的记录）了，条件不为真的就全部过滤掉。
'

# INNER字段可以省去
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name=table2.column_name;

	# 可以省略 as 直接重新命名表名，当然 也可以省略as 重新命名键名
	SELECT a.runoob_id, a.runoob_author, b.runoob_count 
	FROM runoob_tbl a INNER JOIN tcount_tbl b ON a.runoob_author = b.runoob_author;
	
	# 等价于以下WHERE语句
    SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a, tcount_tbl b 	WHERE a.runoob_author = b.runoob_author;

# OUTER字段可以省去
SELECT column_name(s)
FROM table1
LEFT OUTER JOIN table2
ON table1.column_name=table2.column_name;

SELECT column_name(s)
FROM table1
RIGHT OUTER JOIN table2
ON table1.column_name=table2.column_name;

# MySQL中不支持 FULL OUTER JOIN
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name=table2.column_name;
# 可以转换成以下形式：
SELECT a.*,b.*
FROM 表1 a LEFT JOIN 表2 b
ON a.unit_NO = b.unit_NO
UNION
SELECT a.*,b.*
FROM 表1 a RIGHT JOIN 表2 b
ON a.unit_NO = b.unit_NO;
```





### UNION

```sql
'
从下图可以看出：
	UNION仅仅进行 行拼接，而字段则是由 先select的字段 决定

使用UNION命令时需要注意，只能在最后使用一个ORDER BY命令，是将两个查询结果合在一起之后，再进行排序！
绝对不能写两个ORDER BY命令。
'

SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
# 注释：默认地，UNION 操作符选取不同的值。如果允许重复的值，请使用 UNION ALL






```

![image-20220130183317456](F:\计算机\数据库\imgs\image-20220130183317456.png)







## 约束

```sql

'
    NOT NULL - 指示某列不能存储 NULL 值。
    	# 约束强制字段始终包含值。这意味着，如果不向字段添加值，就无法插入新记录或者更新记录。
    	
    UNIQUE - 保证某列的每行必须有唯一的值。
    
    PRIMARY KEY - NOT NULL 和 UNIQUE 的结合。确保某列（或两个列多个列的结合）有唯一标识，有助于更容易更快速地找到表中的一个特定的记录。
    	# PRIMARY KEY 约束拥有自动定义的 UNIQUE 约束。
		# 请注意，每个表可以有多个 UNIQUE 约束，但是每个表只能有一个 PRIMARY KEY 约束。
    
    FOREIGN KEY - 保证一个表中的数据匹配另一个表中的值的参照完整性。
    	# JOIN ... ON 时的依据
    	
    CHECK - 保证列中的值符合指定的条件。
    
    COMMENT 给键做注释
    AUTO_INCREMENT	自动增长
    DEFAULT - 规定没有给列赋值时的默认值。
'


# PRIMARY KEY 约束的实例
    CREATE TABLE Persons
    (
        Id_P int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Address varchar(255),
        City varchar(255),
        PRIMARY KEY (Id_P)  //PRIMARY KEY约束
    )
    CREATE TABLE Persons
    (
        Id_P int NOT NULL PRIMARY KEY,   //PRIMARY KEY约束
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Address varchar(255),
        City varchar(255)
    )
    
    
# foreign key 用法：
    create table if not exists per(
      id bigint auto_increment comment '主键',
      name varchar(20) not null comment '人员姓名',
      work_id bigint not null comment '工作id',
      create_time date default '2021-04-02',
      primary key(id),
      foreign key(work_id) references work(id)
    )

    create table if not exists work(
      id bigint auto_increment comment '主键',
      name varchar(20) not null comment '工作名称',
      create_time date default '2021-04-02',
      primary key(id)
    )
```



### UNIQUE

```sql
# 单键约束
CREATE TABLE Persons
(
P_Id int NOT NULL, # 也可以直接UNIQUE修饰
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
UNIQUE (P_Id)
)

# 联合约束
CREATE TABLE Persons
(
P_Id int NOT NULL,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
CONSTRAINT uc_PersonID UNIQUE (P_Id,LastName)
)


# 使已创建的键P_Id 被 UNIQUE 约束
    ALTER TABLE Persons
    ADD UNIQUE (P_Id)	
    
    
    ALTER TABLE Persons
	ADD CONSTRAINT uc_PersonID UNIQUE (P_Id,LastName)
	
# 撤销
    ALTER TABLE Persons
    DROP INDEX uc_PersonID
```





### PRIMARY KEY

```sql
'
主键必须包含唯一的值。

主键列不能包含 NULL 值。

每个表都应该有一个主键，并且每个表只能有一个主键。
'

# 单键约束
CREATE TABLE Persons
(
P_Id int NOT NULL,	# 可以直接 被 PRIMARY KEY 修饰
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PRIMARY KEY (P_Id)
)

# 联合约束
CREATE TABLE Persons
(
P_Id int NOT NULL,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
CONSTRAINT pk_PersonID PRIMARY KEY (P_Id,LastName)
)


# 在 "P_Id" 列创建 PRIMARY KEY 约束
    ALTER TABLE Persons
    ADD PRIMARY KEY (P_Id)

    ALTER TABLE Persons
    ADD CONSTRAINT pk_PersonID PRIMARY KEY (P_Id,LastName)
    
# 撤销 PRIMARY KEY 约束   
    ALTER TABLE Persons
    DROP PRIMARY KEY
```





### FOREIGH KEY

```sql
'
在创建外键约束时，必须先创建外键约束所依赖的表，并且该列为该表的主键

顾名思义：外键，来自外面的键；也就是说键本身来自其他表

作用：
    FOREIGN KEY 约束用于预防破坏表之间连接的行为。
    FOREIGN KEY 约束也能防止非法数据插入外键列，因为它必须是它指向的那个表中的值之一。
    
影响：
	由于引用了其他表的键，父表（真正持有该键的表，而不是仅仅引用该键的子表）将不能随便删除该键，因为子表还在引用
	引出：级联删除CASCADE
'


CREATE TABLE Orders
(
O_Id int NOT NULL,
OrderNo int NOT NULL,
P_Id int,
PRIMARY KEY (O_Id),
FOREIGN KEY (P_Id) REFERENCES Persons(P_Id)
)


CREATE TABLE Orders
(
O_Id int NOT NULL PRIMARY KEY,
OrderNo int NOT NULL,
P_Id int FOREIGN KEY REFERENCES Persons(P_Id)
)


#  联合约束
    CREATE TABLE Orders
    (
    O_Id int NOT NULL,
    OrderNo int NOT NULL,
    P_Id int,
    PRIMARY KEY (O_Id),
    CONSTRAINT fk_PerOrders FOREIGN KEY (P_Id)
    REFERENCES Persons(P_Id)
    )


# 在 "P_Id" 列创建 FOREIGN KEY 约束
    ALTER TABLE Orders
    ADD FOREIGN KEY (P_Id)
    REFERENCES Persons(P_Id)
    
    ALTER TABLE Orders
    ADD CONSTRAINT fk_PerOrders
    FOREIGN KEY (P_Id)
    REFERENCES Persons(P_Id)
    
# 撤销 FOREIGN KEY 约束 
    ALTER TABLE Orders
    DROP FOREIGN KEY fk_PerOrders   



# 在创建表的时候指定外键约束
CREATE TABLE 表名
    (
        column1 datatype null/not null,
        column2 datatype null/not null,
        ...
        CONSTRAINT 外键约束名 FOREIGN KEY  (column1,column2,... column_n) 
        REFERENCES 外键依赖的表 (column1,column2,...column_n)
        ON DELETE CASCADE--级联删除
    );
    
# 在创建表后增加外键约束
ALTER TABLE 表名
    ADD CONSTRAINT 外键约束名
    FOREIGN KEY (column1, column2,...column_n) 
    REFERENCES 外键所依赖的表 (column1,column2,...column_n)
    ON DELETE CASCADE;--级联删除
```







### CHECK

```sql
'
如果对单个列定义 CHECK 约束，那么该列只允许特定的值。

如果对一个表定义 CHECK 约束，那么此约束会基于行中其他列的值在特定的列中对值进行限制。
'



CREATE TABLE Persons
(
P_Id int NOT NULL,	# 列约束，直接修饰：CHECK (P_Id>0)
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
CHECK (P_Id>0) # 表约束
)


CREATE TABLE Persons
(
P_Id int NOT NULL,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
CONSTRAINT chk_Person CHECK (P_Id>0 AND City='Sandnes')
)



# 在 "P_Id" 列创建 CHECK 约束
    ALTER TABLE Persons
    ADD CHECK (P_Id>0)

    ALTER TABLE Persons
    ADD CONSTRAINT chk_Person CHECK (P_Id>0 AND City='Sandnes')
    
    
# 撤销 CHECK 约束
    ALTER TABLE Persons
    DROP CHECK chk_Person    
```





### DEFAULT

```sql
CREATE TABLE Persons
(
    P_Id int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255) DEFAULT 'Sandnes'
)

CREATE TABLE Orders
(
    O_Id int NOT NULL,
    OrderNo int NOT NULL,
    P_Id int,
    OrderDate date DEFAULT GETDATE()  # 根据函数，插入时自动获取最新默认值
)

# 在 "City" 列创建 DEFAULT 约束
    ALTER TABLE Persons
    ALTER City SET DEFAULT 'SANDNES'
    
    
# 撤销 DEFAULT 约束
    ALTER TABLE Persons
    ALTER City DROP DEFAULT    
```







### AUTO_INCREMENT

```sql
REATE TABLE Persons
(
ID int NOT NULL AUTO_INCREMENT, # 从1开始自增
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PRIMARY KEY (ID)
)


# 要让 AUTO_INCREMENT 序列以其他的值起始，请使用下面的 SQL 语法：
	ALTER TABLE Persons AUTO_INCREMENT=100

```







### 删除未命名的外键

```sql
'
删除外键需要知道外键的名称，如果创建时没有设置名称则会自动生成一个，你需要获取改外键的信息。

使用以下命令获取外键信息：
'

SELECT
  constraint_name
FROM
  information_schema.REFERENTIAL_CONSTRAINTS
WHERE
  constraint_schema = <'db_name'> AND table_name = <'table_name'>;
SELECT *
FROM
  information_schema.KEY_COLUMN_USAGE
WHERE
  constraint_schema = <'db_name'> AND table_name = <'table_name'> AND   
  referenced_table_name IS NOT NULL;
```





## CREATE INDEX

```sql
'
在表中创建索引，以便更加快速高效地查询数据
更新一个包含索引的表需要比更新一个没有索引的表花费更多的时间，这是由于索引本身也需要更新

因此，理想的做法是仅仅在常常被搜索的列（以及表）上面创建索引。
'

CREATE INDEX index_name
ON table_name (column_name)



CREATE INDEX PIndex
ON Persons (LastName)

# 如果您希望索引不止一个列，您可以在括号中列出这些列的名称，用逗号隔开：
CREATE INDEX PIndex
ON Persons (LastName, FirstName)
```







## DROP

```sql
# 撤销索引
	ALTER TABLE table_name DROP INDEX index_name
	
# 撤销数据库
	DROP DATABASE base_name

# 撤销表
	DROP TABLE table_name
	
# 仅仅需要删除表内的数据，但并不删除表本身
	TRUNCATE TABLE table_name
```







## ALTER

```sql
'
如需在表中添加列，请使用下面的语法:
    ALTER TABLE table_name
    ADD column_name datatype
    
如需删除表中的列，请使用下面的语法（请注意，某些数据库系统不允许这种在数据库表中删除列的方式）：
    ALTER TABLE table_name
    DROP COLUMN column_name
    
要改变表中列的数据类型，请使用下面的语法：
    ALTER TABLE table_name
    MODIFY COLUMN column_name datatype
'


CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Age int
);


# 修改表的字段类型
    ALTER TABLE Persons
    MODIFY Age int NOT NULL;
    
    ALTER TABLE Persons
	MODIFY Age int NULL;
	
# 使已创建的键P_Id 被 UNIQUE 约束
    ALTER TABLE Persons
    ADD UNIQUE (P_Id)	
    
    
    ALTER TABLE Persons
	ADD CONSTRAINT uc_PersonID UNIQUE (P_Id,LastName)
# 撤销 unique 修饰
    ALTER TABLE Persons
    DROP INDEX uc_PersonID
    
    
# DEFAULT 修饰
    ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000;
    ALTER TABLE testalter_tbl ALTER i DROP DEFAULT; 
    
# 修改表名
 	ALTER TABLE testalter_tbl RENAME TO alter_tbl;
# 修改存储引擎：修改为myisam
	alter table tableName engine=myisam; 
    
# CHANGE 子语法
	# 给已经存在的colume添加自增语法
	ALTER TABLE student CHANGE id id INT( 11 ) NOT NULL AUTO_INCREMENT;   
	ALTER TABLE testalter_tbl CHANGE j j INT;
	
	
# 指定新增字段的位置，可以使用MySQL提供的关键字 FIRST (设定位第一列)， AFTER 字段名（设定位于某个字段之后）
    ALTER TABLE testalter_tbl DROP i;
    ALTER TABLE testalter_tbl ADD i INT FIRST;
    ALTER TABLE testalter_tbl DROP i;
    ALTER TABLE testalter_tbl ADD i INT AFTER c;
    
    alter table tableName modify name1 type1 first|after name2;
    
    
    
```











## Date 函数

```sql
NOW()
CURDATE()
CURTIME()

DATE(date) # 提取日期或日期/时间表达式的日期部分。
    SELECT ProductName, DATE(OrderDate) AS OrderDate
    FROM Orders
    WHERE OrderId=1
    
    
DATE_ADD(date,INTERVAL expr type)
	# date 参数是合法的日期表达式。expr 参数是您希望添加的时间间隔。
    SELECT OrderId,DATE_ADD(OrderDate,INTERVAL 45 DAY) AS OrderPayDate
    FROM Orders
    
DATE_SUB(date,INTERVAL expr type)
	# 想要向 "OrderDate" 减去 5 天。
    SELECT OrderId,DATE_SUB(OrderDate,INTERVAL 5 DAY) AS SubtractDate
    FROM Orders
    
DATEDIFF(d1,d2) # 函数返回两个日期之间的天数。
	SELECT DATEDIFF('2008-11-30','2008-11-29') AS DiffDate
	
DATE_FORMAT(date,format)
	# date 参数是合法的日期。format 规定日期/时间的输出格式。
	
	
	
'
SECOND
MINUTE
HOUR
DAY
WEEK
MONTH
QUARTER
YEAR
'
EXTRACT(unit FROM date) # 返回日期/时间的单独部分，比如年、月、日、小时、分钟等等
    SELECT EXTRACT(YEAR FROM OrderDate) AS OrderYear,
    EXTRACT(MONTH FROM OrderDate) AS OrderMonth,
    EXTRACT(DAY FROM OrderDate) AS OrderDay
    FROM Orders
    WHERE OrderId=1
```

![image-20220130230039710](F:\计算机\数据库\imgs\image-20220130230039710.png)





### DATE_FORMAT 格式

| 格式 | 描述                                           |
| :--- | :--------------------------------------------- |
| %a   | 缩写星期名                                     |
| %b   | 缩写月名                                       |
| %c   | 月，数值                                       |
| %D   | 带有英文前缀的月中的天                         |
| %d   | 月的天，数值（00-31）                          |
| %e   | 月的天，数值（0-31）                           |
| %f   | 微秒                                           |
| %H   | 小时（00-23）                                  |
| %h   | 小时（01-12）                                  |
| %I   | 小时（01-12）                                  |
| %i   | 分钟，数值（00-59）                            |
| %j   | 年的天（001-366）                              |
| %k   | 小时（0-23）                                   |
| %l   | 小时（1-12）                                   |
| %M   | 月名                                           |
| %m   | 月，数值（00-12）                              |
| %p   | AM 或 PM                                       |
| %r   | 时间，12-小时（hh:mm:ss AM 或 PM）             |
| %S   | 秒（00-59）                                    |
| %s   | 秒（00-59）                                    |
| %T   | 时间, 24-小时（hh:mm:ss）                      |
| %U   | 周（00-53）星期日是一周的第一天                |
| %u   | 周（00-53）星期一是一周的第一天                |
| %V   | 周（01-53）星期日是一周的第一天，与 %X 使用    |
| %v   | 周（01-53）星期一是一周的第一天，与 %x 使用    |
| %W   | 星期名                                         |
| %w   | 周的天（0=星期日, 6=星期六）                   |
| %X   | 年，其中的星期日是周的第一天，4 位，与 %V 使用 |
| %x   | 年，其中的星期一是周的第一天，4 位，与 %v 使用 |
| %Y   | 年，4 位                                       |
| %y   | 年，2 位                                       |







## NULL相关

```sql
'
NULL 值的处理方式与其他值不同。

NULL 用作未知的或不适用的值的占位符。

Note注释：无法比较 NULL 和 0；它们是不等价的。
	与空字符串、0 这些是不等价的，是不能用于比较的
	
无法使用比较运算符来测试 NULL 值，比如 =、< 或 <>。
	我们必须使用 IS NULL 和 IS NOT NULL 操作符。

'

'
涉及到运算时，若某值是NULL，该如何处理？
'
SELECT ProductName,UnitPrice*(UnitsInStock+IFNULL(UnitsOnOrder,0))
FROM Products

# 或者我们可以使用 COALESCE() 函数，如下所示：
SELECT ProductName,UnitPrice*(UnitsInStock+COALESCE(UnitsOnOrder,0))
FROM Products
```





| P_Id | ProductName | UnitPrice | UnitsInStock | UnitsOnOrder |
| :--- | :---------- | :-------- | :----------- | :----------- |
| 1    | Jarlsberg   | 10.45     | 16           | 15           |
| 2    | Mascarpone  | 32.56     | 23           |              |
| 3    | Gorgonzola  | 15.67     | 9            | 20           |











## GROUP BY

```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name;

	# 根据Websites.name来进行分组，分别对每个组进行COUNT(access_log.aid)操作
	# 若不分组，则相当于对整个表进行COUNT，最后只会有一行数据
    SELECT Websites.name,COUNT(access_log.aid) AS nums FROM access_log
    LEFT JOIN Websites
    ON access_log.site_id=Websites.id
    GROUP BY Websites.name;

```





### WITH ROLLUP

```sql
# group by子句使用WITH ROLLUP关键字之后，在所有查询出的分组记录之后增加一条记录，该记录计算查询出的所有记录的总数，即统计记录数量。
```



![image-20220131135622555](F:\计算机\数据库\imgs\image-20220131135622555.png)





![image-20220131135721405](F:\计算机\数据库\imgs\image-20220131135721405.png)













## HAVING

```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value	# 对表中 现有的数据 进行约束
GROUP BY column_name
HAVING aggregate_function(column_name) operator value; # 对表中 统合计算后 的数据进行过滤

'
参考链接：https://www.jianshu.com/p/fbf5d6376f9d

与 WHERE 的区别：
	having子句可以让我们筛选成组后的各组数据，where子句在聚合前先筛选记录
	having中可以直接使用聚合函数，而where中却不可以
	
# 显示每个地区的总人口数和总面积,仅显示那些人口数量超过1000000的地区：
select region,sum(population),sum(area) from bbc group by region having sum(population) > 1000000

在这里，我们不能用where来筛选超过1000000的地区，因为表中不存在这样一条记录。相反，having子句可以让我么筛选成组后的各组数据
'


# 查找总访问量大于 200 的网站，并且 alexa 排名小于 200。
    SELECT Websites.name, SUM(access_log.count) AS nums FROM Websites
    INNER JOIN access_log
    ON Websites.id=access_log.site_id
    WHERE Websites.alexa < 200 	# 约束现有字段alexa
    GROUP BY Websites.name
    HAVING SUM(access_log.count) > 200; # 过滤统合后的数据 SUM


```









## EXISTS

```sql
SELECT column_name(s)
FROM table_name
WHERE EXISTS # 可以配合 NOT 
(SELECT column_name FROM table_name WHERE condition); 

# 找出访问量COUNT 不大于 200 的网站
SELECT Websites.name, Websites.url 
FROM Websites 
WHERE NOT EXISTS (SELECT count FROM access_log WHERE Websites.id = access_log.site_id AND count > 200);


```







## 临时表

```sql
'
临时表只在当前连接可见，当关闭连接时，Mysql会自动删除表并释放所有空间。

TEMPORARY 关键字

当你使用 SHOW TABLES命令显示数据表列表时，你将无法看到 临时表 SalesSummary。
'

 CREATE TEMPORARY TABLE SalesSummary (
    product_name VARCHAR(50) NOT NULL
    , total_sales DECIMAL(12,2) NOT NULL DEFAULT 0.00
    , avg_unit_price DECIMAL(7,2) NOT NULL DEFAULT 0.00
    , total_units_sold INT UNSIGNED NOT NULL DEFAULT 0
);


# 当然也可以手动删除临时表
	DROP TABLE SalesSummary;
```







## 复制表

```sql
# 获取数据表的完整结构。
	SHOW CREATE TABLE runoob_tbl \G;
	
	
# 方法一：
    CREATE TABLE targetTable LIKE sourceTable;
    INSERT INTO targetTable SELECT * FROM sourceTable;

# 方法二：
	create table 新表 select * from 旧表



# 只复制表结构到新表
	create table 新表 select * from 旧表 where 1=2
	
# 可以拷贝一个表中其中的一些字段:
CREATE TABLE newadmin AS
(
    SELECT username, password FROM admin
)


# 可以将新建的表的字段改名:
CREATE TABLE newadmin AS
(  
    SELECT id, username AS uname, password AS pass FROM admin
)


# 可以拷贝一部分数据:
CREATE TABLE newadmin AS
(
    SELECT * FROM admin WHERE LEFT(username,1) = 's'
)


# 可以在创建表的同时定义表中的字段信息:
CREATE TABLE newadmin
(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY
)
AS
(
    SELECT * FROM admin
)  


```





## 元数据/自增序列

```sql
SELECT VERSION( )	服务器版本信息
SELECT DATABASE( )	当前数据库名 (或者返回空)
SELECT USER( )	当前用户名
SHOW STATUS	服务器状态
SHOW VARIABLES	服务器配置变量
```





```sql
'
一张数据表只能有一个字段自增主键

'

# 获取AUTO_INCREMENT值
	select LAST_INSERT_ID( )


# 设置序列的开始值
    CREATE TABLE insect
        (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        PRIMARY KEY (id),
        name VARCHAR(30) NOT NULL, 
        date DATE NOT NULL,
        origin VARCHAR(30) NOT NULL
    )engine=innodb auto_increment=100 charset=utf8;
    
    # 第二种方式
    ALTER TABLE t AUTO_INCREMENT = 100;
```





## 删除重复数据

```sql
# 防止表中出现重复数据
	# 设置指定的字段为 PRIMARY KEY（主键） 或者 UNIQUE（唯一） 索引来保证数据的唯一性
    CREATE TABLE person_tbl
    (
       first_name CHAR(20) NOT NULL,
       last_name CHAR(20) NOT NULL,
       sex CHAR(10),
       UNIQUE (last_name, first_name)
    );


INSERT IGNORE INTO 与 INSERT INTO 的区别
	INSERT IGNORE INTO 会忽略数据库中已经存在的数据，
	如果数据库没有数据，就插入新的数据，如果有数据的话就跳过这条数据
	'在设置了记录的唯一性后，有效保证即使插入重复数据，也不返回错误，只以警告形式返回'
	
INSERT REPLACE INTO :
	如果存在 primary 或 unique 相同的记录，则先删除掉。再插入新记录。
	
	
# 统计重复数据
    SELECT COUNT(*) as repetitions, last_name, first_name
    FROM person_tbl
    GROUP BY last_name, first_name # 以 last_name,first_nasme 组成的元组（整体） 进行 分组
    HAVING repetitions > 1;
# 统计不重复数据 ？？？ 还没测验
    SELECT COUNT(DISTINCT *) as repetitions, last_name, first_name
    FROM person_tbl
    GROUP BY last_name, first_name    

# 过滤重复数据
    SELECT DISTINCT last_name, first_name
    FROM person_tbl;
    
    # 等价于
    SELECT last_name, first_name
    FROM person_tbl
    GROUP BY (last_name, first_name);
    
    
# 删除重复数据
	CREATE TABLE tmp SELECT last_name, first_name, sex FROM person_tbl  GROUP BY (last_name, first_name, sex);
	DROP TABLE person_tbl;
	ALTER TABLE tmp RENAME TO person_tbl;
```









## 注入、导入/导出

```sql
# 注入
	'通过把SQL命令插入到Web表单递交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的SQL命令'
		$name = "Qadir'; DELETE FROM users;"
	 	SELECT * FROM users WHERE name='{$name}'
	 	# 上述动态拼接查询语句，将会删除users表
# 防止SQL注入，我们需要注意以下几个要点：
    1.永远不要信任用户的输入。对用户的输入进行校验，可以通过正则表达式，或限制长度；对单引号和 双"-"进行转换等。
    2.永远不要使用动态拼装sql，可以使用参数化的sql或者直接使用存储过程进行数据查询存取。
    3.永远不要使用管理员权限的数据库连接，为每个应用使用单独的权限有限的数据库连接。
    4.不要把机密信息直接存放，加密或者hash掉密码和敏感的信息。
    5.应用的异常信息应该给出尽可能少的提示，最好使用自定义的错误信息对原始错误信息进行包装
    6.sql注入的检测方法一般采取辅助软件或网站平台来检测，软件一般采用sql注入检测工具jsky，网站平台就有亿思网站安全平台检测工具。MDCSOFT SCAN等。采用MDCSOFT-IPS可以有效的防御SQL注入，XSS攻击等。
    
    
# like语句注入
	like查询时，如果用户输入的值有"_"和"%"，则会出现这种情况：用户本来只是想查询"abcd_"，查询结果中却有"abcd_"、"abcde"、"abcdf"等等；
	用户要查询"30%"（注：百分之三十）时也会出现问题。
```





```sql
# 前提
	1.在my.ini文件中，添加字段 secure_file_priv=""	# 导入导出，允许的文件目录
	2.重启mysql
		a.window+R中键入services.mcs，回车
		b.发现在本机上存在两个mysql=>mysql,mysql8
			net stop mysql
			net start mysql
		

# 仅仅导出表内数据
# 1.简化导出
    SELECT * FROM runoob_tbl 
    INTO OUTFILE '/tmp/runoob.txt';

# 2.
SELECT * FROM avatar INTO OUTFILE 'd:/backup.txt'
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';



# 导出生成该表的所有操作
	mysqldump -u root -p --no-create-info \
    --tab=/tmp RUNOOB runoob_tbl
    # --no-create-info 指的是不需要生成创建表的步骤
	# 使用 --tab 选项来指定导出文件指定的目录，该目标必须是可写的
    # RUNNOOB 指的是数据库；runnob_tb1指的是该数据库下的数据表
# 等价于
	mysqldump -u root -p RUNOOB runoob_tbl > dump.txt

# 导出单一整个数据库的数据
	mysqldump -u root -p RUNOOB > database_dump.txt
# 上述可逆操作，将备份的数据库导入到MySQL服务器中，使用以下命令你需要确认数据库已经创建：
	mysql -u root -p database_name < dump.txt
# 备份所有数据库，可以使用以下命令：
	mysqldump -u root -p --all-databases > database_dump.txt
	
	
# 将导出的数据直接导入到远程的服务器上，但请确保两台服务器是相通的，是可以相互访问的：
	mysqldump -u root -p database_name \
    | mysql -h other-host.com database_name
# 上述可逆操作，要将远程服务器的数据拷贝到本地
	mysqldump -h other-host.com -P port -u root -p database_name > dump.txt
  
```





```sql
# 方式一
	mysql -u用户名    -p密码    <  要导入的数据库数据(runoob.sql)
	
# 方式二：source 命令导入数据库需要先登录到数库终端：
    create database abc;      # 创建数据库
    use abc;                  # 使用已创建的数据库 
    set names utf8;           # 设置编码
    source /home/abc/abc.sql  # 导入备份数据库
    
# 方式三：
	LOAD DATA LOCAL INFILE 'dump.txt' INTO TABLE mytbl;
	# 如果指定LOCAL关键词，则表明从客户主机上按路径读取文件。如果没有指定，则文件在服务器上按路径读取文件。
	# 在本机上测验，用本机的备份数据导入到本机的数据库中表时，发现不能使用local关键字，一旦使用就无法正常导入
	
# mysqlimport
	...
```







## 运算符

```sql
'
算术运算符
	+
	-
	*
	/	等价于	div
	%	等价于	mod
比较运算符
	=
	<>	等价于	!=
	>
	>=
	<
	<=
	
	IS NULL
	IS NOT NULL
	IN 
	NOT IN
	BETWEEN ... AND ...
	NOT BETWEEN ... AND ...
	LIKE
	NOT LIKE
	REGEXP	等价于	RLIKE
	NOT REGEXP
逻辑运算符
	AND
	OR	等价于 ||
	NOT	等价于	!	
	XOR	等价于	^
位运算符
	&
	|
	^
	~
	<<
	>>
'

select 1-2;

select 2=3;
select 5 between 1 and 10;
select 5 in (1,2,3,4,5);
select null is NULL;
select '12345' like '12%';
select 'beijing' REGEXP 'jing';



```

![image-20220131165247118](F:\计算机\数据库\imgs\image-20220131165247118.png)













## 基本函数

```sql
SQL Aggregate 函数计算从列中取得的值，返回一个单一的值。
    AVG() - 返回平均值
    	SELECT site_id, count FROM access_log
		WHERE count > (SELECT AVG(count) FROM access_log);
		
    SUM() - 返回总和
    	SELECT SUM(column_name) FROM table_name;
    COUNT() - 返回行数
        -- 查询所有记录的条数
        select count(*) from access_log;

        -- 查询websites 表中 alexa列中不为空的记录的条数
        select count(alexa) from websites;

        -- 查询websites表中 country列中不重复的记录条数
        select count(distinct country) from websites;    
    
        count(case when job ='SALESMAN' then '1' end) # 销售人数,
        count(case when job ='MANAGER' then '1' end) # 主管人数
        
    FIRST() - 返回第一个记录的值
    	# 注释：只有 MS Access 支持 FIRST() 函数。
    	# 等价于  ORDER BY id ASC LIMIT 1
            SELECT name FROM Websites
            ORDER BY id ASC
            LIMIT 1;
    LAST() - 返回最后一个记录的值
    	# 注释：只有 MS Access 支持 FIRST() 函数。
        SELECT column_name FROM table_name
        ORDER BY column_name DESC
        LIMIT 1;
    
    MAX() - 返回最大值
    	# 从 "Websites" 表的 "alexa" 列获取最大值：
    	SELECT MAX(alexa) AS max_alexa FROM Websites;
    MIN() - 返回最小值
    	# 从 "Websites" 表的 "alexa" 列获取最小值：
    	SELECT MIN(alexa) AS min_alexa FROM Websites;
    	
    
    
    
    
SQL Scalar 函数
    UCASE() - 将某个字段转换为大写
    	SELECT UCASE(column_name) FROM table_name;
    	
    LCASE() - 将某个字段转换为小写
    	SELECT LCASE(column_name) FROM table_name;
    	
    MID() - 从某个文本字段提取字符，MySql 中使用
    	# （起始值是 1）;此外注意是字符数，不管是中文还是因为，一个字符
    	SELECT MID(column_name,start[,length]) FROM table_name;
    	
    	SELECT MID(name,1,4) AS ShortTitle
        FROM Websites;
    SubString(字段，1，end) - 从某个文本字段提取字符

    LEN() - 返回某个文本字段的长度
    	# MySQL 中函数为 LENGTH():
    	SELECT LENGTH(column_name) FROM table_name;
    	   
    ROUND() - 对某个数值字段进行指定小数位数的四舍五入
    	# decimals指保留几位小数，四舍五入
    	SELECT ROUND(column_name,decimals) FROM TABLE_NAME;
    	
    NOW() - 返回当前的系统日期和时间
    FORMAT() - 格式化某个字段的显示方式


```





# JSON数据类型

```sql
'
# https://segmentfault.com/a/1190000024445924
# think-model模块（JS驱动）：https://thinkjs.org/zh-cn/doc/3.0/relation_model.html


# JSON 关键字用来修饰
# MySQL 对 JSON 的存储本质上还是字符串的存储操作。
# 只是当定义为 JSON 类型之后内部会对数据再进行一些索引的创建方便后续的操作而已
'

CREATE TABLE user (
  id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  info JSON
);


-- 手动输入序列化内容
 INSERT INTO user (`name`, `info`) 
 VALUES
 ('lilei', '{"sex": "male", "age": 18, "hobby": ["basketball", "football"], "score": [85, 90, 100]}');
-- 利用内置的JSON_OBJECT，JSON_ARRAY帮助序列化内容
INSERT INTO user
(name,info)
VALUES
(
	"hanmeimei",
    JSON_OBJECT(
    	"sex","female",
        "age",18,
       "hobby",JSON_ARRAY("badminton","sing"),
        "score",JSON_ARRAY(90,95,100)
    )
);
 
 


```



## 添加数据

```sql
JSON_OBJECT：
	-- 快速创建 JSON 对象，奇数列为 key，偶数列为 value，
	-- 使用方法 JSON_OBJECT(key,value,key1,value1)
JSON_ARRAY：
	-- 快速创建 JSON 数组
	-- 使用方法 JSON_ARRAY(item0, item1, item2)
```





## 查询数据

```sql
JSON_EXTRACT(json_doc, path[, path] ...)
	-- 根据 Path 获取部分 JSON 数据
	-- 可简化成 "->"
	-- 与 JSON_VALUE 的区别在于：当json的值是字符类型时，返回值会带上两个双引号。
	-- SELECT JSON_EXTRACT("{'id':'3'}","$.id"); -- 返回结果是：'"3"'
	select name,json_extract("info","$.age") as age,json_extract("info","$.sex") as sex 	from user;
	-- 等价于下列
	select name,info->"$.age" as age,info->"$.sex" as sex from user;
	
JSON_UNQUOTE
	-- 去""
JSON_QUOTE
	-- 加""

# 符号 ->> 的含义
->>：
	--  json_unquote(json_extract())的等效操作符是“->>”。
	-- 等价于 先 JSON_EXTRACT() 再 JSON_UNQUOTE() 的复合写法
	
	
JSON_CONTAINS(json_doc, val[, path])：
	'安装path路径所引导的结果 是否等于 val'
	-- 查询 JSON 数据是否在指定 Path 包含指定的数据，包含则返回1，否则返回0。
	'需要注意的是 JSON_CONTAINS() 查询字符串由于不带类型转换的问题字符串需要使用加上 "" 包裹查询，或者使用 JSON_QUOTE('male') 也可以。'
	SELECT `name` FROM `user` WHERE JSON_CONTAINS(`info`, '"male"', '$.sex') AND JSON_SEARCH(`info`, 'one', 'basketball', null, '$.hobby');
	-- 等价于
	SELECT `name` FROM `user` WHERE JSON_VALUE(`info`, '$.sex') = 'male' AND 'basketball' MEMBER OF(JSON_VALUE(`info`, '$.hobby'));
	-- 等价于
	SELECT `name` FROM `user` WHERE JSON_VALUE(`info`, '$.sex') = 'male' AND JSON_OVERLAPS(JSON_VALUE(`info`, '$.hobby'), JSON_QUOTE('basketball'));
'
注意上方：
	"basketball" MEMBER OF(JSON_VALUE(`info`,"$.hobby"))
	
	JSON_OVERLAPS(JSON_VALUE(`info`, '$.hobby'), JSON_QUOTE('basketball'))
'	
	
	
JSON_CONTAINS_PATH(json_doc, one_or_all, path[, path] ...)
	-- 查询是否存在指定路径，存在则返回1，否则返回0。one_or_all 只能取值 "one" 或 "all"，one 表示只要有一个存在即可，all 表示所有的都存在才行。
	
	
JSON_KEYS(json_doc[, path])
	-- 获取 JSON 数据在指定路径下的所有键值。类似 JavaScript 中的 Object.keys() 方法。
	# 查找 info字段下所有的键
	SELECT JSON_KEYS(`info`,"$") FROM `user`;
	
'详情可了解：https://blog.csdn.net/sssssuuuuu666/article/details/108740580'
 JSON_SEARCH(json_doc, one_or_all, search_str[, escape_char[, path] ...])
 	-- 在指定范围path内查询包含指定字符串search_str的 可匹配路径
 	-- one 返回首次匹配成功的路径，all则返回所有符合匹配的路径
 	-- escape_char 参数指定时要求必须是常量（为空或者一个字符），当escape_char参数为NULL或者不存在的情况下，系统默认使用 \ 作为转义字符。
 	-- 查询的字符串search_str可以用 LIKE 里的 '%' 或 '_' 匹配
 	'由于 JSON_SEARCH 不会做类型转换，所以匹配出来的路径字符串需要进行 JSON_UNQUOTE() 操作。'
 	'另外还有非常重要的一点是 JSON_SEARCH 无法对数值类型数据进行查找，也不知道这个是 Bug 还是 Feature'
 	
 	
 	
'
和 JavaScript 中对象的操作比较类似，通过 . 获取下一级的属性，通过 [] 获取数组元素。

不一样的地方在于需要通过 $ 表示本身，这个也比较好理解

另外就是可以使用 * 和 ** 两个通配符，比如 .* 表示当前层级的所有成员的值，[*] 则表示当前数组中所有成员值。

** 类似 LIKE 一样可以接前缀和后缀，比如 a**b 表示的是以 a 开头，b结尾的路径。
'
```



![image-20220201164109318](F:\计算机\数据库\imgs\image-20220201164109318.png)

![image-20220201163901474](F:\计算机\数据库\imgs\image-20220201163901474.png)





![image-20220201165008688](F:\计算机\数据库\imgs\image-20220201165008688.png)







## 修改数据

```sql
JSON_ARRAY_APPEND(json_doc, path, val[, path, val] ...)
	-- 该方法如同字面意思，给数组添加值
	UPDATE `user` SET `info` = JSON_ARRAY_APPEND(`info`, '$.hobby', 'badminton') WHERE `name` = 'lilei';
	
JSON_ARRAY_INSERT(json_doc, path, val[, path, val] ...)
	-- 区别于 JSON_ARRAY_APPEND() 它可以在指定位置插值


-- JSON_INSERT/JSON_REPLACE/JSON_SET
JSON_[INSERT|REPLACE|SET](json_doc, path, val[, path, val] ...)
	-- JSON_INSERT：当路径不存在才插入
	-- JSON_REPLACE：当路径存在才替换
	-- JSON_SET：不管路径是否存在
	 UPDATE `user` SET `info` = JSON_REPLACE(`info`, '$.age', 20) WHERE `name` = 'lilei';
	 # 注意：info->>"$.age"提取出的不是整数，这意味着+1后得出的是20.0,这在表中显示很不好看、且有歧义,进行位运算|0后，转换成整数，再替换进JSON
	 update user set info=json_replace(info,"$.age",(info->>"$.age"+1)|0) where name="lilei";
	
JSON_REMOVE(json_doc, path[, path] ...)
	-- 移除指定路径的数据
	UPDATE `user` SET `info` = JSON_REMOVE(`info`, '$.score[0]') WHERE `name` = 'lilei';
	
	UPDATE `user` SET `info` = JSON_REMOVE(`info`, JSON_UNQUOTE(JSON_SEARCH(`info`, 'one', 'badminton'))) WHERE `name` = 'lilei';
```











# 事务

```sql
'
# 快照，回退，保存点

事务主要用于处理操作量大，复杂度高的数据。
	比如说，在人员管理系统中，你删除一个人员，你既需要删除人员的基本资料，也要删除和该人员相关的信息，如信箱，文章等等，这样，这些数据库操作语句就构成一个事务！

    1.在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。
    2.事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。
    3.事务用来管理 insert,update,delete 语句
    
一般来说，事务是必须满足4个条件（ACID）：
	原子性（Atomicity，或称不可分割性）
	一致性（Consistency）
	隔离性（Isolation，又称独立性）
	持久性（Durability）。


BEGIN 或 START TRANSACTION 显式地开启一个事务；

COMMIT 也可以使用 COMMIT WORK，不过二者是等价的。COMMIT 会提交事务，并使已对数据库进行的所有修改成为永久性的；

ROLLBACK 也可以使用 ROLLBACK WORK，不过二者是等价的。回滚会结束用户的事务，并撤销正在进行的所有未提交的修改；


SAVEPOINT identifier，SAVEPOINT 允许在事务中创建一个保存点，一个事务中可以有多个 SAVEPOINT；

RELEASE SAVEPOINT identifier 删除一个事务的保存点，当没有指定的保存点时，执行该语句会抛出一个异常；

ROLLBACK TO identifier 把事务回滚到标记点；

SET TRANSACTION 用来设置事务的隔离级别。
	InnoDB 存储引擎提供事务的隔离级别有READ UNCOMMITTED、READ COMMITTED、REPEATABLE READ 和 SERIALIZABLE。
'


```





## 例子

```sql
mysql> use RUNOOB;
Database changed
mysql> CREATE TABLE runoob_transaction_test( id int(5)) engine=innodb;  # 创建数据表
Query OK, 0 rows affected (0.04 sec)
 
mysql> select * from runoob_transaction_test;
Empty set (0.01 sec)
 
mysql> begin;  # 开始事务
Query OK, 0 rows affected (0.00 sec)
 
mysql> insert into runoob_transaction_test value(5);
Query OK, 1 rows affected (0.01 sec)
 
mysql> insert into runoob_transaction_test value(6);
Query OK, 1 rows affected (0.00 sec)
 
mysql> commit; # 提交事务
Query OK, 0 rows affected (0.01 sec)
 
mysql>  select * from runoob_transaction_test;
+------+
| id   |
+------+
| 5    |
| 6    |
+------+
2 rows in set (0.01 sec)
 
mysql> begin;    # 开始事务
Query OK, 0 rows affected (0.00 sec)
 
mysql>  insert into runoob_transaction_test values(7);
Query OK, 1 rows affected (0.00 sec)
 
mysql> rollback;   # 回滚
Query OK, 0 rows affected (0.00 sec)
 
mysql>   select * from runoob_transaction_test;   # 因为回滚所以数据没有插入
+------+
| id   |
+------+
| 5    |
| 6    |
+------+
2 rows in set (0.01 sec)
 
mysql>
```







# 扩展函数



## 字符串

```sql
ASCII(s)
	-- 返回字符串 s 的第一个字符的 ASCII 码
LCASE(s)	LOWER(S)
	-- 将字符串 s 的所有字母变成小写字母
UCASE(s)	UPPER(S)
REVERSE(s)	
	-- 将字符串s的顺序反过来
	
	
LENGTH(s)
	-- 返回字节数
CHAR_LENGTH(s)	
	-- 返回字符串 s 的字符数
	
	
	
	
ROUND(x,n)
	-- 将x保留n位小数，四舍五入
FORMAT(x,n)
	-- 同上，只是将数字 x 进行格式化 "#,###.##" 后输出




CONCAT(s1,s2...sn)	
	-- 字符串 s1,s2 等多个字符串合并为一个字符串
CONCAT_WS(x, s1,s2...sn)	
	-- 同 CONCAT(s1,s2,...) 函数，但是每个字符串之间要加上 x，x 可以是分隔符
LPAD(s1,len,s2)		RPAD(s1,len,s2)
	-- 在字符串 s1 的开始处填充字符串 s2，使字符串长度达到 len
	SELECT LPAD('abc',5,'xx') -- xxabc
LTRIM(s)	RTRIM(s)	TRIM(s)
	-- 去掉字符串 s 开始处的空格
REPEAT(s,n)	
	-- 将字符串 s 重复 n 次
	SPACE(n)	-- 返回 n 个空格
	

'注意在mysql中，字符索引从1开始'
INSERT(s1,x,len,s2)	
	-- 字符串 s2 替换 s1 的 x 位置开始长度为 len 的字符串
	SELECT INSERT("google.com", 1, 6, "runoob");  -- 输出：runoob.com
REPLACE(s,s1,s2)	
	-- 将字符串 s2 替代字符串 s 中的字符串 s1
	SELECT REPLACE('abc','a','x') --xbc
MID(s,x,len)	SUBSTR(S,x,len)		SUBSTRING(s,x,len)
	-- 从x开始截取字符长度len
RIGHT(s,n)		LEFT(s,n)
	-- 返回字符串 s 的后 n 个字符
	SELECT RIGHT('runoob',2) -- ob
SUBSTRING_INDEX(s, delimiter, number)	
	-- 返回从字符串 s 的第 number 个出现的分隔符 delimiter 之后的子串。
	-- 如果 number 是正数，返回第 number 个字符左边的字符串。
	-- 如果 number 是负数，返回第(number 的绝对值(从右边数))个字符右边的字符串。
	SELECT SUBSTRING_INDEX('a*b','*',1) -- a
	SELECT SUBSTRING_INDEX('a*b','*',-1)    -- b
	SELECT SUBSTRING_INDEX(SUBSTRING_INDEX('a*b*c*d*e','*',3),'*',-1)    -- c
STRCMP(s1,s2)	
	-- 比较字符串 s1 和 s2，如果 s1 与 s2 相等返回 0 ，如果 s1>s2 返回 1，如果 s1<s2 返回 -1
	
	
FIELD(s,s1,s2...)	
	-- 返回第一个字符串 s 在字符串列表(s1,s2...)中的位置
	SELECT FIELD("c", "a", "b", "c", "d", "e");
LOCATE(s1,s)	
	-- 从字符串 s 中获取 s1 的开始位置
	SELECT LOCATE("c", "a,b,c,d,e");	-- 答案是：5
FIND_IN_SET(s1,s2)
	SELECT FIND_IN_SET("c", "a,b,c,d,e");	-- 答案是：3
POSITION(s1 IN s)	
	-- 从字符串 s 中获取 s1 的开始位置
	SELECT POSITION('b' in 'abc') -- 2
```







## 数值

```sql
ABS(x)	
	-- 返回 x 的绝对值　
SIGN(x)	
	-- 返回 x 的符号，x 是负数、0、正数分别返回 -1、0 和 1
SQRT(x)	
	-- 返回x的平方根　　
POW(x,y)	
	-- 返回 x 的 y 次方　
LOG(x) 或 LOG(base, x)	
	-- 返回自然对数(以 e 为底的对数)，如果带有 base 参数，则 base 为指定带底数。
MOD(x,y)	
	-- 返回 x 除以 y 以后的余数
PI()	
	-- 返回圆周率(3.141593）
LN(x)	
	--返回数字的自然对数，以 e 为底。
	
	
CEIL(x)
FLOOR(X)
ROUND(X)



GREATEST(expr1, expr2, expr3, ...)	
	-- 返回列表中的最大
LEAST(expr1, expr2, expr3, ...)	
	-- 返回列表中的最小值

RAND()	返回 0 到 1 的随机数　　


	
AVG
COUNT
SUM
MAX
MIN
```





## 日期









## 高级函数

```sql
CASE expression
WHEN condition1 THEN result1
WHEN condition2 THEN result2
...
WHEN conditionN THEN resultN
ELSE result
END	

	-- CASE 表示函数开始，END 表示函数结束。
	-- 如果 condition1 成立，则返回 result1, 如果 condition2 成立，则返回 result2，当全部不成立则返回 result
	-- 当有一个成立之后，后面的就不执行了。	
    SELECT CASE 
      WHEN 1 > 0
      THEN '1 > 0'
      WHEN 2 > 0
      THEN '2 > 0'
      ELSE '3 > 0'
      END
        -- 结果：1 > 0



IF(expr,v1,v2)	
	-- 如果表达式 expr 成立，返回结果 v1；否则，返回结果 v2。
    
    SELECT IF(1 > 0,'正确','错误')    
    -- 结果：正确



LAST_INSERT_ID()	
	-- 返回最近生成的 AUTO_INCREMENT 值
IFNULL(v1,v2)	
	-- 如果 v1 的值不为 NULL，则返回 v1，否则返回 v2。
COALESCE(expr1, expr2, ...., expr_n)	
	-- 返回参数中的第一个非空表达式（从左向右）


BIN(x)	
	-- 返回 x 的二进制编码
CONV(x,f1,f2)	
	-- 返回 f1 进制数变成 f2 进制数	
    SELECT CONV(15, 10, 2);	-- 1111
```















## 自定义函数

```sql
'使用函数创建自增序列管理表(批量使用自增表,设置初始值,自增幅度)'

# 第一步：创建Sequence管理表 sequence
DROP TABLE IF EXISTS sequence; 
CREATE TABLE sequence ( 
name VARCHAR(50) NOT NULL, 
current_value INT NOT NULL, 
increment INT NOT NULL DEFAULT 1, 
PRIMARY KEY (name) 
) ENGINE=InnoDB;

# 第二步：创建取当前值的函数 currval
DROP FUNCTION IF EXISTS currval; 
DELIMITER $ 
CREATE FUNCTION currval (seq_name VARCHAR(50)) 
RETURNS INTEGER
LANGUAGE SQL 
DETERMINISTIC 
CONTAINS SQL 
SQL SECURITY DEFINER 
COMMENT ''
BEGIN
DECLARE value INTEGER; 
SET value = 0; 
SELECT current_value INTO value 
FROM sequence
WHERE name = seq_name; 
RETURN value; 
END
$ 
DELIMITER ;

# 第三步：创建取下一个值的函数 nextval
DROP FUNCTION IF EXISTS nextval; 
DELIMITER $ 
CREATE FUNCTION nextval (seq_name VARCHAR(50)) 
RETURNS INTEGER
LANGUAGE SQL 
DETERMINISTIC 
CONTAINS SQL 
SQL SECURITY DEFINER 
COMMENT ''
BEGIN
UPDATE sequence
SET current_value = current_value + increment 
WHERE name = seq_name; 
RETURN currval(seq_name); 
END
$ 
DELIMITER;

# 第四步：创建更新当前值的函数 setval
DROP FUNCTION IF EXISTS setval; 
DELIMITER $ 
CREATE FUNCTION setval (seq_name VARCHAR(50), value INTEGER) 
RETURNS INTEGER
LANGUAGE SQL 
DETERMINISTIC 
CONTAINS SQL 
SQL SECURITY DEFINER 
COMMENT ''
BEGIN
UPDATE sequence
SET current_value = value 
WHERE name = seq_name; 
RETURN currval(seq_name); 
END
$ 
DELIMITER ;

# 测试函数功能
# 当上述四步完成后，可以用以下数据设置需要创建的sequence名称以及设置初始值和获取当前值和下一个值。

INSERT INTO sequence VALUES ('TestSeq', 0, 1);
# ----添加一个sequence名称和初始值，以及自增幅度  添加一个名为TestSeq 的自增序列

SELECT SETVAL('TestSeq', 10);
# ---设置指定sequence的初始值    这里设置TestSeq 的初始值为10

SELECT CURRVAL('TestSeq');  
# --查询指定sequence的当前值   这里是获取TestSeq当前值

SELECT NEXTVAL('TestSeq');  
# --查询指定sequence的下一个值  这里是获取TestSeq下一个值


```

