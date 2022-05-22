- [总结](#总结)
- [安装](#安装)
- [props传参](#props传参)
- [绑定Attrs](#绑定attrs)
  - [简写 | 省略attrs](#简写--省略attrs)
  - [继承时覆盖](#继承时覆盖)
  - [传值时保留](#传值时保留)
- [继承](#继承)
  - [特定继承](#特定继承)
  - [继承任意](#继承任意)
- [动画](#动画)
  - [未解2 | CSS助手](#未解2--css助手)
- [塑造组件 | as](#塑造组件--as)
- [主题共享](#主题共享)
  - [嵌套|函数重构主题](#嵌套函数重构主题)
  - [在styled组件外获取Theme](#在styled组件外获取theme)
- [全局样式](#全局样式)
- [组件选择器](#组件选择器)
  - [针对React元素](#针对react元素)
- [注意事项](#注意事项)
  - [在render外定义styled组件](#在render外定义styled组件)
  - [scss语法](#scss语法)
    - [&语法 | !!!](#语法--)
    - [未解1](#未解1)
  - [styled组件的Refs](#styled组件的refs)
  - [styled组件样式冲突](#styled组件样式冲突)
  - [模板字符串 | !!!](#模板字符串--)
    - [增删规则](#增删规则)
  - [使用嵌套样式规则](#使用嵌套样式规则)
  - [媒体查询](#媒体查询)
  - [覆盖样式](#覆盖样式)
    - [行内样式](#行内样式)
  - [HTML attribute warnings](#html-attribute-warnings)
    - [问题](#问题)
    - [解决办法](#解决办法)
- [API](#api)
  - [isStyledComponent](#isstyledcomponent)
    - [组件选择器](#组件选择器-1)
  - [Transient props](#transient-props)
  - [shouldForwardProp](#shouldforwardprop)
  - [withConfig](#withconfig)
  - [ThemeConsumer](#themeconsumer)
  - [css | 动态样式规则](#css--动态样式规则)
  - [StyleSheetManager](#stylesheetmanager)

## 总结
```markdown
styled-components组件就是react组件的封装
  isStyledComponent
  styled(reactComponent)
    转换reatc组件为styled组件
    继承时覆盖
    传值时保留
  ref
    取得styled组件

attrs
  element元素上的属性
静态属性
  <Input type=text placeholder="" />

塑造组件
	as={ReversedButton}
		可以塑造成其他组件，如React组件 或 Styled组件

样式
  scss语法
  组件选择器
    styled组件
      styled() => 将React组件转换成Styled组件
    ${Thing}
    div${Thing}
    div&
  ${props=>{}}语法
    ${props=>"border-radius"}:${props=>"4px"}


主题共享
	styled组件
	纯React组件
	嵌套
ThemeProvider theme={Object|Function}

ThemeConsumer
withTheme
ThemeContext
	函数组件中使用
	useContext(ThemeContext)



样式冲突
  重叠选择器，提高优先级
  &&&
  .red-bg.red-bg

keyframes
createGlobalStyle

```




## 安装
```js
import styled,{createGlobalStyle,ThemeProvider,keyframes} from "styled-componennts"
```





## props传参

```jsx
const Button = styled.button`
  /* Adapt the colors based on primary prop */
  background: ${props => props.primary ? "palevioletred" : "white"};
  color: ${props => props.primary ? "white" : "palevioletred"};

  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;

render(
  <div>
    <Button>Normal</Button>
    <Button primary>Primary</Button>
  </div>
);
```



```jsx
// Create an Input component that'll render an <input> tag with some styles
const Input = styled.input`
  padding: 0.5em;
  margin: 0.5em;
  color: ${props => props.inputColor || "palevioletred"};
  background: papayawhip;
  border: none;
  border-radius: 3px;
`;

// Render a styled text input with the standard input color, and one with a custom input color
render(
  <div>
    <Input defaultValue="@probablyup" type="text" />
    <Input defaultValue="@geelen" type="text" inputColor="rebeccapurple" />
  </div>
);
```





## 绑定Attrs

### 简写 | 省略attrs

```jsx
// Static object
const Box = styled.div({
  background: 'palevioletred',
  height: '50px',
  width: '50px'
});

// Adapting based on props
const PropsBox = styled.div(props => ({
  background: props.background,
  height: '50px',
  width: '50px'
}));

render(
  <div>
    <Box />
    <PropsBox background="blue" />
  </div>
);
```









```jsx
const Input = styled.input.attrs(props => ({
  // we can define static props
  type: "text",// 提前确定input中type="text"

  // or we can define dynamic ones
  size: props.size || "1em",
}))`
  color: palevioletred;
  font-size: 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;

  /* here we use the dynamically computed prop */
  margin: ${props => props.size};
  padding: ${props => props.size};
`;

render(
  <div>
    <Input placeholder="A small text input" />
    <br />
    <Input placeholder="A bigger text input" size="2em" />
  </div>
);
```





### 继承时覆盖

```jsx
const Input = styled.input.attrs(props => ({
  type: "text",
  size: props.size || "1em",
}))`
  border: 2px solid palevioletred;
  margin: ${props => props.size};
  padding: ${props => props.size};
`;

// 覆盖原有的Attrs中的type属性
const PasswordInput = styled(Input).attrs({
  type: "password",
})`
  // similarly, border will override Input's border
  border: 2px solid aqua;
`;

render(
  <div>
    <Input placeholder="A bigger text input" size="2em" />
    <br />
    {/* Notice we can still use the size attr from Input */}
    <PasswordInput placeholder="A bigger password input" size="2em" />
  </div>
);
```





### 传值时保留

```js
# 由以下案列可知
传递给styled组件的attrs属性
className 合并
attrs已有属性	保留	
```



![image-20211102142337937](F:\React\React文档\imgs\image-20211102142337937.png)

```jsx
// Using .attrs, we attach the .small class to every <Button />
const Button = styled.button.attrs(props => ({
  className: "small",
  title: "Hello",
}))`
  background: black;
  color: white;
  cursor: pointer;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid black;
  border-radius: 3px;
`;

render(
  <div>
    <Button>Styled Components</Button>
    {/* Here we attach the class .big to this specific instance of the Button */}
    <Button className="big" title="哈喽">The new way to style components!</Button>
  </div>
);
```















## 继承

### 特定继承

```jsx
// The Button from the last section without the interpolations
const Button = styled.button`
  color: palevioletred;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;


const TomatoButton = styled(Button)`
  color: tomato; // 覆盖基础属性
  border-color: tomato; 
`;

render(
  <div>
    <Button>Normal Button</Button>
    <TomatoButton>Tomato Button</TomatoButton>
  </div>
);
```



### 继承任意

```jsx
// This could be react-router-dom's Link for example
const Link = ({ className, children }) => (
  <a className={className}>
    {children} {/* typeof children === 'function' ? children() : children */}
  </a>
);

const StyledLink = styled(Link)`
  color: palevioletred;
  font-weight: bold;
`;

render(
  <div>
    <Link>Unstyled, boring Link</Link>
    <br />
    <StyledLink>Styled, exciting Link</StyledLink>
  </div>
);
```





## 动画

```jsx
// Create the keyframes
const rotate = keyframes`
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
`;

// Here we create a component that will rotate everything we pass in over two seconds
const Rotate = styled.div`
  display: inline-block;
  animation: ${rotate} 2s linear infinite;
  padding: 2rem 1rem;
  font-size: 1.2rem;
`;
```





### 未解2 | CSS助手

```jsx
const rotate = keyframes``

// ❌ This will throw an error!
const styles = `
  animation: ${rotate} 2s linear infinite;
`

// ✅ This will work as intended
const styles = css`
  animation: ${rotate} 2s linear infinite;
```











## 塑造组件 | as

```jsx
const Button = styled.button`
  display: inline-block;
  color: palevioletred;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
  display: block;
`;

const TomatoButton = styled(Button)`
  color: tomato;
  border-color: tomato;
`;

render(
  <div>
    <Button>Normal Button</Button>
    <Button as="a" href="#">Link with Button styles</Button>
        {/*原先Button包裹元素是button标签，as属性赋予后更改为a标签*/}
    <TomatoButton as="a" href="#">Link with Tomato Button styles</TomatoButton>
  </div>
);
```







```jsx
const Button = styled.button`
  display: inline-block;
  color: palevioletred;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
  display: block;
`;

const ReversedButton = props => <Button {...props} children={props.children.split('').reverse()} />

render(
  <div>
    <Button>Normal Button</Button>
    <Button as={ReversedButton}>Custom Button with Normal Button styles</Button>
  </div>
);
```







## 主题共享

```jsx
// Define our button, but with the use of props.theme this time
const Button = styled.button`
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border-radius: 3px;

  /* Color the border and text with theme.main */
  color: ${props => props.theme.main};
  border: 2px solid ${props => props.theme.main};
`;

// We are passing a default theme for Buttons that arent wrapped in the ThemeProvider
Button.defaultProps = {
  theme: {
    main: "palevioletred"
  }
}

// Define what props.theme will look like
const theme = {
  main: "mediumseagreen"
};

render(
  <div>
    <Button>Normal</Button>

    <ThemeProvider theme={theme}>
      <Button>Themed</Button>
    </ThemeProvider>
  </div>
);
```





### 嵌套|函数重构主题

```jsx
// Define our button, but with the use of props.theme this time
const Button = styled.button`
  color: ${props => props.theme.fg};
  border: 2px solid ${props => props.theme.fg};
  background: ${props => props.theme.bg};

  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border-radius: 3px;
`;

// Define our `fg` and `bg` on the theme
const theme = {
  fg: "palevioletred",
  bg: "white"
};

// This theme swaps `fg` and `bg`
const invertTheme = ({ fg, bg }) => ({
  fg: bg,
  bg: fg
});

render(
  <ThemeProvider theme={theme}>
    <div>
      <Button>Default Theme</Button>
		{/*
			内部的ThemeProvider 中theme是一个函数，
			将接受来自上方的theme进行转化，
			再将转换后的theme返回，作为提供给内部的主题
		*/}
      <ThemeProvider theme={invertTheme}>
        <Button>Inverted Theme</Button>
      </ThemeProvider>
    </div>
  </ThemeProvider>
);
```





### 在styled组件外获取Theme

```jsx
# 方式一
// MyComponent.js
import { withTheme } from 'styled-components';
class MyComponent extends React.Component {
  render() {
    console.log('Current theme: ', this.props.theme);
    // ...
  }
}
export default withTheme(MyComponent);

//在App.js中使用
import ThemeMyComponent from "./MyComponent.js"
render(){
    const theme={...}
    <ThemeProvider theme={{theme}}>
    	<ThemeMyComponent />
    </ThemeProvider>
}


    
    
# 方式二
import { useContext } from 'react';
import { ThemeContext } from 'styled-components';

const MyComponent = () => {
  const themeContext = useContext(ThemeContext);

  console.log('Current theme: ', themeContext);
  // ...
}


# 方式三
import { ThemeConsumer } from 'styled-components'

export default class MyComponent extends React.Component {
  render() {
    return (
      <ThemeConsumer>
        {theme => <div>The theme color is {theme.color}.</div>}
      </ThemeConsumer>
    )
  }
}
```







## 全局样式

```jsx
import { createGlobalStyle, ThemeProvider } from 'styled-components'

const GlobalStyle = createGlobalStyle`
  body {
    color: ${props => (props.whiteColor ? 'white' : 'black')};
    font-family: ${props => props.theme.fontFamily};
  }
`

// later in your app

<ThemeProvider theme={{ fontFamily: 'Helvetica Neue' }}>
  <React.Fragment>
    <Navigation /> {/* example of other top-level stuff */}
    <GlobalStyle whiteColor />
  </React.Fragment>
</ThemeProvider>
```







## 组件选择器

![GIF 2021-11-2 12-47-19](F:\React\React文档\imgs\GIF 2021-11-2 12-47-19.gif)

```jsx

const Link = styled.a`
  display: flex;
  align-items: center;
  padding: 5px 10px;
  background: papayawhip;
  color: palevioletred;
`;

const Icon = styled.svg`
  flex: none;
  transition: fill 0.25s;
  width: 48px;
  height: 48px;

  ${Link}:hover & {
    fill: rebeccapurple;
  }
`;

const Label = styled.span`
  display: flex;
  align-items: center;
  line-height: 1.2;

  &::before {
    content: '◀';
    margin: 0 10px;
  }
`;

render(
  <Link href="#">
    <Icon viewBox="0 0 20 20">
      <path d="M10 15h8c1 0 2-1 2-2V3c0-1-1-2-2-2H2C1 1 0 2 0 3v10c0 1 1 2 2 2h4v4l4-4zM5 7h2v2H5V7zm4 0h2v2H9V7zm4 0h2v2h-2V7z"/>
    </Icon>
    <Label>Hovering my parent changes my style!</Label>
  </Link>
);
```





### 针对React元素

```jsx
class A extends React.Component {
  render() {
    return <div />
  }
}

const B = styled.div`
  ${A} { //错误，A不是styled组件
  }
`
```

```jsx
# 正确用法
class A extends React.Component {
  render() {
    return <div className={this.props.className} />
  }
}

const StyledA = styled(A)``

const B = styled.div`
  ${StyledA} {
  }
`
```









## 注意事项

### 在render外定义styled组件

```jsx
# 正确
const StyledWrapper = styled.div`
  /* ... */
`
const Wrapper = ({ message }) => {
  return <StyledWrapper>{message}</StyledWrapper>
}


# 错误
const Wrapper = ({ message }) => {
  // 警告：这会非常慢、且影响渲染性能，不要这要做
  const StyledWrapper = styled.div`
    /* ... */
  `
  return <StyledWrapper>{message}</StyledWrapper>
}
```





### scss语法

#### &语法 | !!!

```jsx
const Thing = styled.div.attrs((/* props */) => ({ tabIndex: 0 }))`
  color: blue;

  &:hover {
    color: red; // <Thing> when hovered
  }

  & ~ & {
    background: tomato; // <Thing> as a sibling of <Thing>, but maybe not directly next to it
  }

  & + & {
	// 绿黄色
    background: lime; // <Thing> next to <Thing>
  }

  &.something {
    background: orange; // <Thing> tagged with an additional CSS class ".something"
  }

  .something-else & {
    border: 1px solid; // <Thing> inside another element labeled ".something-else"
  }
`

render(
  <React.Fragment>
    <Thing>Hello world!</Thing>
    <Thing>How ya doing?</Thing>
    <Thing className="something">The sun is shining...</Thing>
    <div>Pretty nice day today.</div>
    <Thing>Don't you think?</Thing>
    <div className="something-else">
      <Thing>Splendid.</Thing>
    </div>
  </React.Fragment>
)
```



![image-20211101232813386](F:\React\React文档\imgs\image-20211101232813386.png)







#### 未解1

```jsx
const Thing = styled.div`
  && {	
	/* &&是通过重复类，提高优先级；
		若只是&，由于在全局样式中是div${Thing},相当于div&，全局样式多了一个标签选择器优先级更高，将被迫显示颜色：红色；
		若&&，相比于div&，类选择器优先级比标签选择器大，故显示颜色：蓝色
	*/
    color: blue;
  }
`

const GlobalStyle = createGlobalStyle`
  div${Thing} {	//div&Thing，是Thing类的Styled组件，同时包裹元素是div(?这样理解)
    color: red;
  }
`

render(
  <React.Fragment>
    <GlobalStyle />
    <Thing>
      I'm blue
    </Thing>
    <Thing as="span">
      I'm 
    </Thing>
  </React.Fragment>
)
```







### styled组件的Refs

```jsx
const Input = styled.input`
  padding: 0.5em;
  margin: 0.5em;
  color: palevioletred;
  background: papayawhip;
  border: none;
  border-radius: 3px;
`;

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.inputRef = React.createRef();
  }

  render() {
    return (
      <Input
        ref={this.inputRef} {/* 直接传递给包裹元素 */}
        placeholder="Hover to focus!"
        onMouseEnter={() => {
          this.inputRef.current.focus()
        }}
      />
    );
  }
}

render(
  <Form />
);
```





### styled组件样式冲突

```jsx
// MyComponent.js
const MyComponent = styled.div`background-color: green;`;

// my-component.css
// 尝试通过全局"red-bg" class 覆盖
.red-bg {
  background-color: red;
}

// 仍然是绿色
<MyComponent className="red-bg" />

# 原因在于:styled组件是在运行时的末尾将自身样式注入到head标签尾部
# 这导致其样式总是在全局样式之后，优先显效


# 解决办法
/* my-component.css */
// 通过重复 类名 提高该条样式规则的优先级
.red-bg.red-bg {
  background-color: red;
}
```





### 模板字符串 | !!!

#### 增删规则

```jsx
const Title = styled.h1`
  /* Text centering won't break if props.upsidedown is falsy */
  ${props => props.upsidedown && 'transform: rotate(180deg);'}
  // null,undefined,布尔值false  styled-component会自动省略
  text-align: center;
`;
```





### 使用嵌套样式规则

![image-20211102121554537](F:\React\React文档\imgs\image-20211102121554537.png)

````jsx
const EqualDivider = styled.div`
  display: flex;
  margin: 0.5rem;
  padding: 1rem;
  background: papayawhip;
  ${props => props.vertical && "flex-direction: column;"}

  > * {
    flex: 1;

    &:not(:first-child) {
      ${props => props.vertical ? "margin-top" : "margin-left"}: 1rem;
    }
  }
`;

const Child = styled.div`
  padding: 0.25rem 0.5rem;
  background: palevioletred;
`;

render(
  <div>
  <EqualDivider>
    <Child>First</Child>
    <Child>Second</Child>
    <Child>Third</Child>
  </EqualDivider>
  <EqualDivider vertical>
    <Child>First</Child>
    <Child>Second</Child>
    <Child>Third</Child>
  </EqualDivider>
  </div>
);
````





### 媒体查询

```jsx
const ColorChanger = styled.section`
  background: papayawhip;
  color: palevioletred;

  @media(min-width: 768px) {
    background: mediumseagreen;
    color: papayawhip;
  }
`;

render(
  <ColorChanger href="#">
    <h2>Hello world!</h2>
  </ColorChanger>
);
```







### 覆盖样式

#### 行内样式

```jsx
# 覆盖行内样式
const MyStyledComponent = styled(InlineStyledComponent)`
  &[style] {
    font-size: 12px !important;
    color: blue !important;
  }
`
```







```jsx
const MyStyledComponent = styled(AlreadyStyledComponent)`
  &&& {
    color: palevioletred;
    font-weight: bold;
  }
`

```

```css
// Each & gets replaced with the generated class, so the injected CSS then looks like this:

.MyStyledComponent-asdf123.MyStyledComponent-asdf123.MyStyledComponent-asdf123 {
  color: palevioletred;
  font-weight: bold;
}
```







### HTML attribute warnings

#### 问题

```jsx
# 注意以下案列
const Link = props => (
  <a {...props} className={props.className}>
    {props.text}
  </a>
)

const StyledComp = styled(Link)`
  color: ${props => (props.red ? 'red' : 'blue')};
`

<StyledComp text="Click" href="https://www.styled-components.com/" red />
```



```html
<!--被渲染成以下元素
	但作为a标签，其原生htmlDOM不存在属性red或text
-->
<a text="Click" 
   href="https://www.styled-components.com/" 
   red="true" class="[generated class]">Click</a>
```





#### 解决办法

```jsx
const Link = ({ className, red, text, ...props }) => (
  <a {...props} className={className}>
    {text}
  </a>
)

const StyledComp = styled(Link)`
  color: ${props => (props.red ? 'red' : 'blue')};
`

<StyledComp text="Click" href="https://www.styled-components.com/" red />
```



```html
<!--被渲染成-->
<a href="https://www.styled-components.com/" class="[generated class]">
  Click
</a>
```









## API



### isStyledComponent

#### 组件选择器

​	**仅适用于styled组件**



```jsx
import React from 'react'
import styled, { isStyledComponent } from 'styled-components'
import MaybeStyledComponent from './somewhere-else'

// 判断是否是styled组件
// 在生成styled组件中的模板字符串中，可以采用styled组件选择器
let TargetedComponent = isStyledComponent(MaybeStyledComponent)
  ? MaybeStyledComponent
  : styled(MaybeStyledComponent)``

const ParentComponent = styled.div`
  color: cornflowerblue;

  ${TargetedComponent} { //组件选择器
    color: tomato;
  }
`
```





### Transient props 

```jsx
const Comp = styled.div`
  color: ${props =>
    props.$draggable || 'black'};
`;

render(
  <Comp $draggable="red" draggable="true">
        {/* 由于$draggable存在，导致draggable该属性没有被传递进去* /}
    Drag me!
  </Comp>
);
```





### shouldForwardProp 

​	是否转送prop

### withConfig

```jsx
# 已实验 案列存在问题

const Comp = styled('div').withConfig({
  shouldForwardProp: (prop, defaultValidatorFn) =>
      !['hidden'].includes(prop)
      && defaultValidatorFn(prop),
}).attrs({ className: 'foo' })` // 默认：静态className
  color: red;
  &.foo {
    text-decoration: underline;
  }
`;

render(
  <Comp hidden draggable="true">
    Drag Me!
  </Comp>
  <Comp className="bar" draggable="true"> <!--className替换了 静态的className-->
    Drag Me! <!--最终样式：可拖拽，无下划线-->
  </Comp>
);
```





### ThemeConsumer

**详见：主题共享  在styled组件外获取Theme**



```jsx
import { ThemeConsumer } from 'styled-components'

export default class MyComponent extends React.Component {
  render() {
    return (
      <ThemeConsumer>
        {theme => <div>The theme color is {theme.color}.</div>}
      </ThemeConsumer>
    )
  }
}
```





### css | 动态样式规则

```js
import styled, { css } from 'styled-components'

const complexMixin = css`
  color: ${props => (props.whiteColor ? 'white' : 'black')}; // 一条动态规则
`

const StyledComp = styled.div`
  /* This is an example of a nested interpolation */
  ${props => (props.complex ? complexMixin : 'color: blue;')};
```



```jsx
import styled, { css, keyframes } from 'styled-components'

const pulse = keyframes`
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
`

const animation = props =>
  css`
    ${pulse} ${props.animationLength} infinite alternate;
  `

const PulseButton = styled.button`
  animation: ${animation};
```







### StyleSheetManager
