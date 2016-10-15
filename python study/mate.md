# 元编程笔记

# 内省函数  
~~~python
getattr(object, name[, default]) -> value

setattr(obj, name, value, /)
    Sets the named attribute on the given object to the specified value.
    setattr(x, 'y', v) is equivalent to ``x.y = v''

delattr(obj, name, /)
    Deletes the named attribute from the given object.
    delattr(x, 'y') is equivalent to ``del x.y''
~~~

# 偏函数  
~~~python
partial(func, *args, **keywords)
#  new function with partial application of the given arguments and keywords.
~~~

# inspect 自省
~~~python
inspect.getargspec(func)
# 返回一个元组 (args, varargs, keywords, defaults)
~~~

## __getattribute__  

    如果某个类定义了 __getattribute__() 方法，在 每次引用属性或方法名称时 Python 都调用它（特殊方法名称除外，因为那样将会导致讨厌的无限循环）。


# **元类**  

类创建的步骤

    __prepare__() 方法在所有类定义开始执行前首先被调用，用来创建类命名空间。 通常来讲，这个方法只是简单的返回一个字典或其他映射对象。
    __new__() 方法被用来实例化最终的类对象。它在类的主体被执行完后开始执行。
    __init__() 方法最后被调用，用来执行其他的一些初始化工作。


## __prepare__  
函数还要在__new__函数调用之前调用，这个函数必须返回一个用于存放类属性（namespace）的数据结构，默认情况下就是字典类型了。
~~~python  
@classmethod  
def __prepare__(self, *args, **kwargs):  
    print("__prepare__ called")  
#        return type.__prepare__(self, *args, **kwargs)  
    return kwargs  
~~~

##  __new__  
~~~python
def __new__(cls, clsname, bases, clsdict):
    pass
~~~
