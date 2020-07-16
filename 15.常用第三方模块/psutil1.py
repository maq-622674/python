'''
用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。

在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
'''
#1.获取CPU信息
import psutil
# CPU逻辑数量
print(psutil.cpu_count())
#4
# CPU物理核心
print(psutil.cpu_count(logical=False))
#2
# 2说明是双核超线程, 4则是4核非超线程

#统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

#再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

#2.获取内存信息
#使用psutil获取物理内存和交换内存信息，分别使用：
print(psutil.virtual_memory())
print(psutil.swap_memory())
'''
返回的是字节为单位的整数，可以看到，总内存大小是8589934592 = 8 GB，
已用7201386496 = 6.7 GB，使用了66.6%。
而交换区大小是1073741824 = 1 GB。
'''

#3.获取磁盘信息
# 磁盘分区信息
print("*"*10)
print(psutil.disk_partitions())

# 磁盘使用情况
print(psutil.disk_usage('/'))

# 磁盘IO
print(psutil.disk_io_counters())
'''
可以看到，磁盘'/'的总容量是998982549504 = 930 GB，
使用了39.1%。文件格式是HFS，opts中包含rw表示可读写，journaled表示支持日志。
'''

#4.获取网络信息
#psutil可以获取网络接口和网络连接信息：
# 获取网络读写字节／包的个数
print("#"*10)
print(psutil.net_io_counters())

# 获取网络接口信息
print(psutil.net_if_addrs() )

 # 获取网络接口状态
print(psutil.net_if_stats())

#要获取当前网络连接信息，使用net_connections()：
print(psutil.net_connections())
'''
你可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动：

$ sudo python3
Password: ******
Python 3.8 ... on darwin
Type "help", ... for more information.
>>> import psutil
>>> psutil.net_connections()
[
    sconn(fd=83, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62911), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
    sconn(fd=84, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62905), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
    sconn(fd=93, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::', port=8080), raddr=(), status='LISTEN', pid=3725),
    sconn(fd=103, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62918), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
    sconn(fd=105, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
    sconn(fd=106, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
    sconn(fd=107, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
    ...
    sconn(fd=27, family=<AddressFamily.AF_INET: 2>, type=2, ..., pid=1)
]
'''
#5.获取进程信息
print("*"*10)
#所有进程ID
print(psutil.pids())
#获取指定进程ID=3776，其实就是当前python交互环境
p=psutil.Process(21824)
#进程名称
print(p.name())
#进程exe路径
print(p.exe())
#进程工作目录
print(p.cwd())
#进程启动的命令行
print(p.cmdline())
## 父进程ID
print(p.ppid())
#父进程
print(p.parent())
#子进程
print(p.children())
#进程状态
print(p.status())
#进程用户名
print(p.username())
#进程创建时间
print(p.create_time())
#进程终端
#print(p.terminal())
#进程使用的CPU时间
print(p.cpu_times())
#进程使用的内存
print(p.memory_info())
#进程打开的文件
print(p.open_files())
#进程相关网络连接
print(p.connections())
#进程的线程数量
print(p.num_threads())
#所有线程信息
print(p.threads())
#进程环境变量
print(p.environ())
#结束进程
print(p.terminate())
'''
和获取网络连接类似，获取一个root用户的进程需要root权限，启动Python交互环境或者.py文件时，需要sudo权限。

psutil还提供了一个test()函数，可以模拟出ps命令的效果：

$ sudo python3
Password: ******
Python 3.6.3 ... on darwin
Type "help", ... for more information.
>>> import psutil
>>> psutil.test()
USER         PID %MEM     VSZ     RSS TTY           START    TIME  COMMAND
root           0 24.0 74270628 2016380 ?             Nov18   40:51  kernel_task
root           1  0.1 2494140    9484 ?             Nov18   01:39  launchd
root          44  0.4 2519872   36404 ?             Nov18   02:02  UserEventAgent
root          45    ? 2474032    1516 ?             Nov18   00:14  syslogd
root          47  0.1 2504768    8912 ?             Nov18   00:03  kextd
root          48  0.1 2505544    4720 ?             Nov18   00:19  fseventsd
_appleeven    52  0.1 2499748    5024 ?             Nov18   00:00  appleeventsd
root          53  0.1 2500592    6132 ?             Nov18   00:02  configd
...
小结
psutil使得Python程序获取系统信息变得易如反掌。

psutil还可以获取用户信息、Windows服务等很多有用的系统信息，具体请参考psutil的官网：https://github.com/giampaolo/psutil
'''
