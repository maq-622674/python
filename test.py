import pymysql # 导入模块
conn = pymysql.connect(
	host='w.rdc.sae.sina.com.cn', # 主机模块
	port=3306, # 端口号
	user='30y3nm23xl',# 用户名
	password='lzjyz4w2j4ywlkzwi2jylz2k423ill2mmj4jxmy5', # 密码
	database='db', # 需要连接的库
	charset='utf8' # 指定编码utf8
)
cursor = conn.cursor() # 获取游标 
# cursor = conn.cursor(pymysql.cursors.DictCursor) # 获取的查询结果更加规范化 便于分辨
sql = "select * from dep;"
ret = cursor.execute(sql) # ret 受影响的行数
# res = cursor.executemany(sql,[(a,b),(a1,b1),(a2,b2)]) # 插入多行数据时 
print(cursor.fetchall())  # 取出所有的
print(cursor.fetchmany(3))# 取出多条
print(cursor.fetchone())  # 取出单条

cursor.scroll(3,'absolute') # 绝对移动,按照数据最开始位置往下移动3条
cursor.scroll(1,'relative') # 通过上面取了一次数据,游标的位置 ,我现在相对移动了1个记录,那么下次再取,取出的是第三条,我相对于上一条,往下移动了一条
conn.commit()  # 增删改操作时,需要进行提交

cursor.close() # 关闭游标
conn.close() # 关闭连接