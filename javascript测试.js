// const add = (a, b) => console.log(a + b);
// const mul = (a, b) => console.log(a * b);
// !(add, mul)(1, 2); // 2, ","语法直接返回最后值即mul
// !(add || mul)(1, 2); // 3;必须要满足一个是函数；
// !(add && mul)(1, 2); // 2；必须要满足两个都是函数；

/* // 类的构造函数可以直接返回对象，该对象自然不具有该类上的原型属性
class A{
  constructor(){
    return {
      name:"cindiou",
      age:18
    }
  }
  say(){
    console.log("Hello,World!")
  }
}

const a=new A();
console.log("say" in a);
console.log(a) */


/* // 类可以继承函数
function Test(){}
Test.prototype.say=function(){console.log("Hello,World!")}
class A extends Test{}
const a=new A()
a.say() */


/* function Minxins(...args){
  let mounted=false;
  function _(){
    if(new.target===undefined || new.target===_){
      throw new Error();
    }
    
    args.forEach(ctor=>{
      const bs = [new ctor(),ctor,ctor.prototype];
      const df = (target,origin,name)=>{
        Object.defineProperty(target,name,Object.getOwnPropertyDescriptor(origin,name))
      }
      for(let i=0;i<3;i++){
        if(mounted && i>=1){
          continue; // 无需再次挂载静态与原型方法；
        }
        Reflect.ownKeys(bs[i]).forEach(name=>{
          switch(i){
            case 0:
              df(this,bs[i],name);
              break;
            case 1:
              if(["name","prototype"].includes(name)) break;
              df(new.target,bs[i],name);
              break;
            case 2:
              if(name==="constructor") break;
              df(new.target.prototype,bs[i],name);
              break;
            default:
              throw new Error()
          }
        })
      }
    })
    mounted=true; // 原型与静态方法已经挂载；下次实例无需再次挂载
  }
  return _
}


class A{
  constructor(){
    this.a="AAA"
  }
  A_say(){
    console.log("A_Hi!")
  }
  static _Asay(){
    console.log("satatic_A_Hi!")
  }
}

class B{
  constructor(){
    this.b="BBB"
  }
  B_say(){
    console.log("B_Hi!")
  }
  static _Bsay(){
    console.log("satatic_B_Hi!")
  }
}

class Test extends Minxins(A,B) {

}

const t=new Test()
console.log(t.a,t.b)
t.A_say();t.B_say()
Test._Asay();Test._Bsay() 


console.log(process.env.a) */


/* let curIndex = Object.create({_value: 0,}, {
  value: {
    get() {
      return this._value;
    },
    set(newValue) {
      this._value = newValue;
    }
  }
});

console.log(curIndex.value)
curIndex.value=1;
console.log(curIndex.value)
console.log(curIndex.hasOwnProperty("_value")) */


class ClassWithPrivateAccessor {

  #message;

  get #decoratedMessage() {
  }
 #decoratedMessage(msg) {
    this.#message = msg;
  }

  constructor() {
    this.#decoratedMessage = 'hello world';
    console.log(this.#decoratedMessage);
  }
}

new ClassWithPrivateAccessor();
// console.log("Hello,World")