import xlrd
import xlwt
class Excel():
    def __init__(self):
        pass
    def du_excel(self):
        '''
        读取表格的数据
        '''
        pass
    def xie_excel(self):
        '''     
        写表格数据
        '''
        # 创建workbook和sheet对象 注意Workbook的开头W要大写
        num=0
        workbook = xlwt.Workbook()
        #添加一个名为sheet1的表
        sheet1 = workbook.add_sheet('sheet'+str(num), cell_overwrite_ok=True)
        title = ['姓名', '年龄', '性别', '分数']
        stus = [
            ['lili', 20, '女', 89.9],
            ['lucy', 21, '女', 90.9], 
            ['make', 22, '男', 91.9],
            ['mary', 23, '男', 92.9]
        ]
        # 向表头写入数据
        for i in range(len(title)):
            sheet1.write(0,i,title[i])
            
        #向sheet写入数据
        for i in range(len(stus)):
            for j in range(4):
                sheet1.write(i + 1, j, stus[i][j])
                
        #保存数据到‘Workbook2.xls’文件中
        num=input("输入表格的明Zi")
        workbook.save(num+'.xls')
        print('创建execel完成！')
       
        
    def xiugai_excel(self):
        '''
        修改
        '''
    def shanchu_excel(self):
        '''
        删除
        '''

def main():
    p1=Excel()
    p1.xie_excel()
if __name__ == "__main__":
    main()