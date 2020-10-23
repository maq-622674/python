from threading import Timer
def hello():
    print("hello, world")
# 指定10秒后执行hello函数
t = Timer(10.0, hello)
t.start()
'''
上面程序使用 Timer 控制 10s 后执行 hello 函数。

需要说明的是，Timer 只能控制函数在指定时间内执行一次，如果要使用 Timer 控制函数多次重复执行，则需要再执行下一次调度。

如果程序想取消 Timer 的调度，则可调用 Timer 对象的 cancel() 函数。例如，如下程序每 1s 输出一次当前时间：在main1.py
'''