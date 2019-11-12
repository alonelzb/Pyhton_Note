### 理解
- 增加其他函数的功能的函数
- 装饰器本质上是一个 Python 函数或类
- 它可以让其他函数或类在不需要做任何代码修改的前提下增加额外功能，装饰器的返回值也是一个函数/类对象。它经常用于有切面需求的场景
- 一切皆对象

注意重要的一点，当装饰器被应用到某个函数上时，装饰器代码本身就会运行，而不是当被装饰函数被调用时
### 使用场景
1. 授权(Authorization)
    装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中
2. 日志(Logging)
3. 

### 原生装饰器
1. 实现带参数的装饰器时，层层嵌套的函数代码特别难写、难读
2. 因为函数和类方法的不同，为前者写的装饰器经常没法直接套用在后者上
```
def mydecorator(func):
    # def wrapper(*args, **kwargs):
    def wrapper():
        startTime = time.time()
        func()
        # func(*args, **kwargs)
        endTime = time.time()
        print(f'用时 {endTime - startTime} !')
    return wrapper
    # 它的参数是一个函数，然后返回值也是一个函数。其中作为参数的这个函数func()就在返回函数wrapper()的内部执行。然后在函数func()前面加上@deco，func()函数就相当于被注入了计时功能，现在只要调用func()，它就已经变身为“新的功能更多”的函数了。
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
