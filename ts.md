- [简介](#简介)
- [基础类型](#基础类型)
- [其他类型](#其他类型)
	- [字面量类型](#字面量类型)
	- [数组 | 元组](#数组--元组)
	- [对象类型](#对象类型)
		- [额外的属性检测](#额外的属性检测)
	- [函数类型](#函数类型)
	- [泛型](#泛型)
	- [联合类型 | 交叉类型](#联合类型--交叉类型)
	- [类型别名 | 接口](#类型别名--接口)
		- [类实现接口](#类实现接口)
		- [接口继承类](#接口继承类)
	- [keyof](#keyof)
	- [typeof](#typeof)
	- [索引访问类型](#索引访问类型)
	- [条件类型](#条件类型)
	- [映射类型](#映射类型)
	- [模板字面量类型](#模板字面量类型)
	- [枚举](#枚举)
- [重难点](#重难点)
	- [模块](#模块)
		- [动态导入](#动态导入)
		- [模块解析](#模块解析)
	- [内模块 | 命名空间](#内模块--命名空间)
	- [声明合并](#声明合并)
		- [外部模块扩展](#外部模块扩展)
		- [全局模块扩展](#全局模块扩展)
		- [混入](#混入)
	- [类](#类)
	- [装饰器](#装饰器)
- [其他](#其他)
	- [三斜线指令](#三斜线指令)
- [工具类型](#工具类型)
	- [其他案列](#其他案列)


# 简介
```markdown
将一些运行时错误、冗余提早发现
结构化类型语言
  鸭子类型
静态类型检测
	拼写错误
	语法错误
	逻辑错误
	未使用
代码补全功能
// @ts-expect-error


类型推断
	上下文
	递归进行的，检查每个成员及子成员
类型注解
类型断言
	as
	<>

	非空类型断言 !
	
tsc
	--noEmit
	--noEmitOnError
	--target
	--noImplicitAny
	--strictNullChecks
	--watch
	--outFile
		默认是 分别对引入的模块进行编译，每个模块最后都会生成自己的.js文件
		outFile 选项可以将所有编译内容合并成一个文件输入
	--declareation
		生成 .d.ts 声明文件
	--moduleResolution
		指定 模块解析策略 ： Node | Classic
		在使用了 --module AMD | System | ES2015 时的默认值为 Classic
	--module
		ts 转换成 js 时采用的模块标准
	--traceResolution 
		启用编译器的模块解析跟踪,分析模块解析过程
	--noResolve
		只 添加命令行中的传入的文件到编译列表
```



# 基础类型
```markdown
	string
	number
	boolean
	bigint
	symbol
	
	this类型
		函数第一个参数，this绑定
		类中原型函数的返回类型
	unknown
	any
	object
	Function
		()=>void

	void
		没有返回任何值，返回值不明确
	never
		错误 | 死循环
		任何类型不可赋值给never类型
	null
	undefined


```

# 其他类型
```markdown


```


## 字面量类型
```markdown
as const

字符串字面量
布尔字面量
数字字面量
```


## 数组 | 元组
```markdown
数组
	T[]
	Array<T>

	readonly T[]
	ReadonlyArray<T>

	ReadonlyArray类型与Array不可相互赋值
元组
	可选，必须在最后
		type Either2dOr3d = [numer,numer,number?]
	剩余
		[string, number, ...boolean[]]; 
		[string, ...boolean[], number];
	readnoly 元组
		给一个数组字面量  const  断言，也会被推断为  readonly  元组类型（字面量）。
		元组可以赋值给readonly元组，但readonly元组不能赋值给元组 
```

## 对象类型
```markdown
	可选
	只读	
		as const
```

### 额外的属性检测
```typescript
// 当将它们赋值给变量或作为参数传递的时候，对象字面量会被特殊对待而且会经过_额外属性检查_。

interface SquareConfig { 
  color?: string; 
  width?: number; 
} 
function createSquare(config: SquareConfig): { color: string; area: number } { 
  // ... 
} 
let mySquare = createSquare({ colour: "red", width: 100 }); // Error <=>

// 解决办法 一：类型断言：
let mySquare = createSquare({ width: 100, opacity: 0.5 } as SquareConfig);

// 解决办法 二：索引签名
interface SquareConfig { 
  color?: string; 
  width?: number; 
  [propName: string]: any; 
}

// 解决办法 三：将这个对象赋值给一个另一个变量
let squareOptions = { colour: "red", width: 100 }; 
let mySquare = createSquare(squareOptions);
```




## 函数类型
```markdown
	调用签名
	构造函数签名

	函数重载
		重载签名
			在定义重载的时候，一定要把最精确的定义放在最前面。
		实现签名
	可选参数
		回调函数不需要声明参数为可选
		默认值
	剩余参数
	解构赋值
	函数的可赋值性
		void
		参数可以少，但返回值不可以少
			忽略额外的参数在JavaScript里是很常见的。
```

## 泛型
```markdown
	函数
	类
		泛型类仅仅对实例部分生效，注意静态成员并不能使用类型参数。
	接口
	类型别名

	泛型约束
    function createInstance<A extends Animal>(c: new () => A): A { 
      return new c(); 
    }
	泛型参数推断
		失败时，手动指定类型参数
	泛型函数调用签名
		{ <Type>(arg: Type): Type }
```


## 联合类型 | 交叉类型
```markdown
联合类型
	可识别联合
	类型收窄
		typeof
		instanceof
		in
			if
		真值
		等值
			!=
	基于可达性的控制流分析
	类型·判断式
		pet is Fish
	穷举检测
		never


交叉类型
```

## 类型别名 | 接口
```markdown
类型别名
	唯一
	交叉
	存在悬浮显示
接口
	可扩展
		声明合并
		继承extends，允许多继承
			不允许继承时 重写 属性类型
	可选
	readonly
		类似const声明，并不意味着readonly声明的属性就是完全不能更改的
		在检测两个类型是否兼容时，并不会考虑其属性是否是readonly
	索引签名
		数字索引的返回类型一定是字符索引类型的子类型
		强制要求所有属性都要匹配索引签名的返回类型
		仍然可以使用readonly修饰
			readonly [index:number] : number | string


```

```typescript
type Tree<T> = { 
    value: T; 
    left: Tree<T>; 
    right: Tree<T>; 
}

type LinkedList<T> = T & { next: LinkedList<T> }; 
```


### 类实现接口
```typescript
/* 
	类实现接口 implements
		类是具有两个类型的：静态部分的类型和实例的类型。
		当一个类实现了一个接口时，只对其实例部分进行类型检查。 
 */

interface ClockConstructor { 
  new (hour: number, minute: number): ClockInterface; 
} 
interface ClockInterface { 
  tick(): void; 
} 
function createClock(
  ctor: ClockConstructor, 
  hour: number, 
  minute: number 
): ClockInterface { 
  return new ctor(hour, minute); 
} 
class DigitalClock implements ClockInterface { 
  constructor(h: number, m: number) {} 
  tick() { 
    console.log("beep beep"); 
  } 
} 
class AnalogClock implements ClockInterface { 
  constructor(h: number, m: number) {} 
  tick() { 
    console.log("tick tock"); 
  } 
} 
let digital = createClock(DigitalClock, 12, 17); 
let analog = createClock(AnalogClock, 7, 32);

```

### 接口继承类
```typescript
/* 
	当接口继承了一个类类型时，它会继承类的成员但不包括其实现。接口同样会继承到类的 private 和 protected 成员。 
	这意味着当你创建了一个接口继承了一个拥有私有或受保护的成员的类时，这个接口类型只能被这个类或其子类所实现（implement）。
 */

class Control { 
  private state: any; 
} 
interface SelectableControl extends Control { 
  select(): void; 
} 

// 只有继承 Control 的类才有资格实现 SelectableControl 接口
class Button extends Control implements SelectableControl { 
  select() {} 
} 
```




## keyof
```typescript
function useKey<T, K extends Extract<keyof T, string>>(o: T, k: K) {
  var name: string = k; // OK
}
```


## typeof
```markdown
	ReturnType<typeof fn>
	只有对标识符（比如变量名）或者他们的属性使用  typeof  才是合法的。
```

## 索引访问类型
```markdown
	字面量类型
    const APP = ['TaoBao', 'Tmall', 'Alipay'] as const; 
    type app = typeof APP[number]; 
    // type app = "TaoBao" | "Tmall" | "Alipay" 

```


## 条件类型
```typescript
type Flatten<T> = T extends any[] ? T[number] : T; 
type Flatten<Type> = Type extends Array<infer Item> ? Item : Type; 

// 分发条件类型
	type ToArrayNonDist<Type> = [Type] extends [any] ? Type[] : never; 

// 有条件类型递归引用自身
	type ElementType<T> = T extends any[] ? ElementType<T[number]> : T; 

// 有条件类型可以嵌套来构成一系列的匹配模式，按顺序进行求值
type Unpacked<T> = 
    T extends (infer U)[] ? U : 
    T extends (...args: any[]) => infer U ? U : 
    T extends Promise<infer U> ? U : 
    T; 

// 在协变位置上，同一个类型变量的多个候选类型会被推断为联合类型：
type Foo<T> = T extends { a: infer U, b: infer U } ? U : never; 
type T11 = Foo<{ a: string, b: number }>;  // string | number
// 在抗变位置上，同一个类型变量的多个候选类型会被推断为交叉类型：
type Bar<T> = T extends { a: (x: infer U) => void, b: (x: infer U) => void } ? U : never; 
type T21 = Bar<{ a: (x: string) => void, b: (x: number) => void }>;  // string & number
```

```typescript
// 嵌套了有条件类型：
type TypeName<T> = 
    T extends string ? "string" : 
    T extends number ? "number" : 
    T extends boolean ? "boolean" : 
    T extends undefined ? "undefined" : 
    T extends Function ? "function" : 
    "object"; 


type BoxedValue<T> = { value: T }; 
type BoxedArray<T> = { array: T[] }; 
type Boxed<T> = T extends any[] ? BoxedArray<T[number]> : BoxedValue<T>; 

```


## 映射类型
```typescript
	// 映射修饰符
    type CreateMutable<Type> = { 
      -readonly [Property in keyof Type]: Type[Property]; 
    };
    type Concrete<Type> = { 
      [Property in keyof Type]-?: Type[Property]; 
    };

	// as实现键名重新映射
    type Getters<Type> = { 
        [Property in keyof Type as `get${Capitalize<string & Property>}`]: () => Type[Property]
    };
	// 通过as映射成一个  never  从而过滤掉某些属性:
    type RemoveKindField<Type> = { 
        [Property in keyof Type as Exclude<Property, "kind">]: Type[Property] 
    };
```


```typescript
type Keys = 'option1' | 'option2'; 
type Flags = { [K in Keys]: boolean };
/* 
type Flags = { 
    option1: boolean; 
    option2: boolean; 
}
 */

// 若想添加成员，则可以使用交叉类型：
type PartialWithNewMember<T> = { 
  [P in keyof T]?: T[P]; 
} & { newMember: boolean } 


type Proxy<T> = { 
    get(): T; 
    set(value: T): void; 
} 
type Proxify<T> = { 
    [P in keyof T]: Proxy<T[P]>; 
} 
function unproxify<T>(t: Proxify<T>): T { 
    let result = {} as T; 
    for (const k in t) { 
        result[k] = t[k].get(); 
    } 
    return result; 
} 
```



## 模板字面量类型
```markdown
	以字符串字面量类型为基础，可以通过联合类型扩展成多个字符串。
	如果模板字面量里的多个变量都是联合类型，结果会交叉相乘

	内置字符操作类型
		Uppercase
		Lowercase
		Capitalize
		Uncapitalize

```


## 枚举
```typescript
枚举类型与数字类型之间相互兼容，但不同的枚举类型之间并不兼容

// 数字枚举
	// 自增性
	// 反向映射
	// keyof typeof Direction
	enum Direction { 
			Up = 1, 
			Down, 
			Left, 
			Right 
	}

// 字符串枚举
// 异构枚举
// 常量枚举
	// 不同于常规的枚举，它们在编译阶段会被删除。 常量枚举成员在使用的地方会被内联进来。 
// 外部枚举
```


# 重难点
## 模块
```typescript
一个没有顶层导入和导出声明的文件会被认为是一个脚本，它的内容会在全局范围内可见。（因此对模块也是可见的）。
模块会在它自己的作用域，而不是在全局作用域里执行。
这意味着，在一个模块中声明的变量、函数、类等，对于模块之外的代码都是不可见的，除非你显示的导出这些值。

import type { Cat, Dog } from "./animal.js"; 
  使用  type  前缀 ，表明被导入的是一个类型：

整体导入
	重命名
默认导出、导入
转接导出、具有副作用的导入
export = ... 与 import ... = require("");

声明文件 .d.ts ，就是为了逃过TS编译器的类型检测；
	由于ts文件调用任何API都需要该API的相关定义，自己编写的API还好说，但是别人编写该怎么办？甚至某些API是运行环境自带的，比如：浏览器或Node，使用这些自带的API根本无法通过TypeScript编译器的检测，因为使用了一个根本没有定义过得标识符。
```

### 动态导入
```typescript
// 声明 require函数的作用：逃过编译时警告；编译成js代码后，默认会去掉类型注释，生成的js代码就是就是可运行的commonjs代码
declare function require(moduleName: string): any; 

// 这里还导入 ZipCodeValidator 模块，是为了在编写ts代码时做静态类型检测
import { ZipCodeValidator as Zip } from "./ZipCodeValidator"; 
if (needZipValidation) { 
    let ZipCodeValidator: typeof Zip = require("./ZipCodeValidator"); 
    let validator = new ZipCodeValidator(); 
    if (validator.isAcceptable("...")) { /* ... */ } 
}
```


### 模块解析
```typescript
相对导入在解析时是相对于导入它的文件，并且_不能_解析为一个外部模块声明。

非相对模块的导入可以被解析成外部模块声明。使用非相对路径来导入你的外部依赖。

两种解析策略：
	Classic
		扩展名（ .ts 和 .d.ts ）
	Node
		扩展名（ .ts ， .tsx 和 .d.ts ）
		package.json  (如果指定了 "types" 属性)
```



## 内模块 | 命名空间
```typescript
// 多个文件的顶层具有同样的 export namespace Foo {  （不要以为这些会合并到一个 Foo 中！）
命名空间
	嵌套
	别名
	分离
		声明合并
		三斜线指令


namespace Shapes { 
    export namespace Polygons { 
        export class Triangle { } 
        export class Square { } 
    } 
} 
import polygons = Shapes.Polygons; // 命名空间别名

```


## 声明合并
```markdown
“声明合并”是指编译器将针对同一个名字的两个独立声明合并为单一声明。 
合并后的声明同时拥有原先两个声明的特性。 
任何数量的声明都可被合并；不局限于两个声明。


接口
	# 与接口之间的声明合并
	接口的非函数的成员应该是唯一的
	但对于函数成员，每个同名函数声明都会被当成这个函数的一个重载，后面的接口具有更高的优先级。
		字符串字面量函数签名 提升到最顶端

	# 与类之间的声明合并
		添加到原型上

命名空间
	# 与命名空间之间的声明合并
	非导出成员仅在其原有的（合并前的）命名空间内可见。
	合并之后，从其它命名空间合并进来的成员无法访问非导出成员。

	# 函数、类、枚举
```


### 外部模块扩展
```typescript
1. 不能在扩展中声明新的顶级声明－仅可以扩展模块中已经存在的声明
2. 默认导出也不能扩展，只有命名的导出才可以（因为你需要使用导出的名字来进行扩展，并且default 是保留关键字）

// observable.ts 
export class Observable<T> { 
    // ... implementation left as an exercise for the reader ... 
} 


// map.ts 
import { Observable } from "./observable"; 
declare module "./observable" { 
		// 这里相当于在 observable.ts文件 里声明了 重名的interface接口
		// 将在 类的原型 上添加下列声明
    interface Observable<T> { 
        map<U>(f: (x: T) => U): Observable<U>; 
    } 
} 
Observable.prototype.map = function (f) { 
    // ... another exercise for the reader 
} 


// consumer.ts 
import { Observable } from "./observable"; 
import "./map"; // 导入外部扩展模块
let o: Observable<number>; 
o.map(x => x.toFixed());

```


### 全局模块扩展
```typescript
// observable.ts 
export class Observable<T> { 
    // ... still no implementation ... 
} 


declare global { 
    interface Array<T> { 
        toObservable(): Observable<T>; 
    } 
} 
Array.prototype.toObservable = function () { 
    // ... 
}
```


### 混入
```typescript
// Disposable Mixin 
class Disposable { 
    isDisposed: boolean; 
    dispose() {         this.isDisposed = true; 
    } 
} 
// Activatable Mixin 
class Activatable { 
    isActive: boolean; 
    activate() { 
        this.isActive = true; 
    } 
    deactivate() { 
        this.isActive = false; 
    } 
} 
class SmartObject { 
    constructor() { 
        setInterval(() => console.log(this.isActive + " : " + this.isDisposed), 500); 
    } 
    interact() { 
        this.activate(); 
    } 
} 

// 混入声明；接口 多继承，再混入到 类的定义中；
interface SmartObject extends Disposable, Activatable {} 

// 定义实现
applyMixins(SmartObject, [Disposable, Activatable]); 
let smartObj = new SmartObject(); 
setTimeout(() => smartObj.interact(), 1000); 

function applyMixins(derivedCtor: any, baseCtors: any[]) { 
    baseCtors.forEach(baseCtor => { 
        Object.getOwnPropertyNames(baseCtor.prototype).forEach(name => { 
						if(name !== "construcotr"){
							Object.defineProperty(derivedCtor.prototype, name, Object.getOwnPropertyDescrip(name))
						}
        }); 
    }); 
}
```





## 类
```typescript
类有静态部分和实例部分的类型。 
比较两个类类型的对象时，只有实例的成员会被比较。 
静态成员和构造函数不在比较的范围内。

类的私有成员和受保护成员会影响兼容性。 
当检查类实例的兼容时，如果目标类型包含一个私有成员，那么源类型必须包含来自同一个类的这个私有成员。
这允许子类赋值给父类，但是不能赋值给其它有同样类型的类。

修饰符
	public
	protected
	private

	readonly

proteced | private还可以用来修饰构造器函数，表示该类不能直接实例化 或者 只能被子类实例化

存储器属性
静态属性 | 静态代码块
	私有属性

抽象类
	抽象类可以包含成员的实现细节（抽象类中除抽象函数之外，其他函数可以包含具体实现）
	抽象方法必须被继承的派生类实现 extends

把类当做接口使用
	接口 继承 类
```

```typescript
abstract class Department { 
    constructor(public name: string) { 
    } 
    printName(): void { 
        console.log('Department name: ' + this.name); 
    } 
    abstract printMeeting(): void; // 必须在派生类中实现 
} 

```


## 装饰器
```markdown
// https://saul-mirone.github.io/zh-hans/a-complete-guide-to-typescript-decorator/

类装饰器
属性装饰器
方法装饰器
访问器装饰器
参数装饰器

装饰器工厂函数

执行顺序（注意是执行而不是求值顺序）
1. 实例成员：参数装饰器 -> 方法 / 访问器 / 属性 装饰器 
2. 静态成员:参数装饰器 -> 方法 / 访问器 / 属性 装饰器 
3. 构造器: 参数装饰器 
4. 类装饰器

对于属性/方法/访问器装饰器而言，执行顺序取决于声明它们的顺序。
对同一方法中不同参数的装饰器的执行顺序而言， 最后一个参数的装饰器会最先被执行：

多个装饰器的组合
	求值外层装饰器
	求值内层装饰器
	调用内层装饰器
	调用外层装饰器
```



# 其他
## 三斜线指令
```markdown
// https://www.jianshu.com/p/e0912df68c3e

三斜线指令_仅_可放在包含它的文件的最顶端。 
一个三斜线指令的前面只能出现单行或多行注释。
如果它们出现在一个语句或声明之后，那么它们会被当做普通的单行注释，并且不具有特殊的涵义。

/// <reference path="..." />
  import filename.xxx
/// <reference types="..." />
  import lodash from "lodash"

/// <reference lib="es2019.array" />
  用三斜线指令引入 TS 自带的声明文件。
```



# 工具类型
```typescript
type Partial<T> = {
   [ P in keyof T] +?: T[P] | undefined
}

type Required<T> = {
   [P in keyof T] -?: T[P]
}

type Readonly<T> = {
   + readonly [P in keyof T]:T[P]
}

type Record<K extends string | number | symbol,T> = {
  [P in K] : T
}

type Pick<T,K extends keyof  T> = {
   [P in K] : T[P]
}

type Omit<T,K extends keyof T> = {
   [ P in Exclude<keyof T,K>] : T[P]
}

type Exclude<T,E> = T extends E ? never : T;

type Extract<T,U> = T extends U ? T : never;

type NonNullable<T> = Exclude<T,undefined | null>
                    = T extends null | undefined ? never : T;

type Parameters<T extends (...args:any) => any> = T extends (...args:infer P) => any ? P : never;

type ConstructorParameters<T extends abstract new (...args:any) => any> = T extends abstract new (...args: infer P) => any ? P : never

type ReturnType<T extends (...args:any)=>any > = T extends (...args:any)=>infer R ? R : any;

type InstanceType<T extends abstract new (...args:any) => any> = T extends new abstract (...args:any)  => infer R ? R : any;

type ThisParamterType<T> = T extends (this : infer U , ...args:any[]) => any ? U : unknown;

type OmitThisParamter<T> = unknown extends ThisParameter<T> 
  ? T 
  : 
    T extends (...args:infer P) => infer R 
      ? (...args:P) => R 
      : T

```


## 其他案列
```typescript
function pluck<T, K extends keyof T>(o: T, propertyNames: K[]): T[K][] { 
  return propertyNames.map(n => o[n]); 
} 


type FunctionPropertyNames<T> = { [K in keyof T]: T[K] extends Function ? K : never }[keyof T];
type FunctionProperties<T> = Pick<T, FunctionPropertyNames<T>>;

type NonFunctionPropertyNames<T> = { [K in keyof T]: T[K] extends Function ? never : K }[keyof T];
type NonFunctionProperties<T> = Pick<T, NonFunctionPropertyNames<T>>;


```



```typescript
// T1,T2的区别；对extends关键字的理解
type T1 = "a" | "b" extends "a" ? "Yes" : "No";
// T1:"No"
// T2:"Yes"
type T2 = {
  name: string;
  age: number;
} extends { name: string }
  ? "Yes"
  : "No";
```