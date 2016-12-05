# 主要思路
如果直接使用简单的替换， 在每次渲染时， 都会重复这一过程， 这样的方式很不经济
在这个例子模板被翻译成了一个render函数, 模板只在被翻译成render函数时解析一次， 之后每次都通过render生成结果， 避免每次解析和替换字符串的资源消耗

# 流程
主要的工作就是 

1. 解析原始的模板字符， 转化为下面python代码的字符串形式
2. 使用esec函数执行生成的源代码字符串, 在Teplite.render函数中调用动态生成的那个渲染函数

将
~~~
<p>Welcome, {{user_name}}!</p>
<p>Products:</p>
<ul>
{% for product in product_list %}
    <li>{{ product.name }}:
        {{ product.price|format_price }}</li>
{% endfor %}
</ul>
~~~

传化为

~~~python
def render_function(context, do_dots):
    c_user_name = context['user_name']
    c_product_list = context['product_list']
    c_format_price = context['format_price']

    result = []
    append_result = result.append
    extend_result = result.extend
    to_str = str

    extend_result([
        '<p>Welcome, ',
        to_str(c_user_name),
        '!</p>\n<p>Products:</p>\n<ul>\n'
    ])
    for c_product in c_product_list:
        extend_result([
            '\n    <li>',
            to_str(do_dots(c_product, 'name')),
            ':\n        ',
            to_str(c_format_price(do_dots(c_product, 'price'))),
            '</li>\n'
        ])
    append_result('\n</ul>\n')
    return ''.join(result)"
~~~


代码基本比较简单，大段代码都在Templite.__init__ 方法中。看着很累。
主要就是解析模板字符的时候那一大堆的判断语句让代码变得很长。


# 细节
## 扣性能
-  把所用的方法， 变量都换成了本地的。
python自带的函数直接就换了， 模板中的变量， 函数麻烦一点， 先统计（all_vars loop_vars)
之后补上。
- 使用了buffered， 每次解析的结果先存着， 之后一起添加。（多次的List.append 变成了一次 List.extend)

## 检测语法
- 用堆栈来记录标签的对应
- 最后检查CodeBuilder.indent 是否回到0

