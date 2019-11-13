[TOC]
### 理解
- 增加其他函数的功能的函数
- 装饰器本质上是一个 Python 函数或类
- 它可以让其他函数或类在不需要做任何代码修改的前提下增加额外功能，装饰器的返回值也是一个函数/类对象。它经常用于有切面需求的场景
- 一切皆对象
> 概念：python装饰器就是用于拓展原来函数功能的一种函数，是可调用的对象，可以像常规的可调用对象那样调用，这个函数的特殊之处在于它的参数是一个函数，返回值也是一个函数，
> 使用装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。概括的讲，装饰器的作用就是为已经存在的函数或对象添加额外的功能。

### 闭包
在讲装饰器之前，先要了解闭包


注意重要的一点，当装饰器被应用到某个函数上时，装饰器代码本身就会运行，而不是当被装饰函数被调用时
### 使用场景
使用场景：它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
1. 授权(Authorization)
    装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中
2. 日志(Logging)
3. 

### 装饰器执行流程
```python
print('1. 下面是装饰器定义, 跳过')
def mydecorator(myfunc):
    print('2. 装饰器顶层')
    def wrapper():
        print('3. 进入装饰器内部')
        print('4. 准备执行被装饰函数内部代码')
        myfunc()
        print('5. 被装饰函数执行完成')
    print('6. 返回wrapper')
    return wrapper

print('7. 下面使用装饰器')
@mydecorator
def hello():
    print('8. 我是hello函数内部代码块')

if __name__ == "__main__":
    print('9. 下面调用hello函数')
    hello()
    print('10. hello函数调用完成')
```
![2019-11-13 15-08-57 的屏幕截图.png](https://i.loli.net/2019/11/13/WqkV1Yy6DJu4irT.png)
### 原生装饰器
1. 实现带参数的装饰器时，层层嵌套的函数代码特别难写、难读
2. 因为函数和类方法的不同，为前者写的装饰器经常没法直接套用在后者上  

简单的装饰器，计算函数所用时间，被装饰函数无参数

```pyhton
import time

def mydecorator(myfunc):  # 装饰器的参数是函数
    def wrapper():  # wrapper可换成任意名
        start = time.time()
        myfunc()
        end= time.time()
        print(f'用时 {end- start} !')
    return wrapper  # 装饰器的返回值也是函数

@mydecorator
def myfunc():
    print('hellor world!')

myfunc()
```

简单的装饰器，计算函数所用时间，被装饰函数有参数  
可变参数*args和关键字参数**kwargs，有了这两个参数，装饰器就可以用于任意目标函数了, 不管你的函数是0个参数还是多个参数

```python
import time

def mydecorator(myfunc):  # 装饰器的参数是函数
    def wrapper(*args, **kwargs):  # wrapper可换成任意名, *args, **kwargs必须写
        start = time.time()
        myfunc(*args, **kwargs)
        end= time.time()
        print(f'用时 {end - start} !')
    return wrapper  # 装饰器的返回值也是函数

@mydecorator
def myfunc(name):
    print(f'hello {name}!')

myfunc('Python')
```

### 装饰器带参数
```python
import time

def mydecorator(arg):  # 接收装饰器的参数
    def outer_wrapper(myfunc):  # 接收被装饰的函数，myfunc
        def wrapper(*args, **kwargs):  # 接收被装饰函数的参数
            print(arg)
            start = time.time()
            myfunc(*args, **kwargs)
            end= time.time()
            print(f'用时 {end - start} !')
        return wrapper  # 装饰器的返回值也是函数
    return outer_wrapper

@mydecorator(arg='我是装饰器的参数')
def myfunc(name):
    print(f'hello {name}!')

myfunc('Python')
```

### 装饰器引起的问题
你写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、文档字符串、注解和参数签名都丢失了。  
解决方法：任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来注解底层包装函数
```python
from functools import wraps
import time

def mydecorator(myfunc):  # 装饰器的参数是函数
    @wraps(myfunc)
    def wrapper():  # wrapper可换成任意名
        start = time.time()
        myfunc()
        end= time.time()
        print(f'用时 {end- start} !')
    return wrapper  # 装饰器的返回值也是函数

@mydecorator
def myfunc():
    '''
    文档字符串
    '''
    print('hellor world!')

myfunc()
print(myfunc.__name__)
print(myfunc.__doc__)
```


### 基于类的装饰器
```python
from functools import wraps
import time

class Person(object):
    def decorator1(self, myfunc):
        @wraps(myfunc)
        def wrapper(*args, **kwargs):
            print('做为实例方法')
            myfunc(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(self, myfunc):
        @wraps(myfunc)
        def wrapper(*args, **kwargs):
            print('做为类方法')
            myfunc(*args, **kwargs)
        return wrapper

person = Person()

@person.decorator1
def name():
    print('instance')

@Person.decorator2
def age():
    print('class')

name()
age()
```

### wrapt库实现装饰器
- wrapped：被装饰的函数或类方法
- - instance：
        - 如果被装饰者为普通类方法，该值为类实例
        - 如果被装饰者为 classmethod 类方法，该值为类
        - 如果被装饰者为类/函数/静态方法，该值为 None
- args：调用时的位置参数（注意没有 * 符号）
- kwargs：调用时的关键字参数（注意没有 ** 符号）

When applying a decorator to a normal function, the instance argument would always be None.

#### 优势
1. 嵌套层级少：使用 @wrapt.decorator 可以将两层嵌套减少为一层
2. 更简单：处理位置与关键字参数时，可以忽略类实例等特殊情况
3. 更灵活：针对 instance 值进行条件判断后，更容易让装饰器变得通用

### 一些要点总结：

- 一切 callable 的对象都可以被用来实现装饰器
- 混合使用函数与类，可以更好的实现装饰器
- wrapt 模块很有用，用它可以帮助我们用更简单的代码写出复杂装饰器
- “装饰器”只是语法糖，它不是“装饰器模式”
- 装饰器会改变函数的原始签名，你需要 functools.wraps
- 在内层函数修改外层函数的变量时，需要使用 nonlocal 关键字
