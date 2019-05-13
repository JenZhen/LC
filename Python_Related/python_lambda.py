multi = lambda x, y: x * y
实质上lambda 是一个anonymous function 匿名函数
返回一个函数体

例子：
def myfunc(n):
    return lambda a : a * n

myDoubler = myfunc(2)
myTripler = myfunc(3)

myDoubler(10) return 20
myTripler(10) return 30

function wrapper
