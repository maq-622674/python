#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect( 
    host='rm-wz97d5ot77lk3t824sm.mysql.rds.aliyuncs.com', # 主机模块
    port=3306, # 端口号
    user='aaa',# 用户名
    password='1234567890', # 密码
)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)
# 关闭数据库连接
db.close()

############################################
#!/usr/bin/python3
import pymysql
# 打开数据库连接
db = pymysql.connect( 
    host='rm-wz97d5ot77lk3t824sm.mysql.rds.aliyuncs.com', # 主机模块
    port=3306, # 端口号
    user='aaa',# 用户名
    password='1234567890', # 密码
)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
# 关闭数据库连接
db.close()

print("*"*10)

import pymysql # 导入模块



conn = pymysql.connect(
    host='rm-wz97d5ot77lk3t824sm.mysql.rds.aliyuncs.com', # 主机模块
    port=3306, # 端口号
    user='aaa',# 用户名
    password='1234567890', # 密码
    #database='db', # 需要连接的库
    #charset='utf8' # 指定编码utf8
)
print(conn)
cursor = conn.cursor() # 获取游标 
print(cursor)

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
cursor.execute('SHOW DATABASES')

print(cursor.fetchall())
print ("Database version : %s " % data)
# cursor = conn.cursor(pymysql.cursors.DictCursor) # 获取的查询结果更加规范化 便于分辨
#sql = "select * from dep;"
#ret = cursor.execute(sql) # ret 受影响的行数
# res = cursor.executemany(sql,[(a,b),(a1,b1),(a2,b2)]) # 插入多行数据时 
# print(cursor.fetchall())  # 取出所有的
# print(cursor.fetchmany(3))# 取出多条
# print(cursor.fetchone())  # 取出单条
 
# cursor.scroll(3,'absolute') # 绝对移动,按照数据最开始位置往下移动3条
# cursor.scroll(1,'relative') # 通过上面取了一次数据,游标的位置 ,我现在相对移动了1个记录,那么下次再取,取出的是第三条,我相对于上一条,往下移动了一条
# conn.commit()  # 增删改操作时,需要进行提交
 
cursor.close() # 关闭游标
conn.close() # 关闭连接