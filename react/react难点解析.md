- [useEffect难点](#useeffect难点)
  - [问题综述](#问题综述)
  - [useEffect副作用函数中的props、state](#useeffect副作用函数中的propsstate)
  - [函数组件(常量类型)与类组件(引用类型)中的状态](#函数组件常量类型与类组件引用类型中的状态)
  - [清除副作用时机](#清除副作用时机)
  - [依赖数组 与 最小信息传递](#依赖数组-与-最小信息传递)
    - [useReducer巧用](#usereducer巧用)
  - [组件中的函数 与 数据流](#组件中的函数-与-数据流)
  - [网络请求中的竞态现象](#网络请求中的竞态现象)
- [函数式组件 VS 类组件](#函数式组件-vs-类组件)
    - [现象原因](#现象原因)
    - [使用闭包：在类组件中引用特定渲染时的值](#使用闭包在类组件中引用特定渲染时的值)
    - [使用useRef:函数组件引用最新值](#使用useref函数组件引用最新值)


# useEffect难点
https://overreacted.io/zh-hans/a-complete-guide-to-useeffect/


## 问题综述
如何用useEffect模拟componentDidMount生命周期？
	useEffect 就像componentDidMount 和 componentDidUpdate的结合
如何正确地在useEffect里请求数据？[]又是什么？
	
我应该把函数当做effect的依赖吗？
为什么有时候会出现无限重复请求的问题？
	没有设置effect依赖参数的情况
为什么有时候在effect里拿到的是旧的state或prop？
	Effect拿到的总是定义它的那次渲染中的props和state


```markdown
闭包陷阱
  最新值 与 渲染时的值

  useRef
  useReducer
  useEvent

```



## useEffect副作用函数中的props、state
- 每一次渲染都有它自己的 Props and State

- 每一次渲染都有它自己的事件处理函数
	计数案列：延时点击

- 每次渲染都有它自己的Effects
	使用useEffect时，每次渲染都是一个不同的函数 — 并且每个effect函数“看到”的props和state都来自于它属于的那次特定渲染

	会在每次更改作用于DOM并让浏览器绘制屏幕后去调用





## 函数组件(常量类型)与类组件(引用类型)中的状态
（在setTimeout中使用时）
函数组件中使用useState时一般返回的都是常量值，仅仅作用于**本次渲染**；
	1.使用useReducer，转换为使用引用类型，将保证每次引用的都是最新值，而不是当时渲染值；
	2.使用useRef
而在class组件中，若直接使用this.state，由于是引用类型，将导致每次引用时都是**最新值**，而不是当时渲染时的值；




## 清除副作用时机
清除副作用
	React只会在浏览器绘制后运行effects。这使得你的应用更流畅因为大多数effects并不会阻塞屏幕的更新。
	Effect的清除同样被延迟了。上一次的effect会在重新**渲染后被清除**：
		React 渲染{id: 20}的UI。
		浏览器绘制。我们在屏幕上看到{id: 20}的UI。
		React 清除{id: 10}的effect。
		React 运行{id: 20}的effect。
	Effect的清除并不会读取“最新”的props。它只能读取到**定义它的那次渲染中的props值**：




## 依赖数组 与 最小信息传递
	副作用函数是否运行的依赖；
	类似于事件监听中的passive

```javascript
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      // 这个例子只会递增一次
      // 既然我们设置了[]依赖，effect不会再重新运行，它后面每一秒都会调用setCount(0 + 1) 

      setCount(count + 1);
    }, 1000);
    return () => clearInterval(id);
  }, []);

  return <h1>{count}</h1>;
}
```

解决办法：
	1.在依赖中包含所有effect中用到的组件内的值
		**再一次引出的问题**：定时器会在每一次count改变后清除和重新设定

	只在effects中传递最小的信息会很有帮助
	2.修改effect内部的代码以确保它包含的值只会在需要的时候发生变更
		由于我们并**不需要使用count，只是想告知count变化**
		根据前一个状态更新状态的时候，我们可以使用setState的函数形式：
		setCount(c => c + 1);



### useReducer巧用
但是 又会带来新的问题：如果在同一effect中存在多个依赖？
```javascript
function Counter() {
  const [count, setCount] = useState(0);
  const [step, setStep] = useState(1);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(c => c + step);
    }, 1000);
    return () => clearInterval(id);
  }, [step]);

  return (
    <>
      <h1>{count}</h1>
      <input value={step} onChange={e => setStep(Number(e.target.value))} />
    </>
  );
}
```

**假如我们不想在step改变后重启定时器**，我们该如何从effect中移除对step的依赖呢？
当你想更新一个状态，并且这个状态更新依赖于另一个状态的值时，你可能需要用useReducer去替换它们。

```javascript
const [state, dispatch] = useReducer(reducer, initialState);
const { count, step } = state;

useEffect(() => {
  const id = setInterval(() => {
    dispatch({ type: 'tick' }); // Instead of setCount(c => c + step);
  }, 1000);
  return () => clearInterval(id);
}, [dispatch]);

```
React会保证dispatch在组件的声明周期内保持不变。所以上面例子中不再需要重新订阅定时器。



## 组件中的函数 与 数据流
**在组件内定义**的函数每一次渲染都在变。
	1.如果一个函数没有使用组件内的任何值，你应该把它提到组件外面去定义把函数移到Effects里
	2.把它包装成 useCallback Hook:


函数是数据流的一部分吗？
	**在函数式组件中**，用useCallback修饰的函数可以看做数据流的一部分；

	但是，**在class组件中**，函数属性本身并不是数据流的一部分。
		即使我们只需要一个函数，我们也必**须把一堆数据传递下去仅仅是为了做“diff”**			
    因为无法知道传入的this.props.fetchData 是否依赖状态，并且不知道它依赖的状态是否改变了。



1.（在函数式组件中，因为fetchData[用useCallback修饰]只有在Parent的query状态变更时才会改变，所以我们的Child只会在需要的时候才去重新请求数据。）

2.（有趣的是，这种模式在class组件中行不通）
（this.props.fetchData和 prevProps.fetchData始终相等，因此不会重新请求）
（唯一现实可行的办法是硬着头皮把query本身传入 Child 组件，在Child的componentDidUpdate判断前后query变化、再决定是否发起网络请求）
class Parent extends Component {
  state = {
    query: 'react'
  };
  fetchData = () => {
    const url = 'https://hn.algolia.com/api/v1/search?query=' + this.state.query;
    // ... Fetch data and do something ...
  };
  render() {
    return <Child fetchData={this.fetchData} />;
  }
}

class Child extends Component {
  state = {
    data: null
  };
componentDidMount() {
    this.props.fetchData();
  }
  componentDidUpdate(prevProps) {
    // 🔴 This condition will never be true
    if (this.props.fetchData !== prevProps.fetchData) {
      this.props.fetchData();
    }
  }
  render() {
    // ...
  }
}




## 网络请求中的竞态现象
	前后两次请求结果返回的顺序不能保证一致，有可能后请求的先返回，导致结果被覆盖；
```javascript
function Article({ id }) {
  const [article, setArticle] = useState(null);

  useEffect(() => {
    let didCancel = false;

    async function fetchData() {
      const article = await API.fetchArticle(id);
      if (!didCancel) {
        setArticle(article);
      }
    }

    fetchData();

    return () => {
      didCancel = true;
    };
  }, [id]);

  // ...
}
```


（https://overreacted.io/zh-hans/how-are-function-components-different-from-classes/）
# 函数式组件 VS 类组件
```javascript
// 试比较下述两者的区别
function ProfilePage(props) {
  const showMessage = () => {
    // 本次渲染的 props,不是最新的props
    alert('Followed ' + props.user);
  };

  const handleClick = () => {
    setTimeout(showMessage, 3000);
  };

  return (
    <button onClick={handleClick}>Follow</button>
  );
}


class ProfilePage extends React.Component {
  showMessage = () => {
    // this.props 引用的永远是最新的props
    alert('Followed ' + this.props.user);
  };

  handleClick = () => {
    // setTimeout延时，引出问题：props是否最新
    setTimeout(this.showMessage, 3000);
  };

  render() {
    return <button onClick={this.handleClick}>Follow</button>;
  }
}
```

### 现象原因
（在类组件中，调用一个回调函数读取 this.props 的 timeout 会打断这种关联。我们的 showMessage 回调并没有与任何一个特定的渲染“绑定”在一起，所以它“失去”了正确的 props。从 this 中读取数据的这种行为，切断了这种联系。）


### 使用闭包：在类组件中引用特定渲染时的值
```javascript
// 如果你在一次特定的渲染中捕获那一次渲染所用的props或者state，你会发现他们总是会保持一致，就如同你的预期那样：
class ProfilePage extends React.Component {
  render() {
    // Capture the props!
    const props = this.props;

    // Note: we are *inside render*.
    // These aren't class methods.
    const showMessage = () => {
      alert('Followed ' + props.user);
    };

    const handleClick = () => {
      setTimeout(showMessage, 3000);
    };

    return <button onClick={handleClick}>Follow</button>;
  }
}
```


### 使用useRef:函数组件引用最新值
函数式组件捕获了渲染所使用的值。
但是如果我们想要读取并不属于这一次特定渲染的，最新的props和state呢？
	useRef引用
```javascript
// 方法一
function MessageThread() {
  const [message, setMessage] = useState('');
  const latestMessage = useRef('');

  const showMessage = () => {
    alert('You said: ' + latestMessage.current);
  };

  const handleSendClick = () => {
    setTimeout(showMessage, 3000);
  };

  const handleMessageChange = (e) => {
    setMessage(e.target.value);
    latestMessage.current = e.target.value;
  };


// 方法二
function MessageThread() {
  const [message, setMessage] = useState('');

  // 保持追踪最新的值。
  const latestMessage = useRef('');
  useEffect(() => {
    latestMessage.current = message;
  });

  const showMessage = () => {
    alert('You said: ' + latestMessage.current);
  };
```