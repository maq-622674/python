 n=0     
            while True:
                #旧数据
                data=[]
                #新数据
                data1=[]


                data3=[]
                data4=[]
                #原始数据
                shujuchushihua()
                #数据清洗
                shujuqingxi()
                if(data3==data4):
                    print("数据一样")
                else:
                    print("数据不一样")
                    for i,j in zip_longest(data3,data4):
                        if(len(data4)>len(data3)):
                            print("数据增加了")
                            if(i!=j):
                                print(i)
                                print(j)
                        if(len(data4)<len(data3)):
                            print("数据减少了")
                            if(i!=j):
                                print(i)
                                print(j)
                data3=data4
                data=data1
                data4=[]
                data=[]          
                sleep(20)
                n=n+1