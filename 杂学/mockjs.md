- [语义规范](#语义规范)
  - [模板定义规范](#模板定义规范)
    - [注意](#注意)
    - [生成规则和示例：](#生成规则和示例)
  - [占位符定义规范](#占位符定义规范)
    - [注意：](#注意-1)
    - [path](#path)
      - [绝对路径](#绝对路径)
      - [相对路径](#相对路径)
- [静态方法](#静态方法)
- [Random详解](#random详解)
  - [basic](#basic)
  - [date](#date)
  - [image](#image)
  - [color](#color)
  - [Text](#text)
  - [Name](#name)
  - [web](#web)
  - [Address](#address)
  - [Helper](#helper)
  - [唯一标识](#唯一标识)

# 语义规范
- 数据模板定义规范（Data Template Definition，DTD）
- 数据占位符定义规范（Data Placeholder Definition，DPD）


## 模板定义规范
**数据模板中的每个属性由 3 部分构成：属性名、生成规则、属性值：**
  'name|rule': value


### 注意
- 生成规则 有 7 种格式：
  - 'name|min-max': value
    - 'name|min-max.dmin-dmax': value
    - 'name|min-max.dcount': value
  - 'name|count': value
    - 'name|count.dmin-dmax': value
    - 'name|count.dcount': value
  - 'name|+step': value
- 生成规则 的 含义 需要依赖 属性值的类型 才能确定。
- 属性值 中可以含有 @占位符。
- 属性值 还指定了最终值的初始值和类型。


### 生成规则和示例：
```markdown
'name|min-max': string
'name|count': string


'name|+1': number
  属性值自动加 1，初始值为 number。
'name|min-max': number
  属性值 number 只是用来确定类型。
'name|min-max.dmin-dmax': number

'name|1': boolean
  随机生成一个布尔值，值为 true 的概率是 1/2，值为 false 的概率同样是 1/2。
'name|min-max': value
  随机生成一个布尔值，值为 value 的概率是 min / (min + max)，值为 !value 的概率是 max / (min + max)。


'name|count': object
  从属性值 object 中随机选取 count 个属性。
'name|min-max': object
  随机选取 min 到 max 个属性。


'name|1': array
  从属性值 array 中随机选取 1 个元素，作为最终值。
'name|+1': array
  从属性值 array 中顺序选取 1 个元素，作为最终值。
'name|min-max': array
  通过重复属性值 array 生成一个新数组，重复次数大于等于 min，小于等于 max。
'name|count': array
  通过重复属性值 array 生成一个新数组，重复次数为 count。


'name': function
  执行函数 function，取其返回值作为最终的属性值，函数的上下文为属性 'name' 所在的对象。
'name': regexp
  用于生成自定义格式的字符串。
```

```javascript
Mock.mock({
    'regexp1': /[a-z][A-Z][0-9]/,
    'regexp2': /\w\W\s\S\d\D/,
    'regexp3': /\d{5,10}/
})
// =>
{
    "regexp1": "pJ7",
    "regexp2": "F)\fp1G",
    "regexp3": "561659409"
}


Mock.mock({
  'foo': 'Syntax Demo',
  'name': function() {
    return this.foo
  }
})
/*
  {
    "foo": "Syntax Demo",
    "name": "Syntax Demo"
  }
*/
```





## 占位符定义规范
占位符 只是在属性值字符串中占个位置，并不出现在最终的属性值中。
```markdown
@占位符
@占位符(参数 [, 参数])
```

### 注意：
- 用 @ 来标识其后的字符串是 占位符。
- 占位符 引用的是 Mock.Random 中的方法。
- 通过 Mock.Random.extend() 来扩展自定义占位符。
- 占位符 也可以引用 数据模板 中的属性。
- 占位符 会优先引用 数据模板 中的属性。
- 占位符 支持 相对路径 和 绝对路径。


### path
#### 绝对路径
```javascript
Mock.mock({
  "foo": "Hello",
  "nested": {
    "a": {
      "b": {
        "c": "Mock.js"
      }
    }
  },
  "absolutePath": "@/foo @/nested/a/b/c"
})

/*
  {
    "foo": "Hello",
    "nested": {
      "a": {
        "b": {
          "c": "Mock.js"
        }
      }
    },
    "absolutePath": "Hello Mock.js"
  }
*/
```


#### 相对路径
```javascript
Mock.mock({
  "foo": "Hello",
  "nested": {
    "a": {
      "b": {
        "c": "Mock.js"
      }
    }
  },
  "relativePath": {
    "a": {
      "b": {
        "c": "@../../../foo @../../../nested/a/b/c"
      }
    }
  }
})

/*
  {
    "foo": "Hello",
    "nested": {
      "a": {
        "b": {
          "c": "Mock.js"
        }
      }
    },
    "relativePath": {
      "a": {
        "b": {
          "c": "Hello Mock.js"
        }
      }
    }
  }
*/
```





# 静态方法
```markdown
Mock.mock( rurl?, rtype?, template|function( options ) )
  rurl
    表示需要拦截的 URL，可以是 URL 字符串或 URL 正则。例如 /\/domain\/list\.json/、'/domian/list.json'。

  rtype
    表示需要拦截的 Ajax 请求类型。例如 GET、POST、PUT、DELETE 等。

  options
    指向本次请求的 Ajax 选项集，含有 url、type 和 body 三个属性


Mock.setup({
    # 指定被拦截的 Ajax 请求的响应时间，单位是毫秒
    timeout: 400,
})



```

```javascript
var Random = Mock.Random
Random.email()
// => "n.clark@miller.io"
Mock.mock('@email')
// => "y.lee@lewis.org"
Mock.mock( { email: '@email' } )
// => { email: "v.lewis@hall.gov" }


Random.extend({
    constellation: function(date) {
        var constellations = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
        // 这里的this不是指向这个对象
        // 指向的应该是Mock.Random
        return this.pick(constellations)
    }
})
Random.constellation()
// => "水瓶座"
Mock.mock('@CONSTELLATION')
// => "天蝎座"
Mock.mock({
    constellation: '@CONSTELLATION'
})
// => { constellation: "射手座" }
```



# Random详解
## basic
```markdown
Random.boolean( min?, max?, current? )

Random.natural( min?, max? )
  自然数的范围是不小于0
Random.integer( min?, max? )
Random.float( min?, max?, dmin?, dmax? )
Random.range( start?, stop, step? )

Random.character( pool? )
  返回一个随机字符。
  Random.character()
  Random.character( 'lower/upper/number/symbol' )
  Random.character( pool )
Random.string( pool?, min?, max? )
  返回一个随机字符串。
  Random.string()
  Random.string( length )
  Random.string( min, max )
  Random.string( pool, length )
  Random.string( pool, min, max )
```


## date
```markdown
Random.datetime( format? )
  默认值为 yyyy-MM-dd HH:mm:ss。
Random.date( format? )
Random.time( format? )

Ranndom.now( format )
```


## image
```markdown
Random.image( size?, background?, foreground?, format?, text? )
生成一个随机的图片地址。

  background:指示图片的背景色
  foreground:指示图片的前景色（文字）
  format:指示图片的格式。默认值为 'png'，可选值包括：'png'、'gif'、'jpg'。


Random.dataImage( size?, text? )
生成一段随机的 Base64 图片编码。
```


## color
```markdown
Random.color()

Random.hex()
Random.rgb()
Random.rgba()
Random.hsl()
```


## Text
```markdown
Random.paragraph( min?, max? )
  随机生成一段文本。
  Random.paragraph( len )
  Random.paragraph( min, max )
Random.cparagraph( min?, max? )
  随机生成一段中文文本。

Random.sentence( min?, max? )
  随机生成一个句子，第一个单词的首字母大写。
Random.csentence( min?, max? )

Random.title( min?, max? )
  随机生成一句标题，其中每个单词的首字母大写。
Random.ctitle( min?, max? )


Random.word( min?, max? )
  随机生成一个单词。
    Random.string的简化版本，只输出小写英文字母
    Random.string("lower",min?,max?)
Random.cword( pool?, min?, max? )
  随机生成一个汉字。
  Random.cword( length )
  Random.cword( min, max )
  Random.cword( pool )
  Random.cword( pool, length )
  Random.cword( pool, min, max )
```



## Name
```markdown
Random.name( middle? )
Random.first()
Random.last()

中文姓名的读取顺序
Random.cname( middle? )
Random.cfirst()
Random.clast()
  随机生成一个常见的中文姓名。
```


## web
```javascript
Random.ip()
Random.email( domain? )
  Random.email('nuysoft.com')
  // => "h.pqpneix@nuysoft.com"

Random.url( protocol?, host? )
  Random.url()
  // => "mid://axmg.bg/bhyq"
  Random.url('http')
  // => "http://splap.yu/qxzkyoubp"
  Random.url('http', 'nuysoft.com')
  // => "http://nuysoft.com/ewacecjhe"
Random.protocol()
Random.domain()
```


## Address
```javascript
Random.region()
// => "华北"

Random.province()
// => "黑龙江省"

Random.city()
// => "唐山市"
Random.city(true) // 指示是否生成所属的省。
// => "福建省 漳州市"

Random.county()
// => "上杭县"
Random.county(true)
// => "甘肃省 白银市 会宁县"

Random.zip() // 随机生成一个邮政编码（六位数字）。
// => "908812"
```

## Helper
```javascript
Random.capitalize( word )
Random.upper( str )
Random.lower( str )

Random.pick( arr )
  // 从数组中随机选取一个元素，并返回。
Random.shuffle( arr )
```


## 唯一标识
```javascript
Random.guid() // 随机生成一个 GUID。
// => "662C63B4-FD43-66F4-3328-C54E3FF0D56E"

Random.id() // 随机生成一个 18 位身份证。

Random.increment( step? )  // 生成一个全局的自增整数。
```