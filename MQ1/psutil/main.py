import psutil
import time


mem = psutil.virtual_memory()
# 系统总计内存
while True:
    zj = int(mem.total) / 1024 / 1024 / 1024
    # 系统已经使用内存
    ysy = int(mem.used) / 1024 / 1024 / 1024

    # 系统空闲内存
    kx = int(mem.free) / 1024 / 1024 / 1024

    print('系统总计内存:%dGB' % zj)
    print('系统已经使用内存:%dGB' % ysy)
    print('系统空闲内存:%dGB' % kx)
    print('--')
    time.sleep(1)
