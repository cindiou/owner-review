- [初步学习](#初步学习)
  - [变量](#变量)
  - [变量类型](#变量类型)
  - [嵌套调用父选择器](#嵌套调用父选择器)
  - [嵌套属性](#嵌套属性)
  - [mixin](#mixin)
  - [extend](#extend)
  - [import](#import)
  - [插值](#插值)
  - [控制指令](#控制指令)

# 初步学习

```bash
mk "text" && cd &_

sass sass/style.sass:css/style.css
sass --watch sass:css	--style compact
	# 监视sass文件夹下的.sass文件，并自动编译成.css
	
	
expanded
nested
compact
compressed

.scss # 学习
.sass

```





## 变量

```scss
$primary-color:#123456
$primary-border:1px solid $primary-color
    
div.box{
	color:$primary-color
        // $primary-color引用字符串时，需要引号包围
}
```





## 变量类型

```scss
// sass -i
type-of
	type-of(1)	// "number"
	type-of(1px) // "number"
	type-of(1em) // "number"
	type-of(50%)	// "number"

	type-pf('Hello') // "string"
	type-of(1px solid red) // "list"
	type-of(#123) // "color"
	type-of(red) // "color"


// 数字
	// 空格不能省略
/*
	abs
	round
	cell
	floor
	percentage
	min
	max

*/
	
2 * 3
2 + 3
(2/4) 	// 必须带()

5px * 2
// 10px
5px * 2px
// 10px * px
(10px / 2px)
// 5

(2 + 4) * 2px
// 12px




// 字符串
+ 

// $greeting:"Hello,World!"
to-upper-case()
to-lower-case()
str-length()
str-index($grerting,"Hello")	// 索引值从1开始
str-insert($greeting,".net" 14)



// list
// 空格或逗号分隔
border:1px solid red

padding:5px 10px,5px 0	// 嵌套列表
padding:(5px 10px) (5px 0)


length()	// 返回列表个数，索引从1开始
nth(5px 10px,1) // 第几项的值
// 5px

index(1px solid red,solid)	// 值为val在第几项
// 2

append(5px 10px,5px,space)
// (5px 10px 5px)
join(5px 10px,5px 0,comma)
// (5px,10px,5px,0)



// map
$map:(key1:val,key2:val2)
   
length($map)
map-get($map,key1)
    
map-keys($map)
// (key1,key2)

map-values($map)
map-has-key($map,key1)
    
map-merge($map,(key3:val3))
map-remove($map,key1,key2)

    
    
// Boolean
5px > 4px
(5px > 4px) and (5px < 6px)    // and,or,not
(5px > 4px) or (5px < 6px)   
not(5px > 4px)


// 颜色
rgb()
rgba()
hsl()
hsla()
lighten()
darken()
    desaturate() saturate()
    opacify()	transparentize

```





## 嵌套调用父选择器

```scss
ul{
    li{
        &:hover{
            
        }
    }
    & &-text{
        font-size:15px
    }
}

/*
ul li:hover{

}
ul ul-text{
	font-size
}

*/
```





## 嵌套属性

```scss
body{
    font:{
        fomaily:;
        size:;
        weight:;
    }
    
    border:1px solid red {
        left:0;
        right:0;
    }
}
```





## mixin

```scss
@mixin alert($color,$bgColor){
    color:$color;
    background-color:$bgColor;
    
    a{
        color:$color
    }
}


.alert-warning{
    @include alert(#123,#456)
    @include alert($bgColor:#456,$color:#123)
}
```





## extend

```scss
.alert{
    padding:;
}

.alert a{
    font-weight:;
}

.alert-info{
    @extend .alert;
    background-color:#451236
}

/*
.alert,.alert-info{
	padding:;
}
.laert a,.alert-info a{
	font-weight:;
}

.alert-info{
	bahcground-color:#451236;
}
*/
```





## import

```scss
// 文件名必须“_"开头，这样就会当做partial文件，而不会编译

/*
_base.scss
style.scss
*/

// style.scss 文件
@import "base"	// 导入的时候，不需要以_开头
```









## 插值

```scss
$version:"0.0.1"
/* 项目的当前版本是：#{$version}*/
    
$name:"info";
$attr:"border";
.alert-#{$name}{
    #{$attr}-color:#ccc;
}


```





## 控制指令

```scss
$theme:"dark"
    body{
        @if $theme == dark {
        background-color:black;
        } @else if $theme == light {
            background-color:white
                } @else {

                    }
    }


$columns:4
    @for $i form 1 through $columns { // through会包含结尾值,to则不会包含
        .col-#{$i} {
            width:100% / $columns * $i
        }
    }
      

$icons:success error warn;
    @each $icon in $icons {
        background-color:url(../images/icons/#{$icon}.png);
    }

$i:6;
@while $i > 0 {
    .item-#{$i} {
        width:5px * $i;
    }
    $i:$i - 2;// 注意这里的空格
}

$colors:(dark:#000,light:#fff)
@function color($key){
    @if not map-has-key($colors,$key) {
        @error "在$colors不存在该key";
    }
    @return map-get($colors,$key)
}
```

