# 上下文管理器
## 写成类的方式
>1. 执行 with 后的语句获取上下文管理器，例如 open('utf8.txt', 'r') 就是返回一个 2. 2. file object；
3. 加载 __exit__() 方法备用；
4. 执行 __enter__()，该方法的返回值将传递给 as 后的变量（如果有的话）；
5. 执行 with 语法块的子句；
6. 执行 __exit__() 方法，如果 with 语法块子句中出现异常，将会传递 type, value, traceback 给 __exit__()，否则将默认为 None；如果 __exit__() 方法返回 False，将会抛出异常给外层处理；如果返回 True，则忽略异常。

## 通过装饰器的写法  
~~~python
from contextlib import contextmanager as cm

@cm
def test_context():
    < do __enter__ work >
    yield <value> # return as value
    < do __exit__ work >
    #      ps: 这里return会抛出一个 StopIteration, 不会作为__exit__ 的返回值（依然是None)。 所以这里无法像在__exit__ 中返回True 那样来忽略异常。
    #          应该使用try 语句来去除抛错

with test_context() as rst:
    pass
~~~

任何能被yield分割的函数都可以这样搞， 这意味着可以用过这个特征弄一些[高级玩法](http://blog.jobbole.com/64175/)
## 更优雅的处理with的嵌套  
~~~python
    with A() as a, B() as b:
        pass
~~~
