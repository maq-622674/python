
import time
import shutil
import hashlib

class Custom_plug(object):
    def __init__(self):
        pass
    def time_stamp(self):
        '''
        时间戳
        返回值:默认是float类型
        '''
        time_stamp=time.time()
        return time_stamp
    def cutting(self,string_a,cut):
        '''
        string_a参数:string_a字符串
        cut参数:用什么字符来切割例如:_ ./ *
        返回值:list列表类型
        '''
        name=string_a.split(cut)
        return name
    def check_contain_chinese(self,check_str):
        '''
        check_str参数:字符串
        判断字符串是不是全是中文
        返回值:不全是中文或者全是中文 str类型
        '''
        for ch in check_str:
            if u'\u4e00'<=ch<=u'\u9fff':
                pass
            else:
                return "不全是中文"
        return "全是中文"
    def determine_all_numbers(self,parameter):
        '''
        功能:判断是不是全为数字
        '''
        if(parameter.isdigit()==True):
            return "全部为数字"
        else:
            return "不全是数字"
    def copy_files(self,starting_point,end_of):
        '''
        功能:拷贝文件
        starting_point参数:被复制文件夹位置
        end_of参数:复制到哪里
        注意参数路径改为/,这里只能单个 .jpg .txt
        文件夹复制待续
        '''   
        shutil.copyfile(starting_point,end_of)
    def slash(self,param):
        '''
        功能:更改磁盘路径C:\CSDN_L\python改为C:/CSDN_L/python
        '''
        path=param.replace('\\','/')
        print(path)
        return path
    
    def current_time(self):
        '''
        功能:获取当前时间
        :return:
        '''
        time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.time_stamp()))
        return time1




    

def main():
    pass
    #p1=Custom_plug()
    #p1.time_stamp()
if __name__=="__main__":
    main()