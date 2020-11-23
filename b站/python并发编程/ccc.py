#https://blog.csdn.net/kangxiaoyanl/article/details/104941372

'''
先创建一个推送类
#1.同步阻塞的http请求init接口
#2.同步阻塞的http请求login接口(主要获取所有班级ID和名称)
#3.异步无阻塞的http请求init_class接口(根据班级ID获取学生列表接口地址,一次查询一个班级)
#4.异步无阻塞的http请求getleave接口(根据学生卡号查询学生在某个时间点是否处于请假中)
#4.1异步无阻塞的下载3接口请假学生的照片(重复的照片不下载)
#5.异步无阻塞的http请求init_face接口(推送人脸)
'''