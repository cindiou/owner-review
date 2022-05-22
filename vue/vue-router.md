- [安装](#安装)
- [介绍](#介绍)
	- [部分知识](#部分知识)
	- [命名视图](#命名视图)
	- [重定向与别名](#重定向与别名)
	- [路由组件传参](#路由组件传参)
- [进阶](#进阶)
	- [部分内容](#部分内容)
	- [导航守卫](#导航守卫)
		- [执行顺序](#执行顺序)
	- [数据获取](#数据获取)
	- [路由元信息](#路由元信息)
- [标签](#标签)
	- [router-link](#router-link)
	- [router-view](#router-view)
- [构建选项](#构建选项)
- [router对象](#router对象)
	- [实例属性](#实例属性)
	- [实例方法](#实例方法)
- [route对象|路由对象](#route对象路由对象)


$router
	配置VueRouter参数
		routes
$route
	路由对象
标签
	router-view
	router-link



# 安装
- 如果在一个模块化工程中使用它，必须要通过 Vue.use() 明确地安装路由功能：
- 如果使用全局的 script 标签，则无须如此 (手动安装)
- 通过注入路由器，可以在任何组件内通过 this.$router 访问路由器，也可以通过 this.$route 访问当前路由：
```javascript
Vue.use(VueRouter)

const routes = [
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar }
]

const router = new VueRouter({
  routes 
})


const app = new Vue({
  router
}).$mount('#app')
```

# 介绍
## 部分知识
```markdown
### 命名路由
  name

### 高级匹配模式
	{ path: '/optional-params/:foo?' },
	{ path: '/params-with-regex/:id(\\d+)' },
	{ path: '/asterisk/*' },
	{ path: '/optional-group/(foo/)?bar' }
### 捕获所有路由
  {path:"*",component:""}
	$route.params.pathMatch
### 嵌套路由
	以 / 开头的嵌套路径会被当作根路径。 这让你充分的使用嵌套组件而无须设置嵌套的路径
	# 空的子路由
		{ path: '', component: UserHome }

### 匹配优先级

### HTML5 History 模式
	mode:'history' | 'hash'
```

## 命名视图
```vue
<router-view class="view one"></router-view>
<router-view class="view two" name="a"></router-view>
<router-view class="view three" name="b"></router-view>

const router = new VueRouter({
  routes: [
    {
      path: '/',
      components: { // components选项
        default: Foo,
        a: Bar,
        b: Baz
      }
    }
  ]
})
```


## 重定向与别名
```markdown
### 重定向和别名
	redirect
		字符串
			相对
			绝对
		对象
		函数:(to)=>{};
	alias
		别名
```


## 路由组件传参
```markdown
### 路由组件传参
	props属性
		# 默认视图 | 命名视图
		# 可取参数
			Boolean
				如果 props 被设置为 true，route.params 将会被设置为组件属性
			Object
			Function:(to)=>({{ query: to.query.q }})

```

# 进阶
## 部分内容
```markdown
# 过渡动效
	单个
    <transition>
      <keep-alive>
        <router-view></router-view>
      </keep-alive>
    </transition>
	动态过渡

# 路由懒加载
	const Foo = () => import(/* webpackChunkName: "group-foo" */ './Foo.vue')
# 导航故障
	isNavigationFailure(failure, NavigationFailureType.redirected)

```

## 导航守卫
```markdown
	# 为了尽可能复用组件，参数或查询的改变并不会触发进入/离开的导航守卫

	# 全局守卫
		beforeEach((to,from,next)=>{})
			next的参数:Boolean | Object | Error | Function(仅限beforeRouteEnter）
		beforeResolve
		afterEach((to,from)=>{})
	# 路由独享守卫
		beforeEnter((to,from,next)=>{})
	# 组件内守卫
		beforeRouteEnter((to,from,next)=>{})
			不可以访问this
		beforeRouteUpdate
		beforeRouteLeave

  # 监听next抛出的错误
	router.onError()

```

### 执行顺序
**将路由导航、keep-alive、和组件生命周期钩子结合起来的，触发顺序，假设是从a组件离开，第一次进入b组件：**

- beforeRouteLeave:路由组件的组件离开路由前钩子，可取消路由离开。
- beforeEach: 路由全局前置守卫，可用于登录验证、全局路由loading等。
- beforeEnter: 路由独享守卫
- beforeRouteEnter: 路由组件的组件进入路由前钩子。
- beforeResolve:路由全局解析守卫
- afterEach:路由全局后置钩子
- beforeCreate:组件生命周期，不能访问this。
- created:组件生命周期，可以访问this，不能访问dom。
- beforeMount:组件生命周期
- deactivated: 离开缓存组件a，或者触发a的beforeDestroy和destroyed组件销毁钩子。
- mounted:访问/操作dom。
- activated:进入缓存组件，进入a的嵌套子组件(如果有的话)。
- 执行beforeRouteEnter回调函数next。




## 数据获取
```markdown
	路由完成前
		beforeRouteEnter:next(vm=>{})
		beforeRouteUpdate
	路由完成后
		created
		watch:$route
```



## 路由元信息
```markdown
	meta
	# 不像props属性、是会传递到路由组件中去去,meta主要用来标识该路由的一些参数;
	# 比如：该路由是否需要某些权限才能使用，比如登陆鉴权
		to.matched.some(record => record.meta.requiresAuth)
```

# 标签
## router-link
```markdown
<router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>
	to
	tag
		custom
		v-slot="{href,route,navigate,isActive,isExactActive}"
	replace
	append
		若to是一个相对路径形式，若存在append则相对于当前路径、没有则为绝对路径
	exact
		包含匹配。 举个例子，如果当前的路径是 /a/b 开头的，那么 <router-link to="/a"> 也会被设置 CSS 类名。
		<router-link to="/" exact></router-link>
	active-class
		默认值：router-link-active
	exact-active-class
		默认值: "router-link-exact-active"
```
  
## router-view



# 构建选项
```javascript
interface RouteConfig = {
  path: string,
  component?: Component,
  name?: string, // 命名路由
  components?: { [name: string]: Component }, // 命名视图组件
  redirect?: string | Location | Function,
  props?: boolean | Object | Function,
  alias?: string | Array<string>,
  children?: Array<RouteConfig>, // 嵌套路由
  beforeEnter?: (to: Route, from: Route, next: Function) => void,
  meta?: any,

  // 2.6.0+
  caseSensitive?: boolean, // 匹配规则是否大小写敏感？(默认值：false)
  pathToRegexpOptions?: Object // 编译正则的选项
}
```


```markdown
	mode
	base
	routes
	
	linkActiveClass
	linkExactActiveClass
	parseQuery / stringifyQuery

	scrollBehavior
	fallback
```


# router对象
## 实例属性
```markdown
	router.app：配置了 router 的 Vue 根实例。
	router.currentRoute
		当前路由对应的路由信息对象。

	START_LOCATION
    router.beforeEach((to, from) => {
      if (from === VueRouter.START_LOCATION) {
        // 初始导航
      }
    })
```

## 实例方法
```markdown
	beforeEach
	beforeResolve
	afterEach

	push(location, onComplete?, onAbort?)
    如果支持 Promise，router.push 或 router.replace 将返回一个 Promise。
	replace
	back
	forward
	go


	addRoute(route: RouteConfig): () => void
	# 如果该路由规则有 name，并且已经存在一个与之相同的名字，则会覆盖它。
	addRoute(parentName: string, route: RouteConfig): () => void
	getRoutes(): RouteRecord[]

	
	onReady(callback, [errorCallback])
	onError(callback)
```


# route对象|路由对象
```markdown
	# 路由对象是不可变 (immutable) 的，每次成功的导航后都会产生一个新的对象。
    watch: {
      $route(to, from) {
        // 对路由变化作出响应...
      }
    }
    beforeRouteUpdate(to, from, next) {
      // react to route changes...
      // don't forget to call next()
    }
	# 当使用路由参数时，例如从 /user/foo 导航到 /user/bar，原来的组件实例会被复用；这也意味着组件的生命周期钩子不会再被调用。
	

	$route.name

	$route.fullPath
	$route.path
	$route.params
    # 动态路由匹配
	$route.query
	$route.hash

	$route.matched
	$route.redirectedFrom
```