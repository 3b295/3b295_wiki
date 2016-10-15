### embed  

header:   出现在在ipython[1] 上面的字符串
banner1:  同上， 但位置更靠前
user_ns:  注入一个环境上下文(其实就是一个字典，但我不确定每个实现都是字典)


除了header， 其它的参数都不是embed本身负责的， embed只是将不用的参数继续传下去，
如 user_ns 其实是在   ipython/IPython/core/interactiveshell.py 中的 InteractiveShell 中被解析
