- [注意事项](#注意事项)
- [配置文件](#配置文件)
- [主要配置字段](#主要配置字段)
- [Plugin](#plugin)
- [打包优化](#打包优化)
- [自定义](#自定义)
	- [loader](#loader)
	- [plugin](#plugin-1)
- [构建工具](#构建工具)
	- [gulp](#gulp)
	- [rollup](#rollup)
	- [vite](#vite)


# 注意事项
```markdown
vue inspect --mode=development > webpack.config.js


babel-loader 区别 ts-loader

url-loader
	filename
	outputPath
	limit
file-loader

Webpack5资源模块
type:"assert"



配置分离
	(env)=>config
	webpack --config webpack.config.js --env production
	const {merge}=require("webpack-merge")



hash | contenthash | chunkhash	
// 最佳实践
// 推荐一般模块使用contenthash
output:{
	path:"",
	filename:"js/[name].[chunkhash].[ext]",
	chunkFilename:"js/[name].[contenthash].chunk.js",
},
plugins:[
	new MiniCSSExtractPlugin({
		filename:"css/[name].[contenthash].[ext]",
	})
]
```


# 配置文件
```markdown
.prettierrc
	.prettierignore
.git
	.gitignore
.eslintrc.js

tsconfig.json

.browserslistrc
	babel.config.js
	postcss.config.js
```



# 主要配置字段
```markdown
watch
context
mode

external
	键 | 值


entry
	多入口
output
	path
	outputPath
	publicPath
	filename
	chunkFilename

	library
	libraryTarget
		"umd"
	globalObject
module
	rules
		exclude
		sideEffects
resolve
	modules
	extentions
	mainFiles
	mainFields
	alias


devtool
	【inline|hidden|eval】-【nosources】-【cheap[-module]】-source-map
devServer
	publicPath
	contentBase

	proxy
	historyApiFallback

optimization
	usedExports:true,

	chunkIds
		"natural" | "named" | "deterministic"
	splitChunks
		chunks
			"initial" | "async" | "all"
		minSize	20 * 1024
		maxSize
		minChunks
			针对多入口，单入口任何包都只会被导入一次
		cacheGroups
			test
			filename
				"[id]_vendors.js"
			priority

	minimize:true,
	minimizer:[
		new TerserWebpackPlugin({
			extractComments:true,
			terserOptions:{}
		})
	]

	
runtimeChunk
	true
	"single" | "multiple"
	Object
		name


```






# Plugin
```markdown
HtmlWebpackPlugin
	title
	template
	inject
	cache
	minify
		reomveComments
		collapseWhitespace
		minifyCSS
		minifyJS
CleanWebpackPlugin
CopyWebpackPlugin
MiniCSSExtractPlugin
	filename:"css/[name].[hash:8].[ext]"

	isProduction ? MiniCSSExtractPlugin.loader : "style-loader",


webpack.DefinePlugin
webpack.optimize.ModuleConcatenationPlugin
webpack.ProvidePlugin
	shimming | 垫片
	全局变量名：对应库的名称

TerserWebpackPlugin
CSSMinimizerWebpackPlugin
PurgecssWebpackPlugin
CompressionWebpackPlugin
	test:/\.(css|js)$/,
	threshold:20*1024,
	minRatio
	algorithm
	include
	exclude
VueLoaderPlugin

```








# 打包优化
代码分割
代码压缩
CDN
文件压缩
TreeShaking
魔法注释

作用域提升
内联代码

```markdown
	魔法注释 | 代码懒加载
		webpackChunkName
		webpackPrefetch:true
			闲时下载、后于
		webpackPreload

	代码分割
		首屏渲染
			利用浏览器的并行加载
			在减少Http链接数量之间权衡
		更好的命中缓存
		
		runtimeChunk | optimization.splitChunks
	CDN
		externals字段
		EJS模板语法 在 模板index.js中
	代码压缩
		html
		css
		js
			不可达代码
	作用域提升
		webpack.optimize.ModuleConcatenationPlugin
	ThreeShaking
		optimization.usedExports
			生产模式，默认true
		sideEffects
			需要手动开启
			package.json | rules->sideEffects

		CSS
			PurgecssWebpackPlugin
	文件压缩 | HTTP
	内联runtime代码 | 减少请求次数
		const InlineChunkHtmlPlugin=require("react-dev-utils/inline-chunk-html-plugin")
		new InlineChunkHtmlPlugin(HtmlWebpackPlugin,[/^runtime.*\.js$/])
```





# 自定义
## loader
```markdown
	pitch	normal
	pre -> normal -> inline -> post
		enfore	字段
	同步
		this.callback(null,content,sourcemap,meta)
		return content
		# 返回的content必须是javascript模块样式的字符串
	异步
		const callback=this.async()
	scheme-utils
		validate
	load-utils
		getOptions
```

## plugin
```markdown
	tapable库
		syncHook
		asyncParallelHook
		asyncSeriesHook

		tap
		tapPromise
		tapAsync
		
		call
		promise().then()
		callAsync
	
	class Test{
		apply(compiler){
		}
	}	
```



# 构建工具
## gulp
```markdown
	自动化|工作流
	taskRunner
		异步任务
			手动结束
	gulpfile.js
	插件

	const {series,parallel,watch,src,dest}=require("gulp")
```

## rollup
```markdown
	没有loader,专门处理js文件
	ESModule
		@rollup/plugin-commonjs
	解决依赖第三方打包
		@rollup/plugin-node-resolve

	更早使用TreeShaking
	更简洁

	库文件

input
output
	format
	name
	file

	globals
externals
plugins
```


## vite
```markdown
	ESBuild
		ESModule和CommonJS
		TS和JSX
		TreeShaking、sourcemap
		插件扩展、代码压缩
	零配置 | 少量配置
		图片/TS/CSS
		less
			npm install less postcss postcss-preset-env
		vue
			npm install vue vite-plugin-vue2
		react
			npm install react react-dom
	预打包 | Prev Bundling
	重定向
	自动合并

npx vite
npx vite build
npx vite preview
```


