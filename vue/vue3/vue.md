
# 实例属性
app=Vue.createApp(options)

app.component()
	全局组件
app.mixin()
	全局混入
app.directive
app.use

app.config
	globalProperties
	compilerOptions
app.provide
	全局注入

app.mount()
app.version
app.unmount


创建全局属性
app.config.globalProperties.$name="test"
在setup中使用全局属性
const instance = getCunrrentInstance()
instance.appContext.config.globalProperties.$name



# 全局API
全局API
	createApp
	nextTick
	mergeProps
	useCssMoudle
	
	defineComponent
	defineAsyncComponent
	defineCustomComponent

	resolveComponent
	resolveDynamicComponent


```markdown
this指向
$ 开头才不会被组件实例代理
允许多个根元素

模板渲染优先级
	setup > render > template > el


指令
	v-on
		事件处理程序中可以有多个方法，这些方法由逗号运算符分隔：
	v-bind
	v-model

	v-memo
		v-once

template
	v-for 与 v-if优先级

key 
	相同组件类型的身份id
	不适用时，最大限度的减少动态元素并且尽可能尝试就地修改、复用相同元素类型的算法
	使用时，基于key的变化重新排列元素，并且移除、销毁key不存在的元素

子传父事件
	多根节点 与 单根节点 在$attrs上的安排
	emits选项
		数组
		对象

事件总线 mitt
	on
	off
	emit

插槽
	默认插槽
	动态绑定插槽

生命周期函数
  mounted 不会保证所有的子组件也都被挂载完成。
    如果你希望等待整个视图都渲染完毕，可以在 mounted 内部使用 vm.$nextTick：
    updated亦是如此
  beforeDestroy -> beforeUnmount

自定义指令
	事件属性
	函数简写 mouted | updated
	在多根节点的组件上使用，会存在危害
```


# options选项参数
watch
	字符串
	函数
	对象
		handler
		deep
		immediate
	数组

	this.$watch(expOrFn:String|Function,callback:Function,options:Objecyt)

emits选项
expose

provide
	Object
	Function
		this指向 + 响应式
inject
	数组
	对象
		重命名 注入属性名

mixins
extends
	允许多继承

compilerOptions: {
    delimiters: ["${", "}"],
    comments: true,
 }


# v-model 变化
v-model
	modelValue
	update:model-value

	emits:["update:modelValue"]

	v-model:title="title"	



# 全局组件
动态组件
	传值 | 插槽
  is
    字符串
      原生元素标签
      本组件内已注册的组件名称
    组件
缓存组件
异步组件
	defineAsyncComponent
teleport
	to
		添加
	disabled
Suspense
	两个插槽 default fallback

过渡
	v-enter	变成了 v-enter-from





# Composizition API	
```markdown
问题
	逻辑分散

更高级的复用形式
	hooks


# 顶层setup函数
setup选项 | Function	
	不能访问this
		this还没有指向组件实例
		调用发生在 data methods computed之前
	对象不能随便解构
	
函数参数	props,{emit,attrs,slots}
		props解构时：
			const {attr}=toRefs(props)
返回值
	可在template中使用，但非响应式
	还可以返回函数，将作为render函数

```


reactive 
	必须是对象 |  数组
ref
	template自动解包，在setup需要手动解包
		.value
	ref对象被普通对象报过1后，不能再在模板中解包
	若ref对象被reactive包裹，则又可以在模板中自动解包
	
	配合template中的ref属性，引用组件或原生元素
		:ref="(el)=>{}"
readonly
	普通对象 | 响应式对象
toRefs | toRef
	直接对reactive对象进行解构，得到不是响应式对象
computed
	返回的是一个ref对象

watch(响应式对象 | getter | 数组,(newValue,oldValue,onInvalidate)=>{},options)
	懒执行 | 侦听多个源
	停止执行 | 清除副作用
	getter函数形式，会 浅比较 返回值，若返回值不同则会调用副作用函数，若相同则不触发

	多个同步更改只会触发一次侦听器。
		await nextTick()
watchEffect
	默认自动执行一次
	停止侦听
	清除副作用
	执行时机：元素更新或挂载之前还是之后执行
		选项 {flush:"pre" | "post" | "sync"}


isProxy | isReactive | isReadonly
toRaw
markRaw
shallowReadonly
shallowReactive

unRef
isRef
shallowRef
	triggerRef
customRef(track,trigger)
	


生命周期函数
	setup调用发生在beforeCreated之前，在setup中没有beforeCreated | created的钩子函数
	unmounted

provide | inject


defineProps
	 只能是要么使用运行时声明，要么使用类型声明
	返回props
const props = withDefaults(defineProps<Props>(), {
  msg: 'hello',
  labels: () => ['one', 'two']
})
defineEmit
	返回emit



# jsx函数
render选项
h函数
  import {h} from "vue"
	函数式组件
	VNodes 必须唯一

	resolveComponent
		只需要对全局注册的组件使用 resolveComponent。而对于局部注册的却可以跳过
	resolveDynamicComponent
插槽的本质





# 单文件组件
可以同时存在多个style标签
<style>
/* global styles */
</style>

<style scoped>
/* local styles */
</style>

<style module>
/* local styles */
</style>
	$style
默认情况下，作用域样式不会影响到 <slot/> 渲染出来的内容，因为它们被认为是父组件所持有并传递进来的

scoped属性
module属性


选择器
	:deep()
	:slotted()
	:global()

	v-bind
		动态css




# 版本差异
```markdown
指令 | 生命周期
key

$attrs
挂载节点
	多根节点
data
props.default

v-model
v-for
v-bind
vnode生命周期

```


```markdown
	当用 Vue Router 配置路由组件时，你不应该使用 defineAsyncComponent

	指令
		事件
		在Vue3中当应用于多根组件时，将忽略该指令，并返回一个警告。
		(el,bindings,vnode)=>{
			// vnode.context Vue2中组件实例
			// bindings.instance	Vue3中组件实例
		}

	移除过滤器、事件总线、propsData参数（在创建 Vue 实例的过程中传入 prop）

	key
		<template v-for> 的 key 应该设置在 <template> 标签上 (而不是设置在它的子节点上)。
		v-if中不再能通过故意使用相同的 key 来强制重用分支

	在Vue2中，$attrs不包括class/style属性
  	因为移除了 .native 修饰符 与 $listeners。任何未在 emits 中声明的事件监听器都会被算入组件的 $attrs，并将默认绑定到组件的根节点上

	挂载元素
		不再是替换整个挂载点，而是作为innerHTML插入到挂载点中

	data选项
		只允许函数
		# Vue3中合并操作现在是浅层次的而非深层次的 (只合并根级属性)
    
	props中的default函数
		Vue3中传递了形参props,可以使用inject函数；但是this将不在指向组件实例、而是window对象

	v-model
		根本性的差异
		允许我们在自定义组件上使用多个 v-model
		v-model:title.capitalize=""
			参数 title
			修饰符 capitalize
				默认 modelModifiers
				titleModifiers.capitalize


	v-for 与 v-if优先级
	v-bind合并行为

	VNode生命周期
		vue2
			@hook:updated
		vue3
			@vnode-updated
			这些事件现在也可用于 HTML 元素，和在组件上的用法一样。
```
