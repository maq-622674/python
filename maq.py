# a=[
#     {"a":"val1","b":"val2"},
#     {"a":"val1","b":"val2"},
#     {"c":"val1","d":"val2"},
#     {"e":"val1","f":"val2"},
#     {"e":"val1","f":"val2"},
# ]
# bbb=[]
# max_bbb=[]
# first=0
# for i in range(len(a)):
#     if(i==0):
#         first=a[i]
#     if(i>0):
#         if(a[i]==first):
#             print("1",first)
#             print("2",a[i])
#             bbb.append(first)
#             bbb.append(a[i])
#         else:
#             pass
#         first=a[i]
# print(bbb)
# max_bbb.append(bbb)     
# print(max_bbb)
    #print(i) 
#1.循环第一次保存数据然后跳出循环
#2.循环第二次和第一次的数据进行比较
#2.1如果数据相等 则输出
#2.2如果数据不相等 什么也不干
#2.3清空第一次保存的数据
#2.4将第二次的数据赋给第一次的

def GetInfo(htmlSource):
    """爬取信息"""
    Selector = etree.HTML(htmlSource)#转换为xpath能查询的文本
    #获取期数、
    term = Selector.xpath('//td[@class="td_title01"]/span/a/font/strong/text()')[0] 
    #获取开奖日期
    date = str(Selector.xpath('//td[@class="td_title01"]/span/text()')[1])
    date = date.split(' ')[1].split('：')[1]  #获取开奖日期，注意其中：是中文符号的
    #获取开奖号码
    num = Selector.xpath('//div[@class="ball_box01"]/ul/li/text()')
    num = " ".join(num)      #连接获取中奖号码
    #获取当前销量和滚动奖池
    money = Selector.xpath('//table[@class="kj_tablelist02"]/tr/td/span/text()')      #销售量为下标为2， 奖池下标为3 
    saleMoney = str(''.join(money[2].split(',')).partition('元')[0])
    jackpot = str(''.join(money[3].split(',')).partition('元')[0])
    #在并发处理的时候，可能会会出现下标越界问题，不知道是不是因为requests线程不安全还是啥的，数据会丢失，所以得重新收集销量信息
    Prize = []
    for i in range(3,9):
        prize = Selector.xpath('//table[@class="kj_tablelist02"]/tr[%d]/td/text()'%i)
        if i == 3:
            try:
                #格式化数据
                num_ =  prize[6].replace('\r\n\t\t\t\t','')
                prize[7].replace('\r\n\t\t\t\t','')
            except:
                num_ =  prize[5].replace('\r\n\t\t\t\t','')
            if num_.isdigit():
                pass
            else:
                num_ = 0
        else:
            num_ =  prize[1].replace('\r\n\t\t\t\t','')
        Prize.append(num_)
    #列表用以后面数据持久化操作时循环取出