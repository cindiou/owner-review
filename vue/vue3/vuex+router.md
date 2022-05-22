# vuex
app.use(store).use(router)

createStore
	# 使用常量替代 Mutation 事件类型
useStore
	自定义Hook
		useMapper
		useState
		useGetters

	module.context
		vuex热重载

	$store属性的类型声明
	useStore返回值store类型声明


# vue-router
createRouter
	history:createWebHistory() || createWenHashHistory()

	NotFound
		/:pathMatch(.*)
		/:pathMatch(.*)*

	路由匹配语法
		动态路由对应的组件切换时将被复用

	嵌套路由
		更具体的路由应放在之前
		空路由

	手动跳转
		name + params 搭配

	beforeEnter、redirect同时配置时，只有redirect有效

	路由组件传参
		props

	路由元信息
		route.matched
		route.meta

	数据获取
		$route不再是不可变对象？
		需要直接监听 $route.params

	滚动行为
		scrollBehavior(to,for,savedPosition)
	导航故障

useRouter
useRoute


## 全局标签
router-link
	navigate,route,href,isActive,isExactActive
router-view
	route,Component
	# 可以使用插槽

```html
<transition>
	<keep-alive>
		<router-view>
			
		</router-view>
	</keep-alive>
</transition>


<router-view v-slot="{route,Component}">
	<transition>
		<keep-alive>
			<component :is="Component">
				<span></span>
			</component>
		</keep-alive>
	</transition>
</router-view>
```


## 动态添加路由
addRoute
	返回值也可以删除动态添加的路由

	# 若新增加的路由与当前位置相匹配，就需要你用 router.push() 或 router.replace() 来手动导航，才能显示该新路由
	router.replace(router.currentRoute.value.fullPath)
removeRoute()
	路由对象对应的 name 属性
getRoutes()
hasRoute()






## 导航守卫
	由于next函数可能被调用多次，推荐不再使用next函数，而是返回一个值
		promise
			这意味着这些导航守卫接受async函数

	beforeEnter 守卫 只在进入路由时触发，不会在 params、query 或 hash 改变时触发。
		这些情况都会对组件进行复用，只会触发组件内守卫beforeRouteUpdate。不会触发beforeEnter

		数组



## 细微差异
	跳转或解析不存在的命名路由会产生错误：

	Vue Router 不再使用 path-to-regexp，而是实现了自己的解析系统，允许路由排序并实现动态路由
		// 由于取消了 path-to-regexp，所以不再支持未命名的参数：

	删除 router-link 上的属性 tag/event/append

	# 忽略 mixins 中的导航守卫

	# 所有的导航现在都是异步的
		app.use(router)
		router.isReady().then(() => app.mount('#app'))


# nginx配置
```nginx
location / {
	root 
	try_files $uri $uri/ /index.html;
	index index.html index.htm;
}
```

