# 外部可访问
`flask run --host=0.0.0.0`
`app.run(host='0.0.0.0')`
# debug模式
`export FLASK_ENV=development`

使用route（）装饰器将函数绑定到URL。
Converter types:

string
(default) accepts any text without a slash

int
accepts positive integers

float
accepts positive floating point values

path
like string but also accepts slashes

uuid
accepts UUID strings

- 项目端点的规范URL带有斜杠
- 如果您访问的URL不带斜杠，Flask会将您重定向到带斜杠的规范URL。

# url_for(endpoint, **values)
要构建指向特定函数的URL，请使用url_for（）函数。
它接受函数名称作为其第一个参数以及任意数量的关键字参数，每个参数对应于URL规则的可变部分。
未知变量部分作为查询参数附加到URL。


url_for('static', filename='style.css')

# Cookies
- 设置cookie 
```
from flask import make_response
resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
 ```
- 获取cookie `request.cookies.get('username')`

# Blueprint
比较好的习惯是将蓝图放在一个单独的包里
蓝图可以极大地简化大型应用并为扩展提供集中的注册入口
## 为什么使用蓝图？
Flask 中蓝图有以下用途：

- 把一个应用分解为一套蓝图。这是针对大型应用的理想方案：一个项目可以实例化 一个应用，初始化多个扩展，并注册许多蓝图。
- 在一个应用的 URL 前缀和（或）子域上注册一个蓝图。 URL 前缀和（或）子域的 参数成为蓝图中所有视图的通用视图参数（缺省情况下）。
- 使用不同的 URL 规则在应用中多次注册蓝图。
- 通过蓝图提供模板过滤器、静态文件、模板和其他工具。蓝图不必执行应用或视图 函数。
- 当初始化一个 Flask 扩展时，为以上任意一种用途注册一个蓝图。
Flask 中的蓝图不是一个可插拨的应用，因为它不是一个真正的应用，而是一套可以 注册在应用中的操作，并且可以注册多次。那么为什么不使用多个应用对象呢？可以 使用多个应用对象（参见 应用调度 ），但是这样会导致每个应用都使 用自己独立的配置，且只能在 WSGI 层中管理应用。
而如果使用蓝图，那么应用会在 Flask 层中进行管理，共享配置，通过注册按需改 变应用对象。蓝图的缺点是一旦应用被创建后，只有销毁整个应用对象才能注销蓝图。

## 蓝图的概念¶
> 蓝图的基本概念是：在蓝图被注册到应用之后，所要执行的操作的集合。当分配请求 时， Flask 会把蓝图和视图函数关联起来，并生成两个端点之前的 URL 
