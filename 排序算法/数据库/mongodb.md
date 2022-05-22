# 概念

| SQL术语/概念 | MongoDB术语/概念 | 解释/说明                           |
| :----------- | :--------------- | :---------------------------------- |
| database     | database         | 数据库                              |
| table        | collection       | 数据库表/集合                       |
| row          | document         | 数据记录行/文档                     |
| column       | field            | 数据字段/域                         |
| index        | index            | 索引                                |
| table joins  |                  | 表连接,MongoDB不支持                |
| primary key  | primary key      | 主键,MongoDB自动将_id字段设置为主键 |



## 文档

```javascript
/*

需要注意的是：

文档中的键/值对是有序的。
文档中的值不仅可以是在双引号里面的字符串，还可以是其他几种数据类型（甚至可以是整个嵌入的文档)。
MongoDB区分类型和大小写。
MongoDB的文档不能有重复的键。
文档的键是字符串。除了少数例外情况，键可以使用任意UTF-8字符。
文档键命名规范：

键不能含有\0 (空字符)。这个字符用来表示键的结尾。
.和$有特别的意义，只有在特定环境下才能使用。
以下划线"_"开头的键是保留的(不是严格要求的)。

*/
```





## 集合

```javascript
它有很高的性能以及队列过期的特性(过期按照插入的顺序). 有点和 "RRD" 概念类似。

Capped collections 是高性能自动的维护对象的插入顺序。

它非常适合类似记录日志的功能和标准的 collection 不同，你必须要显式的创建一个capped collection，指定一个 collection 的大小，单位是字节。

collection 的数据存储空间值提前分配的。


```







## 元数据

| 集合命名空间             | 描述                                      |
| :----------------------- | :---------------------------------------- |
| dbname.system.namespaces | 列出所有名字空间。                        |
| dbname.system.indexes    | 列出所有索引。                            |
| dbname.system.profile    | 包含数据库概要(profile)信息。             |
| dbname.system.users      | 列出所有可访问数据库的用户。              |
| dbname.local.sources     | 包含复制对端（slave）的服务器信息和状态。 |

```javascript

```



## 数据类型

```javascript
/*
ObjectId 类似唯一主键，可以很快的去生成和排序，包含 12 bytes，含义是：

    前 4 个字节表示创建 unix 时间戳,格林尼治时间 UTC 时间，比北京时间晚了 8 个小时
    接下来的 3 个字节是机器标识码
    紧接的两个字节由进程 id 组成 PID
    最后三个字节是随机数
*/

> var newObject = ObjectId()
> newObject.getTimestamp()
// ISODate("2017-11-25T07:21:10Z")

// ObjectId 转为字符串
> newObject.str
// 5a1919e63df83ce79df8b38f


```

| 数据类型           | 描述                                                         |
| :----------------- | :----------------------------------------------------------- |
| String             | 字符串。存储数据常用的数据类型。在 MongoDB 中，UTF-8 编码的字符串才是合法的。 |
| Integer            | 整型数值。用于存储数值。根据你所采用的服务器，可分为 32 位或 64 位。 |
| Boolean            | 布尔值。用于存储布尔值（真/假）。                            |
| Double             | 双精度浮点值。用于存储浮点值。                               |
| Min/Max keys       | 将一个值与 BSON（二进制的 JSON）元素的最低值和最高值相对比。 |
| Array              | 用于将数组或列表或多个值存储为一个键。                       |
| Timestamp          | 时间戳。记录文档修改或添加的具体时间。                       |
| Object             | 用于内嵌文档。                                               |
| Null               | 用于创建空值。                                               |
| Symbol             | 符号。该数据类型基本上等同于字符串类型，但不同的是，它一般用于采用特殊符号类型的语言。 |
| Date               | 日期时间。用 UNIX 时间格式来存储当前日期或时间。你可以指定自己的日期时间：创建 Date 对象，传入年月日信息。 |
| Object ID          | 对象 ID。用于创建文档的 ID。                                 |
| Binary Data        | 二进制数据。用于存储二进制数据。                             |
| Code               | 代码类型。用于在文档中存储 JavaScript 代码。                 |
| Regular expression | 正则表达式类型。用于存储正则表达式。                         |











## 初步

```javascript
/*
admin： 从权限的角度来看，这是"root"数据库。要是将一个用户添加到这个数据库，这个用户自动继承所有数据库的权限。一些特定的服务器端命令也只能从这个数据库运行，比如列出所有的数据库或者关闭服务器。

local: 这个数据永远不会被复制，可以用来存储限于本地单台服务器的任意集合

config: 当Mongo用于分片设置时，config数据库在内部使用，用于保存分片的相关信息。
*/

show dbs

db

use <DateBase>
```





# 详解

https://segmentfault.com/a/1190000039031122

https://docs.mongodb.com/manual/reference/operator/aggregation/

## 设置账号与密码

```javascript
// https://blog.csdn.net/HH_KELE/article/details/105804643
// https://blog.csdn.net/LZW15082682930/article/details/114539265
// https://blog.csdn.net/suprezheng/article/details/116596538


// 1.创建admin管理员用户：专门用来管理账号；不能用来关闭数据库
use admin	// 关键：进入admin数据库
db.createUser({ user: "admin", pwd: "xing1aizhangmingye", roles: [{ role: "userAdminAnyDatabase", db: "admin" }] })

// 2.创建完admin管理员，创建一个超级管理员root。root角色用于关闭数据库
db.createUser({user: "cindiou",pwd: "mongo-054091", roles: [ { role: "root", db: "admin" } ]})


// 3.创建某个数据库自己的账号："dbOwner"代表数据库所有者角色，拥有最高该数据库最高权限。比如新建索引等
use InnerWorld	// 一定要切换到对应的数据库
db.createUser({user: "Mr.yellow",pwd: "ungiven_h",roles: [ { role: "dbOwner", db: "InnerWorld" } ]})

    /* // 例如：
    use test
    db.createUser(
        {
            user: "test",
            pwd: "123",
            roles: [
            {role: "readWrite", db: "test"},  # 针对test库有读写权限，操作自己的库有读写权限
            {role: "read", db: "db1"}
            ]  # 针对db1库读权限,操作其他库有读权限
        }
    )

    */

'参看用户'
	show users
'删除用户'
    // 删除用户必须由账号管理员来删，所以，切换到admin角色
    use admin
    db.auth("admin","password")

    // 删除单个用户
    db.system.users.remove({user:"XXXXXX"})

    // 删除所有用户
    db.system.users.remove({})


 '登入'
    # 方式一
    mongo --port 27017 -u "root" -p "123" --authenticationDatabase "admin"
    # 方式二：在登录之后用db.auth("账号","密码")登录
    mongo
    use admin
    db.auth("root","123")



'重启数据库'
    mongod --remove
    mongod --config "D:\Program Files (x86)\MongoDB\mongodb\bin\mongod.cfg" --bind_ip 0.0.0.0 --install --auth
    
 '对于admin用户，可以直接以下种方式进入'
	mongo -ucindiou -pmongo-054091
'但是出admin之外对于其他用户，如：InnerWorld的Mr.yellow用户，必须指明所在表'
	mongo -uMr.yellow -pungiven_h --authenticationDatabase "InnerWorld"
	
    
```









## 数据库

```javascript
show dbs

// 创建的数据库 runoob 
// 只有向 runoob 数据库插入一些数据，才会开始真正创建
use runoob

// 展示当前所选择的数据库
db

// 创建名为"runoob"的集合
db.createCollection("runoob")

// 向集合runoob中插入数据后
db.runoob.insert({"name":"菜鸟教程"})


// 删除当前正在使用的数据库
db.dropDatabase()

'MongoDB 中默认的数据库为 test，如果你没有创建新的数据库，集合将存放在 test 数据库中。'

'注意: 在 MongoDB 中，集合（表）只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。'

```







### 数据库关系 | $in

```javascript
`
MongoDB 中的关系可以是：

    1:1 (1对1)
    1: N (1对多)
    N: 1 (多对1)
    N: N (多对多)
`

'一个用户可以有多个地址，所以是一对多的关系'
//以下是 user 文档的简单结构：
{
   "_id":ObjectId("52ffc33cd85242f436000001"),
   "name": "Tom Hanks",
   "contact": "987654321",
   "dob": "01-01-1991"
}

//以下是 address 文档的简单结构：
{
   "_id":ObjectId("52ffc4a5d85242602e000000"),
   "building": "22 A, Indiana Apt",
   "pincode": 123456,
   "city": "Los Angeles",
   "state": "California"
} 
```



#### 嵌入式关系

```javascript
//嵌入式关系
使用嵌入式方法，我们可以把用户地址嵌入到用户的文档中：
	// db.users.findOne({"name":"Tom Benzamin"},{"address":1})
'缺点是，如果用户和用户地址在不断增加，数据量不断变大，会影响读写性能。'

{
   "_id":ObjectId("52ffc33cd85242f436000001"),
   "contact": "987654321",
   "dob": "01-01-1991",
   "name": "Tom Benzamin",
   "address": [
      {
         "building": "22 A, Indiana Apt",
         "pincode": 123456,
         "city": "Los Angeles",
         "state": "California"
      },
      {
         "building": "170 A, Acropolis Apt",
         "pincode": 456789,
         "city": "Chicago",
         "state": "Illinois"
      }]
} 
```





#### 引入式关系

```javascript
'把用户数据文档和用户地址数据文档分开，通过引用文档的 id 字段来建立关系'
'用户文档的 address_ids 字段包含用户地址的对象id（ObjectId）数组'
var result = db.users.findOne({"name":"Tom Benzamin"},{"address_ids":1})
var addresses = db.address.find({"_id":{"$in":result["address_ids"]}})
	//查找 "_id" 在 result["address_ids"]数组的项


{
   "_id":ObjectId("52ffc33cd85242f436000001"),
   "contact": "987654321",
   "dob": "01-01-1991",
   "name": "Tom Benzamin",
   "address_ids": [
      ObjectId("52ffc4a5d85242602e000000"),
      ObjectId("52ffc4a5d85242602e000001")
   ]
}
```





##### 注意事项

```javascript
var result = db.users.findOne({"name":"Tom Benzamin"},{"address_ids":1})
注意这一句中的 findOne 不能写成 find，因为 find 返回的数据类型是'数组'，findOne 返回的数据类型是'对象'。

如果这一句使用了 find，那么下面一句应该改写为:

var addresses = db.address.find({"_id":{"$in":result[0]["address_ids"]}})
```





#### DBRefs引用

```javascript
`
{ $ref : , $id : , $db :  }
三个字段表示的意义为：

    $ref：集合名称
    $id：引用的id
    $db:数据库名称，可选参数
`
'不推荐采用DBRefs引用，使用手动引用更合适'
'链接：https://www.compose.com/articles/mongodb-and-the-trouble-with-dbrefs/'


{
   "_id":ObjectId("53402597d852426020000002"),
   "address": {
   "$ref": "address_home",
   "$id": ObjectId("534009e4d852427820000002"),
   "$db": "runoob"},
   "contact": "987654321",
   "dob": "01-01-1991",
   "name": "Tom Benzamin"
}


>var user = db.users.findOne({"name":"Tom Benzamin"})
>var dbRef = user.address
>db[dbRef.$ref].findOne({"_id":(dbRef.$id)})
// 在 MongoDB4.0 版本是这样写：
>db[dbRef.$ref].findOne({"_id":ObjectId(dbRef.$id)})
```













## 集合

| 字段        | 类型 | 描述                                                         |
| :---------- | :--- | :----------------------------------------------------------- |
| capped      | 布尔 | （可选）如果为 true，则创建固定集合。固定集合是指有着固定大小的集合，当达到最大值时，它会自动覆盖最早的文档。 **当该值为 true 时，必须指定 size 参数。** |
| autoIndexId | 布尔 | 3.2 之后不再支持该参数。（可选）如为 true，自动在 _id 字段创建索引。默认为 false。 |
| size        | 数值 | （可选）为固定集合指定一个最大值，即字节数。 **如果 capped 为 true，也需要指定该字段。** |
| max         | 数值 | （可选）指定固定集合中包含文档的最大数量。                   |

```javascript
`
db.createCollection(name, options)
    name: 要创建的集合名称
    options: 可选参数, 指定有关内存大小及索引的选项
`

// 先确定在哪个数据库中创建集合
use runnob

// 创建名为"runoob"的集合
db.createCollection("runoob")

show tables	// 等价于：show collections

// 删除数据库runoob下集合runoob
db.runoob.drop()
```







### 固定集合

```javascript
'固定集合（Capped Collections）是性能出色且有着固定大小的集合'
'当集合空间用完后，再插入的元素就会覆盖最初始的头部的元素'
'可以插入及更新,但更新不能超出collection的大小,否则更新失败; 不允许删除'

// size单位字节，size与max同时起作用，只要一方满足就说明集合已满
db.createCollection("cappedLogCollection",{capped:true,size:10000,max:1000})
// 判断集合是否是固定集合
db.collection_name.isCapped()

//将集合posts转换成固定集合,注意：此时再添加max字段将毫无作用
db.runCommand({"convertToCapped":"posts",size:10000})

// 按照插入顺序返回
db.collection_name.find().sort({$natural:-1})




```







### 自动增长

```javascript

// 1.第一步：建立变量存储表
// 为此，创建 counters 集合，序列字段值可以实现自动长：
db.createCollection("counters")
db.counters.insert({_id:"productid",sequence_value:0})

// 2.第二步：创建 Javascript 函数
// 借用counter表中存储的数据，实现递增
>function getNextSequenceValue(sequenceName){
   var sequenceDocument = db.counters.findAndModify(
      {
         query:{_id: sequenceName },
         update: {$inc:{sequence_value:1}},
         "new":true
      });
   return sequenceDocument.sequence_value;
}

// 3.第三步：使用 Javascript 函数
>db.products.insert({
   "_id":getNextSequenceValue("productid"),
   "product_name":"Apple iPhone",
   "category":"mobiles"})

>db.products.insert({
   "_id":getNextSequenceValue("productid"),
   "product_name":"Samsung S3",
   "category":"mobiles"})
```











## 文档

```javascript
`
文档的数据结构和 JSON 基本一样。
所有存储在集合中的数据都是 BSON 格式。
BSON 是一种类似 JSON 的二进制形式的存储格式，是 Binary JSON 的简称。


```



### 插入

```javascript
# 插入
    db.COLLECTION_NAME.insert(document)
    或
    db.COLLECTION_NAME.save(document)

    save()：如果 _id 主键存在则更新数据，如果不存在就插入数据。
	// 该方法新版本中已废弃，可以使用 db.collection.insertOne() 或 db.collection.replaceOne() 来代替。
    db.col.save({ // 替换了 _id 为 56064f89ade2f21f36b03136 的文档数据
        "_id" : ObjectId("56064f89ade2f21f36b03136"),
        "title" : "MongoDB",
        "description" : "MongoDB 是一个 Nosql 数据库",
        "by" : "Runoob",
        "url" : "http://www.runoob.com",
        "tags" : [
                "mongodb",
                "NoSQL"
        ],
        "likes" : 110
    })
    

    insert(): 若插入的数据主键已经存在，则会抛 org.springframework.dao.DuplicateKeyException 异常，提示主键重复，不保存当前数据。
	// 该方法等价于 insertOne() 和 insertMany()
    db.collection.insertMany(
       [ <document 1> , <document 2>, ... ],
       {
          writeConcern: <document>,	// 写入策略，默认为 1，即要求确认写操作，0 是不要求。
          ordered: <boolean>		// 指定是否按顺序写入，默认 true，按顺序写入。
       }
    )
```







### 更新

```javascript
# 更新
    db.collection.update(
       <query>,	//  update的查询条件，类似sql update查询内where后面的。
       <update>, // : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
       {
         upsert: <boolean>, // 如果不存在update的记录，是否插入objNew,true为插入;默认是false，不插入。
         multi: <boolean>, // mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新
         writeConcern: <document> // 抛出异常的级别
       }
    )
    'multi参数导致的区别'
        // db.collection.updateOne() 向指定集合更新单个文档
        // db.collection.updateMany() 向指定集合更新多个文档
    
    db.col.update({'title':'MongoDB 教程'},{$set:{'title':'MongoDB'}})

	// 全部更新：
	db.col.update( { "count" : { $gt : 3 } } , { $set : { "test2" : "OK"} },false,true );

	// 只添加第一条：
	db.col.update( { "count" : { $gt : 4 } } , { $set : { "test5" : "OK"} },true,false );

	// 移除集合中的键值对，使用的 $unset 操作符：
	// 如果指定的字段不存在则操作不做任何处理
	db.col.update({"_id":"56064f89ade2f21f36b03136"}, {$unset:{ "test2" : "OK"}})


	// $setOnInsert,数据存在时不进行操作：
	db.collection.update({'title':'MongoDB 教程'}, {$setOnInsert: {'title':'MongoDB'}})

	// 数据存在时更新，数据不存在时插入
	db.collection.update({'title':'MongoDB 教程'}, {$set: {'title':'MongoDB'}},{upsert:true})
```







### 删除

```javascript
# 删除
db.collection.remove(
   <query>,		// （可选）删除的文档的条件。
   <justOne>	// 如果设为 true 或 1，则只删除一个文档;如果不设置该参数，或使用默认值 false，则删除所有匹配条件的文档
)

	// 想删除所有数据，可以使用以下方式（类似常规 SQL 的 truncate 命令）：
	db.col.remove({})

    // 如删除集合下全部文档：
    db.inventory.deleteMany({})

    // 删除 status 等于 A 的全部文档：
    db.inventory.deleteMany({ status : "A" })

    // 删除 status 等于 D 的一个文档：
    db.inventory.deleteOne( { status: "D" } )
```









### 查询

```javascript
# 查询

// 还有一个 findOne() 方法，它只返回一个文档。
db.collection.find(query, projection)
    // query ：可选，使用查询操作符指定查询条件
    // projection ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。


	// 易读的方式来读取数据，可以使用 pretty() 方法，语法格式如下：
	db.col.find().pretty()

	// qty 大于 50 小于 80
	db.posts.find( {  qty: { $gt: 50 ,$lt: 80}} )

	// 注：_id(主键)字段默认为 1，可指定 {_id:0} 来不输出 _id 字段值。
		_id 键默认返回，需要主动指定 _id:0 才会隐藏
	// 如：{title:1}，表示查询出的每条记录中只显示 title 字段内容。
	// {by:0}，表示查询出的每条记录中不显示 by 字段内容(其他字段都展示)。
	db.collection.find(query, {title: 1, by: 1}) // inclusion模式 指定返回的键，不返回其他键
	db.collection.find(query, {title: 0, by: 0}) // exclusion模式 指定不返回的键,返回其他键
	db.collection.find(query, {_id:0, title: 1, by: 1}) // 正确


// AND条件
	db.col.find({key1:value1, key2:value2}).pretty()

//OR条件
    db.col.find(
       {
          $or: [
             {key1: value1}, {key2:value2}
          ]
       }
    ).pretty()


// AND 和 OR 联合使用
	db.col.find({"likes": {$gt:50}, $or: [{"by": "菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()
```





| 操作       | 格式                     | 范例                                        | RDBMS中的类似语句       |
| :--------- | :----------------------- | :------------------------------------------ | :---------------------- |
| 等于       | `{<key>:<value>`}        | `db.col.find({"by":"菜鸟教程"}).pretty()`   | `where by = '菜鸟教程'` |
| 小于       | `{<key>:{$lt:<value>}}`  | `db.col.find({"likes":{$lt:50}}).pretty()`  | `where likes < 50`      |
| 小于或等于 | `{<key>:{$lte:<value>}}` | `db.col.find({"likes":{$lte:50}}).pretty()` | `where likes <= 50`     |
| 大于       | `{<key>:{$gt:<value>}}`  | `db.col.find({"likes":{$gt:50}}).pretty()`  | `where likes > 50`      |
| 大于或等于 | `{<key>:{$gte:<value>}}` | `db.col.find({"likes":{$gte:50}}).pretty()` | `where likes >= 50`     |
| 不等于     | `{<key>:{$ne:<value>}}`  | `db.col.find({"likes":{$ne:50}}).pretty()`  | `where likes != 50`     |





## 索引

```javascript
`
索引通常能够极大的提高查询的效率，如果没有索引，MongoDB在读取数据时必须扫描集合中的每个文件并选取那些符合查询条件的记录。

这种扫描全集合的查询效率是非常低的，特别在处理大量的数据时，查询可以要花费几十秒甚至几分钟，这对网站的性能是非常致命的。

索引是特殊的数据结构，索引存储在一个易于遍历读取的数据集合中，索引是对数据库表中一列或多列的值进行排序的一种结构
`
db.collection_name.createIndex(keys, options)
	// 1 为指定按升序创建索引，如果你想按降序来创建索引指定为 -1 即可
	db.col.createIndex({"title":1,"description":-1})

	// 加 background:true 的选项，让创建工作在后台执行
	db.values.createIndex({open: 1, close: 1}, {background: true})


// 1、查看集合索引
db.col.getIndexes()

// 2、查看集合索引大小
db.col.totalIndexSize()

// 3、删除集合所有索引
db.col.dropIndexes()

// 4、删除集合指定索引
db.col.dropIndex("索引名称")
```

| Parameter          | Type          | Description                                                  |
| :----------------- | :------------ | :----------------------------------------------------------- |
| background         | Boolean       | 建索引过程会阻塞其它数据库操作，background可指定以后台方式创建索引，即增加 "background" 可选参数。 "background" 默认值为**false**。 |
| unique             | Boolean       | 建立的索引是否唯一。指定为true创建唯一索引。默认值为**false**. |
| name               | string        | 索引的名称。如果未指定，MongoDB的通过连接索引的字段名和排序顺序生成一个索引名称。 |
| dropDups           | Boolean       | **3.0+版本已废弃。**在建立唯一索引时是否删除重复记录,指定 true 创建唯一索引。默认值为 **false**. |
| sparse             | Boolean       | 对文档中不存在的字段数据不启用索引；这个参数需要特别注意，如果设置为true的话，在索引字段中不会查询出不包含对应字段的文档.。默认值为 **false**. |
| expireAfterSeconds | integer       | 指定一个以秒为单位的数值，完成 TTL设定，设定集合的生存时间。 |
| v                  | index version | 索引的版本号。默认的索引版本取决于mongod创建索引时运行的版本。 |
| weights            | document      | 索引权重值，数值在 1 到 99,999 之间，表示该索引相对于其他索引字段的得分权重。 |
| default_language   | string        | 对于文本索引，该参数决定了停用词及词干和词器的规则的列表。 默认为英语 |
| language_override  | string        | 对于文本索引，该参数指定了包含在文档中的字段名，语言覆盖默认的language，默认值为 language. |



### 定时删除

```javascript
利用 TTL 集合对存储的数据进行失效时间设置：经过指定的时间段后或在指定的时间点过期，MongoDB 独立线程去清除数据。类似于'设置定时自动删除任务'，可以清除历史记录或日志等前提条件，设置 Index 的关键字段为'日期类型' new Date()。

例如数据记录中 createDate 为日期类型时：

 设置时间180秒后自动清除。
 // 设置在创建记录后，180 秒左右删除。
db.col.createIndex({"createDate": 1},{expireAfterSeconds: 180})

由记录中设定'日期点'清除。
// 设置 A 记录在 2019 年 1 月 22 日晚上 11 点左右删除，A 记录中需添加 "ClearUpDate": new Date('Jan 22, 2019 23:00:00')，且 Index中expireAfterSeconds 设值为 0。
db.col.createIndex({"ClearUpDate": 1},{expireAfterSeconds: 0})

其他注意事项:
     索引关键字段'必须'是 Date 类型。
     '非立即执行'：扫描 Document 过期数据并删除是独立线程执行，默认 60s 扫描一次，删除也不一定是立即删除成功。
     单字段索引，混合索引不支持。
```







### 覆盖查询

```javascript
`
覆盖查询是以下的查询：
    所有的查询字段是索引的一部分
    所有的查询返回字段在同一个索引中

因为索引存在于RAM中，从索引中获取数据比通过扫描文档读取数据要快得多
`

// ensureIndex 等价于 createIndex
db.users.ensureIndex({gender:1,user_name:1})

// gender、user_name都属于 所建立的索引字段
// 也就是说，对于上述查询，MongoDB的不会去数据库文件中查找。相反，它会从索引中提取数据，这是非常快速的数据查询。
db.users.find({gender:"M"},{user_name:1,_id:0})


'索引字段必须是简单数据类型'
如果是以下的查询，'不能'使用覆盖索引查询：
    所有索引字段是一个数组
    所有索引字段是一个子文档
```





### 查询分析

```javascript
// 准备
db.users.ensureIndex({gender:1,user_name:1})

// explain 操作提供了查询信息，使用索引及查询统计等。有利于我们对索引的优化。
db.users.find({gender:"M"},{user_name:1,_id:0}).explain()


{
   "cursor" : "BtreeCursor gender_1_user_name_1",
   "isMultiKey" : false,
   "n" : 1,
   "nscannedObjects" : 0,
   "nscanned" : 1,
   "nscannedObjectsAllPlans" : 0,
   "nscannedAllPlans" : 1,
   "scanAndOrder" : false,
   "indexOnly" : true,
   "nYields" : 0,
   "nChunkSkips" : 0,
   "millis" : 0,
   "indexBounds" : {
      "gender" : [
         [
            "M",
            "M"
         ]
      ],
      "user_name" : [
         [
            {
               "$minElement" : 1
            },
            {
               "$maxElement" : 1
            }
         ]
      ]
   }
}

现在，我们看看这个结果集的字段：

    // indexOnly: 字段为 true ，表示我们使用了索引。
    cursor：因为这个查询使用了索引，MongoDB 中索引存储在B树结构中，所以这是也使用了 BtreeCursor 类型的游标。如果没有使用索引，游标的类型是 BasicCursor。这个键还会给出你所使用的索引的名称，你通过这个名称可以查看当前数据库下的system.indexes集合（系统自动创建，由于存储索引信息，这个稍微会提到）来得到索引的详细信息。
    // n：当前查询返回的文档数量。
    nscanned/nscannedObjects：表明当前这次查询一共扫描了集合中多少个文档，我们的目的是，让这个数值和返回文档的数量越接近越好。
    // millis：当前查询所需时间，毫秒数。
    indexBounds：当前查询具体使用的索引
```









### 高级索引

```javascript
{
   "address": {
      "city": "Los Angeles",
      "state": "California",
      "pincode": "123"
   },
   "tags": [
      "music",
      "cricket",
      "blogs"
   ],
   "name": "Tom Benzamin"
}


'索引数组字段'
//在数组中创建索引，需要对数组中的每个字段依次建立索引。所以在我们为数组 tags 创建索引时，会为 music、cricket、blogs三个值建立单独的索引。
    使用以下命令创建数组索引：
    >db.users.ensureIndex({"tags":1})


    创建索引后，我们可以这样检索集合的 tags 字段：
    >db.users.find({tags:"cricket"})


'索引子文档字段'
//假设我们需要通过city、state、pincode字段来检索文档，由于这些字段是子文档的字段，所以我们需要对子文档建立索引。
    >db.users.ensureIndex({"address.city":1,"address.state":1,"address.pincode":1})

    一旦创建索引，我们可以使用子文档的字段来检索数据：
    >db.users.find({"address.city":"Los Angeles"})   

```







### 索引限制

```javascript
每个索引占据一定的存储空间，在进行插入，更新和删除操作时也需要对索引进行操作。
// 所以，如果你很少对集合进行读取操作，建议不使用索引。

查询限制
    索引不能被以下的查询使用：
        正则表达式及非操作符，如 $nin, $not, 等。
        算术运算符，如 $mod, 等。
        $where 子句
        
      
最大范围
    集合中索引不能超过64个
    索引名的长度不能超过128个字符
    一个复合索引最多可以有31个字段        



```







### 全文搜索

```javascript
'对每一个词建立一个索引，指明该词在文章中出现的次数和位置'
'当用户查询时，检索程序就根据事先建立的索引进行查找，并将查找的结果反馈给用户的检索方式。'

启用全文检索
	//  在 2.6 版本以后是默认开启全文检索的
	>db.adminCommand({setParameter:true,textSearchEnabled:true})

	//或者使用命令：
	mongod --setParameter textSearchEnabled=true


创建全文索引
	db.posts.ensureIndex({post_text:"text"})

    {
       "post_text": "enjoy the mongodb articles on Runoob",
       "tags": [
          "mongodb",
          "runoob"
       ]
    }

使用全文索引
	db.posts.find({$text:{$search:"runoob"}})


删除全文索引
	// 第一步：使用 find 命令查找索引名：
	>db.posts.getIndexes()

	// 第二步：通过以上命令获取索引名后，执行以下命令来删除索引（本例的索引名为post_text_text）
	>db.posts.dropIndex("post_text_text")
```











## 聚合 | !!!

### 管道

```javascript
db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)

'在一个管道处理完毕后将结果传递给下一个管道处理。管道操作是可以重复的'
'表达式：处理输入文档并输出。表达式是无状态的，只能用于计算当前聚合管道的文档，不能处理其它的文档。'
`
$project：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。
$match：用于过滤数据，只输出符合条件的文档。$match使用MongoDB的标准查询操作。
$group：将集合中的文档分组，可用于统计结果。

$limit：用来限制MongoDB聚合管道返回的文档数。
$skip：在聚合管道中跳过指定数量的文档，并返回余下的文档。
$sort：将输入文档排序后输出。

$unwind：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
$geoNear：输出接近某一地理位置的有序文档。
`

// $project
db.article.aggregate(
    { $project : { // 只显示_id ,title,author三个字段
        title : 1 ,
        author : 1 ,
    }}
 );


// $match,$group
'注意管道流的处理顺序'
db.articles.aggregate( [	// 获取分数大于70小于或等于90记录条数
                        { $match : { score : { $gt : 70, $lte : 90 } } },
                        { $group: { _id: null, count: { $sum: 1 } } }
                       ] );

```





#### 案列 | !!!

```javascript
按日、按月、按年、按周、按小时、按分钟聚合操作如下：
// 1.取出m_id=10001,且mark_time>new Date(2017,8,0)
// 2.在上面基础上，将日期分化成 单天序列1-31,并计数
// 3.在以上基础上，再进行排序
db.getCollection('m_msg_tb').aggregate(
[
    {$match:{m_id:10001,mark_time:{$gt:new Date(2017,8,0)}}},
    {$group: {
       _id: {$dayOfMonth:'$mark_time'},
        pv: {$sum: 1}
        }
    },
    {$sort: {"_id": 1}}
])


`
时间关键字如下：

     $dayOfYear: 返回该日期是这一年的第几天（全年 366 天）。
     $dayOfMonth: 返回该日期是这一个月的第几天（1到31）。
     $dayOfWeek: 返回的是这个周的星期几（1：星期日，7：星期六）。
     $year: 返回该日期的年份部分。
     $month： 返回该日期的月份部分（ 1 到 12）。
     $week： 返回该日期是所在年的第几个星期（ 0 到 53）。
     $hour： 返回该日期的小时部分。
     $minute: 返回该日期的分钟部分。
     $second: 返回该日期的秒部分（以0到59之间的数字形式返回日期的第二部分，但可以是60来计算闰秒）。
     $millisecond：返回该日期的毫秒部分（ 0 到 999）。
     $dateToString： { $dateToString: { format: , date: } }。
`
```









### 分组

```javascript
// 等价于：select by_user as _id, count(*) as num_tutorial from mycol group by by_user
> db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : 1}}}])
{
   "result" : [
      {
         "_id" : "runoob.com",
         "num_tutorial" : 2
      },
      {
         "_id" : "Neo4j",
         "num_tutorial" : 1
      }
   ],
   "ok" : 1
}
>


```



| 表达式    | 描述                                                         | 实例                                                         |
| :-------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| $sum      | 计算总和。                                                   | db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : "$likes"}}}]) |
| $avg      | 计算平均值                                                   | db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$avg : "$likes"}}}]) |
| $min      | 获取集合中所有文档对应值得最小值。                           | db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$min : "$likes"}}}]) |
| $max      | 获取集合中所有文档对应值得最大值。                           | db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$max : "$likes"}}}]) |
| $push     | 将值加入一个数组中，不会判断是否有重复的值。                 | db.mycol.aggregate([{$group : {_id : "$by_user", url : {$push: "$url"}}}]) |
| $addToSet | 将值加入一个数组中，会判断是否有重复的值，若相同的值在数组中已经存在了，则不加入。 | db.mycol.aggregate([{$group : {_id : "$by_user", url : {$addToSet : "$url"}}}]) |
| $first    | 根据资源文档的排序获取第一个文档数据。                       | db.mycol.aggregate([{$group : {_id : "$by_user", first_url : {$first : "$url"}}}]) |
| $last     | 根据资源文档的排序获取最后一个文档数据                       | db.mycol.aggregate([{$group : {_id : "$by_user", last_url : {$last : "$url"}}}]) |













## 查询方式

### 原子操作 | findAndModify

```javascript
'原子操作就是要么这个文档保存到Mongodb，要么没有保存到Mongodb，不会出现查询到的文档没有保存完整的情况'


db.books.findAndModify ( {
   query: {
            _id: 123456789,
            available: { $gt: 0 }
          },
   update: {
             $inc: { available: -1 },
             $push: { checkout: { by: "abc", date: new Date() } }
           }
} )


// 位操作
{$bit : { field : {and | or | xor: 5}}}

// 修改字段名称
{ $rename : { old_field_name : new_field_name } }

// 数组相关
{ $pop : { field : 1 } } // 1表示删除第一个，-1表示最后一个

{ $pull : { field : _value } } // 删除一个等于value值。

{ $push : { field : value } }
{ $pushAll : { field : value_array } }


$addToSet	// 增加一个值到数组内，而且只有当这个值不在数组内才增加。
```







### 其他操作符 | !!!

```javascript
'参考链接'
'https://docs.mongodb.com/manual/reference/operator/query/'

// exists
// type
// set	unset

// bit
// bitAllClear	bitAllSet
// bitAnyClear	bitAnySet

// in	nin	  size
// pop  pull
// push	pushAll	addToSet

// eq   ne	  lt	gt	lte		gte

// not  and	  or
// nor
	// 指一下情况，1.任一一字段不存在；2.字段都存在、但都不满足条件
	db.inventory.find( { $nor: [ { price: 1.99 }, { sale: true } ]  } )


// inc	mod	  mul	div


// $regexp	$options



// $text	$search




查询出age为奇数的数据(对2求余为1即为奇数) $mod
db.student.find({age:{$mod:[2,1]}})

查询出存在opt字段的数据 $exists
db.student.find({opt:{$exists:true}})

查询出不存在opt字段的数据
db.student.find({opt:{$exists:false}})

查询出name不为little2的数据 $ne
db.student.find({name:{$ne:"little2"}})

查询出age为16，18，19的数据 $in
db.student.find({age:{$in:[16,18,19]}})

查询出age不为16，18，19的数据 $nin
db.student.find({age:{$nin:[16,18,19]}})

查询出love有三个的数据 $size
db.student.find({love:{$size:3}})

查询出name不是以litt开头的数据 $not $regex
db.student.find({name:{$not:/^litt.*/}})
```



#### $expr

```javascript
{ $expr: { <expression> } }
'允许在查询语句中使用聚合表达式'
'创建查询表达式，能比较同一文档中不同字段'
'聚合表达式定义：https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#std-label-aggregation-expressions'
 
 
 
 '案列一'
 // 表结构
{ "_id" : 1, "category" : "food", "budget": 400, "spent": 450 }
{ "_id" : 2, "category" : "drinks", "budget": 100, "spent": 150 }
{ "_id" : 3, "category" : "clothes", "budget": 100, "spent": 50 }
{ "_id" : 4, "category" : "misc", "budget": 500, "spent": 300 }
{ "_id" : 5, "category" : "travel", "budget": 200, "spent": 650 }
 
 // 查询 字段spend > 字段budget 的文档
db.monthlyBudget.find( { $expr: { $gt: [ "$spent" , "$budget" ] } } )
 
 
 
 
'案列二'
 // 表结构
 db.supplies.insertMany([
   { "_id" : 1, "item" : "binder", "qty" : NumberInt("100"), "price" : NumberDecimal("12") },
   { "_id" : 2, "item" : "notebook", "qty" : NumberInt("200"), "price" : NumberDecimal("8") },
   { "_id" : 3, "item" : "pencil", "qty" : NumberInt("50"), "price" : NumberDecimal("6") },
   { "_id" : 4, "item" : "eraser", "qty" : NumberInt("150"), "price" : NumberDecimal("3") },
   { "_id" : 5, "item" : "legal pad", "qty" : NumberInt("42"), "price" : NumberDecimal("10") }
])
 
 
 
 // 查询打折后价格小于5的文档；打折后的价格根据qty字段是否小于100决定
 let discountedPrice = {
   $cond: {
      if: { $gte: ["$qty", 100] },
      then: { $multiply: ["$price", NumberDecimal("0.50")] },
      else: { $multiply: ["$price", NumberDecimal("0.75")] }
   }
};
 db.supplies.find( { $expr: { $lt:[ discountedPrice,  NumberDecimal("5") ] } });
 
```





#### $jsonSchema

```javascript
// https://docs.mongodb.com/manual/reference/operator/query/jsonSchema/#mongodb-query-op.-jsonSchema
// 创建时约束表结构 或 操作特定的文档结构
db.createCollection( <collection>, { validator: { $jsonSchema: <schema> } } )

db.collection.find( { $jsonSchema: <schema> } )
db.collection.aggregate( [ { $match: { $jsonSchema: <schema> } } ] )
db.collection.updateMany( { $jsonSchema: <schema> }, <update> )
db.collection.deleteOne( { $jsonSchema: <schema> } )
                          
                          
                          
db.createCollection("students", {
   validator: {
      $jsonSchema: {
         bsonType: "object",// 类型约束
		// 必须具备的字段名称                    
         required: [ "name", "year", "major", "address" ],
         properties: {//全部的字段名称
            name: {
               bsonType: "string",
               description: "must be a string and is required"
            },
            year: {
               bsonType: "int",
               minimum: 2017,// 取值范围
               maximum: 3017,
               description: "must be an integer in [ 2017, 3017 ] and is required"
            },
            major: {
                // 枚举
               enum: [ "Math", "English", "Computer Science", "History", null ],
               description: "can only be one of the enum values and is required"
            },
            gpa: {
               bsonType: [ "double" ],
               description: "must be a double if the field exists"
            },
            address: {
               bsonType: "object",
               required: [ "city" ],
               properties: {
                  street: {
                     bsonType: "string",
                     description: "must be a string if the field exists"
                  },
                  city: {
                     bsonType: "string",
                     "description": "must be a string and is required"
                  }
               }
            }
         }
      }
   }
} )



let myschema =  {
      required: [ "item", "qty", "instock" ],
      properties: {
         item: { bsonType: "string" },
         qty: { bsonType: "int" },
         size: {
            bsonType: "object",
            required: [ "uom" ],
            properties: {
               uom: { bsonType: "string" },
               h: { bsonType: "double" },
               w: { bsonType: "double" }
            }
          },
          instock: { bsonType: "bool" }
      }
 }
```





#### $elemMatch

```javascript
// 数组中的元素满足
`
具有两种用法：find(<1>,<2>)
	1.在查询字段中使用，如:<1>;筛选符合的文档
	2.在影射字段中使用,如:<2>；对文档中的某些字段进行过滤
`


'案列一'
{ _id: 1, results: [ 82, 85, 88 ] }
{ _id: 2, results: [ 75, 88, 89 ] }


db.scores.find(
   { results: { $elemMatch: { $gte: 80, $lt: 85 } } }
)



'案列二'
db.survey.insertMany( [
   { "_id": 1, "results": [ { "product": "abc", "score": 10 },
                            { "product": "xyz", "score": 5 } ] },
   { "_id": 2, "results": [ { "product": "abc", "score": 8 },
                            { "product": "xyz", "score": 7 } ] },
   { "_id": 3, "results": [ { "product": "abc", "score": 7 },
                            { "product": "xyz", "score": 8 } ] },
   { "_id": 4, "results": [ { "product": "abc", "score": 7 },
                            { "product": "def", "score": 8 } ] }
] )


db.survey.find(
   { results: { $elemMatch: { product: "xyz", score: { $gte: 8 } } } }
)


'案列三：注意区别'
// results中的存在元素product字段都不等于"xyz"
db.survey.find(
   { "results": { $elemMatch: { product: { $ne: "xyz" } } } }
)

// results中的任意元素product字段都不等于"xyz"
db.survey.find(
   { "results.product": { $ne: "xyz" } }
)
```





#### $all

```javascript
// tags数组中元素同时具有"ssl"、"security"
{ tags: { $all: [ "ssl" , "security" ] } }
// 等价于
{ $and: [ { tags: "ssl" }, { tags: "security" } ] }



db.inventory.find( {
                     qty: { $all: [
                                    { "$elemMatch" : { size: "M", num: { $gt: 50} } },
                                    { "$elemMatch" : { num : 100, color: "green" } }
                                  ] }
                   } )

// 查询出结果
{
   "_id" : ObjectId("5234ccb7687ea597eabee677"),
   "code" : "efg",
   "tags" : [ "school", "book"],
   "qty" : [
             { "size" : "S", "num" : 10, "color" : "blue" },
             { "size" : "M", "num" : 100, "color" : "blue" },
             { "size" : "L", "num" : 100, "color" : "green" }
           ]
}
{
   "_id" : ObjectId("52350353b2eff1353b349de9"),
   "code" : "ijk",
   "tags" : [ "electronics", "school" ],
   "qty" : [
             { "size" : "M", "num" : 100, "color" : "green" }
           ]
}
```





#### 映射操作



##### $

```javascript
// 映射后的数组下的元素取 几 个


'案列一'
{ "_id" : 1, "semester" : 1, "grades" : [ 70, 87, 90 ] }
{ "_id" : 2, "semester" : 1, "grades" : [ 90, 88, 92 ] }
{ "_id" : 3, "semester" : 1, "grades" : [ 85, 100, 90 ] }
{ "_id" : 4, "semester" : 2, "grades" : [ 79, 85, 80 ] }
{ "_id" : 5, "semester" : 2, "grades" : [ 88, 88, 92 ] }
{ "_id" : 6, "semester" : 2, "grades" : [ 95, 90, 96 ] }

db.students.find( { semester: 1, grades: { $gte: 85 } },
                  { "grades.$": 1 } )

//结果
{ "_id" : 1, "grades" : [ 87 ] }
{ "_id" : 2, "grades" : [ 90 ] }
{ "_id" : 3, "grades" : [ 85 ] }



'案列二'
{ "_id" : 7, semester: 3, "grades" : [ { grade: 80, mean: 75, std: 8 },
                                       { grade: 85, mean: 90, std: 5 },
                                       { grade: 90, mean: 85, std: 3 } ] }
{ "_id" : 8, semester: 3, "grades" : [ { grade: 92, mean: 88, std: 8 },
                                       { grade: 78, mean: 90, std: 5 },
                                       { grade: 88, mean: 85, std: 3 } ] }

db.students.find(
   { "grades.mean": { $gt: 70 } },
   { "grades.$": 1 }
)

//结果
{ "_id" : 7, "grades" : [  {  "grade" : 80,  "mean" : 75,  "std" : 8 } ] }
{ "_id" : 8, "grades" : [  {  "grade" : 92,  "mean" : 88,  "std" : 8 } ] }
```





##### $elemMatch

```javascript
'文档映射：对筛选后的文档再进行挑选，只返回其中一部分字段'
'$与$elementMatch都是返回数组中符合的第一个元素'

'案列一'
db.players.insertOne( {
   name: "player1",
   games: [ { game: "abc", score: 8 }, { game: "xyz", score: 5 } ],
   joined: new Date("2020-01-01"),
   lastLogin: new Date("2020-05-01")
} )

db.players.find( {}, 
                { games: { $elemMatch: { score: { $gt: 5 } } }, 
                 joined: 1, 
                 lastLogin: 1 
                } 
 )

// 结果
{
   "_id" : ObjectId("5edef64a1c099fff6b033977"),
   "joined" : ISODate("2020-01-01T00:00:00Z"),
   "lastLogin" : ISODate("2020-05-01T00:00:00Z"),
   "games" : [ { "game" : "abc", "score" : 8 } ]
}





'案列二'
{
 _id: 1,
 zipcode: "63109",
 students: [
              { name: "john", school: 102, age: 10 },
              { name: "jess", school: 102, age: 11 },
              { name: "jeff", school: 108, age: 15 }
           ]
}
{
 _id: 2,
 zipcode: "63110",
 students: [
              { name: "ajax", school: 100, age: 7 },
              { name: "achilles", school: 100, age: 8 },
           ]
}
{
 _id: 3,
 zipcode: "63109",
 students: [
              { name: "ajax", school: 100, age: 7 },
              { name: "achilles", school: 100, age: 8 },
           ]
}
{
 _id: 4,
 zipcode: "63109",
 students: [
              { name: "barney", school: 102, age: 7 },
              { name: "ruth", school: 102, age: 16 },
           ]
}



db.schools.find( { zipcode: "63109" },
                 { students: { $elemMatch: { school: 102, age: { $gt: 10} } } } )


{ "_id" : 1, "students" : [ { "name" : "jess", "school" : 102, "age" : 11 } ] }
{ "_id" : 3 }
{ "_id" : 4, "students" : [ { "name" : "ruth", "school" : 102, "age" : 16 } ] }
```





##### $slice

```javascript
// 从哪个索引开始，又返回数组中的几个元素

{ item: "socks", qty: 100, details: { colors: [ "blue", "red" ], sizes: [ "S", "M", "L"] } }


db.inventory.find( { }, { qty: 1, "details.colors": { $slice: 1 } } )
// 结果
{ "_id" : ObjectId("5ee92a6ec644acb6d13eedb1"), "qty" : 100, "details" : { "colors" : [ "blue" ] } }

'当$slice作为映射排除的主力时，将返回文档中其余所有字段'
db.inventory.find( { }, { _id: 0, "details.colors": { $slice: 1 } } )
// 结果
{ "item" : "socks", "qty" : 100, "details" : { "colors" : [ "blue" ], "sizes" : [ "S", "M", "L" ] } }


'案列'
db.posts.insertMany([
   {
     _id: 1,
     title: "Bagels are not croissants.",
     comments: [ { comment: "0. true" }, { comment: "1. croissants aren't bagels."} ]
   },
   {
     _id: 2,
     title: "Coffee please.",
     comments: [ { comment: "0. fooey" }, { comment: "1. tea please" }, { comment: "2. iced coffee" }, { comment: "3. cappuccino" }, { comment: "4. whatever" } ]
   }
])


db.posts.find( {}, { comments: { $slice: 3 } } )
// 结果
{
   "_id" : 1,
   "title" : "Bagels are not croissants.",
   "comments" : [ { "comment" : "0. true" }, { "comment" : "1. croissants aren't bagels." } ]
}
{
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "0. fooey" }, { "comment" : "1. tea please" }, { "comment" : "2. iced coffee" } ]
}


db.posts.find( {}, { comments: { $slice: -3 } } )
//结果
{
   "_id" : 1,
   "title" : "Bagels are not croissants.",
   "comments" : [ { "comment" : "0. true" }, { "comment" : "1. croissants aren't bagels." } ]
}
{
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "2. iced coffee" }, { "comment" : "3. cappuccino" }, { "comment" : "4. whatever" } ]
}



db.posts.find( {}, { comments: { $slice: [ 1, 3 ] } } )
//结果
{
   "_id" : 1,
   "title" : "Bagels are not croissants.",
   "comments" : [ { "comment" : "1. croissants aren't bagels." } ]
}
{
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "1. tea please" }, { "comment" : "2. iced coffee" }, { "comment" : "3. cappuccino" } ]
}
```







#### 辅助操作

##### $comment

```javascript
'$comment:说明查询意义，可以给查询条件注释'


db.records.find(
   {
     x: { $mod: [ 2, 0 ] },
     $comment: "Find even values."
   }
)

// 分别统计奇数与偶数的和
db.records.aggregate( [
   { $match: { x: { $gt: 0 }, $comment: "Don't allow negative inputs." } },
   { $group : { _id: { $mod: [ "$x", 2 ] }, total: { $sum: "$x" } } }
] )
```



##### $rand

```javascript

'案列一'
db.donors.insertMany(
   [
     { donorId: 1000, amount: 0, frequency: 1 },
     { donorId: 1001, amount: 0, frequency: 2 },
     { donorId: 1002, amount: 0, frequency: 1 },
     { donorId: 1003, amount: 0, frequency: 2 },
     { donorId: 1004, amount: 0, frequency: 1 }
   ]
)

// 随机更新amount字段的值
db.donors.updateMany(
   {},
   [
      { $set:
         { amount:
            { $floor:
               { $multiply: [ { $rand: {} }, 100 ] }
            }
         }
      }
    ]
)




'案列二'
db.voters.insertMany(
   [
     { name: "Archibald", voterId: 4321, district: 3, registered: true },
     { name: "Beckham", voterId: 4331, district: 3, registered: true },
     { name: "Carolin", voterId: 5321, district: 4, registered: true },
     { name: "Debarge", voterId: 4343, district: 3, registered: false },
     { name: "Eckhard", voterId: 4161, district: 3, registered: false },
     { name: "Faberge", voterId: 4300, district: 1, registered: true },
     { name: "Grimwald", voterId: 4111, district: 3, registered: true },
     { name: "Humphrey", voterId: 2021, district: 3, registered: true },
     { name: "Idelfon", voterId: 1021, district: 4, registered: true },
     { name: "Justo", voterId: 9891, district: 3, registered: false }
   ]
)

// 以一半的概率随机选择符合条件的文档
db.voters.find(
   {  district: 3,
      $expr: { $lt: [0.5, {$rand: {} } ] }
   },
   { _id: 0, name: 1, registered: 1 }
)

```





#### 更新操作符

```javascript
'使用格式'
{
   <operator1>: { <field1>: <value1>, ... },
   <operator2>: { <field2>: <value2>, ... },
   ...
}


'字段'
$set
$unset
$setOnInsert
$rename
$inc
$mul

$min
$max

$currentDate

// ==========================================
'数组'        
$push
$pushAll
$andToSet
$pop
$pull

$
$[]
$[element]
                 
// ==========================================
'修饰符:$push结合使用'
$each
	// 除了$push,还可以与$addToSet
$position
$slice
$sort

```





##### $currentDate

```javascript
db.customers.insertOne(
   { _id: 1, status: "a", lastModified: ISODate("2013-10-02T01:11:18.965Z") }
)

db.customers.updateOne(
   { _id: 1 },
   {
     $currentDate: {
        lastModified: true,	// 更新lastModified字段
         // 插入新的字段cancellatio,其中存在子文档date,其日期类型是timestamp
        "cancellation.date": { $type: "timestamp" }
     },
     $set: {
        "cancellation.reason": "user request",
        status: "D"
     }
   }
)
// 等价于
'为了访问聚合变量Now、CLUSTER_TIME,必须使用带有"$$"前缀被引号包裹的'
db.customers.updateOne(
  { _id: 1 },
  [
   { $set: { lastModified: "$$NOW", cancellation: {date: "$$CLUSTER_TIME", reason: "user request"}, status: "D" } }
  ]
)


// 结果
{
   "_id" : 1,
   "status" : "D",
   "lastModified" : ISODate("2020-01-22T21:21:41.052Z"),
   "cancellation" : {
      "date" : Timestamp(1579728101, 1),
      "reason" : "user request"
   }
}
```









##### $min

```javascript
'只要当要更新的值 小于 原先值时，才更新；若更新的值不小于原先值，则不会更新'

db.scores.insertOne( { _id: 1, highScore: 800, lowScore: 200 } )

// 更新值lowScore=150 小于 原先值lowScore=200,允许更新
db.scores.updateOne( { _id: 1 }, { $min: { lowScore: 150 } } )


```





##### $

```javascript
'充当一个占位符，指代在一个文档第一个符合要求的字段（例如，数组中第一个符合要求的元素）'
'非常方便的更新数组中第一个符合元素（有可能是嵌合子文档）'
'$指代数组中第一个符合要求的索引'

`
# updateOne | updateMany | findAndModify | findOneAndUpdate
注意事项
	1.不能与upsert一起使用
	2.不能在嵌套数组中使用
	3.当使用$unset后，不会将符合元素移除，而是会设置成Null
	4.当匹配数组元素时，使用了负性操作符，例如：$not、$nor、$nin，就不能使用$更新字段;除非负性操作符是在$elemMatch中使用的
	
`

'案列一'
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 85, 80, 80 ] },
   { "_id" : 2, "grades" : [ 88, 90, 92 ] },
   { "_id" : 3, "grades" : [ 85, 100, 90 ] }
] )

db.students.updateOne(
   { _id: 1, grades: 80 },
   { $set: { "grades.$" : 82 } }
)

{ "_id" : 1, "grades" : [ 85, 82, 80 ] }		// 第一个符合的文档，此时$=0,且只更新其中一个符合的值
{ "_id" : 2, "grades" : [ 88, 90, 92 ] }
{ "_id" : 3, "grades" : [ 85, 100, 90 ] }




'案列二'
{
  _id: 4,
  grades: [
     { grade: 80, mean: 75, std: 8 },
     { grade: 85, mean: 90, std: 5 },	// 符合要求，此时$=1
     { grade: 85, mean: 85, std: 8 }
  ]
}

db.students.updateOne(
   { _id: 4, "grades.grade": 85 },
   { $set: { "grades.$.std" : 6 } }
)
// 等价于
db.students.updateOne(
   {
     _id: 4,
     grades: { $elemMatch: { grade: { $lte: 90 }, mean: { $gt: 80 } } }
   },
   { $set: { "grades.$.std" : 6 } }
)


{
   "_id" : 4,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 8 },
      { "grade" : 85, "mean" : 90, "std" : 6 },	// 更新std
      { "grade" : 85, "mean" : 85, "std" : 8 }
   ]
}
```





##### $[]

```javascript
'更新符合匹配成功的数组中 所有 元素'
`
可以允许 在嵌套数组中使用

与upsert结合使用时，需注意明确查询语句，若查询语句不存在则有可能将会报错，如：
    db.emptyCollection.updateOne(
       { },
       { $set: { "myArray.$[]": 10 } },	// myArrar数组存在,则将每个数组元素的值设为10；但但数组不存在时，则会直接抛出错误
       { upsert: true }
    )
    db.emptyCollection.updateOne(
       { myArray: 5 },
       { $set: { "myArray.$[]": 10 } },	// myArrar数组中存在元素5的值,并将所有值改为10；可若数组不存在也会报错
       { upsert: true }
    )

// 正确使用
db.collection.updateOne(
   { myArray: [ 5, 8 ] },
   { $set: { "myArray.$[]": 10 } },// 先找myArray数组是[5,8]的文档，后将myArray中的每个元素改为10；若不存在则新建字段 myArray;[5,8]，再经过$set，把每一个元素值变成10，即：myArray: [ 10, 10 ] 
   { upsert: true }
)
`


'案列一'
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 85, 82, 80 ] },
   { "_id" : 2, "grades" : [ 88, 90, 92 ] },
   { "_id" : 3, "grades" : [ 85, 100, 90 ] }
] )


db.students.updateMany(
   { },
   { $inc: { "grades.$[]": 10 } },
)

{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 102 ] }
{ "_id" : 3, "grades" : [ 95, 110, 100 ] }


'案列二：结合负性查询'
db.results.insertMany( [
   { "_id" : 1, "grades" : [ 85, 82, 80 ] },
   { "_id" : 2, "grades" : [ 88, 90, 92 ] },
   { "_id" : 3, "grades" : [ 85, 100, 90 ] }
] )


db.results.updateMany(
   { "grades" : { $ne: 100 } },
   { $inc: { "grades.$[]": 10 } },
)

{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 102 ] }
{ "_id" : 3, "grades" : [ 85, 100, 90 ] }




'案列三'
db.students2.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 8 },
         { "grade" : 85, "mean" : 90, "std" : 6 },
         { "grade" : 85, "mean" : 85, "std" : 8 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 8 },
         { "grade" : 87, "mean" : 90, "std" : 5 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   }
] )


db.students2.updateMany(
   { },
   { $inc: { "grades.$[].std" : -2 } },
)

```







##### $[element]

```javascript
'筛选数组中 适合的元素 进行更新操作'
'options配置中arrayFilters字段筛选符合的元素'
`
同$[] 一样 在于upsert 结合使用时，必须明确查询语句
    db.collection.updateOne(
       { myArray: [ 0, 1 ] },	// 查询语句明确
       { $set: { "myArray.$[element]": 2 } },
       { arrayFilters: [ { element: 0 } ], upsert: true }
    )
`

'案例一'
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 95, 92, 90 ] },
   { "_id" : 2, "grades" : [ 98, 100, 102 ] },
   { "_id" : 3, "grades" : [ 95, 110, 100 ] }
] )


db.students.updateMany(
   { },
   { $set: { "grades.$[element]" : 100 } },
   // 只更新数组中其 值不小于100 的元素，将这些元素的值设为100
   { arrayFilters: [ { "element": { $gte: 100 } } ] }
)


{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 100 ] }	// 更新
{ "_id" : 3, "grades" : [ 95, 100, 100 ] }	// 更新



'案例二'
db.students2.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 6 },
         { "grade" : 85, "mean" : 90, "std" : 4 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 6 },
         { "grade" : 87, "mean" : 90, "std" : 3 },
         { "grade" : 85, "mean" : 85, "std" : 4 }
      ]
   }
] )

db.students2.updateMany(
   { },
   { $set: { "grades.$[elem].mean" : 100 } },
    // 元素中的grade字段值 不小于 85 才更新元素中的mean字段值为 100
   { arrayFilters: [ { "elem.grade": { $gte: 85 } } ] }
)

{
   "_id" : 1,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 6 },
      { "grade" : 85, "mean" : 100, "std" : 4 },
      { "grade" : 85, "mean" : 100, "std" : 6 }
   ]
}
{
   "_id" : 2,
   "grades" : [
      { "grade" : 90, "mean" : 100, "std" : 6 },
      { "grade" : 87, "mean" : 100, "std" : 3 },
      { "grade" : 85, "mean" : 100, "std" : 4 }
   ]
}


'案列三'
// 仍是案列二的表
db.students3.updateMany(
   { },
   { $inc: { "grades.$[elem].std" : -1 } },
    // and的关系;只有这些条件都满足的元素才...
   { arrayFilters: [ { "elem.grade": { $gte: 80 }, "elem.std": { $gt: 5 } } ] }
)


'案列四'
db.alumni.insertMany( [
   {
      "_id": 1,
      "name": "Christine Franklin",
      "degrees": [
         { "level": "Master" },
         { "level": "Bachelor" }
      ],
  },
   {
      "_id": 2,
      "name": "Reyansh Sengupta",
      "degrees": [ { "level": "Bachelor" } ],
   }
] )

db.alumni.updateMany(
   { },
   { $set : { "degrees.$[degree].gradcampaign" : 1 } },
    // 只有元素中level字段值 不等于 "Bachelor"才更新（没有该字段则添加）gradcampaign字段
   { arrayFilters : [ {"degree.level" : { $ne: "Bachelor" } } ] }
)


{
  _id: 1,
  name: 'Christine Franklin',
  degrees: [
     { level: 'Master', gradcampaign: 1 },
     { level: 'Bachelor' }
  ]
},
{
  _id: 2,
  name: 'Reyansh Sengupta',
  degrees: [ { level: 'Bachelor' } ]
}
```





###### 在嵌套数组中与$[]结合

```javascript
db.students4.insertOne(
   { "_id" : 1,
      "grades" : [
        { type: "quiz", questions: [ 10, 8, 5 ] },
        { type: "quiz", questions: [ 8, 9, 6 ] },
        { type: "hw", questions: [ 5, 4, 3 ] },
        { type: "exam", questions: [ 25, 10, 23, 0 ] },
      ]
   }
)


db.students4.updateMany(
   {},
   { $inc: { "grades.$[t].questions.$[score]": 2 } },
    // grades中的元素t满足其type字段 = "quiz"
    // 找到这些符合元素t后，进入其questions字段，其内的元素为score
    // 找到这些值 > 8 的元素
    // 将这些元素的值 + 2 更新
   { arrayFilters: [ { "t.type": "quiz" }, { "score": { $gte: 8 } } ] }
)


{
   "_id" : 1,
   "grades" : [
      { "type" : "quiz", "questions" : [ 12, 10, 5 ] },	// 满足
      { "type" : "quiz", "questions" : [ 10, 11, 6 ] },	// 满足
      { "type" : "hw", "questions" : [ 5, 4, 3 ] },
      { "type" : "exam", "questions" : [ 25, 10, 23, 0 ] }
   ]
}


'请描述下方语句的含义'
db.students4.updateMany(
   {},
   { $inc: { "grades.$[].questions.$[score]": 2 } },
   { arrayFilters: [  { "score": { $gte: 8 } } ] }
)


```







##### $each

```javascript
'与$push结合使用'
db.students.updateOne(
   { name: "joe" },
   { $push: { scores: { $each: [ 90, 92, 85 ] } } }
)
// 等价于
db.students.updateOne(
   { name: "joe" },
   { $pushAll: { scores: [ 90, 92, 85 ]} }
)



'与$addToSet'
db.inventory.updateOne(
   { _id: 2 },
   { $addToSet: { tags: { $each: [ "camera", "electronics", "accessories" ] } } }
 )

```





##### $position

```javascript
'案列一'
db.students.insertOne( { "_id" : 1, "scores" : [ 100 ] } )

db.students.updateOne(
   { _id: 1 },
   {
     $push: {
        scores: {
           $each: [ 50, 60, 70 ],
           $position: 0
        }
     }
   }
)

//结果
{ "_id" : 1, "scores" : [  50,  60,  70,  100 ] }



'案列二：还可以使用负索引'
db.students.insertOne(
   { "_id" : 3, "scores" : [  50,  60,  20,  30,  70,  100 ] }
)

db.students.updateOne(
   { _id: 3 },
   {
     $push: {
        scores: {
           $each: [ 90, 80 ],
           $position: -2
        }
     }
   }
)

//结果
{ "_id" : 3, "scores" : [ 50, 60, 20, 30, 90, 80, 70, 100 ] }


```



##### $sort

```javascript
'对数组中的元素进行排序'

'案列一：数值'
db.students.insertOne( { "_id" : 2, "tests" : [  89,  70,  89,  50 ] } )

db.students.updateOne(
   { _id: 2 },
   { $push: { tests: { $each: [ 40, 60 ], $sort: 1 } } }
)

{ "_id" : 2, "tests" : [  40,  50,  60,  70,  89,  89 ] }


// 简写
db.students.updateOne(
   { _id: 3 },
   { $push: { tests: { $each: [ ], $sort: -1 } } }
)



'案列二：嵌套文档中的某一字段'
db.students.insertOne(
   {
     "_id": 1,
     "quizzes": [
       { "id" : 1, "score" : 6 },
       { "id" : 2, "score" : 9 }
     ]
   }
)


db.students.updateOne(
   { _id: 1 },
   {
     $push: {
       quizzes: {
         $each: [ { id: 3, score: 8 }, { id: 4, score: 7 }, { id: 5, score: 6 } ],
          // 注意这里可以直接使用score,指的就是按数组元素中的score字段 递增排序
         $sort: { score: 1 }
       }
     }
   }
)

{
  "_id" : 1,
  "quizzes" : [
     { "id" : 1, "score" : 6 },
     { "id" : 5, "score" : 6 },
     { "id" : 4, "score" : 7 },
     { "id" : 3, "score" : 8 },
     { "id" : 2, "score" : 9 }
  ]
}


```











##### $slice

```javascript
'只保留对应个数的数组元素'
'负号：表示从后往前'
'正号：表示从前往后'



'案列一'
{ "_id" : 1, "scores" : [ 40, 50, 60 ] }

db.students.updateOne(
   { _id: 1 },
   {
     $push: {
       scores: {
         $each: [ 80, 78, 86 ],
         $slice: -5	// 只取最后5个
       }
     }
   }
)

// 结果
{ "_id" : 1, "scores" : [  50,  60,  80,  78,  86 ] }



'案列二'
{ "_id" : 2, "scores" : [ 89, 90 ] }
db.students.updateOne(
   { _id: 2 },
   {
     $push: {
       scores: {
         $each: [ 100, 20 ],
         $slice: 3	// 只取前3个
       }
     }
   }
)


// 结果
{ "_id" : 2, "scores" : [  89,  90,  100 ] }

```



###### 修饰符综合案列

```javascript
db.students.insertOne(
   {
      "_id" : 5,
      "quizzes" : [
         { "wk": 1, "score" : 10 },
         { "wk": 2, "score" : 8 },
         { "wk": 3, "score" : 5 },
         { "wk": 4, "score" : 6 }
      ]
   }
)


db.students.updateOne(
   { _id: 5 },
   {
     $push: {
       quizzes: {
          $each: [ { wk: 5, score: 8 }, { wk: 6, score: 7 }, { wk: 7, score: 6 } ],
          $sort: { score: -1 },	// 先排序，再取前三个
          $slice: 3
       }
     }
   }
)

// 结果
{
  "_id" : 5,
  "quizzes" : [
     { "wk" : 1, "score" : 10 },
     { "wk" : 2, "score" : 8 },
     { "wk" : 5, "score" : 8 }
  ]
}




```











#### 聚合操作符

##### $function

```javascript
'自定义查询；但是尽量不要使用'
'$expr+$function 查询速度高于 $where'


'案列一'
db.players.find( { $where: function() {
   return (hex_md5(this.name) == "15b0a220baa16331e8d80e15367677ad")
} } );


db.players.find( {$expr: { $function: {
      body: function(name) { return hex_md5(name) == "15b0a220baa16331e8d80e15367677ad"; },
      args: [ "$name" ],
      lang: "js"
} } } )


'案列二'
db.players.insertMany([
   { _id: 1, name: "Miss Cheevous",  scores: [ 10, 5, 10 ] },
   { _id: 2, name: "Miss Ann Thrope", scores: [ 10, 10, 10 ] },
   { _id: 3, name: "Mrs. Eppie Delta ", scores: [ 9, 8, 8 ] }
])



db.players.aggregate( [
   { $addFields:
      {
        isFound:
            { $function:
               {
                  body: function(name) {
                     return hex_md5(name) == "15b0a220baa16331e8d80e15367677ad"
                  },
                  args: [ "$name" ],
                  lang: "js"
               }
            },
         message:
            { $function:
               {
                  body: function(name, scores) {
                     let total = Array.sum(scores);
                     return `Hello ${name}.  Your total score is ${total}.`
                  },
                  args: [ "$name", "$scores"],
                  lang: "js"
               }
            }
       }
    }
] )


// 结果
{ "_id" : 1, "name" : "Miss Cheevous", "scores" : [ 10, 5, 10 ], "isFound" : false, "message" : "Hello Miss Cheevous.  Your total score is 25." }
{ "_id" : 2, "name" : "Miss Ann Thrope", "scores" : [ 10, 10, 10 ], "isFound" : true, "message" : "Hello Miss Ann Thrope.  Your total score is 30." }
{ "_id" : 3, "name" : "Mrs. Eppie Delta ", "scores" : [ 9, 8, 8 ], "isFound" : false, "message" : "Hello Mrs. Eppie Delta .  Your total score is 25." }


```







##### $accumulator

```javascript
'merge函数的主要作用是 $accumulator 有可能超过超过其特定的内存限制，开启`allowDiskUse`后将会启用disk、并在其上完成操作，等到结果完成后 使用`merge`合并操作，合并硬盘上完成的结果'
`
	init
	initArgs

	accumulate
	accumulateArgs

	finalize
	merge
`


'案列一'
db.books.insertMany([
  { "_id" : 8751, "title" : "The Banquet", "author" : "Dante", "copies" : 2 },
  { "_id" : 8752, "title" : "Divine Comedy", "author" : "Dante", "copies" : 1 },
  { "_id" : 8645, "title" : "Eclogues", "author" : "Dante", "copies" : 2 },
  { "_id" : 7000, "title" : "The Odyssey", "author" : "Homer", "copies" : 10 },
  { "_id" : 7020, "title" : "Iliad", "author" : "Homer", "copies" : 10 }
])



db.books.aggregate([
{
  $group :
  {
    _id : "$author",
    avgCopies:
    {
      $accumulator:
      {
        init: function() {                        // Set the initial state
          return { count: 0, sum: 0 }
        },
        accumulate: function(state, numCopies) {  // Define how to update the state
          return {
            count: state.count + 1,
            sum: state.sum + numCopies
          }
        },
        accumulateArgs: ["$copies"],              // Argument required by the accumulate function
        merge: function(state1, state2) {         // When the operator performs a merge,
          return {                                // add the fields from the two states
            count: state1.count + state2.count,
            sum: state1.sum + state2.sum
          }
        },
        finalize: function(state) {               // After collecting the results from all documents,
          return (state.sum / state.count)        // calculate the average
        },
        lang: "js"
      }
    }
  }
}
])


// 结果
{ "_id" : "Dante", "avgCopies" : 1.6666666666666667 }
{ "_id" : "Homer", "avgCopies" : 10 }


'案列二'
db.restaurants.insertMany([
  { "_id" : 1, "name" : "Food Fury", "city" : "Bettles", "cuisine" : "American" },
  { "_id" : 2, "name" : "Meal Macro", "city" : "Bettles", "cuisine" : "Chinese" },
  { "_id" : 3, "name" : "Big Crisp", "city" : "Bettles", "cuisine" : "Latin" },
  { "_id" : 4, "name" : "The Wrap", "city" : "Onida", "cuisine" : "American" },
  { "_id" : 5, "name" : "Spice Attack", "city" : "Onida", "cuisine" : "Latin" },
  { "_id" : 6, "name" : "Soup City", "city" : "Onida", "cuisine" : "Chinese" },
  { "_id" : 7, "name" : "Crave", "city" : "Pyote", "cuisine" : "American" },
  { "_id" : 8, "name" : "The Gala", "city" : "Pyote", "cuisine" : "Chinese" }
])


'<userProfileCity>参数，是一个查询参数，需要用户自定义，这里待定，需要用户指定'
db.restaurants.aggregate([
{
  $group :
  {
    _id : { city: "$city" },
    restaurants:
    {
      $accumulator:
      {
        init: function(city, userProfileCity) {        // Set the initial state
          return {
            max: city === userProfileCity ? 3 : 1,     // If the group matches the user's city, return 3 restaurants
            restaurants: []                            // else, return 1 restaurant
          }
        },
        initArgs: ["$city", <userProfileCity>],        // Argument to pass to the init function
        accumulate: function(state, restaurantName) {  // Define how to update the state
          if (state.restaurants.length < state.max) {
            state.restaurants.push(restaurantName);
          }
          return state;
        },
        accumulateArgs: ["$name"],                     // Argument required by the accumulate function
        merge: function(state1, state2) {
          return {
            max: state1.max,
            restaurants: state1.restaurants.concat(state2.restaurants).slice(0, state1.max)
          }
        },
        finalize: function(state) {                   // Adjust the state to only return field we need
          return state.restaurants
        }
        lang: "js"
      }
    }
  }
}
])


// If the value of userProfileCity is Bettles, this operation returns the following result:
{ "_id" : { "city" : "Bettles" }, "restaurants" : { "restaurants" : [ "Food Fury", "Meal Macro", "Big Crisp" ] } }
{ "_id" : { "city" : "Onida" }, "restaurants" : { "restaurants" : [ "The Wrap" ] } }
{ "_id" : { "city" : "Pyote" }, "restaurants" : { "restaurants" : [ "Crave" ] } }
```











##### $cond

```javascript
// 表inventory的结构
{ "_id" : 1, "item" : "abc1", qty: 300 }
{ "_id" : 2, "item" : "abc2", qty: 200 }
{ "_id" : 3, "item" : "xyz1", qty: 250 }


// 想要给上述表，添加一个字段discount：当qty字段所对应的项值不下于250时discount=30,否则discount=20
db.inventory.aggregate(
   [
      {
         $project:
           {
             item: 1,
             discount:
               {
                 $cond: { if: { $gte: [ "$qty", 250 ] }, then: 30, else: 20 }
               }
           }
      }
   ]
)


// 简写
db.inventory.aggregate(
   [
      {
         $project:
           {
             item: 1,
             discount:
               {
                 $cond: [ { $gte: [ "$qty", 250 ] }, 30, 20 ]
               }
           }
      }
   ]
)
```







##### $switch

```javascript
$switch: {
   branches: [
      { case: <expression>, then: <expression> },
      { case: <expression>, then: <expression> },
      ...
   ],
   default: <expression>
}



'案列一'
// 结果："less than"
{
   $switch: {
      branches: [
         { case: { $eq: [ 0, 5 ] }, then: "equals" },
         { case: { $gt: [ 0, 5 ] }, then: "greater than" },
         { case: { $lt: [ 0, 5 ] }, then: "less than" }
      ]
   }
}


'案列二'
// grades表
{ "_id" : 1, "name" : "Susan Wilkes", "scores" : [ 87, 86, 78 ] }
{ "_id" : 2, "name" : "Bob Hanna", "scores" : [ 71, 64, 81 ] }
{ "_id" : 3, "name" : "James Torrelio", "scores" : [ 91, 84, 97 ] }


db.grades.aggregate( [
  {
    $project:
      {
        "name" : 1,
        "summary" :
        {
          $switch:
            {
              branches: [
                {
                  case: { $gte : [ { $avg : "$scores" }, 90 ] },
                  then: "Doing great!"
                },
                {
                  case: { $and : [ { $gte : [ { $avg : "$scores" }, 80 ] },
                                   { $lt : [ { $avg : "$scores" }, 90 ] } ] },
                  then: "Doing pretty well."
                },
                {
                  case: { $lt : [ { $avg : "$scores" }, 80 ] },
                  then: "Needs improvement."
                }
              ],
              default: "No scores found."
            }
         }
      }
   }
] )

```







##### $addFields

```javascript
'相似于$project,是 aggregation pipeline(集合管道符) $set的别名'
'添加新的字段，或者覆盖已有字段的值'

'案列一'
{
  _id: 1,
  student: "Maya",
  homework: [ 10, 5, 10 ],
  quiz: [ 10, 8 ],
  extraCredit: 0
}
{
  _id: 2,
  student: "Ryan",
  homework: [ 5, 6, 5 ],
  quiz: [ 8, 8 ],
  extraCredit: 8
}

// 聚合操作
db.scores.aggregate( [
   {
     $addFields: {
       totalHomework: { $sum: "$homework" } ,	//求和homework字段
       totalQuiz: { $sum: "$quiz" }	 // 求和quiz字段
     }
   },
   {
     $addFields: { totalScore:
                  // 将这三个字段的值相加
       { $add: [ "$totalHomework", "$totalQuiz", "$extraCredit" ] } }
   }
] )

// 结果
{
  "_id" : 1,
  "student" : "Maya",
  "homework" : [ 10, 5, 10 ],
  "quiz" : [ 10, 8 ],
  "extraCredit" : 0,
  "totalHomework" : 25,
  "totalQuiz" : 18,
  "totalScore" : 43
}
{
  "_id" : 2,
  "student" : "Ryan",
  "homework" : [ 5, 6, 5 ],
  "quiz" : [ 8, 8 ],
  "extraCredit" : 8,
  "totalHomework" : 16,
  "totalQuiz" : 16,
  "totalScore" : 40
}



'案列二：在子文档中添加新字段'
{ _id: 1, type: "car", specs: { doors: 4, wheels: 4 } }
{ _id: 2, type: "motorcycle", specs: { doors: 0, wheels: 2 } }
{ _id: 3, type: "jet ski" }


db.vehicles.aggregate( [
        {
           $addFields: {
              "specs.fuel_type": "unleaded"
           }
        }
   ] )

// 结果
{ _id: 1, type: "car",
   specs: { doors: 4, wheels: 4, fuel_type: "unleaded" } }
{ _id: 2, type: "motorcycle",
   specs: { doors: 0, wheels: 2, fuel_type: "unleaded" } }
{ _id: 3, type: "jet ski",
   specs: { fuel_type: "unleaded" } }



'案列三：已有字段会进行覆盖'
{ _id: 1, dogs: 10, cats: 15 }


db.animals.aggregate( [
  {
    $addFields: { "cats": 20 }
  }
] )

// 结果
{ _id: 1, dogs: 10, cats: 20 }

```









##### $concatArray

```javascript
'实例一'
{ $concatArrays: [
   [ "hello", " "], [ "world" ]
] }


// 结果
[ "hello", " ", "world" ]


'实例二'
{ $concatArrays: [
   [ "hello", " "],
   [ [ "world" ], "again"]
] }


// 结果
[ "hello", " ", [ "world" ], "again" ]



'案列一'
{ "_id" : 1, instock: [ "chocolate" ], ordered: [ "butter", "apples" ] }
{ "_id" : 2, instock: [ "apples", "pudding", "pie" ] }
{ "_id" : 3, instock: [ "pears", "pecans"], ordered: [ "cherries" ] }
{ "_id" : 4, instock: [ "ice cream" ], ordered: [ ] }


db.warehouses.aggregate([
   { $project: { items: { $concatArrays: [ "$instock", "$ordered" ] } } }
])

// 结果
{ "_id" : 1, "items" : [ "chocolate", "butter", "apples" ] }
{ "_id" : 2, "items" : null }
{ "_id" : 3, "items" : [ "pears", "pecans", "cherries" ] }
{ "_id" : 4, "items" : [ "ice cream" ] }



'案列二'
db.scores.insertMany([
   { _id: 1, student: "Maya", homework: [ 10, 5, 10 ], quiz: [ 10, 8 ], extraCredit: 0 },
   { _id: 2, student: "Ryan", homework: [ 5, 6, 5 ], quiz: [ 8, 8 ], extraCredit: 8 }
])


db.scores.aggregate([
   { $match: { _id: 1 } },
   { $addFields: { homework: { $concatArrays: [ "$homework", [ 7 ] ] } } }
])

// 结果
{ "_id" : 1, "student" : "Maya", "homework" : [ 10, 5, 10, 7 ], "quiz" : [ 10, 8 ], "extraCredit" : 0 }




```





##### $mergeObjects| !

```javascript
'按顺序依次合并对应数组中的元素对象中的每个键'
'相同键，最后合并的生效'

'简单实例'
{ $mergeObjects: [ { a: 1 }, null ] }
// { a: 1 }


{ $mergeObjects: [ null, null ] }
// { }

{
  $mergeObjects: [
    { a: 1 },
    { a: 2, b: 2 },
    { a: 3, b: null, c: 3 }
  ]
}
// { a: 3, b: null, c: 3 }



'案列一'
db.sales.insertMany( [
   { _id: 1, year: 2017, item: "A", quantity: { "2017Q1": 500, "2017Q2": 500 } },
   { _id: 2, year: 2016, item: "A", quantity: { "2016Q1": 400, "2016Q2": 300, "2016Q3": 0, "2016Q4": 0 } } ,
   { _id: 3, year: 2017, item: "B", quantity: { "2017Q1": 300 } },
   { _id: 4, year: 2016, item: "B", quantity: { "2016Q3": 100, "2016Q4": 250 } }
] )


db.sales.aggregate( [
   { $group: { _id: "$item", mergedSales: { $mergeObjects: "$quantity" } } }
] )


{
  _id: 'A',
  mergedSales: { '2017Q1': 500, '2017Q2': 500, '2016Q1': 400, '2016Q2': 300, '2016Q3': 0, '2016Q4': 0 }
},
{
  _id: 'B',
  mergedSales: { '2017Q1': 300, '2016Q3': 100, '2016Q4': 250 }
}
```





##### $replaceRoot | $ifNull | $concat

```javascript
'将新的对象作为根对象返回'
'$$ROOT:指旧的根对象，可以用来$mergeObject'


db.collection.aggregate([
    // { _id: "$_id", first: "", last: "" } 作为默认值，来与$name所对应的对象进行合并
   { $replaceRoot: { newRoot: { $mergeObjects: [ { _id: "$_id", first: "", last: "" }, "$name" ] } } }
])


db.collection.aggregate([
    // 如果没有name字段就标记missingName为true
   { $replaceRoot: { newRoot: { $ifNull: [ "$name", { _id: "$_id", missingName: true} ] } } }
])




'案列一'
{ "_id" : 1, "name" : "Arlene", "age" : 34, "pets" : { "dogs" : 2, "cats" : 1 } }
{ "_id" : 2, "name" : "Sam", "age" : 41, "pets" : { "cats" : 1, "fish" : 3 } }
{ "_id" : 3, "name" : "Maria", "age" : 25 }


db.people.aggregate( [
   { $replaceRoot: { newRoot: { $mergeObjects:  [ { dogs: 0, cats: 0, birds: 0, fish: 0 }, "$pets" ] }} }
] )

// 根对象发生了改变
{ "dogs" : 2, "cats" : 1, "birds" : 0, "fish" : 0 }
{ "dogs" : 0, "cats" : 1, "birds" : 0, "fish" : 3 }
{ "dogs" : 0, "cats" : 0, "birds" : 0, "fish" : 0 }



'案例二'
db.students.insertMany([
   {
      "_id" : 1,
      "grades" : [
         { "test": 1, "grade" : 80, "mean" : 75, "std" : 6 },
         { "test": 2, "grade" : 85, "mean" : 90, "std" : 4 },
         { "test": 3, "grade" : 95, "mean" : 85, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "test": 1, "grade" : 90, "mean" : 75, "std" : 6 },
         { "test": 2, "grade" : 87, "mean" : 90, "std" : 3 },
         { "test": 3, "grade" : 91, "mean" : 85, "std" : 4 }
      ]
   }
])


db.students.aggregate( [
   { $unwind: "$grades" },	// 打开grades字段，数组拆分成每个元素
   { $match: { "grades.grade" : { $gte: 90 } } },
   { $replaceRoot: { newRoot: "$grades" } }
] )


{ "test" : 3, "grade" : 95, "mean" : 85, "std" : 6 }
{ "test" : 1, "grade" : 90, "mean" : 75, "std" : 6 }
{ "test" : 3, "grade" : 91, "mean" : 85, "std" : 4 }



'案列三'
db.contacts.aggregate( [
   {
      $replaceRoot: {
         newRoot: {
            full_name: {
               $concat : [ "$first_name", " ", "$last_name" ]
            }
         }
      }
   }
] )

{ "full_name" : "Gary Sheffield" }
{ "full_name" : "Nancy Walker" }
{ "full_name" : "Peter Sumner" }


'案列四：使用$$ROOT'
db.contacts.insertMany( [
   { "_id" : 1, name: "Fred", email: "fred@example.net" },
   { "_id" : 2, name: "Frank N. Stine", cell: "012-345-9999" },
   { "_id" : 3, name: "Gren Dell", home: "987-654-3210", email: "beo@example.net" }
] )


db.contacts.aggregate( [
   { $replaceRoot:
      { newRoot:
         { $mergeObjects:
             [
                { _id: "", name: "", email: "", cell: "", home: "" },
                "$$ROOT"	//原先根字段保底
             ]
          }
      }
   }
] )


{
  _id: 1,
  name: 'Fred',
  email: 'fred@example.net',
  cell: '',
  home: ''
},
{
  _id: 2,
  name: 'Frank N. Stine',
  email: '',
  cell: '012-345-9999',
  home: ''
},
{
  _id: 3,
  name: 'Gren Dell',
  email: 'beo@example.net',
  cell: '',
  home: '987-654-3210'
}
←  	$redact (aggregation)
```









##### $sortByCount

```javascript
The $sortByCount stage is equivalent to the following $group + $sort sequence:
// 等价于
    { $group: { _id: <expression>, count: { $sum: 1 } } },
    { $sort: { count: -1 } }


{ "_id" : 1, "title" : "The Pillars of Society", "artist" : "Grosz", "year" : 1926, "tags" : [ "painting", "satire", "Expressionism", "caricature" ] }
{ "_id" : 2, "title" : "Melancholy III", "artist" : "Munch", "year" : 1902, "tags" : [ "woodcut", "Expressionism" ] }
{ "_id" : 3, "title" : "Dancer", "artist" : "Miro", "year" : 1925, "tags" : [ "oil", "Surrealism", "painting" ] }
{ "_id" : 4, "title" : "The Great Wave off Kanagawa", "artist" : "Hokusai", "tags" : [ "woodblock", "ukiyo-e" ] }
{ "_id" : 5, "title" : "The Persistence of Memory", "artist" : "Dali", "year" : 1931, "tags" : [ "Surrealism", "painting", "oil" ] }
{ "_id" : 6, "title" : "Composition VII", "artist" : "Kandinsky", "year" : 1913, "tags" : [ "oil", "painting", "abstract" ] }
{ "_id" : 7, "title" : "The Scream", "artist" : "Munch", "year" : 1893, "tags" : [ "Expressionism", "painting", "oil" ] }
{ "_id" : 8, "title" : "Blue Flower", "artist" : "O'Keefe", "year" : 1918, "tags" : [ "abstract", "painting" ] }


db.exhibits.aggregate( [ { $unwind: "$tags" },  { $sortByCount: "$tags" } ] )

// res
{ "_id" : "painting", "count" : 6 }
{ "_id" : "oil", "count" : 4 }
{ "_id" : "Expressionism", "count" : 3 }
{ "_id" : "Surrealism", "count" : 2 }
{ "_id" : "abstract", "count" : 2 }
{ "_id" : "woodblock", "count" : 1 }
{ "_id" : "woodcut", "count" : 1 }
{ "_id" : "ukiyo-e", "count" : 1 }
{ "_id" : "satire", "count" : 1 }
{ "_id" : "caricature", "count" : 1 }

```







##### $facet | $bucket | $bucketAuto

```javascript
`
# 参考链接:https://docs.mongodb.com/manual/reference/operator/aggregation/bucketAuto/#example


$facet 主要用来 同时根据源文档结构生成新的文档结构（旧的文档结构将会被完全移除，只包含新构建的一系列字段）
	// 类似于：{$replaceRoot:{newRoot:{$mergeObjects:[{},{},{},...]}}}


$bucket:主要用来，将某一数字字段划分，范围为boundaries(划分成功后，_id为<lowerbound>),范围失败将归为default(即：_id将标记为<literal>)
    {
      $bucket: {
          groupBy: <expression>,
          boundaries: [ <lowerbound1>, <lowerbound2>, ... ],
          default: <literal>,
          output: {
             <output1>: { <$accumulator expression> },
             ...
             <outputN>: { <$accumulator expression> }
          }
       }
    }
`

```





###### 纯bucket示例

```javascript
'$bucket案列'
db.artists.insertMany([
  { "_id" : 1, "last_name" : "Bernard", "first_name" : "Emil", "year_born" : 1868, "year_died" : 1941, "nationality" : "France" },
  { "_id" : 2, "last_name" : "Rippl-Ronai", "first_name" : "Joszef", "year_born" : 1861, "year_died" : 1927, "nationality" : "Hungary" },
  { "_id" : 3, "last_name" : "Ostroumova", "first_name" : "Anna", "year_born" : 1871, "year_died" : 1955, "nationality" : "Russia" },
  { "_id" : 4, "last_name" : "Van Gogh", "first_name" : "Vincent", "year_born" : 1853, "year_died" : 1890, "nationality" : "Holland" },
  { "_id" : 5, "last_name" : "Maurer", "first_name" : "Alfred", "year_born" : 1868, "year_died" : 1932, "nationality" : "USA" },
  { "_id" : 6, "last_name" : "Munch", "first_name" : "Edvard", "year_born" : 1863, "year_died" : 1944, "nationality" : "Norway" },
  { "_id" : 7, "last_name" : "Redon", "first_name" : "Odilon", "year_born" : 1840, "year_died" : 1916, "nationality" : "France" },
  { "_id" : 8, "last_name" : "Diriks", "first_name" : "Edvard", "year_born" : 1855, "year_died" : 1930, "nationality" : "Norway" }
])

db.artists.aggregate( [
  // First Stage
  {
    $bucket: {
      groupBy: "$year_born",                        // Field to group by
      boundaries: [ 1840, 1850, 1860, 1870, 1880 ], // Boundaries for the buckets
      default: "Other",                             // Bucket id for documents which do not fall into a bucket
      output: {                                     // Output for each bucket
        "count": { $sum: 1 },
        "artists" :
          {
            $push: {
              "name": { $concat: [ "$first_name", " ", "$last_name"] },
              "year_born": "$year_born"
            }
          }
      }
    }
  },
  // Second Stage
  {
    $match: { count: {$gt: 3} }
  }
] )


// 结果
{ "_id" : 1840, "count" : 1, "artists" : [ { "name" : "Odilon Redon", "year_born" : 1840 } ] }
{ "_id" : 1850, "count" : 2, "artists" : [ { "name" : "Vincent Van Gogh", "year_born" : 1853 },
                                           { "name" : "Edvard Diriks", "year_born" : 1855 } ] }
{ "_id" : 1860, "count" : 4, "artists" : [ { "name" : "Emil Bernard", "year_born" : 1868 },
                                           { "name" : "Joszef Rippl-Ronai", "year_born" : 1861 },
                                           { "name" : "Alfred Maurer", "year_born" : 1868 },
                                           { "name" : "Edvard Munch", "year_born" : 1863 } ] }
{ "_id" : 1870, "count" : 1, "artists" : [ { "name" : "Anna Ostroumova", "year_born" : 1871 } ] }

```







###### bucket + facet

```javascript
db.artwork.insertMany([
  { "_id" : 1, "title" : "The Pillars of Society", "artist" : "Grosz", "year" : 1926,
      "price" : NumberDecimal("199.99") },
  { "_id" : 2, "title" : "Melancholy III", "artist" : "Munch", "year" : 1902,
      "price" : NumberDecimal("280.00") },
  { "_id" : 3, "title" : "Dancer", "artist" : "Miro", "year" : 1925,
      "price" : NumberDecimal("76.04") },
  { "_id" : 4, "title" : "The Great Wave off Kanagawa", "artist" : "Hokusai",
      "price" : NumberDecimal("167.30") },
  { "_id" : 5, "title" : "The Persistence of Memory", "artist" : "Dali", "year" : 1931,
      "price" : NumberDecimal("483.00") },
  { "_id" : 6, "title" : "Composition VII", "artist" : "Kandinsky", "year" : 1913,
      "price" : NumberDecimal("385.00") },
  { "_id" : 7, "title" : "The Scream", "artist" : "Munch", "year" : 1893
      /* No price*/ },
  { "_id" : 8, "title" : "Blue Flower", "artist" : "O'Keefe", "year" : 1918,
      "price" : NumberDecimal("118.42") }
])




db.artwork.aggregate( [
  {
    $facet: {                               // Top-level $facet stage
      "price": [                            // Output field 1
        {
          $bucket: {
              groupBy: "$price",            // Field to group by
              boundaries: [ 0, 200, 400 ],  // Boundaries for the buckets
              default: "Other",             // Bucket id for documents which do not fall into a bucket
              output: {                     // Output for each bucket
                "count": { $sum: 1 },
                "artwork" : { $push: { "title": "$title", "price": "$price" } },
                "averagePrice": { $avg: "$price" }
              }
          }
        }
      ],
      "year": [                                      // Output field 2
        {
          $bucket: {
            groupBy: "$year",                        // Field to group by
            boundaries: [ 1890, 1910, 1920, 1940 ],  // Boundaries for the buckets
            default: "Unknown",                      // Bucket id for documents which do not fall into a bucket
            output: {                                // Output for each bucket
              "count": { $sum: 1 },
              "artwork": { $push: { "title": "$title", "year": "$year" } }
            }
          }
        }
      ]
    }
  }
] )
```



查询结果

```json
{
  "price" : [ // Output of first facet
    {
      "_id" : 0,
      "count" : 4,
      "artwork" : [
        { "title" : "The Pillars of Society", "price" : NumberDecimal("199.99") },
        { "title" : "Dancer", "price" : NumberDecimal("76.04") },
        { "title" : "The Great Wave off Kanagawa", "price" : NumberDecimal("167.30") },
        { "title" : "Blue Flower", "price" : NumberDecimal("118.42") }
      ],
      "averagePrice" : NumberDecimal("140.4375")
    },
    {
      "_id" : 200,
      "count" : 2,
      "artwork" : [
        { "title" : "Melancholy III", "price" : NumberDecimal("280.00") },
        { "title" : "Composition VII", "price" : NumberDecimal("385.00") }
      ],
      "averagePrice" : NumberDecimal("332.50")
    },
    {
      // Includes documents without prices and prices greater than 400
      "_id" : "Other",
      "count" : 2,
      "artwork" : [
        { "title" : "The Persistence of Memory", "price" : NumberDecimal("483.00") },
        { "title" : "The Scream" }
      ],
      "averagePrice" : NumberDecimal("483.00")
    }
  ],
    
    
  "year" : [ // Output of second facet
    {
      "_id" : 1890,
      "count" : 2,
      "artwork" : [
        { "title" : "Melancholy III", "year" : 1902 },
        { "title" : "The Scream", "year" : 1893 }
      ]
    },
    {
      "_id" : 1910,
      "count" : 2,
      "artwork" : [
        { "title" : "Composition VII", "year" : 1913 },
        { "title" : "Blue Flower", "year" : 1918 }
      ]
    },
    {
      "_id" : 1920,
      "count" : 3,
      "artwork" : [
        { "title" : "The Pillars of Society", "year" : 1926 },
        { "title" : "Dancer", "year" : 1925 },
        { "title" : "The Persistence of Memory", "year" : 1931 }
      ]
    },
    {
      // Includes documents without a year
      "_id" : "Unknown",
      "count" : 1,
      "artwork" : [
        { "title" : "The Great Wave off Kanagawa" }
      ]
    }
  ]
}
```









##### $lookup | !!

```javascript
'联合另一张，将符合要求的另一张表的文档嵌入到当前文档中的某个字段中'
'联合状态、子查询在交叉集中'
'解决：手动引用的问题'
// 普通写法：找到对应用户的邮箱
	var u=db.users.findOne({name:<user_name>})
    db.addresses.find({_id:{$in:u.address}})
    
// 使用lookup后的等价写法
    db.users.aggregate([
        {
            $match:{name:<user_name>}	// 过滤用户
        },
        {
            $lookup:{
                from:"address",
                foreignField:"_id"
                localField:"adddress"
            	as:"entiry_addresses",
            }
        }
    ])



```







###### 案列一

```javascript
// 表 orders
db.orders.insertMany( [
   { "_id" : 1, "item" : "almonds", "price" : 12, "quantity" : 2 },
   { "_id" : 2, "item" : "pecans", "price" : 20, "quantity" : 1 },
   { "_id" : 3  }
] )


// 表inventory
db.inventory.insertMany( [
   { "_id" : 1, "sku" : "almonds", "description": "product 1", "instock" : 120 },
   { "_id" : 2, "sku" : "bread", "description": "product 2", "instock" : 80 },
   { "_id" : 3, "sku" : "cashews", "description": "product 3", "instock" : 60 },
   { "_id" : 4, "sku" : "pecans", "description": "product 4", "instock" : 70 },
   { "_id" : 5, "sku": null, "description": "Incomplete" },
   { "_id" : 6 }
] )


'等价于'
`
SELECT *, inventory_docs
FROM orders
WHERE inventory_docs IN (
   SELECT *
   FROM inventory
   WHERE sku = orders.item
);
`
db.orders.aggregate( [
   {
     $lookup:
       {
         from: "inventory",
         localField: "item",
         foreignField: "sku",
         as: "inventory_docs"
       }
  }
] )
```





```json
{
   "_id" : 1,
   "item" : "almonds",
   "price" : 12,
   "quantity" : 2,
   "inventory_docs" : [
      { "_id" : 1, "sku" : "almonds", "description" : "product 1", "instock" : 120 }
   ]
}
{
   "_id" : 2,
   "item" : "pecans",
   "price" : 20,
   "quantity" : 1,
   "inventory_docs" : [
      { "_id" : 4, "sku" : "pecans", "description" : "product 4", "instock" : 70 }
   ]
}
{
   "_id" : 3,
   "inventory_docs" : [
      { "_id" : 5, "sku" : null, "description" : "Incomplete" },
      { "_id" : 6 }
   ]
}
```







###### 案列二:在数组中使用

```javascript
// 表classes
db.classes.insertMany( [
   { _id: 1, title: "Reading is ...", enrollmentlist: [ "giraffe2", "pandabear", "artie" ], days: ["M", "W", "F"] },
   { _id: 2, title: "But Writing ...", enrollmentlist: [ "giraffe1", "artie" ], days: ["T", "F"] }
] )

// 表members
db.members.insertMany( [
   { _id: 1, name: "artie", joined: new Date("2016-05-01"), status: "A" },
   { _id: 2, name: "giraffe", joined: new Date("2017-05-01"), status: "D" },
   { _id: 3, name: "giraffe1", joined: new Date("2017-10-01"), status: "A" },
   { _id: 4, name: "panda", joined: new Date("2018-10-11"), status: "A" },
   { _id: 5, name: "pandabear", joined: new Date("2018-12-01"), status: "A" },
   { _id: 6, name: "giraffe2", joined: new Date("2018-12-01"), status: "D" }
] )


db.classes.aggregate( [
   {
      $lookup:
         {
            from: "members",
            localField: "enrollmentlist",
            foreignField: "name",
            as: "enrollee_info"
        }
   }
] )
```





```json
{
   "_id" : 1,
   "title" : "Reading is ...",
   "enrollmentlist" : [ "giraffe2", "pandabear", "artie" ],
   "days" : [ "M", "W", "F" ],
   "enrollee_info" : [
      { "_id" : 1, "name" : "artie", "joined" : ISODate("2016-05-01T00:00:00Z"), "status" : "A" },
      { "_id" : 5, "name" : "pandabear", "joined" : ISODate("2018-12-01T00:00:00Z"), "status" : "A" },
      { "_id" : 6, "name" : "giraffe2", "joined" : ISODate("2018-12-01T00:00:00Z"), "status" : "D" }
   ]
}
{
   "_id" : 2,
   "title" : "But Writing ...",
   "enrollmentlist" : [ "giraffe1", "artie" ],
   "days" : [ "T", "F" ],
   "enrollee_info" : [
      { "_id" : 1, "name" : "artie", "joined" : ISODate("2016-05-01T00:00:00Z"), "status" : "A" },
      { "_id" : 3, "name" : "giraffe1", "joined" : ISODate("2017-10-01T00:00:00Z"), "status" : "A" }
   ]
}

```









###### 案列三：结合mergeObjects

```javascript
'案列二'
db.orders.insertMany( [
   { "_id" : 1, "item" : "almonds", "price" : 12, "quantity" : 2 },
   { "_id" : 2, "item" : "pecans", "price" : 20, "quantity" : 1 }
] )

db.items.insertMany( [
  { "_id" : 1, "item" : "almonds", description: "almond clusters", "instock" : 120 },
  { "_id" : 2, "item" : "bread", description: "raisin and nut bread", "instock" : 80 },
  { "_id" : 3, "item" : "pecans", description: "candied pecans", "instock" : 60 }
] )

db.orders.aggregate( [
   {
      $lookup: {
         from: "items",
         localField: "item",    // field in the orders collection
         foreignField: "item",  // field in the items collection
         as: "fromItems"
      }
   },
   {
      $replaceRoot: { newRoot: { $mergeObjects: [ { $arrayElemAt: [ "$fromItems", 0 ] }, "$$ROOT" ] } }
   },
   { $project: { fromItems: 0 } }
] )


// 结果
{
  _id: 1,
  item: 'almonds',
  description: 'almond clusters',
  instock: 120,
  price: 12,
  quantity: 2
},
{
  _id: 2,
  item: 'pecans',
  description: 'candied pecans',
  instock: 60,
  price: 20,
  quantity: 1
}


```









###### 案列四：无关联子查询

```javascript
db.absences.insertMany( [
   { "_id" : 1, "student" : "Ann Aardvark", sickdays: [ new Date ("2018-05-01"),new Date ("2018-08-23") ] },
   { "_id" : 2, "student" : "Zoe Zebra", sickdays: [ new Date ("2018-02-01"),new Date ("2018-05-23") ] },
] )


db.holidays.insertMany( [
   { "_id" : 1, year: 2018, name: "New Years", date: new Date("2018-01-01") },
   { "_id" : 2, year: 2018, name: "Pi Day", date: new Date("2018-03-14") },
   { "_id" : 3, year: 2018, name: "Ice Cream Day", date: new Date("2018-07-15") },
   { "_id" : 4, year: 2017, name: "New Years", date: new Date("2017-01-01") },
   { "_id" : 5, year: 2017, name: "Ice Cream Day", date: new Date("2017-07-16") }
] )



'等价于sql查询'
`
SELECT *, holidays
FROM absences
WHERE holidays IN (
   SELECT name, date
   FROM holidays
   WHERE year = 2018
);
`
db.absences.aggregate( [
   {
      $lookup:
         {
           from: "holidays",
           pipeline: [
              { $match: { year: 2018 } },	// 筛选 集合holidays中符合文档
               // 映射文档中的date字段为：{name:,date:}的形式
              { $project: { _id: 0, date: { name: "$name", date: "$date" } } },
               // 只保留映射文档中的date字段，其他都删除
              { $replaceRoot: { newRoot: "$date" } }
           ],
           as: "holidays"
         }
    }
] )
```



```json
{
  _id: 1,
  student: 'Ann Aardvark',
  sickdays: [
    ISODate("2018-05-01T00:00:00.000Z"),
    ISODate("2018-08-23T00:00:00.000Z")
  ],
  holidays: [
    { name: 'New Years', date: ISODate("2018-01-01T00:00:00.000Z") },
    { name: 'Pi Day', date: ISODate("2018-03-14T00:00:00.000Z") },
    { name: 'Ice Cream Day', date: ISODate("2018-07-15T00:00:00.000Z")
    }
  ]
},
{
  _id: 2,
  student: 'Zoe Zebra',
  sickdays: [
    ISODate("2018-02-01T00:00:00.000Z"),
    ISODate("2018-05-23T00:00:00.000Z")
  ],
  holidays: [
    { name: 'New Years', date: ISODate("2018-01-01T00:00:00.000Z") },
    { name: 'Pi Day', date: ISODate("2018-03-14T00:00:00.000Z") },
    { name: 'Ice Cream Day', date: ISODate("2018-07-15T00:00:00.000Z")
    }
  ]
}
```







###### 案列五：关联子查询

```javascript
// restaurants(饭店)表
db.restaurants.insertMany( [
   {
      _id: 1,
      name: "American Steak House",
      food: [ "filet", "sirloin" ],
      beverages: [ "beer", "wine" ]	// 饮料
   },
   {
      _id: 2,
      name: "Honest John Pizza",
      food: [ "cheese pizza", "pepperoni pizza" ],
      beverages: [ "soda" ]
   }
] )

// orders(订单)表
db.orders.insertMany( [
   {
      _id: 1,
      item: "filet",
      restaurant_name: "American Steak House"
   },
   {
      _id: 2,
      item: "cheese pizza",
      restaurant_name: "Honest John Pizza",
      drink: "lemonade"
   },
   {
      _id: 3,
      item: "cheese pizza",
      restaurant_name: "Honest John Pizza",
      drink: "soda"
   }
] )


// The match is performed before the pipeline is run.
'查询操作'
db.orders.aggregate( [
   {
      $lookup: {
         from: "restaurants",
         localField: "restaurant_name",	// 第一个查询条件：orders.restaurants_name == restaurants.name
         foreignField: "name",
         // let命名变量
         let: { orders_drink: "$drink" },//是如何知道这个drink字段是到orders表中访问，而不是restaurants表中？
         pipeline: [ {
            $match: {
               // 执行以下表达式：饭店提供的饮料beverages必须存在订单要求的饮料drink
                // $表示取后面字段在某表中所对应的值
               $expr: { $in: [ "$$orders_drink", "$beverages" ] }
            }
         } ],
         as: "matches"
      }
   }
] )

// 等价于
db.orders.aggregate( [
   {
      $lookup: {
         from: "restaurants",
         let: { orders_restaurant_name: "$restaurant_name",
                orders_drink: "$drink" },
         pipeline: [ {
            $match: {
               $expr: {
                  $and: [
                     { $eq: [ "$$orders_restaurant_name", "$name" ] },
                     { $in: [ "$$orders_drink", "$beverages" ] }
                  ]
               }
            }
         } ],
         as: "matches"
      }
   }
] )



// The previous examples correspond to this pseudo-SQL statement:
SELECT *, matches
FROM orders
WHERE matches IN (
   SELECT *
   FROM restaurants
   WHERE restaurants.name = orders.restaurant_name
   AND restaurants.beverages = orders.drink
);
```



```json

{
   "_id" : 1, "item" : "filet",
   "restaurant_name" : "American Steak House",
   "matches" : [ ]
}
{
   "_id" : 2, "item" : "cheese pizza",
   "restaurant_name" : "Honest John Pizza",
   "drink" : "lemonade",
   "matches" : [ ]
}
{
   "_id" : 3, "item" : "cheese pizza",
   "restaurant_name" : "Honest John Pizza",
   "drink" : "soda",
   "matches" : [ {
      "_id" : 2, "name" : "Honest John Pizza",
      "food" : [ "cheese pizza", "pepperoni pizza" ],
      "beverages" : [ "soda" ]
   } ]
}
```















### 条件操作符

```javascript
$gt -------- greater than  >

$gte --------- gt equal  >=

$lt -------- less than  <

$lte --------- lt equal  <=

$ne ----------- not equal  !=

$eq  --------  equal  =
    
    
// db.col.find({likes : {$lt :200, $gt : 100}})
    
    
    
// mongoDb3.2 以上版本新增了位运算进行计算；将数字转换成二进制后，按位进行位运算：
bit        1  1  1  1  1  1  1  1 共8位
position   7  6  5  4  3  2  1  0  找到指定位数

//$bitsAllClear 所有指定为都为 0。
db.user.find({"bitData":{$bitsAllClear:[1,4]}}) 将二进制的第 2 位以及第 5 位上为 0 的匹配出来。

// $bitsAllSet 所有指定的都为 1。
db.user.find({"bitData":{$bitsAllSet:[1,4]}}) 将二进制的第 2 位以及第 5 位上为 1 的匹配出来。

// $bitsAnyClear 任意一位都为 0 的匹配出来与 $bitsAllClear 一致。
// $bitsAnySet 任意一位都为 1 的匹配出来与 $bitsAllSet 一致。

// 还有一种就是直接通过数字进行位运算 即位语言运算符中的 & 一致。
db.user.find({"bitData":{$bitsAllClear:8}}) 即 bitData 这个列与 8 数字进行 & 位运算结果为 0 的显示出来。
db.user.find({"bitData":{$bitsAllSet:8}}) 即 bitData 这个列与 8 数字进行 & 位运算结果不为 0 的显示出来。

//通过数字进行计算的话：
 $bitsAllClear 与 $bitsAnyClear 一致。
 $bitsAllSet 与 $bitsAnySet一致。
```







### $type操作符

```javascript
// $type操作符是基于BSON类型来检索集合中匹配的数据类型，并返回结果

db.col.find({"title" : {$type : 2}})
// 等价于下行，因为查表 2所对应的就是'string'
db.col.find({"title" : {$type : 'string'}})

```

| **类型**                | **数字** | **备注**         |
| :---------------------- | :------- | :--------------- |
| Double                  | 1        |                  |
| String                  | 2        |                  |
| Object                  | 3        |                  |
| Array                   | 4        |                  |
| Binary data             | 5        |                  |
| Undefined               | 6        | 已废弃。         |
| Object id               | 7        |                  |
| Boolean                 | 8        |                  |
| Date                    | 9        |                  |
| Null                    | 10       |                  |
| Regular Expression      | 11       |                  |
| JavaScript              | 13       |                  |
| Symbol                  | 14       |                  |
| JavaScript (with scope) | 15       |                  |
| 32-bit integer          | 16       |                  |
| Timestamp               | 17       |                  |
| 64-bit integer          | 18       |                  |
| Min key                 | 255      | Query with `-1`. |
| Max key                 | 127      |                  |









### 正则|模糊查询

```javascript
// 查询 title 包含"教"字的文档：
db.col.find({title:/教/})

// 查询 title 字段以"教"字开头的文档：
db.col.find({title:/^教/})

// 查询 titl e字段以"教"字结尾的文档：
db.col.find({title:/教$/})

'上述可以写成下面这种形式'
db.posts.find({post_text:{$regex:"runoob",$options:"$i"}})


// name字段匹配正则表达式/^jo/i，但不匹配数组["john"]中的字符串
{name:{$regex:/^jo/i, $nin:['john']}}

// name字段匹配正则表达式 /^joe/i,/^jack/ 其中之一
{name:{$in:[/^joe/i,/^jack/}}



```







### limit与skip方法

```javascript
'skip，sort，和limit三者执行顺序和位置无关'
'但是在聚合aggregate中使用的时候，具有管道流的特质，执行顺序是按照位置关系顺序执行的'

// 使用limit()方法来读取指定数量的数据外，还可以使用skip()方法来跳过指定数量的数据
db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)
	// db.col.find({},{"title":1,_id:0}).limit(1).skip(1)


`
不要轻易使用Skip来做查询，否则数据量大了就会导致性能急剧下降，这是因为Skip是一条一条的数过来的，多了自然就慢了。

db.test.sort({"amount":1}).skip(100000).limit(10)  //183ms
db.test.find({amount:{$gt:2399927}}).sort({"amount":1}).limit(10)  //53ms
`
```





### sort

```javascript
'sort() 方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式'
'其中 1 为升序排列，而 -1 是用于降序排列'

db.col.find({},{"title":1,_id:0}).sort({"likes":-1})
//skip(), limilt(), sort()三个放在一起执行的时候，执行的顺序是先 sort(), 然后是 skip()，最后是显示的 limit()。
```



















































