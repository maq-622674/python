'''
前面章节一直在介绍如何使用多线程实现并发编程，其实 Python 还支持多进程编程。

要知道，每个 Python 程序在执行时，系统都会生成一个新的进程，该进程又称父进程（或主进程）。在此基础上，Python os 模块还提供有 fork() 函数，该函数可以在当前程序中再创建出一个进程（又称子进程）。

也就是说，程序中通过引入 os 模块，并调用其提供的 fork() 函数，程序中会拥有 2 个进程，其中父进程负责执行整个程序代码，而通过 fork() 函数创建出的子进程，会从创建位置开始，执行后续所有的程序（包含创建子进程的代码）。
注意，os.fork() 函数在 Windows 系统上无效，只在 UNIX 及类 UNIX 系统上（包括UNIX、Linux 和 Mac OS X）效。

fork() 方法的语法格式为：
pid = os.fork()

其中，pid 作为函数的返回值，主进程和子进程都会执行该语句，但主进程执行 fork() 函数得到的 pid 值为非 0 值（其实是子进程的进程 ID），而子进程执行该语句得到的 pid 值为 0。因此，pid 常常作为区分父进程和子进程的标志。
在大多数操作系统中，都会为执行的进程配备唯一的 ID 号，os 模块提供了 getpid() 和 getppid() 函数，可分别用来获取当前进程的 ID 号和父进程的 ID 号。

下面程序演示了 os.fork() 方法的具体使用：
'''
import os
print('父进程 ID =', os.getpid())
# 创建一个子进程，下面代码会被两个进程执行
pid = os.fork()
print('当前进程 ID =',os.getpid()," pid=",pid)
#根据 pid 值，分别为子进程和父进程布置任务
if pid == 0:
    print('子进程, ID=',os.getpid()," 父进程 ID=",os.getppid())
else:
    print('父进程, ID=',os.getpid()," pid=",pid)
'''
从输出结果可以看到，当前程序在执行时，系统生成了进程号为 2884 的进程，该进程负责执行当前程序中的所有代码。与此同时，程序第 4 行创建了进程号为 2885 的子进程，该进程将执行第 4 行开始（包括第 4 行）后续的所有代码。

注意，程序第 7 行代码的 if 判断语句，通过判断 pid 值是否为 0，分别为父进程和 fork() 函数创建的子进程布置了不同的执行任务，即子进程负责执行 if 代码块，而父进程则负责执行 else 代码块。
'''