- [标签](#标签)
- [纯文本](#纯文本)
- [嵌入](#嵌入)
- [属性Attribute](#属性attribute)
- [条件语句](#条件语句)
  - [case](#case)
  - [if](#if)
- [迭代](#迭代)
- [代码Code](#代码code)
- [混入Minxin](#混入minxin)
- [继承](#继承)
  - [替换](#替换)
  - [添加](#添加)
- [包含](#包含)
  - [案列一](#案列一)
  - [包含纯文本](#包含纯文本)

# 标签

```jsx
// 使用缩进来表示标签间的嵌套关系
ul
  li Item A
  li Item B
  li Item C

  
// 自闭合标签
  // 可以通过在标签后加上 / 来明确声明此标签是自闭合的
foo/
foo(bar='baz')/
    
<foo />
<foo bar="baz" />
```





# 纯文本

```jsx
// 一个很常见的坑就是控制渲染出的 HTML 中那些空格

p 这是一段纯洁的<em>文本</em>内容.
	// <p>这是一段纯洁的<em>文本</em>内容.</p>


p
  | 管道符号总是在最开头，
  | 不算前面的缩进。

```









# 嵌入

```jsx
- var title = "On Dogs: Man's Best Friend";
- var author = "enlore";
- var theGreat = "<span>转义!</span>";

h1= title
p #{author} 笔下源于真情的创作。
p 这是安全的：#{theGreat}
	// #{ 和 } 里面的代码也会被求值，转义，并最终嵌入到模板的渲染输出中
	// <p>这是安全的：&lt;span&gt;转义!&lt;/span&gt;</p>



// 里面可以是任何的正确的 JavaScript 表达式，您可以自由发挥。
- var msg = "not my inside voice";
p This is #{msg.toUpperCase()}



- var riskyBusiness = "<em>我希望通过外籍教师 Peter 找一位英语笔友。</em>";
.quote
  // 嵌入没有转义的文本进入模板中 !{}
  p 李华：!{riskyBusiness}



// 嵌入用 Pug 书写的标签
p.
  这是一个很长很长而且还很无聊的段落，还没有结束，是的，非常非常地长。
  突然出现了一个 #[strong 充满力量感的单词]，这确实让人难以 #[em 忽视]。
p.
  使用带属性的嵌入标签的例子：
  #[q(lang="es") ¡Hola Mundo!]
```











# 属性Attribute

```markdown
可以用逗号作为属性分隔符，不过不加逗号也是允许的。

```



```jsx
a(href='baidu.com') 百度
a(class='button' href='baidu.com') 百度
a(class='button', href='baidu.com') 百度

- var authenticated = true
body(class=authenticated ? 'authed' : 'anon')


// 属性很长时
input(
  type='checkbox'
  name='agreement'
  checked
)

input(data-json=`
  {
    "非常": "长的",
    "数据": true
  }
`)


// 太过奇怪的属性，请用引号括起来；如下列的 "(click)"
div(class='div-class' '(click)'='play()')


// 属性嵌入
- var url = 'pug-test.html';
a(href='/' + url) 链接


- var btnType = 'info'
- var btnSize = 'lg'
button(type='button' class=`btn btn-${btnType} btn-${btnSize}`)
```



```jsx
// 不转义的属性;需要使用 != 而不是 =。
div(escaped="<code>")
div(unescaped!="<code>")

<div escaped="&lt;code&gt;"></div>
<div unescaped="<code>"></div>



// 样式属性
a(style={color: 'red', background: 'green'})




// 类属性
- var classes = ['foo', 'bar', 'baz']
a(class=classes)
//- the class attribute may also be repeated to merge arrays
	a.bang(class=classes class=['bing'])


- var currentUrl = '/about'
a(class={active: currentUrl === '/'} href='/') Home
a(class={active: currentUrl === '/about'} href='/about') About


// &attributes 将一个对象转化为一个元素的属性列表
div#foo(data-bar="foo")&attributes({'data-foo': 'bar'})
<div id="foo" data-bar="foo" data-foo="bar"></div>
    
    
```





# 条件语句

## case

```jsx
- var friends = 10
case friends
  when 0
    p 您没有朋友
  when 1
    p 您有一个朋友
  default
    p 您有 #{friends} 个朋友

// 分支传递 (Case Fall Through)
- var friends = 0
case friends
  when 0
	//  Pug 中则是，传递会在遇到非空的语法块前一直进行下去。
  when 1
    p 您的朋友很少
  default
    p 您有 #{friends} 个朋友


- var friends = 0
case friends
  when 0
	// 如果您不想输出任何东西的话，您可以明确地加上一个原生的 break 语句：
    - break
  when 1
    p 您的朋友很少
  default
    p 您有 #{friends} 个朋友
```



## if

```jsx
 var user = { description: 'foo bar baz' }
- var authorised = false
#user
  if user.description
    h2.green 描述
    p.description= user.description
  else if authorised
    h2.blue 描述
    p.description.
      用户没有添加描述。
      不写点什么吗……
  else
    h2.red 描述
    p.description 用户没有描述
    
    
    
unless user.isAnonymous
  p 您已经以 #{user.name} 的身份登录。
  
if !user.isAnonymous
  p 您已经以 #{user.name} 的身份登录。
```





# 迭代

```jsx
ul
  each val, index in ['〇', '一', '二']
    li= index + ': ' + val


ul
  each val, index in {1:'一',2:'二',3:'三'}
    li= index + ': ' + val


- var values = [];
ul
  each val in values.length ? values : ['没有内容']
    li= val
// 等价于
- var values = [];
ul
  each val in values
    li= val
  else
    li 没有内容
    
    
- var n = 0;
ul
  while n < 4
    li= n++
```









# 代码Code

```jsx
- for (var x = 0; x < 3; x++)
  // 这里没有使用 "=" 表示item仅仅作为文本节点
  li item
  
<li>item</li>
<li>item</li>
<li>item</li>


-
  var list = ["Uno", "Dos", "Tres",
          "Cuatro", "Cinco", "Seis"]
each item in list
  // 注意这里的 “=” 表示要对item求值
  li= item


<li>Uno</li>
<li>Dos</li>
<li>Tres</li>
<li>Cuatro</li>
<li>Cinco</li>
<li>Seis</li>



// = 隐含着自动对代码进行转义
p= '这个代码被 <转义> 了！'
<p>这个代码被 &lt;转义&gt; 了！</p>


p!= '这段文字' + ' <strong>没有</strong> 被转义！'
<p>这段文字 <strong>没有</strong> 被转义！</p>
```





# 混入Minxin

```jsx
mixin pet(name)
  li.pet= name

ul
  +pet('猫')
  +pet('狗')
  +pet('猪')
/*
    <ul>
      <li class="pet">猫</li>
      <li class="pet">狗</li>
      <li class="pet">猪</li>
    </ul>
*/


// 混入块
mixin article(title)
  .article
    .article-wrapper
      h1= title
      if block
        block
      else
        p 没有提供任何内容。

+article('Hello world')

+article('Hello world')
  p 这是我
  p 随便写的文章
 /*
     <div class="article">
      <div class="article-wrapper">
        <h1>Hello world</h1>
        <p>没有提供任何内容。</p>
      </div>
    </div>

    <div class="article">
      <div class="article-wrapper">
        <h1>Hello world</h1>
        <p>这是我</p>
        <p>随便写的文章</p>
      </div>
    </div>
*/
 
  
  
// 剩余参数
mixin list(id, ...items)
  ul(id=id)
    each item in items
      li= item

+list('my-list', 1, 2, 3, 4)



// 用 &attributes 方法来传递 attributes 参数
mixin link(href, name)
  a(href=href)&attributes(attributes)= name

+link('/foo', 'foo')(class="btn")

```





# 继承

## 替换

```jsx
//- 父模板定义了整个页面的总体布局和结构，而扩展的模板只能为其特定的块添补或者替换内容


//- 父级模板
//- layout.pug
html
  head
    title 我的站点 - #{title}
    block scripts
      script(src='/jquery.js')
  body
    block content
    block foot
      #footer
        p 一些页脚的内容
```



```jsx
//- page-a.pug
extends layout.pug

//- 用来覆盖 父级模板 layout.png 中的block scripts
block scripts
  script(src='/jquery.js')
  script(src='/pets.js')

//- 用来覆盖 父级模板 layout.png 中的block content
block content
  h1= title
  - var pets = ['猫', '狗']
  each petName in pets
    include pet.pug


//- pet.pug
p= petName
```





```jsx
//- sub-layout.pug
//- 子级模板 用来覆盖 layout.png 中的block content
extends layout.pug

block content
  .sidebar
    block sidebar
      p 什么都没有
  .primary
    block primary
      p 什么都没有
      
      
//- page-b.pug
//- 孙子级模板 用来覆盖子级模板 sub-layout.pug 中的block content
extends sub-layout.pug

block content
  .sidebar
    block sidebar
      p 什么都没有
  .primary
    block primary
      p 什么都没有
```





## 添加

```jsx
// Pug 允许您去替换（默认的行为）、prepend（向头部添加内容），或者 append（向尾部添加内容）一个块。


//- layout.pug
html
  head
    block head
      script(src='/vendor/jquery.js')
      script(src='/vendor/caustic.js')
  body
    block content
    
    
    
//- page.pug
extends layout.pug

//- 这里将不再是替换父级模板中的 block head,而是向尾部添加
//- 可简写成：append head
block append head
  script(src='/vendor/three.js')
  script(src='/game.js')
    

```







# 包含

## 案列一

```jsx
//- 把另外的文件内容插入进来。

//- index.pug
doctype html
html
  include includes/head.pug
  body
    h1 我的网站
    p 欢迎来到我这简陋得不能再简陋的网站。
    include includes/foot.pug


//- includes/head.pug
head
  title 我的网站
  script(src='/javascripts/jquery.js')
  script(src='/javascripts/app.js')

//- includes/foot.pug
footer#footer
  p Copyright (c) foobar
```



```html
<!DOCTYPE html>
<html>

<head>
  <title>我的网站</title>
  <script src="/javascripts/jquery.js"></script>
  <script src="/javascripts/app.js"></script>
</head>

<body>
  <h1>我的网站</h1>
  <p>欢迎来到我这简陋得不能再简陋的网站。</p>
  <footer id="footer">
    <p>Copyright (c) foobar</p>
  </footer>
</body>

</html>
```





## 包含纯文本

```jsx
// -被包含的如果不是 Pug 文件，那么就只会当作文本内容来引入。
//- index.pug
doctype html
html
  head
    style
      include style.css
  body
    h1 我的网站
    p 欢迎来到我这简陋得不能再简陋的网站。
    script
      include script.js


/* style.css */
h1 {
  color: red;
}

// script.js
console.log('真了不起！');
```







```html
<!DOCTYPE html>
<html>

<head>
  <style>
    /* style.css */
    h1 {
      color: red;
    }
  </style>
</head>

<body>
  <h1>我的网站</h1>
  <p>欢迎来到我这简陋得不能再简陋的网站。</p>
  <script>
    // script.js
    console.log('真了不起！');
  </script>
</body>

</html>
```

