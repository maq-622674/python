# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect( 
    host='rm-wz97d5ot77lk3t824sm.mysql.rds.aliyuncs.com', # 主机模块
    port=3306, # 端口号
    user='aaa',# 用户名
    password='123456789', # 密码
)
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount

# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values

# 关闭Cursor和Connection:
cursor.close()

conn.close()