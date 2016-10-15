# 描述器
通过描述器可以捕获核心的实例操作（get， set， delete）

## get
用于访问属性。它返回属性的值，或者在所请求的属性不存在的情况下出现 AttributeError 异常。
~~~
>>> p = Point(2,3)
>>> p.x # Calls Point.x.__get__(p, Point)
2
>>> Point.x # Calls Point.x.__get__(None, Point)
<__main__.Integer object at 0x100671890>
>>>
~~~  

## set
将在属性分配操作中调用。不会返回任何内容。

## delete
控制删除操作。不会返回内容。
