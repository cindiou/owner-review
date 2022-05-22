# 复习清单
圆角
	border-raidus
	border-top-left-radius
边框
	border-style
	border-width
	border-color

	border-image
	
	border-left

	border-spacing
	border-collapse

	table-layout

	outline

补充样式
	list-style

	white-space
		nowrap
		pre
		pre-wrap
		pre-line
	vertical-aligin

字体
	font-family
	font-weight
	font-size
	font-style

	text-decoration
	text-transform
	text-indent
	text-overflow

	text-align
	line-height

	letter-spacing
	word-spacing
	word-break
	word-wrap
背景 | 复合样式
	background
		color
		image
		repeat
		attachment
		position
		size
		origin
		clip
		
选择器
	!import > style > id > class > 标签 > * > 继承
	属性
	伪元素
	伪类
	层级
	结构
		nth-of-type
		nth-child
	继承
		文字相关可以被继承
		布局相关不能，除非显示inherit
	约分比较 | 权重比较



盒子模型
	box-sizing
	margin叠加 | 传递问题
	文字只出现在content区域
		margin-box | border-box | padding-box | content-box

伪类与伪元素


定位
	static
	relative

	positive
	fixed
		不一定相对于浏览器定位，对于父元素存在transition或performance等...
	sticky



overflow
	visible | hidden | auto | scroll
display | visibility

重置样式
默认样式
省略符号
	# 必须有一个固定的高
	overflow:hidden;
	white-space:nowrap;
	text-overflow:ellipsis


过渡 
	transition
		property
		duration
		delay
		timing-function
形变
	transform
		origin
		style
			flat | preserve-3d

		translate
			translateX
			translateY
		rotate
		skew
		scale

		backface-visibility
			visible | hidden
		perspective
		perspective-origin
		
		
动画
	animation
		name
		duration
		delay
		timing-function
		iteration-count
		fill-mode
			forwards
			backwards
			steps
		direction
		play-state
			running
			paused
渐变
		linear-gradient
			point | angle,color percentage
		radial-gradient
			color percentage
		conic-gradient
			conic-gradient(from 90deg at 60% 45%, red, yellow, green)
text-shadow
box-shadow
	insert? x y blur spread color	
mask
	url() repeat position/size		
box-reflect
	dir distance 渐变|遮罩


分栏布局
	column-count
		column-width
	column-gap
	column-rule
	column-span
flex
	flex-flow
		flex-direction
		flex-wrap
	justify-content
		
	align-items
	align-content
		# 注意区别
	flex
		grow
		shrink
		basic
	order
	align-self
grid
	template
		rows
		columns
		areas
	place-content
		align-content
		justify-content
			stretch
			start
			center
			end
			space-between
			space-around
			space-evenly
	place-items
		align-items
		justify-items
			stretch
			start
			end
			center
	gap
		grid-row-gip
		grid-column-gap
		
	area
		grid-column
			start
			end
		grid-row
	place-self


视口


流式布局 
	百分比布局
	宽高写死，空白部分间距填充
rem布局
	等比缩放
	em
	rem
		font-size
	

响应式
	

user-select: none | all | text
pointer-events

cursor
opacity
filter
	blur
	opacity
	contrast
	drop-shadow

	grayscale
	brightness
	saturate
clip-path
	circle
	ellipse
	polygen
	path

min-width
max-width



calc
min
max

var
attr

content
	url
	content:var(--a) var(--b)
	content:"(" attr(data-index) ")"
	content:"\1f4a1"

	counter-reset
	counter-increment
	counter


# 技巧
	img{display:block}

	a{display:block;width:100%;height:100%}
	label input[type=radio]{display:none}

  display:inline-block
	没有内容时默认存在一个行高；
	vertical-align:bottom;

	:hover
	可以用来捕捉鼠标范围
	:target/:checked
		可以用来步骤点击行为
			配合a标签，扩大选取
			配合label标签，扩大选取

	<p class="foo bar">Hello,World</p>
	.foo{color:red} <!--.foo.foo{color:red}-->
	.bar{color:blue}
		上述class样式，最终样式 只与声明样式时的上下顺序相关、而与class属性的书写的先后顺序无关；
		如果，要是先声明的样式.foo生效，可以重叠class样式、变相提高权重使其生效，如：.foo.foo.foo;该方法也可以 用在styled-component组件中 或 vue的style.scoped块中（vue作用域css的实现机制，导致了每个类的权重都变相提高了）

# 八股文
```markdown
选择器优先级
	如果优先级相同，则最后出现的样式生效；
	继承得到的样式的优先级最低；

	内联样式（也是行内样式；style属性） > 内部样式（style标签）、外部样式
	内部、外部样式表谁在后面谁生效

继承属性与不可继承的属性
	文本类的属性
		可继承
	布局相关
		不可继承
		text-decoration
		vertical-align

display:inline/inline-block/block
	inline
		挨在一起
		宽度由内容决定
		不可以设置width/height 或 垂直方向上的margin/padding
	block
		换行
		默认继承父元素的宽度
		可以设置宽高、margin/padding
	inline-block
		挨在一起
		宽度由内容决定
		可以设置宽高、margin/padding


隐藏元素的方法
	A.仍然占据页面空间
	B.仍然响应绑定事件

	hidden
	display:none
		不占据页面空间，当仍存在dom树中

	visibility:hidden
	clip-path:circle()
	transform:scale(0,0)
		A

	opacity:0
		A | B

	z-index
	position


visiblity:hidden | display:none的区别
	是否仍然占据页面空间，即：仍存在在渲染树中
	是否是继承属性
		子元素是否可以逃脱
	重流|重绘
	屏幕阅读器


@import与link
	用途：：@import只能引入css,且不能兼容低版本的浏览器
	link是标签，意味着可以js操控

	加载顺序与优先级：
		link引入的css并行加载，@import是页面加载后加载（无样式内容闪烁）；
			测试后，不存在加载顺序的区别；样式优先级也是源自它们在html页面中的先后顺序
	

transition | animation
	是否需要手动触发


requestAnimationFrame
	浏览器在下次重绘之前调用指定的回调函数更新动画

	回调函数执行次数通常与 浏览器屏幕刷新次数 相匹配。
	屏幕刷新频率（次数）： 屏幕每秒出现图像的次数。普通笔记本为60Hz。

	CPU节能
		页面失活，停止执行
	函数节流
		更好的节省函数执行的开销，一个刷新间隔内函数执行多次时没有意义

	setTimeout | setInterval
		不够精确
			加入到等待队列；但是等待队列中可能存在很多任务，导致回调函数迟迟没有被执行
		间隔过短，丢帧；不能符合浏览器的刷新频率


盒子模型
	box-sizing



translate改变位置而不是使用定位
	改变transform或opacity不会触发浏览器重新布局（reflow）或重绘（repaint），只会触发复合（compositions）。
	
	⽽改变绝对定位会触发重新布局，进⽽触发重绘和复合。transform使浏览器为元素创建⼀个 GPU 图层，但改变绝对定位会使⽤到 CPU


display:inline-block间隙问题
span之间的空格是如何产生的？
	浏览器会把inline内联元素间的空白字符（空格、换行、Tab等）渲染成一个空格;

	解决方法：
		1.不换行书写
		2.float:left
		3.父元素：font-size:0;子元素：font-size:16px;
		4.父元素：letter-spacing:-8px;子元素：letter-spacing:normal;


CSS新特性


替换元素
	具体在页面的呈现效果不是由CSS决定的，是独立于CSS的；CSS可以影响其位置，但不会影响其本身的内容；
		iframe
		img
		video
	默认尺寸
		固有尺寸
		HTML尺寸
		CSS尺寸
	在很多CSS属性上有自己的表现规则
		vertical:baseline
	所有的替换元素都是内联水平元素



图片格式
	BMP
	GIF
	JPEG
	SVG
	PNG
	WEBP
		同时支持有损和无损压缩的
		相同质量的图片，WebP具有更小的文件体积

CSSSprites
	减少网页的http请求
	减少图片的字节

	制作|维护|使用，都比较麻烦


物理像素 | 逻辑像素
	图片失真


line-height
	单行文本居中
	一个容器没有设置高度，那么撑开容器高度的是 line-height

	单位
		em
		px
		百分数
		数值


CSS优化和提高性能的方法
	css压缩

	尽量少的去对标签进行选择，而是用class。
	选择器优化嵌套，尽量避免层级过深
	不使用@import前缀，它会影响css的加载速度

	css雪碧图，同一页面相近部分的小图标
	不滥用web字体

CSS预处理器 | 后处理器
预处理器
	为CSS注入可编程的能力，方便复用、更好的生成CSS文件
		嵌套
		变量
		逻辑
后处理器
	PostCSS:前缀、浏览器兼容




媒体查询
	媒体类型与作用条件 限制样式的作用范围；
	响应式页面
		link
		@media


判断元素是否处于可视区域
	getBoundingClientRect
	IntersectionObserver

	offsetTop < window.innerHeight + window.scrollY


CSS工程化
	宏观设计
		样式重置
		文件组织
			全局样式文件
			根据使用的框架选用哪种CSS模块化
	webpack
		编码
			预处理器
			浏览器适配
		构建 | 代码分割
			.css文件
			<style>标签
		可维护性


常见的CSS单位
	分辨率对页面影响
	px
	ch/ex

	%
		一般认为子元素的百分比相对于直接父元素。
		也有相对于自身的情况比如（border-radius、translate等）
	rem/em
	vw/vh
	vmin/vmax

移动端适配
	像素密度
	屏幕大小
		媒体查询 | 响应式设计

浮动
	影响
		脱离文档流
		只影响后面的
		宽度由内容决定
		不会遮挡文字 | 图文混排

		如何撑起父元素
			BFC ：float/display:inline-block
			空元素 | ::after伪类
	清除浮动
	clear
		只有块级元素才有效的
		“元素盒子的边不能和前面的浮动元素相邻”，避免浮动元素对该元素的影响

BFC规范
	独立的容器；与外界隔离
	特点
		处于BFC中的块级盒子上下排布
		块级盒子的margin box一定与BFC的border box左边相互接触
		处于相同BFC中的块级盒子发生margin重叠

		BFC盒子不会相互影响与重叠（例如：BFC不会与float盒子重叠）
		BFC盒子会计算内部float元素的高度
	生成条件
	作用
		margin重叠
		高度塌陷
		两栏自适应布局

层叠上下文
	七阶层叠水平
	影响
		层叠元素要比普通元素层叠优先级更高
		层叠上下文自成一个层叠世界
	层叠准则
		谁大先上
		后来居上
	生成条件
		天生派
		传统派
		改革派
	
	z-index


定位
	无依赖的绝对、固定定位

	fixed
		指定元素相对于屏幕视⼝（viewport）的位置来指定元素位置。元素的位置在屏幕滚动时不会改变
	absolute
		包含块的pandding box
	relative
		无侵入性
	sticky
		粘性定位:在 position:relative 与 position:fixed 定位之间切换;
		
		指定 top, right, bottom 或 left 四个阈值其中之一，才可使粘性定位生效。否则其行为与相对定位相同。
		


float/display/position之间的关系
	1."position:absolute"和"position:fixed"优先级最高，有它存在的时候，浮动不起作用
	2.如果position的值为relative并且float属性的值存在，则relative相对于浮动后的最终位置定位。


absolute与fixed
共同
	块状化
	破坏流
	伸缩性与包裹性
差异
	包含块
	滚动条存在时，是否跟随父元素移动


```


# 常见CSS题目
## 简单题
```markdown
画扇形
	border-radius是相对于border-box
画三角形


宽高自适应的正方形
	width:20%;height:20vh;

	利用元素的margin/padding百分比是相对父元素width的性质来实现：

	利用子元素的margin-top的值来实现：
		.square {
			width: 30%;
			overflow: hidden;
			background: yellow;
		}
		.square::after {
			content: '';
			display: block;
			margin-top: 100%;
		}

画一条0.5px的线
	transform: scale(0.5,0.5);
	采用meta viewport的方式


设置小于12px的字体
	transform: scale
	图片


<div id="container" data-device={{window.devicePixelRatio}}></div>
如何解决1px问题
	在一些 Retina屏幕 的机型上，移动端页面的 1px 会变得很粗，呈现出不止 1px 的效果

	直接写 0.5px
		兼容性不行
		#container[data-device="2"] {
			border:0.5px solid #333
		}

	伪元素先放大后缩小
		#container[data-device="2"] {
				position: relative;
		}
		#container[data-device="2"]::after{
					position:absolute;
					top: 0;
					left: 0;
					width: 200%;
					height: 200%;
					content:"";
					transform: scale(0.5);
					transform-origin: left top;
					box-sizing: border-box;
					border-bottom: 1px solid #333;
		}

	viewport 缩放来解决

```



## 两栏布局
```markdown
宽度自适应
高度自适应
	等高布局
		border
		padding+margin
		table-cell
		flex

.outer{
	height:100px;
	&::after{
		content:"";
		display:block;
		clear:both;
	}
	.left{
		width:100px;
		height:100px;
		float:left;
		background-color:aqua;
	}
	.right{
		height:100px;
		background-color:lime;

		/*第一种:auto*/
		width:auto;
		margin-left:100px;
		
		/*第二种：BFC的区域不会与浮动元素发生重叠*/
		overflow:hidden
	}
}

3.display:flex
4.position:absolute
	margin-left

	left
	right
	top
	bottom

```

## 三栏布局
```markdown
1.position:absolute
2.float
	center -> margin:0 right 0 left;
3.display:flex


双飞翼布局:整体宽度100%
	center -> margin:0 right 0 left;
	left -> margin-left:-100%
	roght -> margin-right:-right
圣杯布局:整体宽度100%-left-right
	


```


## 垂直居中布局
```markdown
1.
	line-height
	text-align

2.
	::before
	::after

	vertical-align
	text-justify

3.
	aosolute + 
		top:calc(50%-高度/2);left:calc(50%-宽度/2)
		margin
		transform
		格式化宽度 + margin:auto

4.flex grid

5.display:table | display:tabel-cell
```


```vue
<template>
	<div class="cs-x">
		<span>Hello</span>
		<span class="placeholder"></span>
	</div>
</template>

<style>
	.cs-x{
		width:200px;
		height:200px;
		background-color: red;
		
		text-align:justify;
	}
	.cs-x::after,.cs-x::before{
		content:"";
		display:inline-block;
		
		vertical-align:middle;
	}
	.cs-x::before{
		height:100%
	}

	.cs-x::after{
		width:100%;
	}

	.cs-x span{
		display:inline-block;
		vertical-align:middle;
	}
</style>
```


## table布局
```markdown
table-layout:fixed;
text-align: center;
vertical-align: middle;

display:table-caption;

display:table
	 table的宽度默认由内容的宽高撑开，如果table设置了宽度，宽度默认被它里面的td平均分，如果给某一个td设置宽度，那么table剩余的宽度会被其他的td平均分（有点类似flex布局）
display:table-row
	tr中的td默认高度会继承tr的高度，若给任一td设置了高度，其他td的高度也同样变高。适合多列等高布局
	给tr设置高度只起到min-height的作用，默认会平分table的高度。
	设置宽度、margin、都不起作用
display:table-cell
	td默认继承tr的高度，且平分table的宽度
	对设置了float、absolute的元素不起作用

多栏布局
	一边定宽，一边自适应
	等高
垂直居中

```
