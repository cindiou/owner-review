- [疑难杂症](#疑难杂症)
  - [if块中的函数](#if块中的函数)
  - [{}中函数](#中函数)
  - [对实例赋予属性，该属性一定会时该实例的属性吗](#对实例赋予属性该属性一定会时该实例的属性吗)
  - [声明提升](#声明提升)
  - [module.exports与exports](#moduleexports与exports)
- [算法](#算法)
  - [实现开立方](#实现开立方)
  - [无重复字符的最长子串](#无重复字符的最长子串)
- [面试题](#面试题)
  - [手写](#手写)
    - [Object.create](#objectcreate)
    - [instanceof](#instanceof)
    - [new](#new)
    - [数据真实类型](#数据真实类型)
    - [call/apply/bind](#callapplybind)
    - [节流/防抖](#节流防抖)
    - [函数柯里化](#函数柯里化)
    - [深拷贝|浅拷贝](#深拷贝浅拷贝)
    - [日期格式化](#日期格式化)
    - [封装Ajax](#封装ajax)
    - [promise](#promise)
    - [数组相关](#数组相关)
      - [shuffle](#shuffle)
      - [flat](#flat)
      - [filter](#filter)
    - [字符串repeat方法](#字符串repeat方法)
    - [解析Params](#解析params)
    - [将数字每千分位用逗号隔开](#将数字每千分位用逗号隔开)
    - [实现非负大整数相加](#实现非负大整数相加)
    - [实现add(1)(2)(3)](#实现add123)
    - [将js对象转化为树形结构](#将js对象转化为树形结构)
    - [手写发布订阅者模式](#手写发布订阅者模式)
    - [手写路由](#手写路由)
      - [hash模式](#hash模式)
      - [history模式](#history模式)

# 疑难杂症


## if块中的函数
```javascript
# 在现代浏览器，在if语句中函数的声明不会提升，但是在老的IE版本中，if语句中的函数声明会提升

function f() { console.log('I am outside!'); }
(function () {
  if(false) {
    // 重复声明一次函数f
    function f() { console.log('I am inside!'); }
  }

  f(); // 报错，此时f=undefined
  
  /*相当于：
      var foo;
      if(false){
        foo=function(){...};
      }
      console.log(f);
  */
}());

```

## {}中函数
```javascript
console.log(window.a,a); // undefined,undefined
{
  console.log("A 前", window.a,a); // undefined,function
  a = 11;
  function a() {}
  console.log("A 后", window.a,a); // 11,11
}
console.log(window.a,a); // 11,11

console.log(window.a,a); // 11,11
{
  console.log("B 前", window.a,a); // 11,function
  function a() {}
  a = 2;
  console.log("B 后", window.a,a); // function,2
}
// 这里存在疑问
console.log(window.a,a); // function,function
```

```javascript
// 主要问题
{
	console.log(window.A,A) // undefined ƒ A(){}
	function A(){};
	A=1;
}
{
	console.log(window.B,B)
	B=1;
	function B(){};
}

```


## 对实例赋予属性，该属性一定会时该实例的属性吗

```javascript
function Person(country){
    this._country=country;
}
Object.defineProperty(Person.prototype,"country",{
    enumerable:true,
    configurable:true,
    set(val){
        this._country=val;
	},
    get(){
        return this._country;
    }
})
var p=new Person("China")
console.log("country=",p.country)
p.country="America"
console.log("own=",p.hasOwnProperty("country"))
console.log("_country=",p._country)

/*
country= China
own= false
_country= America
*/

class Person{
    constructor(country){
        this._country=country;
    }
    get country(){
        return this._country
    }
    set country(val){
        this._country=val;
    }
}
var p=new Person("China")
console.log("country=",p.country)
p.country="America"
console.log("own=",p.hasOwnProperty("country"))
console.log("_country=",p._country)
/*
country= China
own= false
_country= America
*/

```


## 声明提升
```javascript
// var允许重复声明；
// function函数声明，与var都具有声明提升效果

console.log("add=",typeof add); // "function"
function add(a,b){
    return a,b
}
console.log("add=",typeof add); // "function"
var add=1;                      
console.log("add=",typeof add); // "number"


/*//等价于
function add(a,b){}
var add;    // var可以重复声明
console.log();
console.log()
add=1;
console.log()
*/

````




## 作用域

```javascript
const a="Hello";
function foo(){
    console.log(a);
}

function bar(){
    const a="World";
    foo(); // "Hello"
}

bar()


// =================================
const a="Hello";
function foo(){
    console.log(b);
}

function bar(){
    const b="World";
    foo(); // Uncaught ReferenceError: b is not defined
}

bar()


```







## module.exports与exports

```javascript
const module={
    exports:{}
}

;(function(module,exports){
    exports=3;
})(module,module.exports)


console.log(module)
```







# 算法

## 实现开立方

```javascript
/*
f(x)=x^3-m;
	3x^2
	f(x)=f(x0)+f'(x0)(x-x0)+...
	0=f(x0)+f'(x0)(x-x0)
	x=x0-f(x0)/f'(x0)
*/
function cubic(x){
    let temp=x;
    while(Math.abs(Math.pow(temp,3)-x)>Number.EPSILON){
        temp = (2 * temp + x / (temp * temp)) / 3;;
    }
    return temp;
}

```



##  无重复字符的最长子串
```javascript
/*
 s = "bbbbb"    // 1 "b"
 s = "abcabcbb" // 3 "abc"
*/
var lengthOfLongestSubstring = function (s) {
    let map = new Map();
    let i = -1, res = 0;

    for (let j = 0; j < s.length; j++) {
        if (map.has(s[j])) {
            // i = Math.max(i, map.get(s[j]))
            i = map.get(s[j])
        }
        res = Math.max(res, j - i)
        map.set(s[j], j)
    }
    return res
};

```







# 面试题

## 手写

### Object.create

```javascript
function create(o){
    function F(){}
    F.prototype=o;
    return new F()
}



```





### instanceof

```javascript
function instanceOf(target,origin){
    if(typeof origin !== "function"){
        throw new Error();
    }
    if(typeof target !== "object" || typeof target !== "function" || !!target) return false;
    const proto = Object.getPrototypeOf(target);
    while(proto){
        if(proto === origin.prototype) return true;
        proto = Object.getPrototypeof(proto)
    }
    
    return false;
}



```







### new

```javascript
function New(constructor,...args){
    if(typeof constructor !== "fcucntion"){
        throw new Error();
    }
    const o=Object.create(constructor.prototype);
    
    // 构造函数返回值是否是对象
    const ret=constructor.apply(o,args);
    const flag=ret && (typeof ret === "object" || typeof ret === "function");
    return flag ? ret : o;
}
```



### 数据真实类型

```javascript
function type(o){
    const s=Object.prototype.toString.call(o);
    return s.match(/\[object (.*?)\]/)[1].toLowerCase();
}


['Null',
 'Undefined',
 'Object',
 'Array',
 'String',
 'Number',
 'Boolean',
 'Function',
 'RegExp'
].forEach(function (t) {
  // 在type函数(函数也是对象)上，添加专门检测某一类型的静态函数
  type['is' + t] = function (o) {
    return type(o) === t.toLowerCase();
  };
});


```





### call/apply/bind

```javascript
// 函数调用的方式：纯函数调用，对象方法调用，绑定调用，构造函数调用；

// call
Function.prototype._call=function(ctx,...args){
    if(typeof this !== "function"){
        // 有可能是这种情形 Function.prototype.call.apply(add,[callCTX,1,2])
        return new Error();
    }
    ctx = ctx || window;
    const key = Symbol("fn");	// 防止覆盖全局window上的同名键
    ctx[key]=this;
    const res=ctx.fn(...args); // 对象调用方式
    
    delete ctx[key]
    return res
}



// apply
Function.prototype._apply=function(ctx,it // 伪数组){
    if(typeof this !== "function"){
        return new Error()
    }
    ctx = ctx || window;
    const key = Symbol("fn");
    ctx[key]=this
    
    let res=null;
	if(it){ // 不是伪数组，应该报错还是怎么做；
        res=ctx[key](...it)
    }else{
        res=ctx[key]();
    }

	delete ctx[key]
	return res;
}



// bind
Function.prototype._bind=function(ctx,...args){
    if(typeof this !== "function"){
        throw new Error();
    }
    ctx = ctx || window;
    const self=this;
    
    return function(...newArgs){
        return self.apply(
            // 是否采用new的形式调用
        	new.target !== "undefined" ? this : ctx,
            args.concat(newArgs)
        )
    }
    
    /*
    return function Fn() {
        // 根据调用方式，传入不同绑定值
        return fn.apply(
          this instanceof Fn ? this : context,
          args.concat(...arguments)
        );
      };
    */
}

```









### 节流/防抖

```javascript
// https://www.zoo.team/article/anti-shake-throttle 细节
//https://vue3js.cn/interview/JavaScript/debounce_throttle.html#%E4%BB%A3%E7%A0%81%E5%AE%9E%E7%8E%B0

/*
三、应用场景
防抖在连续的事件，只需触发一次回调的场景有：

搜索框搜索输入。只需用户最后一次输入完，再发送请求
手机号、邮箱验证输入检测
窗口大小resize。只需窗口调整完成后，计算窗口大小。防止重复渲染。
节流在间隔一段时间执行一次回调的场景有：

滚动加载，加载更多或滚到底部监听
搜索框，搜索联想功能
*/

function debounce(fn,delay,immediate){
    let timer;
    
    return function(){
        if(timer){
            clearTimeout(timer);
            timer=null;
        }
        const args=arguments;
        
        if(immediate){
            immediate=false;	// false
            fn.apply(this,arguments);
        }
        timer=setTimeout(()=>{
            fn.apply(this,args)
        },delay)
    }
}



function throttle(fn,delay){
    let timer;
    
    return function(){
        if(timer) return;	// 到底需不需要取消之前的回调函数；之前的函数是否需要执行？
        const args=arguments;
        
        timer=setTimeout(()=>{
            timer=null;
            fn.apply(this,args)
        },delay)
    }
}

// 比如下面这种实现，就会导致原先的回调函数不会执行，取消原来的后可能会绑定一个新的上下文环境
function throttled(fn, delay) {
    let timer = null
    let starttime = Date.now()
    return function () {
        let curTime = Date.now() // 当前时间
        let remaining = delay - (curTime - starttime)  // 从上一次到现在，还剩下多少多余时间
        let context = this
        let args = arguments
        clearTimeout(timer)
        if (remaining <= 0) {
            fn.apply(context, args)
            starttime = Date.now()
        } else {
            timer = setTimeout(fn, remaining);
        }
    }
}

窟窿

```









### 函数柯里化

```javascript
// es5
function curry(fn){
	var args = [].slice.call(arguments,1);
    var l = fn.length
    if(l <= args.length){
        return fn.apply(this,args)
    }
    return function(){
        var nextArgs = [].slice.call(arguments,0);
  		nextArgs = args.concat(nextArgs);
        if(l <= nextArgs.length){
            return fn.apply(this,nextArgs);
        }else{
            nextArgs.unshift(fn);
            
            // 不满足，递归的解决
            return curry.apply(this,nextArgs);
        }
    }
}



// es6
function curry(fn,...args){
    if(fn.length <= args.length){
        return fn.apply(null,args)
    }else{
        return curry.bind(null,fn,...args)
    }
}
```







### 深拷贝|浅拷贝

```javascript
# 在实现拷贝时，必须考虑到 存储器属性，符号属性，不可枚举属性？
# JSON可允许的数据类型，

# 没有解决循环引用？

// 浅拷贝：Object.assign/扩展操作符/slice/contact

function shallowCopy(o){
    if(Array.isArray(o)){
        // 假如这个数组除了索引属性外，还有其他属性呢？
        return o.slice();
    }
    const ret={};
    for(const key in o){
        if(o.hasOwnProperty(key)){
            ret[key]=o[key]
		}
    }
    return ret;
}


// 深拷贝：JSON，第三方库
function deepClone(o,mark=new WeakMap()){
    let res=null;
    if(Array.isArray(o)){
        res=[];
    }else{
        res={};
    }
    
    if(map.has(o)) return map.get(o);
    map.set(o,res);
    
    for(const key in o){ // 符号属性没有解决
        if(o.hasOwnProperty(key)){
            const val=o[key];
            if(typeof val === "object" || typeof val === "function"){
                res[key]=deepClone(val,mark);
            }else{
                res[key]=val;
            }
        }
    }
    return res;
}

```





### 日期格式化

```javascript
Date.prototype.format = function(fmt){
  var o = {
    "M+" : this.getMonth()+1,                 //月份
    "d+" : this.getDate(),                    //日
    "h+" : this.getHours(),                   //小时
    "m+" : this.getMinutes(),                 //分
    "s+" : this.getSeconds(),                 //秒
    "q+" : Math.floor((this.getMonth()+3)/3), //季度
    "S"  : this.getMilliseconds()             //毫秒
  };

  if(/(y+)/.test(fmt)){
    fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
  }
        
  for(var k in o){
    if(new RegExp("("+ k +")").test(fmt)){
      fmt = fmt.replace(
        RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));  
    }       
  }

  return fmt;
}

const d=new Date();

```







### 封装Ajax

```javascript
// promise 封装实现：
function getJSON(url) {
  // 创建一个 promise 对象
  let promise = new Promise(function(resolve, reject) {
    let xhr = new XMLHttpRequest();
    // 新建一个 http 请求
    xhr.open("GET", url, true);
    // 设置状态的监听函数
    xhr.onreadystatechange = function() {
      if (this.readyState !== 4) return;
      // 当请求成功或失败时，改变 promise 的状态
      if (this.status === 200) {
        resolve(this.response);
      } else {
        reject(new Error(this.statusText));
      }
    };
    // 设置错误监听函数
    xhr.onerror = function() {
      reject(new Error(this.statusText));
    };
    // 设置响应的数据类型
    xhr.responseType = "json";
    // 设置请求头信息
    xhr.setRequestHeader("Accept", "application/json");
    // 发送 http 请求
    xhr.send(null);
  });
  return promise;
}
```









### promise

```javascript
class _Promise{
    static FULFILLED = Symbol("FUlFILLED");
	static REJECTED = Symbol("REJECTED");
	static PEDDING = Symbol("PEDDING");
	static schedule = typeof window === "object" && window.queueMicrotask || setTimeout

	value;
	reason;
	_status=_Promise.PEDDING;
	store=[];

	get status(){
        return this._status;
    }
	set status(val){
        if(![_Promise.REJECTED,_Promise.FULFILLED].includes(val)){
            throw new Error();
        }
        const [launchResolve,launchReject]=this.store;
        switch(val){
            case _Promise.REJECTED:
                launchReject && launchReject();
                this._status=_Promise.REJECTED;
            case _Promise.FULFILLED:
                launchResolve && launchResolve();
                this._status=_Promise.FULFILLED;
        }
    }

	static in_thenbale(o){
        if(!!o || typeof o !== "object" || typeof o !== "function") return false;
        const thenFn=o["then"]
        if(typeof thenFn !== "function") return false;
        return thenFn;
    }
	static in_resolve(value){
        if(this.status === _Promise.PEDDING){
            _Promise.in_connect(
                value,
           		this,
                (value)=>{
                	this.status=_Promise.FULFILLED;
                    this.value=value;
            	},(reason)=>{
                	this.status=_Promise.REJECTED;
                    this.reason=reason;
            })
        }
    }
	static in_reject(reason){
        if(this.status === _Promise.PEDDING){
            this.status=_Promise.REJECTED;
            this.reason=reason;
        }
    }

	static in_connect(prev,next,nextResolve,nextReject){
        if(prev === next){
            throw new TypeError("Chaining cycle detected for promise #<Promise>")
        }
        const thenFn=Promise.in_thenable(prev);
        let done=false;
        if(thenFn){
            try{
                thenFn.call(
                    prev,
                    (value)=>{
                    	if(done) return;
                		done=true;
                        _Promise.in_connect(value,next,nextResolve,nextReject)
                    },
                    (reason)=>{
                        if(done) return;
                        done=true;
                        nextReject(reason);
                    }
                )
            }catch(e){
                if(done) return;
                done=true;//防止状态变化
                nextReject(e)
            }
        }else{
            nextResolve(prev)
        }
    }

	constructor(executor){
        try{
            executor(this.in_resolve.bind(this),this.in_reject.bind(this));
        }catch(e){
            this.in_reject(e);
        }
    }

	then(onFulfilled,onRejected){
        onFulfilled = typeof onFulfilled === "function" ?  onFulfilled : val=>val;
        onRejected = typeof onRejected === "function" ? onRejected : reason => {
            throw reason;
        };
        
        const next = new _Promise((resolve,reject)=>{
            const simple = (fn)=>()=>{
				_Promise.schedule(()=>{
                    try{
                        const prevResult = fn();
                        resolve(prevResult);
                    }catch(e){
                        reject(e);
                    }
                })
            }
            
            switch(this.status){
                case _Promise.PEDDING:
                    return this.store.push(...[
                        simple(()=>onFulfilled(this.value)),
                        simple(()=>onRejected(this.reason))
                    ]);
                case _Promise.FULFILLED:
                    return simple(()=>onFulfilled(this.value))();
                case _Promise.REJECTED:
                    return simple(()=>onRejected(this.reason))();
            }
        })
        
        return next;
    }

	catch(onRejected){
        return this.then(undefined,onRecjcted)
    }
	finally(cb){
        return this.then(
        	(val)=>{
                return _Promise.resolve(cb()).then(()=>val)
            },
            (e)=>{
                return _Promise.resolve(cb()).catch(()=>{throw e})
            }
        )
    }

	static all(it){
        return new _Promise((resolve,reject)=>{
            const res=[];
            const tmep=Array.from(it);
            for(const p of temp){
                _Promise.resolve(p).then(
                	(val)=>{
                        if(res.push(val) === temp.length){
                            resolve(res)
                        }
                    },
                    (e)=>{
                        reject(e)
                    }
                )
            }
        })
    }

	static race(it){
        return new _Promise((resolve,reject)=>{
            for(const p of it){
                _Promise.resolve(p).then(resolve,reject)
            }
        })
    }

	static allSettled(it){
        return new _Promise((resolve,reject)=>{
            const temp=Array.from(it);
            const res=[]
            for(const p of temp){
                _Promise.resolve(p).then(
                	(value)=>{
                        if(res.push({
                            value,
                            status:"fulfilled"
                        }) === temp.length){
                            resolve(res);
                        }
                    },
                    (reason)=>{
                        if(res.push({
                            reason,
                            status:"rejected"
                        }) === temp.length){
                            resolve(res)
                        }
                    }
                )
            }
        })
    }

	static any(it){
        return new _Promise((resolve,reject)=>{
            const res=[]
            const temp=Array.from(it);
            for(const p of temp){
                _Promise.resolve(p).then(
                	(val)=>{
                        resolve(val);
                    },
                    (e)=>{
                        if(res.push(e) === temp.length){
                            reject(res);
                        }
                    }
                )
            }
        })
    }
}




```







### 数组相关

#### shuffle

```javascript
Array.prototype.shuffle=function(){
    const l=this.length;
    for(let i=0;i<l;i++){
        const r=Math.floor(l * Math.random());
        [this[i],this[r]] = [this[r],this[i]]
    }
}
```





#### flat

```javascript
// Infinity === Infinity - 1
# 其他方式：toString()+split();JSON.stringfy() + 正则替换

Array.prototype.flat=function(depth=1){
    if(depth===0) return this.slice();
    
    return this.reduce((acc,v)=>{
        if(Array.isArray(v)){
            return acc.concat(v.flat(depth-1))
        }else{
            return acc.concat(v)
        }
    },[])
}

```







#### filter

```javascript
Array.prototype._filter = function(fn) {
    if (typeof fn !== "function") {
        throw Error('参数必须是一个函数');
    }
    const res = [];
    for (let i = 0, len = this.length; i < len; i++) {
        fn(this[i]) && res.push(this[i]);
    }
    return res;
}

```









### 字符串repeat方法

```javascript
function repeat(s, n) {
    return (new Array(n + 1)).join(s);
}
```







### 解析Params

```javascript
let url = 'http://www.domain.com/?user=anonymous&id=123&id=456&city=%E5%8C%97%E4%BA%AC&enabled';
parseParam(url)
/* 结果
{ user: 'anonymous',
  id: [ 123, 456 ], // 重复出现的 key 要组装成数组，能被转成数字的就转成数字类型
  city: '北京', // 中文需解码
  enabled: true, // 未指定值得 key 约定为 true
}
*/



# 针对上述题解的答案
function parseParam(url) {
  const paramsStr = /.+\?(.+)$/.exec(url)[1]; // 将 ? 后面的字符串取出来
  const paramsArr = paramsStr.split('&'); // 将字符串以 & 分割后存到数组中
  let paramsObj = {};
  // 将 params 存到对象中
  paramsArr.forEach(param => {
    if (/=/.test(param)) { // 处理有 value 的参数
      let [key, val] = param.split('='); // 分割 key 和 value
      val = decodeURIComponent(val); // 解码
      val = /^\d+$/.test(val) ? parseFloat(val) : val; // 判断是否转为数字
      if (paramsObj.hasOwnProperty(key)) { // 如果对象有 key，则添加一个值
        paramsObj[key] = [].concat(paramsObj[key], val);
      } else { // 如果对象没有这个 key，创建 key 并设置值
        paramsObj[key] = val;
      }
    } else { // 处理没有 value 的参数
      paramsObj[param] = true;
    }
  })
  return paramsObj;
}
```





### 将数字每千分位用逗号隔开

```javascript
function format(n) {
  // 是否是十进制，已解决 toString()会自动转换为十进制
  // 是否对小数部分也需要处理
  const s = n.toString();
  const [i, f] = s.split(".");
  const res = [];
  for (let c = 0; c < i.length; c++) {
    const index = i.length - c - 1; // 真实的索引，c为计数
    if (c !== 0 && c % 3 === 0) {
      res.unshift(",");
    }
    res.unshift(i[index]);
  }
  return f ? res.join("") + "." + f : res.join("");
}

format(12323.33)  // '12,323.33'
```



### 实现非负大整数相加

```javascript
// a,b -> string

// ~NaN === -1
// ~ -1 === 0
function sumBigNumber(a,b){
    const l1=a.split("");
    const l2=b.split("");
    
    let res="",up=0;
    while(l1.length || l1.length || up){
        const sum=~~l1.pop() + ~~l2.pop() + up;
        up=Math.floor(sum/10);
        res= sum%10 + res;
    }
    return res.replace(/^0+/, '');
}
```







### 实现add(1)(2)(3)

```javascript
# console.log 会调用 toString()
# 而temp.toString中的m就是add的参数

var add = function (m) {
  var temp = function (n) {
    return add(m + n);
  }
  temp.toString = function () {
    return m;
  }
  return temp;
};
console.log(add(3)(4)(5)); // 12
console.log(add(3)(6)(9)(25)); // 43


# 下面的curry实现的也很有意思，只有当不传入参数时就会开始调用fn
function add (...args) {
    //求和
    return args.reduce((a, b) => a + b)
}
function currying (fn) {
    let args = []
    return function temp (...newArgs) {
        if (newArgs.length) {
            args = [
                ...args,
                ...newArgs
            ]
            return temp
        } else { // 没有参数就开始调用
            let val = fn.apply(this, args)
            args = [] //保证再次调用时清空
            return val
        }
    }
}
let addCurry = currying(add)
console.log(addCurry(1)(2)(3)(4, 5)())  //15
console.log(addCurry(1)(2)(3, 4, 5)())  //15
console.log(addCurry(1)(2, 3, 4, 5)())  //15

```







### 将js对象转化为树形结构

```javascript
// 转换前：
source = [{
            id: 1,
            pid: 0, // 父节点
            name: 'body'
          }, {
            id: 2,
            pid: 1,
            name: 'title'
          }, {
            id: 3,
            pid: 2,
            name: 'div'
          }]
// 转换为: 
tree = [{
          id: 1,
          pid: 0,
          name: 'body',
          children: [{
            id: 2,
            pid: 1,
            name: 'title',
            children: [{
              id: 3,
              pid: 1,
              name: 'div'
            }]
          }
        }]

    
function jsonToTree(data) {
  // 初始化结果数组，并判断输入数据的格式
  let result = []
  if(!Array.isArray(data)) {
    return result
  }
  // 使用map，将当前对象的id与当前对象对应存储起来
  let map = {};
  data.forEach(item => {
    map[item.id] = item;
  });
  // 
  data.forEach(item => {
    let parent = map[item.pid];
    if(parent) { 
      # 这一段代码很有意思
      (parent.children || (parent.children = [])).push(item);
    } else { // 没有父节点，说明要么是孤立节点或者根节点
      result.push(item);
    }
  });
  return result;
}
```

### 手写发布订阅者模式
```javascript
// 生命周期，这里可以存在一个回调，每当给一个已经存在eventName添加新的listener时会触发一个事件

class EventEmitter{
    _events=new Map();

    on(eventName,listener){ // 允不允许添加重复的事件
        if(typeof listener !== "function"){
            return throw new Error("listener is not a function")
        }
        const callbacks = this._events.get(eventName) || [];
        callbacks.push(listener);
        this._events.set(eventName,callbacks);
    }

    once(eventName,listener){
        if(typeof listener !== "function"){
            return throw new Error("listener is not a function")
        }
        const wrapper = (...args)=>{
            listener.apply(null,args);
            this.off(eventName,wrapper);//自己卸载
        }
        // 有可能提前注销
        wrapper._initialCallback=listener;
        this.on(eventName,wrapper)
    }

    emit(eventName,...args){
        if(!this._events.has(eventName)){
            // 显示提示不存在该事件名称
            return throw new Error(`can't find eventName:${eventName}`)
        }
        const callbacks = this._events.get(eventName);
        callbacks.forEach(cb=>{
            cb && cb.apply(null,args)
        })
    }
    off(eventName,listener){
        // 如果不存在listener意味着删除所有
        if(listener === undefined){
            return this._events.delete(eventName)
        }

        const callbacks = this._events.get(eventName) || [];
        const newCallbacks=callbacks.filter(cb=>![cb,cb._intialCallback].includes(listener))

        this._events.set(eventName,newCallbacks)
    }
}
```


### 手写路由
```markdown
 https://zhuanlan.zhihu.com/p/130995492
```
#### hash模式
```javascript
class HashRouter{
    curURL="/";
    _events=new Map();
    constructor(){
        for(const eventName of ["load","hashchange"]){
            window.addEventListener(eventName,this.refresh.bind(this),false)
        }
    }

    dealHashURL(...hashs){
        return hashs.map(h=>h.match(/#(.+)/)[1]  || "/")
    }

    refresh(e){
        let [past,now]=[this.curURL,null]
        if("newValue" in e){
            // "hashChange"
            const {oldURL,newURL}=e;
            ([past,now] = this.dealHashURL(oldURL,newURL))
        }else{
            ([now]=this.dealHashURL(window.location.hash))
        }

        this.curURL=now;
        this.emit("change",past,now)
    }

    on(eventName,listener){
        const callbacks=this._events.get(eventName) || []
        callbacks.push(listener)
        this._events.set(eventName,callbacks)
    }
    emit(eventName,...args){
        (this._events.get(eventName) || [])
            .map(cb=>cb && cb.apply(null,args))
    }
}

```



#### history模式
```javascript
// history模式仅改变地址栏地址显示，不会刷新页面
// pushState、replaceState并不会触发popstate事件


class HistoryRouter{
    curURL="/";
    _events=new Map();

    static{
        function _enchance_(type){
            const fn=window.history[type];
            return function(){
                const ret = fn.apply(this,arguments);
                const e=new Event(type);
                e.args=Array.from(arguments);
                window.dispatchEvent(e);
                return ret;// 返回结果
            }
        }
        for(const fnName of ["pushState","replaceState"]){
            window.history[fnName]=_enhance_(fnName.toLowerCase())
        }
    }
    constructor(){
        for(const eventName of ["load","popchange","pushstate","replacestate"]){
            window.addEventListener(eventName,this.refresh.bind(this),false)
        }
    }

    refresh(e){
        const [past,now]=[this.curURL,window.location.pathname];
        this.emit("change",past,now)
    }

    on(eventName,listener){
        const callbacks=this._events.get(eventName) || []
        callbacks.push(listener)
        this._events.set(eventName,callbacks)
    }
    emit(eventName,...args){
        (this._events.get(eventName) || [])
            .map(cb=>cb && cb.apply(null,args))
    }
}

```


