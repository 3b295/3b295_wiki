>**keyword-only**  

python2 函数参数顺序如下  a不能存在*b之后
~~~python
def func(a, *b, **c):
    pass
~~~
这在python3 被允许的，这里c需要作为关键词参数被传进来
~~~python
def func(a, *b, c):
    pass
~~~
**例子:**
1. 只能以关键词参数传递
~~~python
def func(*, a, b, c):
    pass
~~~
2. 不接受变长长参数
~~~python
def func(a, *):
    pass
~~~
