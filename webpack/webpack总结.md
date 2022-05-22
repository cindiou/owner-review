- [总结](#总结)
	- [webpack关键词](#webpack关键词)
	- [配置选项](#配置选项)
	- [entry配置多入口](#entry配置多入口)
	- [rules配置实例](#rules配置实例)
	- [配置文件](#配置文件)
	- [配置分离](#配置分离)
- [浏览器预设|browserslist](#浏览器预设browserslist)
- [代码格式化](#代码格式化)
	- [ESlint](#eslint)
	- [prettier](#prettier)
		- [常见配置选项](#常见配置选项)
- [loader](#loader)
	- [与plugin的主要区别：](#与plugin的主要区别)
	- [PostCSS](#postcss)
	- [文件资源加载](#文件资源加载)
	- [Babel](#babel)
- [字段讲解](#字段讲解)
	- [devtool](#devtool)
	- [devServer](#devserver)
- [打包优化](#打包优化)
	- [代码分割](#代码分割)
		- [splitChunks](#splitchunks)
		- [懒加载](#懒加载)
		- [runtimeChunk | 运行时分割](#runtimechunk--运行时分割)
	- [CDN| 内容分发网络](#cdn-内容分发网络)
		- [externals](#externals)
	- [代码压缩](#代码压缩)
		- [js](#js)
		- [css](#css)
		- [HTML](#html)
	- [作用域提升](#作用域提升)
	- [ThreeShaking](#threeshaking)
		- [JS](#js-1)
			- [usedExports](#usedexports)
			- [sideEffects](#sideeffects)
		- [CSS](#css-1)
	- [http压缩](#http压缩)
	- [html内联runtime.js](#html内联runtimejs)
- [补充内容](#补充内容)
	- [shimming | ProvidePlugin](#shimming--provideplugin)
	- [MiniCSSExtractPlugin](#minicssextractplugin)
	- [hash | contenthash | chunkhash](#hash--contenthash--chunkhash)
	- [打包库文件](#打包库文件)
	- [打包时间分析](#打包时间分析)
- [自定义](#自定义)
	- [loader](#loader-1)
		- [normalLoader | pitchLoader](#normalloader--pitchloader)
		- [resolveLoader](#resolveloader)
		- [执行顺序](#执行顺序)
		- [同步loader|异步loader](#同步loader异步loader)
		- [接受参数 | 验证参数](#接受参数--验证参数)
		- [案列：](#案列)
			- [babel-loader](#babel-loader)
			- [md-loader](#md-loader)
	- [plugin](#plugin)
		- [tapable库了解](#tapable库了解)
		- [案列 | 自动上传](#案列--自动上传)




# 总结
## webpack关键词
```markdown
模块化
	打包
预处理
安全、优化、兼容性
热更新
	开发效率
依赖图
  tree shaking

静态的模块化打包工具

```


## 配置选项
```javascript
// 命令行：
// webpack --config wb.config.js --env production
  /* 默认配置文件：webpack.config.js */
// webpack --watch
// webpack serve
  /* 开启本地webpack-dev-server提供的服务 */

// 配置文件是为了辅助解析，是对命令行输入的的固化
const {CleanWebpackPlugin}=require("clean-webpack-plugin")
const HtmlWebpackPlugin=require("html-webpack-plugin")
const CopyWebpackPlugin=require("copy-webpack-plugin")
const {VueLoaderPlugin}=require("vue-loader")
const {DefinePlugin}=require("webpack")

module.exports={
  watch:true,
  context:path.resolve(__dirname,"./"), // 必须是绝对路径；默认是工作目录，是entry的基目录
  - entry:"./src/index.js",

  output:{
    filename:"js/[name].bundle.js",
    path:path.resolve(__dirname,"./dist"),
    // 在打包后的静态资源前做一个路径的拼接;
    publicPath:"", // 打包后的文件插入到index.html后的路径，publicPath + filename
  },
  module:{
    rules:[]
  },
  plugins:[
    new CleanWebpackPlugin()
    new HtmlWebpackPlugin({
      title:"",
      template:""
    }),
    new CopyWebpackPlugin({
				patterns:[
					{
						from:"./public",
						globOptions:{
							ignore:[
								"**/index.html",
								"**/.DS_Store",
							]
						}
					}
				]
    }),
    new DefinePlugin({
      BASE_URL:"'./'"
    }),
    new VueLoaderPlugin()
  ],
  resolve:{
    modules:["node_modules"],
    extentions:[".wasm",".js",".mjs",".json",".jsx",".ts",".vue"],
		mainFiles:["index"],
    mainFields:["browser","module","main"],
    alias:{
      "@":path.resolve(__dirname,"./src"),
    }
  },
  devtool:"cheap-module-source-map",// source-map文件，
  devServer:{ // 开启服务的目录是webpack.config.js启动的目录
    public:"",// 设置后必须与
    contentBase:"",//手动在模板index.html设置的资源的请求目录
    watchContentBase:true,

    hot:true,
    hotOnly:true, // 编译错误后，不刷新

    host:"0.0.0.0",//默认是127.0.0.1，回环地址；同一路由下的其他主机无法访问
    port:8080,
    open:true,// 是否自动打开浏览器
    compress:true,
    proxy:{
      "/api":{
        secure:false,// 针对https进行代理，忽略安全性，
        changeOrigin:true,// 代理时，伪造请求的host
        target:"",//代理域名
        pathRewrite:{
          "^/api":"", // 重写代理时的路径
        }
      }
    },
    - historyApiFallback:true,// 针对history模式
    + historyApiFallback:{ // 更加详细设置
      rewrites:[
        {
          from:/\/abc\/?/,
          to:"index.html"
        }
      ]
    }
  }
}

```

## entry配置多入口
```javascript
{
  - entry:{ // 多入口,会带来一个问题：如果每个入口文件 都 依赖了某个库，那么这个库会被打包多次
    "index":"./src/index.js",
    "main":"./src/main.js"
  },
  - entry:{
    "index":{
      import:"./src/index.js",
      dependOn:"loadsh",
    }
    "main":{
      import:"./src/main.js",
      dependOn:"loadsh",
    },
    "lodash":"lodash", // 比如上述两者都依赖lodash，可以单独打包lodash
  }

  // 入口都同时依赖多个包
  - entry:{
    "index":{
      import:"./src/index.js",
      dependOn:["loadsh","axios"],
    }
    "main":{
      import:"./src/main.js",
      dependOn:["loadsh","axios"],
    },
    "lodash":"lodash",
    "axios":"axios",
  }
  // 对上述两者同时分割
  entry:{
    "index":{
      import:"./src/index.js",
      dependOn:"shared",
    }
    "main":{
      import:"./src/main.js",
      dependOn:"shared",
    },
    shared:["loadsh","axios"],
  }
}
```


## rules配置实例
```javascript
{
  rules:[
      {
        test:/\.js$/,
        exclude:[/node_module/],
        use:[ // 存在先后优先级:从下往上/从右往左
          "babel-loader",
          "eslint-loader",
        ],
        loader:"",// 若单个loader则可以直接使用loader选项
      },
      {
        test:/\.scss$/,
        use:[
          "style-loader",
          {
            loader:"css-loader",
            options:{
              importLoaders:2
            }
          },
          "postcss-loader",
          "sass-loader"
        ]
      },
      - {
        test:/\.(jpe?g|png|gif)/,
        use:[
          {
            loader:"url-loader",
            options:{
              - filename:"img/[name].[hash:8].[ext]",
              filename:"[name].[hash:8].[ext]",
              outputPath:"img"

              limit:50 * 1024 // 超过该大小自动转换图片为DataURL
            }
          }
        ]
      },
      {
        test:/\.(jpe?g|png|gif)/,
        type:"assert",
        generator:{
          filename:"img/[name].[hash:8][ext]",
        },
        parser:{
          dataUrlCondition:{
            maxSize:50 * 1024
          }
        }
      }
    ],
}
```



## 配置文件
```markdown
# 一般来说配置文件 MODULE_CONFIG.config.(js|mjs|json) 可以写成 .MODULE_CONFIGrc.(js|mjs|json)

.prettierrc
.prettierignore
.eslintrc.js
tsconfig.json

.browserslistrc
babel.config.js
postcss.config.js

```


## 配置分离
```markdown
# 工作目录：process.cwd()

"build":"webpack --config webpack.common.js --env production"
"start":"webpack serve --config webpack.common.js --env development"


const {merge}=require("webpack-merge")
const devConfig=require("./webpack.dev.js")
const prodConfig=require("./webpack.prod.js")

module.exports=function(e){
	const {production}=e;	# 区分环境变量 process.env.NODE_ENV

	//用来给其他配置文件使用；如：babel.config.js
	// 这里给env环境变量赋值时，node会默认序列化
	process.env.isProduction="true";

	const common= {
		# entry相对的是context路径，context路径默认是工作目录，即package.json所在的目录
		context:path.resolve(__dirname,"./")
		entry:"../scr/main.js"
	}
	return merge(
		common,
		production ? prodConfig : devConfig
	)
}

```


# 浏览器预设|browserslist
```markdown
browserslist
	在不同前端工具，共享目标浏览器和Node.js版本的配置
	# caniuse网站
		postcss-preset-env
		babel
		Autoprefixer

	语法规则
		last 2 version
		not dead
		> 5%
		not ie <= 8
	配置文件:两种方式
		.browserslistrc文件
		package.json中配置
			"browserslist":[
			]
			# 或者以下
			"browserslist":{
				"development":[],
				"production":[],
			}
```    



# 代码格式化
## ESlint
``` markdown
# npm install -D eslint
# npx eslint --init
	配置文件.eslintrc.js
		env
		extends
		parseOptions 
		plugins
		rules
		
	commonjs => 配置sourceType:"module";支持esmodule
		

{
	test:/\.m?js/,
	use:[
		"babel-loader",
		"eslint-loader",  # 注意安装顺序
	]
}
# npx eslint ,/src/index.js
```

	
## prettier
``` 
# 不需要的格式化的文件，可以配置文件.prettierignore文件
node_modules
dist

# 配置文件.prettierrc | prettier.config.js | .prettierrc.js
# 或在package.config.json中配置prettier字段

```

### 常见配置选项
```markdown
tabs:false
tabWidth:2
printWidth:80
semi:false
trailingComma:none | all | es5
singleQuote:false
quotes:false
endOfLine: if | crlf | cr | auto

bracketSpacing:true
bracketSameLine
jsxSingleQuote
parser
rangeStart
rangeEnd


overrides 数组
	files 数组
		// "files": "*.test.js",
		//  "files": ["*.html", "legacy/**/*.js"],
	exludeFiles
	options


```





# loader
## 与plugin的主要区别：
```markdown
Loader | Plugin
# loader主要针对特定模块进行处理
# plugin可以执行更加宽泛的任务，贯穿整个webpack周期；
	资源管理|环境注入|打包优化

	# 内置插件


loader 可以有三种方式加载
  内联方式
  命令行模式
    --module-bind "css=style-loader!css-loader"
    # webpack5已经不再支持
  配置文件
```


## PostCSS
```markdown

PostCSS
	postcss
		postcss-cli
	postcss-loader
	postcss-preset-env	# 集成了autoprefixer，功能更加强大
		autoprefixer

# 初步配置	
{
	test:/\.css$/,
	use:[
		"style-loader",
		"css-loader",
		{
			loader:"postcss-loader",
			options:{
				postcssOptions:{
					plugins:[
						require("autoprefix")
					],
				}
			}
		},
		"less-loader"
	]
}
# 上述这样写，实在是太麻烦了；
# 引出 postcss.config.js
module.exports={
	plugins:[
		- require("autoprefix"),
		+ "postcss-preset-env",

		# 为什么一个需要require，一个不需要？
		# 其实这里可以不require;reuqire出现在一些插件需要参数，这时采用require的方式可以传入参数
		# 比如：require("abcd")({a:"b"})
	],
}

# 然后就可以
{
	test:/\.css$/,
	use:[
		"style-loader",
		- "css-loader",
		+ {
			loader:"css-loader",
			options:{
				# 一般情况下，postcss不会处理@import;必须回头重新处理
				importLoaders:2
			}
		}
		"postcss-loader",
		"less-loader",
	],

}

```



## 文件资源加载
```markdown
# 解决：路径依赖问题；针对：import ... from ".png/gif/jpg/jpeg";
file-loader
	占位符:
		[name]
		[hash?:length]
		[ext]
		[contentHash]
{
	test:/\.(gif|png|jpe?g)$/,
	use:[
		{
			loader:"file-loader",
			options:{
				- name:"img/[name].[hash:8].[ext]"
				name:"[name].[hash:8].[ext]",
				outputPath:"img",
			}
		}
	],
}

url-loader
	limit选项：100*1024


webpack5自有资源加载方式
# 注意这里的[hash:6][ext]之间不需要"."，默认[ext]已包含"."
4种新的模块类型：
assert	=> url-loader
assert/resource	=> file-loader
assert/source
assert/inline

{
	test:/\.(jpe?g|png|gif)$/,
	type:"assert",
	generator:{
		filename:"img/[name].[hash:6][ext]"
	},
	parser:{
		dataUrlCondition:{
			maxSize:100 * 1024,
		}
	}
}


# 加载字体文件
{
	test:/\.(woff2|eot|ttf)$/,
	type:"assert/resource",
	generator:{
		filename:"font/[name].[hash:6][ext]"
	}

}
```


## Babel
```markdown
	工具链 <= 编译器
	代码兼容/补丁/转换
	babel
	@babel/core
		@babel/cli
	@babel/preset-env
		@babel/plugin-transform-arrow-functions
		@babel/plugin-transform-block-scoping
	babel-loader


# 在webpack中使用
{
	test:/\.m?js/,
	exlude:/node_modules/,
	use:[
		{
			loader:"babel-loader",
			options:{
				plugins;[],
				presets:[]
			}
		}
	]
}
# 简化上述；使用配置文件
# babel.config.(js|mjs|json) 或者 .babelrc.(js|mjs|json)
module.exports={
	presets:[
		[
			"@babel/preset-env",
			{
				# 补丁功能
				# npm install core-js regenerator-runtime
				# false:不使用;usage:只有编写的源文件使用
				# entry:连所依赖的第三方库都补丁;同时必须在入口文件：
import "core-js/stable";import "regenerator-runtime/runtime";
				useBuiltIns: false | "usage" | "entry",
				corejs:3.8
			}
		],
		["@babel/preset-react"],
		["@babel/preset-typescript"]
	],
	plugins:[
		# 前面所施行的补丁，默认都是添加在全局的；
		# 如果我们编写的代码作为第三方库，将导致污染别人的代码；推荐采用以下方式
		[
			"@babel/plugin-transform-runtime",
			{
				corejs:3 # 除了需要引入core-js;还需要引入@babel/runtime-corejs3
			}
		]
	]
}



# ts-loader和babel-loader的选择
	ts-loader:无法polyfill
	babel-loader:无法对错误检测
	# 结合两者：tsc类型检测，babel完成对类型的转换
	
package.json:{
	# 可以和在一起书写 "tsc --noEmit & webpack --config wk.config.js"
	build:"webpack --config wk.config.js",
	# --noEmit 与 --noEmitOnError 存在区别
	"type-check":"tsc --noEmitOnError",
	"type-check-watch":"npm run type-check -- --watch",
}
```



# 字段讲解
## devtool
```markdown
	源码经过转换（babel,typescript）/丑化(生成模式)后的代码，与源码天差地别；一旦出错，错误所发生的行号、列号肯定与实际在源码中出错的地方不合，那么该如何进行调试
	bundle.js.map
	source-map文件：打包代码映射到源文件
		# 浏览器自动加载source-map,可以重构原始源
	在转换后的代码，添加一个注释指向sourcemap;
		//# sourceMappingURL=common.bundle.js.map
	source-map文件 大概是源文件的2.5倍大小 加载™比较损耗性能


# 可选值
	false | none (生产模式：默认值；什么值都不设置) | "eval" (开发模式：默认值):都不生成source-map
		eval模式：使代码字符串中的 //# 注释生效；依然可以有效定位错误

	source-map
	eval-source-map
		不生成source-map文件，但source-map信息被编码成base64嵌入到eval函数中
	inline-source-map
		不生成source-map;直接将source-map信息全部转换为base64，放在bundle.js末尾
	cheap-source-map
		生成source-map，比选项"source-map"编译要快;但不生成错误具体所在的列信息
	cheap-module-source-map
		# cheap-moudle 必须连在一起使用
		# cheap-source-map 对被babel-loader/ts-loader转换过的代码，并不能映射成源文件；而cheap-module-source-map却能
		类似cheap-source-map,比源自loader的source-map更好
		
	hidden-source-map
		依然生成souce-map文件，只是删除了打包后文件末尾的魔法注释：//#；导致不能定位到错误，当然可以手动添加//# sourceMapURL=bundle.map.js
	nosources-source-map
		只有错误提示，不会生成源代码文件；


	组合规则
	【inline|hidden|eval】-【nosources】-【cheap[-module]】-source-map


	推荐：
		开发|测试：source-map|cheap-module-source-map
		生产：什么都不写 | false
```


## devServer
```markdown
# 网络服务+热更新（hot module replacement）
# 三种方式
- webpack-dev-middlewave
- webpack --watch + liverServer
- webpack-dev-server
	webpack serve --config webpack.config.js
	# 会重新全部编译，不会生成文件，仅仅存在于内存
# 热更新：
devServer:{ # 开启服务的目录是webpack.config.js启动的目录
	hot:true
	publicPath:
		# 需要与output中的publicPath中一致
		# express.Static()
		# 修改webpack开启本地服务的路径
	contentBase
		# 比如在模板index.html引入了一些外部资源，这些外部资源的引用路径
	watchContentBase
		# 外部引用中资源变化时，是否重新刷新
	hotOnly:true
		# 编译失败不会刷新整个页面
	host:
		# 默认是localhost,只能本台主机访问，同一个局域网下的其他主机不能访问，可以设置成“0.0.0.0”
	port
	open
		# 是否自动打开浏览器
	compress
		# 是否开启静态文件压缩
	proxy:{
		"/why":{
			target:"http://localhost:8888/",

			pathRewrite:{
				"^/why":""
			},
		secure:false # 针对https代理
		changeOrigin:true # 代理伪装，代理服务器（webpack开启的本地服务）向跨源的服务器请求时，伪装请求头中的host为 跨源服务器的host
		}

	}
	# 针对history模式的配置，刷新会返回404错误
	historyApiFallback:true
	historyApiFallback:{
		rewrites:[
			{from:/\/abc\//,to:"/index.html"}
		]
	}
}
	module.hot.accept
	vue通过vue-loader已经实现了模块热更新；
	react通过脚手架也已经实现了

```




# 打包优化
```markdown
# 只要是import方法导入的（动态、异步导入的）的模块,webpack都会分离，打包成一个独立的文件


# 代码分割：
	魔法注释：
		webpackChunkName
		webpackPrefetch
		webpackPreload
```


## 代码分割

### splitChunks
```javascript
module.exports={
  output:{
    path:path.resolve(),
    filename:"",

		// 动态导入的包的名字
		// 当然,魔法注释:webpackChunkName 也可以设置[name]
    chunkFilename:"[name].[hash:8].chunk.js",
  }
  optimization:{
		/*
			natural 自然数|不能见名知意，也不利于浏览器缓存
			named 使用包所在的目录，开发时推荐
			deterministic 根据文件生成一个id，文件相同生成的id也相同，production时推荐
		*/
		chunkIds:"natural" | "named" | "deterministic"


    // 一般来说，引入的包都会打包到一个文件中；但是这会导致这个文件体积过大，不利于首屏渲染；
    // 分包=>浏览器并行加载多个包
    splitChunks:{
      // "initial" | "async" | "all"
      // 同步 | 异步 | 全部 
      chunks:"all",// 规定只要是导入就代码就分离

      // 两个值一样时，minSize的优先级大于maxSize
      minSize:20 * 1024,// 只有拆分出来的包大于该值时，才会拆分；否则就不拆分
      maxSize:20 * 1024,// 若拆分出来的包大于此值时，就继续拆分

      minChunks:2,// 只有引入的包的次数不下于该值时，才会拆分; 针对多入口，单个入口任何包都只会被导入一次

      cacheGroups:{
        vendors:{
          test:/[\\/]node_modules[\\/]/,
          filename:"[id]_vendors.js",
          priority:-10,
        }，
        default:{
          minChunks:2,
          // filename:"common_[id].js",
          name:"chunk-common",// name是固定的，不能用placeholder
          chunks:"initial",// 这里也可以设置
          priority:-20,
          // 对已经打包过的包进行重新使用
          reuseExistingChunk:true,
        }
      }
    }
  }
}

```



### 懒加载
```markdown
# import动态脚本
	1.下载 javascript
	2.解析 脚本


# 优化：闲暇时下载=>命中缓存
	魔法注释
	下载优先级
		preload 立即下载、与父chunk并行下载
		prefetch 闲杂时下载、父chunk下载完毕后才下载
button.addEventListener("click",()=>{
	import(
		/* webpackChunkName: 'element' */
		/* webpackPrefetch:true */
	).then({default:element}=>{
		document.body.appendChild(element)
	})
})
```


### runtimeChunk | 运行时分割
```markdown
将runtime相关的代码抽离到一个单独的chunk文件中
	runtime代码：对模块进行解析、加载、模块信息相关的代码


有利于根据不同文件的加载情形 配置缓存命中
```


```javascript
module.exports={
	/* 
		true | multiply：每个运行时代码都进行分离
		single：所有的运行时代码都进行分离
		Object
	 */
	runtimeChunk:{
		- name:"runtime",//合并运行时代码时，自定义打包后的名
		name(entryponit){
			// 每个运行时代码都进行分离
			return `${entrypoint.name}-runtime`
		}
	}
}

```


## CDN| 内容分发网络
```markdown
1. 所有的静态资源都从CDN静态服务器下载
output:{
	filename:"",
	path:,
	publickPath:,// 配置所有静态资源的公共url
}

2.只有第三方包才从cdn下载
unpkg
jsDelivr
cdnjs

bootcdn
```


### externals
```javascript
// 生成环境下使用
	根据不同的环境，来决定是否使用cdn加载第三方包
	EJS模板
// externals键值对的含义：
/* 
	键：表示不需要被打包的库的名称
	值：库在浏览器中暴露的全局对象；
		// 因为我们最后是通过script标签手动引入包，而第三方包在浏览器环境下都暴露了自己的全局对象
*/
module.exports={
	externals:{
		lodash:"_",
		dayjs:"dayjs"
	}
}
```


```html
<% if(process.env.NODE_ENV==="production") { %>
	<script src=""></script>
	<script src=""></script>
<% } %>
```

##  代码压缩
### js
```markdown
代码压缩
	丑化|简化标识符、表达式等
	删除不可达的逻辑、不使用的代码块 


```


```javascript
// webpack5以上已经自动安装了
const TerserPlugin=require("terser-webpack-plugin");

module.exports={
	optimization:{
		minimize:true,// 启用默认的压缩设置
		minimizer:{
			new TerserPlugin({
				extractComments:false,
				parallel:true,
				terserOptions:{
					compress:{
						arguments:true,
						dead_code:true,
					},
					mangle:true,
					toplevel:true,
					keep_classnames:true,
					keep_fnames:true,
				}
			})
		}
	}
}
```

### css
```javascript
# css-minimizer-webpack-plugin
// 需要下载

const CSSMinimizerPlugin=require("css-minimizer-webpack-plugin");

module.exports={
	plugins:[
		new CSSminimizerPlugin()
	]
}
```


### HTML
```markdown


```
```javascript
module.exports={
	plugins:[
		new HtmlWebpackPlugin({
			title:"",
			template:"",
			inject:"head",// 使用默认设置，注入静态资源到head标签
			cache:"",// 当文件没有变化时，直接使用缓存
			minify: isProduction ? {
				removeComments:true,
				collapseWhitespace:true,
				minifyJS:{ // 可以直接设置true
					mangle:{
						toplevel:true,
					}
				},
				minifyCSS:true, // style标签中的css样式

				removeRedundantAttributes:true,
				removeEmptyAttributes:true,
				removeStyleLinkTypeAttributes:true,
				
			} : false,
		})
	]
}

```







## 作用域提升
```markdown
默认webpack在生产模式下已经配置
功能：将函数合并在一个模块中执行（webpack生成后的代码使用了大量的闭包，嵌套层级深）

const webpack=require("webpack");
new webpack.optimize.ModuleConcatenationPlugin()
// 静态分析 

```


## ThreeShaking
### JS
```markdown
思想源自LISP，纯函数无副作用，可以放心消除；
 最早使用在rollup
 依赖静态模块分析(不执行代码，直到模块之间的依赖)
	即：ES2015

实现Tree Shaking
- usedExports:标记某些函数是否被使用，再通过Terser优化
	

-  sideEffects:跳过整个模块、文件，直接查看该文件是否有副作用
```

#### usedExports
```javascript
module.exports={
	optimize:{
		usedExports:true,
		// production默认为true,开启后webpack会对未使用的函数进行标注（魔法注释的一种），形如：unused export，之后TerserPlugin会解析这些魔法注释，删除这些没有使用的函数
		minize:true,
		minizer:[
			new TerserPlugin({

			})
		]
	}
}

```

#### sideEffects
```json
// 在package.json中声明该工程中每个模块不存在副作用；
/*
主要针对一种导入：
	// 仅仅导入调用：但该模块有可能向全局注入注入了某些成员，例如：window.foo="bar",这种模块就不是纯模块，是有副作用的、影响了外界的

	import "./src/math.js";
*/

sideEffects:false	// 所有的模块都无副作用，webpack compiler可以放心删除一些导入调用的模块

// 当上述会带来一个问题，如：import "style.css"
// 会导致编写的css样式无法被打包
sideEffects:[
	"**.css",// 标注所有.css文件都是有副作用的
]
```

```javascript
// 第二种解决办法
module.exports={
	module:{
		rules:[
			{
				test:/\.css$/i,
				use:[
					"style-loader",
					"css-loader",
				],
				sideEffects:true,// 标注所有的.css文件都是有副作用的
			}
		]
	}
}

```


### CSS
```markdown
npm install -D purgecss-webpack-plugin


```

```javascript
const glob=require("glob");
// 检查所有的文件；因为js是可以动态的添加某个class或创建一个新的元素、然后使得标签选择器匹配成功
const PurgeCSSPlugin=require("purgecss-webpack-plugin")

module.exports={
	plugins:[
		new PurgeCSSPlugin({
			paths:glob.sync(path.join(__dirname,"/**/*"),{
				nodir:true, // 只检测文件
			}),
			safelist(){ // 白名单
				return {
					// 默认 没有匹配到的标签选择器会被purgecss摇下来
					standard:["body","html"]
				}
			}
		})
	]
}
```



## http压缩
```markdown
npm install compression-webpack-plugin -D


```

```javascript
const CompressionPlugin = require("compression-webpack-plugin");
module.exports={
	plugins:[
		new CompressionPlugin({
			test:/\.(css|js)$/,
			threshold:20 * 1024,	// 多大才压缩
			minRatio:0.7,// 压缩比例
			algorithm:"gzip",
			include:
			exlude:
		})
	]
}

```


## html内联runtime.js
```javascript
// 原因：一般打包后的runtime文件一般都较小，没必要分包，增加一次请求；
// 新的疑问：既然如此为何还要将运行时代码拆分出来？

// npm install -D react-dev-utils
const HtmlWebpackPlugin=require("html-webpack-plugin")
const InlineChunkHtmlPlugin=require("react-dev-utils/inline-chunk-html-plugin");


module.exports={
	plugins:[
		new InlineChunkHtmlPlugin(HtmlWebpackPlugin,[/^runtime.*\.js$/])
		// 将该正则形式匹配到的文件 注入到 index.html中，内联
	]
}

```





# 补充内容
## shimming | ProvidePlugin
```javascript
// 不推荐使用
	每个模块应该是一个封闭性的；

const {ProvidePlugin}=require("webpack")

plugins:[
	new ProvidePlugin({
		// 当在代码中遇到一个变量找不到时，通过ProvidePlugin,自动导入对应的库;这是如果配置splitChunks.cacheGroups，则会打包该自动导入的库
		// 相当于在webpack的环境中注入了一个全局变量，该全局变量来自于一个库

		// 全局变量名：对应库的名称
		axios:"axios"，
		get:["axios","get"],// get=axios.get
	})
]


```

## MiniCSSExtractPlugin
```markdown
对于css样式的加载
	在开发环境中，直接通过style标签内联
	在生产环境，则通过link外部样式


```

```javascript
const MiniCSSExtractPlugin =require("mini-css-extract-plugin");

module.exports={
	module:{
		rules:[
			{
				test:/\.css$/,
				use:[
					isProduction ? MiniCSSExtractPlugin.loader : "style-loader",
					"css-loader",
				]
			}
		]
	}
	plugins:[
		new MiniCSSExtractPlugin(
			{
				filename:"css/[name].[hash:8].[ext]"
			}
		),
	]
}
```



## hash | contenthash | chunkhash
```markdown
# 上下依赖 <=> 节点|模块

hash
	针对多入口，形成的不同链路;一个入口的中文件改变，导致另一个入口的文件命令也会一起改变（hash值变化），链路根节点的相互影响

chunkhash
	针对一条入口链路中的分支，模块引用；如果某个文件A引用了另一个文件B，但是该文件A发生变动，会导致明明没有发生变化的被引用文件B也会一起变动hash

contenthash
	针对每一个文件，链路中的节点，文件变动不会影响依赖任何文件的变动


多入口文件，若使用hash、一个入口文件变动会导致另一个没有变动的入口文件的命名发生变化；
	hash：本次build的标志
文件依赖，引用了其他模块的文件变动，会导致这些被引用的文件命名也会发生变化
	chunkhash:引用路径节点（模块）是否发生变化
	出口文件一般设置成chunkhash，只要依赖的子模块发生变动，就重新命名
conenthash
	只与自身内容相关
```

```javascript
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


## 打包库文件
```javascript
module.exports={
	mode:"development",
	entry:"./index.js",
	output:{
		path:path.resolve(__dirname,"./build"),
		filename:"cindiou_utils.js",

		libraryTarget:"umd",// 哪种环境适配；umd即适配浏览器，也是commonjs，甚至amd,

		// 正如：vue挂载window时是Vue,
		// lodash挂载到window是_,react-dom挂载到window是ReactDOM一样；
		library:"cindiouUtils",
		globalObject:"this",// 挂载到浏览器哪个对象上，默认是self，即：self["cindiouUtils"]=factory(),设置这个属性，可以将编写的模块挂载browser中任何其他全局对象，比如：document
	}
}

```




## 打包时间分析
```javascript
// 参看包的大小分析
// 第一种方法
- 在package.json scripts加入以下快捷命令
	stats:"webpack --config webpack.config.json --env production --profile --json=stats.json"
- https://webpack.github.io/analyse/

// 第二种方法
npm install webpack-bundle-analyzer -D
const {BundleAnalyzerPlugin}=require("webpack-bundle-analyzer");

module.exports={
	plugins:[
		new BundleAnalyzerPlugin()
	]
}

```


```javascript
// 查看每个loader,plugin的打包时间信息
// npm install -D speed-mesurement-webpack-plugin
const SpeedMeasurePlugin=require("speed-measure-webpack-plugin")

module.exports=new SpeedMeasurePlugin().wrap(config);// 把整个配置传入
```


# 自定义
## loader
```markdown
pitch loader从前往后
normal loader从后往前

```

### normalLoader | pitchLoader
```javascript
// loader本质是一个导出为函数的JavaScript模块
// loader runner库会调用这个函数，然后将上一个loader产生的结果或者资源文件传入进去


// normal loader
module.exports=function(content,sourcemap,meta){ // 接受其他loader处理的结果

	return content; // 处理结果返回
}


// pitch loader
module.exports.pitch=function(content){
 
}
```

### resolveLoader
```javascript
// 自定义loader的处理顺序
module.exports={
	comtext:__dirname,
	module:{
		rules:[
			{
				test:/\.js$/,
				// use属性可以使用相对模块，相对的是context,
				use:[
					"./customLoader/testloader.js",
				]
			}
		]
	},
}

// 上述写法 简写
module.exports={
	comtext:__dirname,
	module:{
		rules:[
			{
				test:/\.js$/,
				use:[
					"testloader",
				]
			}
		]
	},
	resolve:{
		moduels:[],
		extensions:[],
		mainFiles:[],
		mainFields:[],
		alias:{},
		resolveLoader:{
			// 跟加载文件同理
			// loader的加载路径
			modules:["node_module","./customLoader"]
		}
	}
}

```



### 执行顺序
```javascript
// 多个loader针对同一文件进行配置，也可以如下：
// loader栈：[loader01,loader02,loader03]
// 正常的执行顺序:从后往前，即：03->02->01

// 添加enfore后：
// loader栈:[loader01,loader03,loader02],
// 执行顺序:03->01->02

# Normal执行顺序
// pre -> normal -> inline -> post
// pre总是优先执行


module.exports={
	module:{
		rules:[
			{
				test:/\.js$/,
				loader:"customloader_01",
			},
			{
				test:/\.js$/,
				loader:"customloader_02",
				enfore:"pre",
			},
			{
				test:/\.js$/,
				loader:"customloader_03",
			},
		]
	}
}

```


### 同步loader|异步loader
```javascript
// 同步
module.exports=function(content,sourcemap,meta){
	// 方式1
	this.callback(null,content,sourcemap,meta)

	// 方式2
}

// 异步
module.exports=function(content){
	const callback=this.async();
	setTimeout(()=>{
		callback(content);
	})
}
```


### 接受参数 | 验证参数
**scheme文件**
```json
{
	"type":"Object",
	"properties":{
		"name":{
			"type":"string",
			"description":"名字"
		},
		"age":{
			"type":"number",
			"description":"年龄"
		}
	}
}

```

**配置参数**
```javascript
// npm install -D loader-utils scheme-utils

const {getOptions} = require("load-utils")
const {validate} = require("schema-utils")
const scheme = require("./scheme.json")

module.exports=function(content){
	const options=getOptions(this);
	// options就是webpack.config.json中传递给loader的参数

	validate( // 对传入的参数进行验证
		schema,options
	)

	return content;
}
```


### 案列：
#### babel-loader
```javascript
// npm install @babel/core @babel/preset-env loader-utils -D
const {getOptions} = require("loader-utils")
const babel = require("@babel/core")
module.exports=function(content){
	const options=getOptions(this);
	const callback=this.async();

	// 通过babel代码的形式进行转化
	babel.transform(content,options,(error,result)=>{
		if(error){
			callback(error)
		}else{
			callback(null,result.code)
		}
	})
}
```

#### md-loader
```javascript
// 入口文件
import "highlight.js/styles/default.css";
// 引入hightlight默认的高亮样式


```


```javascript
// npm install -D marked
const marked = require("marked")
const hljs = require("highlight.js")
module.exports=function(content){
	marked.setOptions({
		// 给转换的html字符串 添加class类
		highlight(code,lang){
			return hljs.highlight(lang,code).value
		}
	})
	const htmlContent = marked(content)
	// 利用marked将md转换为html

	// html-loader也可以完成下面这些操作；将字符串转换为javascript字符串
	const ret=`var code="${htmlContent}";export default code`

	return ret; // 必须返回javascript格式的字符串；也就是.js文件中代码的样式
}
```





## plugin


### tapable库了解
```markdown
# tapable库
	同步
		syncHook
		syncLoopHook
			返回值为true，就循环触发
		syncBallHook
			返回值为true，就不触发剩下的回调函数
		syncWaterfallHook
			将返回值作为接下来回调的第一个参数
	异步
		并行
			asyncParallelHook
		串行 
			asyncSeriesHook
```


```javascript
// npm install tapable
const {
	SyncHook,
	SyncBallHook,
	SyncLoopHook,
	SyncWaterfallHook,
	AsyncParallelHook,AsyncSeriesHook
} = require("tapable")

class Tsst(){
	constructor(){
		this.hooks={
			syncHook:new SyncHook(["name","age"]),
			asyncHook:new AsyncSeriesHook(["name","age"])
		}

		// 监听
		this.hooks.syncHook.tap("event1",(name,age)=>{
			console.log(name,age)
		})
		this.hooks.syncHook.tap("event2",(name,age)=>{ // 同时监听多个事件
			console.log(name,age)
		})


		// 异步回调
		this.hooks.asyncHook.tapAsync("event1",(name,age,done)=>{
			setTimeout(()=>{
				console.log(name,age);
				done() // 两秒之后才将执行权限传递给下一个回调
			},2000)
		})

		this.hooks.asyncHook.tapPromise("event1",(name,age)=>{
			return new Promise((resolve,reject)=>{
				setTimeout(()=>{
					console.log(name,age)
					resolve()
				},2000)
			})
		})
	}

	emit(){
		// 会触发上述两个事件
		this.hooks.syncHook.call("cindiou",18)

		// 触发异步回调
		this.hooks.asyncHook.callAsync("cindiou",18,()=>{
			console.log("异步监听结束！")
		})


		this.hooks.asyncHook.promise("cindiou",18).then(()=>{
			console.log("异步监听结束！")
		})
	}
}

```

### 案列 | 自动上传

```javascript
// npm install node-ssh
const {NodeSSH} = require("node-ssh");


class AutoUploadPlugin{
	constructor(options){
		this.ssh=new NodeSSH()
		this.options=options; // 接受参数，替换下面的参数
	}
	async apply(compiler){
		compiler.hooks.afterEmit.tapAsync("AutoUploadPlugin",async (compilation,done)=>{
			// 1.获取输出文件夹
			const outputPath = compilation.outputOptions.path;


			// 2.链接服务器、删除原来目录中的内容
			await this.connectServer()
			const remoteSavePath="/root/test"
			await this.ssh.execCommand(`rm -rf ${remoteSavePath}`);


			// 3.上传文件到服务器
			await this.uploadFiles(outputPath,remoteSavePath)

			// 4.关闭ssh服务
			this.ssh.dispose()

			done()
		})
	}


	async connectServer(){
		await this.ssh.connect({
			host:"".
			username:"root",
			password:""
		})

		console.log("链接服务器成功")
	}

	async uploadFiles(localOutputPath,remoteSavePath){
		const result = await this.ssh.putDirectory(localOutputPath,remoteSavePath,{
			recursive:true,
			concurrency:10
		})

		console.log(`传送服务器:${result ? "成功" : "失败"}`)
	}
}
```






