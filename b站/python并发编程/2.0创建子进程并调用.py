from multiprocessing import Process

def run_proc():
    print("子进程运行中")

if __name__ == "__main__":
    print("父进程运行")
    p=Process(target=run_proc)
    print("子进程将要执行")
    p.start()