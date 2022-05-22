- [普通HTML](#普通html)
- [视口](#视口)
- [如何解决图片过大加载慢的问题](#如何解决图片过大加载慢的问题)
- [拖放事件](#拖放事件)
- [canvas](#canvas)
- [svg](#svg)
- [Worker线程](#worker线程)
- [IntersectionObserver | MutationObserver](#intersectionobserver--mutationobserver)
- [Web Components](#web-components)
- [dom相关](#dom相关)
- [CSS操作](#css操作)
- [剪贴操作](#剪贴操作)

# 普通HTML 
```markdown
src和href区别

语义化
	对结构化的内容采用合适的标签处理
		seo优化
		方便其他设备解析
		页面结构清晰，方便团队维护
	strong b
	em i

DOCTYPE 文档类型
	告诉浏览器应该以什么类型的文档来解析
	CSS1Compat
		以其支持的最高标准呈现页面
	BackCompat
		较宽松的向后兼容的方式
		模拟老式浏览器的行为，以防止老站点无法工作；
	document.compatMode



script标签中defer和async的区别
	defer 在 DomContentLoaded之前
meta标签
	charset
	http-equiv
	name
		viewport
		keywords
		description
		author
		robots


块级标签 与 行内标签


HTML5有哪些更新
	语义化标签
	媒体标签
	表单标签 
	DOM查询
	Web存储
	拖放
	canvas 与 SVG
		分辨率
		事件处理
		复杂度过高
	websocket
	History API 



window.load事件 与 document.DOMContentLoaded事件
	执行顺序 | 时机

link标签 与 @import引入
	rel
		stylesheet
		icon
		dns-prefetch
		preconnect
		prerender

		preload
			所有预下载的资源，只是下载到浏览器的缓存，并没有执行。
			as
				style | script | image | media | doucment | font
			media
			type
		prefetch


iframe
	数据传输
	共享代码
	局部刷新
	第三方介入

	阻塞主页面的 onload 事件
	无法被一些搜索引擎索识别
	会产生很多页面，不容易管理

	
img | 响应式图像
	loading
		lazy
		auto
		eager
	体积 | 像素密度 | 视觉风格

	srcset
		如果srcset属性都不满足条件，那么就加载src属性指定的默认图像。
	sizes
		不同尺寸的屏幕，显示不同大小的图像，


	<picture>
	<map><area></area></map>


a
	rel
	download



浏览器乱码
	编写html的编码 与 声明html的编码
	声明html的编码 与 数据库返回数据的编码
渐进增强 与 优雅降级
	主要是针对低版本的浏览器进行页面重构，保证基本的功能情况下，再针对高级浏览器进行效果、交互等方面的改进和追加功能，以达到更好的用户体验。
	 一开始就构建完整的功能，然后再针对低版本的浏览器进行兼容。




HTML 离线存储
SeviceWorker 与 WebWorker


```


# 视口
```markdown
设备上一个css像素代表多少个物理像素
	分辨率增大了，但屏幕尺寸并没有变大多少
	devicePixelRatio

	布局视口 layout viewport
		document.documentElement.clientWidth
		默认值：980px
		width=device-width
			布局视口宽度=设备宽度
	可视视口 visual viewport
		window.innerWidth

layout viewport(布局视口)：在PC端上，布局视口等于浏览器窗口的宽度。而在移动端上，由于要使为PC端浏览器设计的网站能够完全显示在移动端的小屏幕里，此时的布局视口会远大于移动设备的屏幕，就会出现滚动条。js获取布局视口：document.documentElement.clientWidth | document.body.clientWidth；

visual viewport(视觉视口)：用户正在看到的网页的区域。用户可以通过缩放来查看网站的内容。如果用户缩小网站，我们看到的网站区域将变大，此时视觉视口也变大了，同理，用户放大网站，我们能看到的网站区域将缩小，此时视觉视口也变小了。不管用户如何缩放，都不会影响到布局视口的宽度。js获取视觉视口：window.innerWidth；

ideal viewport(理想视口)：布局视口的一个理想尺寸，只有当布局视口的尺寸等于设备屏幕的尺寸时，才是理想视口。js获取理想视口：window.screen.width；


```





# 如何解决图片过大加载慢的问题
```markdown
# https://segmentfault.com/a/1190000040062155
如何解决图片过大加载慢的问题

压缩大图（PNG to JPEG、图片压缩率/分辨率调整）
合并小图（精灵图）
CDN加速

浏览器缓存策略
懒加载（Lazy Loading）
资源预加载(了解下dns-prefetch、preload、prefetch、prerender的link标签属性)

时间差加载（先加载小图、缩略图或低分辨率图，浏览器同时静默加载大图，用户再通过点击放大等交互操作以浏览高清图片）
不同客户端定制不同分辨率和质量的图片

渐进式加载（图片渐渐清晰，可能会切割图片，也可考虑结合CDN和缓存使用）
```





# 拖放事件
```
拖放
	drag
	dragstart
	dragend
	dragenter
	dragover
	dragleave
	drop

	e.dataTransfer
		dropEffect
      必须放在dragover事件
		effectAllowed

		files
		types
		items

		setData()
		clearData()
		setDragImage()

		getData()
```





# canvas
```markdown
# https://www.runoob.com/w3cnote/html5-canvas-intro.html

<canvas> 是脚本调用各种方法生成图像，SVG 则是一个 XML 文件，通过各种子元素生成图像。

建议永远不要使用 css 属性来设置 <canvas> 的宽高。
  替换内容

路径
	beginPath
	closePath
	lineTo
	moveTo

	strokeStyle
	stroke()
	fillStyle
	fill()
		//填充闭合区域。如果path没有闭合，则fill()会自动闭合路径。
线型
	lineWidth
	lineCap
		butt
		round
		square
	lineJoin
		bevel
		round
		miter
			ctx.miterLimit

	lineDashOffset=0
	setLineDash([线段长，间距长])
	getLineDash()

矩形
	rect(x,y,width,height)
		# 绘制路径
		fillStyle="red"
		fill()
	fillRect(x,y,w,h)
	strokeRect(x,y,w,h)

	clearRect(x,y,w,h)

弧线
	arc(x,y,r,startAngle,endAngle,是否逆时针)
	arcTo(x1,y1,x2,y2,r)
		，当前点与第一个点形成一条直线，第一个点与第二个点形成另一条直线，然后画出与这两根直线相切的弧线。


文本
	fillText(text,x,y,maxWidth ?)
	strokeText(...)
		不支持文本断行，所有文本一定出现在一行内。如果要生成多行文本，只有调用多次 fillText() 方法。

	ctx.font="Bold 20px Arial";
	ctx.textAlign="center"
		direction
		textBaseline

	ctx.measureText(text).width




渐变色 | 图像填充
	# 赋值ctx.fillStyle

	ctx.createLinearGradient(x1,y1,x2,y2)
	ctx.createRadialGradient(x0, y0, r0, x1, y1, r1) 

	ctx.createPattern(image, repetition) 


阴影
	shadowOffsetX
	shadowOffsetY
	shadowBlur
	shadowColor




图像处理
	drawImage(image,ix,iy,iw,ih,cx,cy,cw,ch)
	drawImage(image,cx,cy,cw,ch)
	drawImage(image,cx,cy)

	const img=new Image()
	img.src=""
	img.onload=function(){
		console.log(this.naturalWidth,this.naturalHeight)
  }



	# 像素处理
	getImageData(cx,cy,cw,ch)
		返回一个对象
		data
		width
		height

	putImageData(ImageData,cx,cy)
	putImageData(ImageData,cx,cy,ix,iy,iw,ih)

	createImageData(w,h)
	createImageData(ImageData)
		# 赋值ImageData
		# 所有像素都是透明的黑色


save | restore
	将画布的当前样式保存到堆栈，相当于在内存之中产生一个样式快照。
ctx.canvas

ctx.clip()
	把已经创建的路径转换成裁剪路径。
	只能遮罩在这个方法调用之后绘制的图像
	

图像变换
	rotate(45 * Math.PI / 180); 
		必须在 fillRect() 方法之前调用，否则是不起作用的旋转中心点始终是画布左上角的原点
	scale(xratio,yratio)
		ctx.scale(-1, 1) 为水平翻转， ctx.scale(1, -1) 表示垂直翻转。
	translate(x,y)
		# 移动原点
	transform()
	setTransform()





转化成元素
	toDataURL(type,quality=0.95)
		image/jpeg
		image/png
		image/webp

	toBlob((blob)=>{},type,quality=0.95)
```




# svg
```markdown
文本文件
	image/svg+xml
可以写在一个独立的文件中，被<img>等标签直接引入
css通过background-image也可以直接引入

javascript 和 css进行操作


标签及属性
	svg
		width
		height
		viewBox
			x y w h
			缩放
	circle
		cx
		cy
		r
	line
		x1
		y1
		x2
		y2
	polyline | polygon
		points
			横坐标与纵坐标之间与逗号分隔，点与点之间用空格分隔
	rect
		x
		y
		width
		height
		rx
		ry
			用来圆滑四个角
	ellipse
		cx
		cy
		rx
		ry
	path
		d
			M 
			L 
				H
				V
			Z
			大写表示绝对定位，小写表示相对定位

			C x1 y1, x2 y2, x y (or c dx1 dy1, dx2 dy2, dx dy)
				S x2 y2, x y (or s dx2 dy2, dx dy)
			Q x1 y1, x y (or q dx1 dy1, dx dy)
				 T x y (or t dx dy)
			
			A rx ry x-axis-rotation large-arc-flag sweep-flag x y
	text
		x
		y
	
共有属性:也可以直接在css中使用或在style属性中使用
	fill
	stroke
	stroke-width
	stroke-lineCap
	stroke-dasharray	
		实线,间隔,实线,间隔...
	strok-dashoffset
	stroke-lineJoin
	
	fill-opacity
	stroke-opacity

	fill-rule
		nonzero
		evenodd
	
	transform
		rotate(deg x y)
			绕着点(x,y)旋转deg度

功能性标签
	use
		href
			对已有svg元素的引用、复制
		x
		y
	g
		将多个形状编组，便于复用
	defs
		内部的元素不会呈现，相当于template，仅供引用
	image
		xlink:href
		width
		height
	a
		xlink:href
	animate
		attributeName
		from
		to
		dur
		repeatCount
			indefinite
	animateTransform
		由于animate对css的transform不起作用，补充

		attributeName
		type
			rotate
			translate
		begin
		dur
		from
		to
		repeatCount

```

# Worker线程
```markdown

全局限制
	DOM限制
通信限制
同源限制


const worker=new Worker(url,options={name:"default"})
worker.name
	self.name
worker.onerror
	self.addEventListener("error",()=>{})
wroker.postMessage()
	# 可以传递二进制数据，不需要反序列化
	拷贝赋值
		存在性能问题；解决：transfer objects,直接将二进制处理权限转移给worker线程		worker.postMessage(arraybuffer,[arraybuffer]
	self.postMessage()
worker.onmessage=(e)=>{}
	self.addEventListener("message",(e)=>{})
worker.terminate()
	self.close()

	importScripts(url1,url2,...)

实现长轮询
function createWorker(fn,name="default"){
	const blob=new Blob([`(${fn.toString()})()`],{type:"application/javascript"});
	const url=URL.createObjectURL(blob);
	return new Worker(url,{name});
}	

```

# IntersectionObserver | MutationObserver
```markdown
MutationObserver
	异步
	变动记录封装成一个数组
	变动类型

const observer=new MutationObserver((mutations,self)=>{})
observer.
	observe(elDom,options)
		childList
		attriubutes
		charactorData

		subtree
		attributeOldValue
		attributeFilter
		charactorDataOldValue

	disconnect()
	takeRecords()
		清除所有变动记录并返回
MutaionRecord
	type
	target

	oldValue
	attributeName

	addedNodes
	removedNodes
	previousSibling
	nextSibling

IntersectionObserver
	其实现应该采用了requestIdleCallback;
	只有线程空闲下来才会执行，优先级非常低
const obervser=new IntersectionObserver((entries,self)=>{},options)
observer.observe(elDom)

IntersectionObserveEntry
	time	毫秒
	target
	rootBounds
	boudingClientRect
	intersectionRect
	intersectionRatio
options
	threshold
		默认[0];执行回调的门槛值
	root
		不仅可以观察元素相对于视口的可见性；
		还可以观察元素相对于所在容器的可见性
		默认值:doucment.body
	rootMargin
		扩展或缩小交叉区域的大小
		默认值:"0px 0px 0px 0px"
observer.unobserve(elDom)
observer.disconnect()

无限滚动
	sentinel
惰性加载
	data-src

```



# Web Components 
```markdown
组件化
Shadow Dom
	CSS完全私有化|模块化，无法对全局部分样式复用
template|slot


生命周期
connectedCallback： 当 custom element首次被插入文档DOM时，被调用。
disconnectedCallback： 当 custom element从文档DOM中删除时，被调用。
adoptedCallback： 当 custom element被移动到新的文档时，被调用。
attributeChangedCallback： 当 custom element增加、删除、修改自身属性时，被调用。
  static get observedAttributes() {}

注意事项：
- custom element 的名称不能是单个单词，且其中必须要有短横线。
- 可以继承任何内置元素




let shadow = elementRef.attachShadow({mode: 'open'});
open 表示可以通过页面内的 JavaScript 方法来获取 Shadow DOM
let myShadowDom = myCustomElem.shadowRoot;


const template=document.querySelect().content
const shadowRoot=this.attchShadow(tmeplate.cloneNode(true))


customElements.define('hello-world', HelloWorld);
document.createElement("hello-world");



vue/react -> 编译web component
	转换成原生组件使用，不再引用vue/react包
	转换的代码包有没有可能变多
策略模式
	MyComponent extends Component extends HTMLElement
	Componenent封装一系列方法，MyComponent直接使用

外部模板
	new Blob([],{type:"text/html;charset=utf-8"})
	Ajax
		responseType="document"
外部样式
	document.createElement('link');
	问题：可能导致无样式内容闪烁
外部脚本
	import



getRootNode()可以用来判断一个元素是否在Shadowdom中

composed
	如果属性值为 false，那么事件将不会跨越 shadow DOM 的边界传播。
	mode为closed并不会影响该值，composed依然等于true，也就是mode=closed的自定义元素内部的click事件一样能够响应并顺利传播到window
isConnected
	仅仅是createElement、返回false，只有当插入(appendChild)到DOM树后才返回true
	如果该节点与 DOM 树连接则返回 true, 否则返回 false



:host()
:host-context()
::slotted()
::part()
```



# dom相关
```markdown
nodeType
nodeName
nodeValue

textContent
	文本，不会包含标签
ownerDocument

parentNode
	element
	doucment
	document=fragement
parentElement
	只有父元素是元素类型的节点
nextSibling
	文本
	注释
	元素
previousSibling
lastChinld
	递归遍历
firstChild

childNodes
	动态的引用
	元素
	文本
	注释
isConnected


# 方法
hasChildNodes()
appendChild
cloneNode(true)
	事件没有绑定
	id.name属性重复
removeChild
insertBefore
replaceChild

getRootNode()
contains
compareDocumentPosition
	0
	1
	2
	4
	8
	16

isSameNode
isEqualNode





children
	只 元素节点 集合
	动态
firstElementChild
lastElementChild
childElementCount

append()
	字符串可以
	同时添加多个
prepend()


remove()
	从父节点移除
replaceWith()
before()
	在当前节点之前添加节点
	字符串可以
	同时添加多个	
after()




NodeList
	包含各种节点
	具备forEach
	只有.childNodes返回的是动态的，其他都是静态
		document.querySelectorAll
HTMLCollection
	只包含元素节点
	都是动态
		.children
		document.images
		document.links
		document.frames
			直接通过id/name引用对应元素



hasAttributes()
attributes
	属性对象 集合
		name
		value
	动态的
标准属性
	可以直接通过el.[name]的形式访问
	HTML元素的属性大小写不敏感；当JS敏感
		for -> htmlFor
		class -> className

getAttributeNames()
hasAttribute()
getAttribute()
	获得标椎属性，自定义属性
setAttribute()
removeAttribute()

data-*
	dataset.





document.doctype
	.documentElement
	.body
	.title
	.head
	
	.scrollingElment
	.activeElement
	.fullscreenElement
	currentScript
		脚本所在DOM节点

	links
	images
	frames
	scripts
	styleSheets


	domain
	cookie
	lastModified
	characterSet
	referrer
	compatMode

	hidden
	visibilityState
	readyState

	designMode
	implementation




open()
write()
	页面是否渲染结束（） => 追加还是重写覆盖
close()


# 除了document,还可以在元素节点上使用
querySelector
querySelectorAll	
	不支持伪元素和伪类
getElementsByTagName
getElementByClassName
	正常模式下的CSS中的class是大小写敏感的

# 只能在document对象上
getElementById()
	效率更高




elementFromPoint
	相对于视口
	页面指定位置最上层的元素节点

elementsFromPoint
	指定坐标的所有元素；




createElement
createTextNode
createDocumentFragment
createComments
createEvent


hasFocus()
	是否被激活或获得焦点；
getSelection()



createNodeIterator
createTreeWalker

富文本编辑
	execCommand()
	queryCommandSupported




id
lang
dir
title
draggbale

tagName

accessKey
tabIndex


hidden
	CSS设置的优先级高于Element.hidden
contenteditable




attributes
className
classList
	add
	remove
	toggle
	contains
data-*

textContent
innerHTML
outerHTML
	如果一个节点没有父节点，设置outerHTML会报错



clientHeight
	只对块级元素有效
	元素自身宽度 + padding宽度 - 滚动条宽度
clientWidth
	document.body.clientHeight > document.documentElement.clientHeight
clientLeft
	left border
clientTop
	top border



scrollHeight
	溢出元素的实际总高度 + padding - 滚动条
scrollWidth
scrollLeft
	可读写 
	'document.documentElement.scrollTop-window.scrollY'
scrollTop



offsetParent
	祖先元素中postion不等于static的元素，没有则是body
	如果元素本身是不可见的(display:none)或者fixed，那么offsetParent=null
offsetHeight
	自身宽度 + padding + border + 滚动条
offsetWidth
offsetLeft
	相对于offsetParent的距离

	递归的得出相对于浏览器边界的距离
offsetTop



style



children
childElementCount
firstElementChild
lastElementChild

nextElementSibling
previousElementSibling




querySelector
	注意查找顺序：是先从全局范围内查找，再从这些结果中查找属于当前元素的符合条件
querySelectorAll
getElementsByClassName
	千万注意：返回的是可变的集合；
	这意味着如果根据某个class选择了元素，如果js操作移除了该集合中某个元素的class，将会导致该元素被移除该集合；

	最好将这些可变集合转换数组后再用JS操控
getElementsByTagName




closest()
	接受一个CSS选择器作为参数，返回匹配该选择器最近的祖先节点（包括当前节点）
matches()
	元素是否匹配某个CSS选择器；
scrollIntoView(true)
	默认值：true，顶部对齐；false，底部对齐



getBoudingClientRect
	可见视口
	基于边框
		width/height + padding + border
	属性都是继承自原型的，Object.keys()无法得到
		left
			别名：x
		top
			别名：y
		right
		bottom
		width
		height
getClientRects
	用于判断行内元素是否换行，以及行内元素每一行的的偏移位置




insertAdjacentElement(position,elDom)
	beforebegin
	afterbegin
	beforeend
	afterend
insertAdjacentHTML
insertAdjacentText



click()
focus({preventScroll:false})
	聚焦并滚动到当前聚焦点
	document.activeElement
blur()
remove()


```



# CSS操作
```markdown
CSSStyleDeclaration接口
	元素节点的 style 属性（ Element.style ）
	CSSStyle 实例的 style 属性
	window.getComputedStyle() 的返回值


	驼峰标识
	关键字或保留字
		float -> cssFloat
	必须带单位
	只是行内样式，不是元素的全部样式
		getComputedStyle


	cssText
		读写所有样式
	length
	parentRule
		只在CSSRule块中才有意义
	
	item()
		返回指定索引处的属性名是否设置了"!important"
	getPropertyValue()
	getPropertyPriority()
	removeProperty()
	setProperty(name,value,"important")


CSS属性检测
	判断元素的style对象的某个属性值是否为字符串；
		不同浏览器的前缀写法也需要考虑
CSS对象
	CSS.escape
		<div id="foo#bar">
		这种特殊的id属性查找：
			doucment.querySelector("#foo\\#bar")
			=document.querySelector(`#${CSS.escape('foo#bar')}`)
	CSS.supports()
		CSS.supports('transform-origin', '5px') 
		CSS.supports('display: table-cell') 
			不支持结尾带分号，否则查询结果有误


getComputedStyle(propName,presudo_name)
	单位是绝对单位
	简写形式无效，margin -> marginLeft / font -> fontSize



StyleSheet接口
	<link>元素和<style>元素的样式表
		document.styleSheets
		el.sheet

	disabled
		是否禁用该张样式表
	href
	media
		mediaText
		appendMedium
	title
	type

	parentStyleSheet
		有值说明该张样式表是通过@import加载的；
		返回的是使用@import语句的样式表（上一级样式表）
	ownerRule
		有些样式表是通过@import引入的，ownerRule返回那行@import规则
	ownerNode
		样式表所在的实体元素，如:<link>和<style>;
		由样式表通过@import引入的样式表的ownerNode=null
	cssRules
		伪数组对象CSSRuleList,每个成员都是当前样式表的一条CSS规则
			每条规则：CSSRule对象
		每条规则具有以下属性
			cssText
			parentStyleSheet
			parentRule
			type
				1	普通样式规则
				3	@import
				4	@media
				5	@font-face

			style
				返回的是CSSStyleDeclaration对象
			selectorText


	insertRule(rule,index)
		在该样式表中插入行的样式规则
	deleteRule(index)



	
	
CSSRule
CSSStyleRule
CSSMediaRule
	media
	conditionText


const mdl=window.matchMedia('(min-width:400px)')
mdl.
	media
	matches
		是否匹配查询规则
	onchange=(e)=>{if(e.matches){}}
		监听窗口变动

	addListener
	removeListener
```


# 剪贴操作
```markdown
document.execCommand("copy" | "cut" | "paste")
	同步操作 -> 卡顿
	必须文字内容选中，再执行 execCommand() 方法才有效

navigator.clipboard
	异步
		async函数
	只有HTTPS协议才可使用该API，开发环境localhost也行
	写入不需要授权，但读取需要

	在开发者工具运行时，需要异步、快速点击一下网页的页面窗口，使其变为当前页


	readText()
		读取剪贴板里的文本数据
		需要用户许可，最好放在try...catch中
	read()
		读取剪贴板里的内容，可以是二进制图片数据
		返回的是：clipboardItems数组对象
			types
			getType
	writeText()
	write([
		new ClipboardItem({[blob.type]:blob})
	])	
		注意，Chrome 浏览器目前只支持写入 PNG 格式的图片。


copy/pastes/cut事件
	注意：先阻止浏览器的默认行为
copy
	e.clipboardData.setData(type,data)	
		document.getSelection()
	getData(type)
	clearData([type])
	items
		type
	files
```