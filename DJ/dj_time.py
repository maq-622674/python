import time

class Time():
    def __init__(self):
        pass
    def time_stamp(self):
        '''
        时间戳
        '''
        time_stamp=time.time()
        print(time_stamp)
    
def main():
    p1=Time()
    p1.time_stamp()
if __name__ == "__main__":
    main()