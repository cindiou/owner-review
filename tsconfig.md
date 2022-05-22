# 注意事项
```markdown
注意 ts 在针对文件的改变而引起的错误的时候，可能并不是否灵敏；
package.json中main、types字段都可以决定模块声明的引入路径，且types优先级要比main字段要高，但是在ts 转为 js后(commonjs模块)导入模块的依赖路径仍然是main字段决定的

在命令行上指定的编译选项会覆盖在 tsconfig.json 文件里的相应选项。

注意，这是一个json文件，当然不一定要放在根目录下，可以通过tsc --project path/to/tsconfig.json指定配置文件。

如果 "files" 和 "include" 都没有被指定，编译器默认包含当前目录和子目录下所有的TypeScript文件（ .ts ,  .d.ts  和  .tsx ），除了在 "exclude" 里指定的文件

当执行tsc命令时，ts编译器会首先在当前目录寻找tsconfig.json文件，如果当前目录没有tsconfig.json文件，它会一直向上级目录寻找，直到找到一个tsconfig.json文件，tsconfig.json文件所在的目录为项目的根目录。

```

# 常见配置参数
```markdown

files
	由于默认情况下，tsc会编译当前项目下的所有ts文件
	以通过files配置来指定编译的入口文件，files的属性值为一个数组，可以指定要编译的具体文件，但是其不能使用通配符进行指定。
	files的属性值不能是空数组([])

include
	可以使用通配符，并且可以和files一起使用，最终编译的源文件包含，files和include的合集

exclude
	可以使用通配符；只能排除include中包含的文件，并且不是可编译文件的依赖文件



compilerOptions
控制编译过程和编译结果
	noEmitOnError
	noImplicitAny
	noImplicitThis
	strictNullChecks
	alwaysStrict
	declaration
	declarationDir
		通过设置declarationDir将所有声明文件放到同一个目录下。
	sourceMap
	allowJS
		使用import语句引入模块时，例如import {add} from "./add，默认情况下ts编译器会自动寻找src/add.ts和src/add.d.ts，它不会去考虑src/add.js，我们可以通过将allowJS设置为true来更改这一默认行为。
	checkJS
		使用allowJS可以让编译器在编译阶段包含js文件，但是编译器并不会对js文件进行类型检查。为了能工让ts编译器对js文件进行类型检查，需要设置"checkJS": true。

	removeComments
	rootDir
		typescirpt项目的默认的根目录为tsconfig.json文件所在的目录，所有的相对路径都是相对于这个根目录的
	outDir
		指定编译结果的输出目录的;默认是将编译结果输出文件输出到源文件所在目录下
		该目录下的文件永远会被编译器排除
	outFile
		打包成一个bundle，即一个js文件，前提是module选项被设置成System或者AMD。如果想要支持其他的module选项，可以借助webpack、parcel等工具。

	target
		输出的文件中采用哪个es版本
	lib
		是用于指定要引入的库文件，当ts文件中使用到了一些全局的类库的时候才会配置。如果不配置lib，那么其默认会引入dom库，但是如果配置了lib，那么就只会引入指定的库了。


	module
		如果不显式配置module，那么其值与target的配置有关，其默认值为target === "es3" or "es5"?"commonjs" : "es6"，
		如果我们希望最终使用commonjs模块标准，那么我们用
		export =语法导出，用import module = require("module")来导入；
	moduleResolution
		用于配置模块的解析规则，主要有两种，分别为classic和node。默认值为module ==="amd" or "system" or "es6" or "es2015"?"classic" : "node"


	baseUrl
		所有非相对模块导入都会被当做相对于 baseUrl 。
		相对模块的导入不会被设置的 baseUrl 所影响，因为它们总是相对于导入它们的文件

		如果我们引入了一个非相对模块，那么编译器只会到node_modules目录下去查找，但是如果配置了baseUrl，那么编译器在node_modules中没有找到的情况下，还会到baseUrl中指定的目录下查找；同样moduleResolution属性值为classic的时候也是一样，除了到当前目录下找之外(逐层)，如果没有找到还会到baseUrl中指定的目录下查找；

		就是相当于拓宽了非相对模块的查找路径范围。

	paths
		相对于baseUrl所在的路径的,主要用于到baseUrl所在目录下查找的时候进行的路径映射。

	rootDirs
		可以在“虚拟”目录下解析相对模块导入，就_好像_它们被合并在了一起一样。
		每当编译器在某一 rootDirs 的子目录下发现了相对模块导入，它就会尝试从每一个 rootDirs 中导入。


	typeRoots
		指定类型声明文件的查找路径。只能识别目录下的.d.ts文件，不能识别.ts文件。
		默认值为node_modules/@types，即在node_modules下的@types里面查找。需要注意的是这里仅仅是d.ts文件的查找路径。
		相当于在引入非相对模块的时候拓宽了类型声明文件的查找范围

		不管typeRoots怎么配置，编译器都会到node_modules/@types下查找类型配置文件，并且不管是classic解析还是node解析，都会到node_modules/@types目录下查找类型声明文件
	types
		用于指定需要包含的模块(自动引入的声明)，只有在这里列出的模块的声明文件才会被加载进来,其属性值为一个数组	

		不配置types，那么node_modules/@types目录下的所有模块的定义都会加载进来；如果将types设置为一个空的数组，那么typeRoots配置的目录里的声明文件都将不会被加载进来；也就是说通过指定 "types": [] 来禁用自动引入 @types 包。
		typeRoots用于导入目录下所有的声明至全局空间，但是如果设置了types，则只会导入types指定的包声明至全局空间。


compileOnSave
extends


非相对模块的查找顺序为，根据moduleResolution的配置，确定是使用node还是classic模块进行基础解析，如果找不到，则查看typeRoots和types的配置，如果还是找不到，则查看baseUrl和paths的配置，需要注意的是typeRoots和types的配置只能是查找.d.ts类型声明文件，如果还是找不到，那么就在编译入口所在目录下查找有没有对应模块的定义了，

```