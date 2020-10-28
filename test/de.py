import time
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    time.sleep(10)
    del b
    del a
    print("++++++")

if __name__ == '__main__':
    my_func()