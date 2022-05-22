- [Webpack原理](#webpack原理)
	- [读源码的方式](#读源码的方式)
	- [编译文件分析](#编译文件分析)
	- [原理初探](#原理初探)
	- [gulp](#gulp)
		- [更复杂的配置](#更复杂的配置)
	- [rollup](#rollup)
		- [不原生支持commonjs](#不原生支持commonjs)
		- [其他配置](#其他配置)
	- [vite](#vite)
	- [其他](#其他)

# Webpack原理
## 读源码的方式
```markdown
流程图、类比
粗浅、整体 => 详细、局部
	看函数名称 -> 调用链
	具体看函数实现
```



## 编译文件分析
```markdown
	CommonJS
		所有模块可导出成员组成一个大的对象；模块路径作为键，该模块内导出的成员封装成一个对象、作为对应键的值
		实现 模块缓存 __webpack_module_cache__;导入函数__webpack_require__先检查缓存中是否存在，决定是使用缓存、还是去对应路径中取导出的成员集合
		所有的模块封装成一个立即执行闭包函数，执行模块内部除导出外的任何代码；
	ESModule
		缓存与导入函数 没有变化；
		实现了三个函数：
			o	判断是否是自身的属性
			r	标记当前模块:__esModule=true;toStringTag="module"
			d	# 关键函数；通过get存储器 实现只读代理
			n 	# 根据__esModule 进行进一步的判断
		每个模块都是一个函数，不将模块与运行时分开了，导出的成员定义在该函数，通过r函数代理暴露给外界（闭包模式）；

		先从入口文件开始执行，在执行过程中导入其他模块

```

## 原理初探
```markdown
webpack-cli的作用：合并命令行与webpack.config.js的参数，传递给webpack后启动webpack


插件的执行贯穿整个webpack，取决于插件本身监听了哪些hooks
```



## gulp
```markdown

Gulp 自动化|工作流
	任务运行 | taskRunner | 文件Stream流

	gulp都是异步任务，需要手动结束；若函数返回值是stream流、event emitter、promise、child process、observable等


Webpack
	静态化、模块、打包 | moduleBundle

```


```javascript
// 公共 | 私有任务(不导出的任务)
// gulpfile.js 默认启动文件

// 执行单个任务，每个任务都是异步的
// npx glup foo
const foo=(cb)=>{
	console.log()
	cb()
}
module.exports={
	foo
}

// 省略名称
// npx gulp
module.exports.default=function(cb){
	console.log();
	cb()
}


// 多个任务组合执行
// 私有任务 task1/task2/task3
const {series,parallel} = require("gulp");
const seriesTask=series(taks1,task2,task3)
const parallelTask=parallel(task1,task2,task3)

// 复合任务仍然可以复合
const composedTask=series(seriesTask,parallelTask)
module.exports={
	seriesTask,
	parallelTask,
	composedTask,
}

// 文件读写
const {src,dest}=require("gulp");
const babel=require("gulp-babel");
const terser=require("gulp-terser")

const jsByBabel=()=>{
	return src("./src/index.js") // 输入
	.pipe(babel({presets:["@babel/preset-env"]})) // 转换
	.pipe(terser({mangle:{toplevel:true}}))
	.pipe(dest("./dist")) // 输出
}



// 文件监听;文件变动后，自动执行下列任务
const {watch} = require("gulp")
watch("./src/**/*.js",taskRunner)



 src( String | Array )
 路径匹配:glob
	"./src/**/*.js"
	"script/*.js"
	["src/**/*.js","!scr/vendor/"]
		// 取反匹配


```



### 更复杂的配置
```javascript
// npm install -D @babel/core postcss
// npm install -D gulp-babel gulp-terser gulp-less gulp-postcss gulp-postcss-preset-env gulp-htmlmin gulp-inject browser-sync

```


## rollup
```markdown
主要是针对ES Module打包
一般处理javascript文件
更简洁/更易于理解
早期先使用Tree Shaking

使用场景
rollup 库文件
webpack 实际项目

```


```javascript
// npx rollup src/index.js -f cjs -o dist/bundle.js
/* 
-f amd
-f umd
	--name utils
	// 库名
-f iife
 */


 // 配置文件：rollup.config.js
 // npx rollup -c
 // 多出口
export default {
	input:"./src/main.js",
	-output:{
		format:"umd",
		name:"utils",
		file: "dist/utils.main.js",
	},
	output:[
		{
			format:"umd",
			name:"utils",
			file: "dist/utils.main.js",
		},
		{
			format:"amd",
			file:"dist/utils.amd.js"
		},
		{
			format:"cjs",
			file:"dist/utils.commonjs.js"
		},
		{
			format:"es",
			file:"dist/utils.es.js"
		},
		{
			format:"iife",
			name:"utils",
			file:"dist/utils.browser.js"
		}
	]
}
```



### 不原生支持commonjs
```javascript
// 必须使用插件 
// npm install @rollup/plugin-commonjs
// rollup只支持commonjs的导出功能module.exports，仍不支持导入require

import cmmonjs from "@rollup/plugin-commonjs";
import nodeResolve from "@rollup/plugin-node-resolve" // 解决引入第三方包没有被打包的问题

// npm install @babel/core @babel/preset-env
// 配置babel.config.js文件
// @babel/plugin-babel" =>babel-loader
import babel from "@babel/plugin-babel"

import {terser} from "rollup-plugin-terser"

export default {
	input:"",
	output:{
		format:"",
		name:"",
		file:"",
		globals:{
			// 使用external排除第三方包后，打包文件将不再含有lodash，必须在index.html手动引入，此时我们在源文件使用的全局变量"lodash"必须映射到"_"
			"lodash":"_",
		}
	},
	externals:["loadsh"]
	plugins:[
		commonjs(),
		nodeResolve(),
		babel({
			babelHelpers:"bundled"
		}),
		teser()
	]
}
```


### 其他配置
```json
//scripts
"build":"rollup -c --environment production"
"server":"rollup -c --environment development -w"
```


```javascript
// rollup.config.js
import commonjs from "@rollup/plugin-commonjs"
import resolve from "@rollup/node-resolve"
import babel from "@rollup/babel"
import {terser} from "rollup-plugin-terser"
// npm install @babel/core postcss
import postcss from "rollup-plugin-postcss"
// npm install vue-template-compiler
import vue from "rollup-plugin-vue"
import replace from "rollup-plugin-replace"
// replace 注入环境变量，因为打包后的vue代码中存在process.env.NODE_ENV
import serve from "rollup-plugin-server"
import livereload from "rollup-plugin-livereload"
// 以上需要手动引用打包后的路径

const isProd=process.env.NODE_ENV === "production";
const plugins=[
	commonjs(),
	resolve(),
	replace({
		"process.env.NODE_ENV":`"${process.env.NODE_ENV}"`
	}),
	babel({
		babelHelpers:"bundled",
	}),
	postcss(),
	vue(),
].concat(
	isProd ? [
		terser()
	] : [
		new serve({
			port:8000,
			contentBase:"." // 不同于webpack中的devServer中的contentBase
		}),
		new livereload()
	]
)

export default {
	input:"",
	output:{
		format:"umd",
		name:"",
		file:"",
	},
	external:["lodash"],
	plugins,
}
```




## vite
```javascript
// ESBuild解析
支持CommonJS和ES6模块化
支持TreeShaking
支持TypeScript/JSX语法
支持代码压缩
支持扩展插件
支持sourceMap
支持GO/JavaScript的API

超快的构建速度
  go语言 -> 机器代码
  充分利用多内核
  没用使用第三代码，整体性更强，一开始就考虑各种性能问题
```

```javascript
// npm install vite
/* 
   npx vite 启动本地服务
   npx vite build 打包
   npx vite preview
*/
/* 
vue3=@vitejs/plugin-vue
vue3=@vitejs/plugin-vue-jsx

vue2=vite-plugin-vue2
 */

// 配置文件：vite.config.js
import {createVuePlugin} from "vite-plugin-vue"
export default {
  plugins:[
    createVuePlugin()
  ]
}
```


```markdown
构建工具
基于 rollup/ESBuild 的模块化打包工具


vite网络基于connect
  connect更易于重定向，这也是更换Koa实现内部服务的原因

入口文件
  src/index.html
  分析index.html依赖 -> 自动加载文件
  // lodash-es;多个js请求

优点
  零配置
  无需配置loader，直接就可以引用
    对.css|less|scss的支持
      只需下载包、无需配置：
        npm install less
        npm install postcss postcss-preset-env
          postcss.config.js
    对ts文件的支持：包都不需要下载
    对图片 | 文件的支持：亦如此
    对vue的支持：
      npm install vue
    对react的支持
      npm install react react-dom
      // 需要注意jsx语法在vite中必须在.jsx文件
  预打包 | prev bundling
    由于package.json中dependecies字段声明的第三包很少被修改，大多数情况仅仅是作为库文件使用，直接提前打包这些不变资源，下次就可以避免重复打包
  内置vue热更新
    根据时间戳重新请求

  增强开发速度、打包速度相对较慢

  自动合并一个文件下的多次导入
    lodash-es
  重定向 | 将编译后的东西返回
    style.less -> style.js
```

```markdown
# vanillaJS：原生开发

npm init @vitejs/app
// 等价于
  第一步：npx @vitejs/create-app
  第二步：
```







## 其他
```markdown
vue inspect --mode=development > webpack.config.js

vue inspect --mode=production > webpack.config.js

```