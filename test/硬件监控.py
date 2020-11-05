# import psutil
# import datetime
# import time

# class MessyServerHardware:
# 	def __init__(self):
# 		self.__now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# 		self.__serverStartTime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

# 	def cpu(self):
# 		self._cpuCount = psutil.cpu_count(logical=False)						# 查看cpu物理个数	
# 		self._cpu = str(psutil.cpu_percent(interval=2, percpu=False)) + '%'		# CPU的使用率
# 																					# interval是获取2s内的cpu使用率波动
# 																					# 这个获取的不是很准确，仅供参考
# 		return self._cpu

# 	def memory(self):
# 		self._free = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2))									# 总物理内存(DDR)
# 		self._total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2))									# 剩余物理内存(DDR)
# 		self._memory = int(psutil.virtual_memory().total - psutil.virtual_memory().free) / float(psutil.virtual_memory().total)	# 物理内存使用率(DDR)
# 		self._memory = str(int(self._memory * 100)) + '%'
# 		list = [self._memory,self._free,self._total]
# 		return list

# 	def user(self):
# 		self._users_count = len(psutil.users())							# 当前登录用户名
# 		self._users_list = ",".join([u.name for u in psutil.users()])	# 用户个数
# 		list = [self._users_count,self._users_list]
# 		return list

# 	def network(self):
# 		self._net = psutil.net_io_counters()
# 		self._bytes_rcvd = '{0:.2f} Mb'.format(self._net.bytes_sent / 1024 / 1024)	# 网卡接收流量
# 		self._bytes_sent = '{0:.2f} Mb'.format(self._net.bytes_recv / 1024 / 1024)	# 网卡发送流量
# 		list = [self._bytes_rcvd,self._bytes_sent]
# 		return list

# 	def main(self):
# 		list = {
# 			'now_time':self.__now_time,
# 			'serverStartTime':self.__serverStartTime,
# 			'cpu':self.cpu(),
# 			'memory':[
# 				self.memory()[0],
# 				self.memory()[1],
# 				self.memory()[2],
# 			],
# 			'user':[
# 				self.user()[0],
# 				self.user()[1],
# 			],
# 			'network':[
# 				self.network()[0],
# 				self.network()[1],
# 			]
# 		}
# 		return list

# serMeg = MessyServerHardware().main()
# print('最近一次监测数据时间:%s' % serMeg['now_time'])
# print('服务器启动时间:%s' % serMeg['serverStartTime'])
# print('CPU使用率:%s' % serMeg['cpu'])
# print('内存使用率:%s,剩余内存:%s,总内存:%s' % (serMeg['memory'][0],serMeg['memory'][1],serMeg['memory'][2]))
# print('当前登录用户:%s,用户名为:%s' % (serMeg['user'][0],serMeg['user'][1]))
# print('入网流量:%s,出网流量:%s' % (serMeg['network'][0],serMeg['network'][1]))

# coding:utf-8

import os
import threading



def cmd_neicun():
    # popen返回文件对象，跟open操作一样
    temp=()
    f = os.popen(r"systeminfo", "r")
    d = f.read()  # 读文件  
    f.close()
    if "物理内存总量" in d:
        d1=d.strip().split('物理内存总量:')[1].split('可用的物理内存')[0].strip()
        if 'MB' in d1:
            d11=d1.split('MB')[0].strip()
            if ',' in d11:
                d11=int(d11.split(',')[0])
            temp=temp+(d11,)   
        #print(d1)
    #d1=d.split('可用的物理内存')[1]
    if "可用的物理内存" in d:
        d2=d.strip().split('可用的物理内存:')[1].split('虚拟内存')[0].strip()
        if 'MB' in d2:
            d22=d2.split('MB')[0].strip()
            if ',' in d22:
                d22=int(d22.split(',')[0])
            temp=temp+(22,) 

  
 
cmd_neicun()
# temp=(1,2,3,4,5)
# temp=temp[:2]+(8,)+temp[2:]
# print(temp[:2]+(8,))
# print(temp)



    #return d
#bbb=cmd_neicun()
# print("bbb",bbb)
   
# str = '{"key": "wwww", "word": "qqqq"}'
# j = json.loads(str)
# print(j)
# print(type(j))
# t1=threading.Thread(target=cmd_neicun)
# t1.start()

# import os
# import commands

# #vcgencmd measure_temp
# #cat /sys/class/thermal/thermal_zone0/temp


# # Return CPU temperature as a character string                                      
# def getCPUtemperature():
#     res = os.popen('vcgencmd measure_temp').readline()
#     return(res.replace("temp=","").replace("'C\n",""))

# # Return GPU temperature as a character string
# def get_gpu_temp():
#     gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
#     return  float(gpu_temp)
#     # Uncomment the next line if you want the temp in Fahrenheit
#     # return float(1.8* gpu_temp)+32


# # Return RAM information (unit=kb) in a list                                       
# # Index 0: total RAM                                                               
# # Index 1: used RAM                                                                 
# # Index 2: free RAM                                                                 
# def getRAMinfo():
#     p = os.popen('free')
#     i = 0
#     while 1:
#         i = i + 1
#         line = p.readline()
#         if i==2:
#             return(line.split()[1:4])

# # Return % of CPU used by user as a character string                                
# def getCPUuse():
#     return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
# )))

# # Return information about disk space as a list (unit included)                     
# # Index 0: total disk space                                                         
# # Index 1: used disk space                                                         
# # Index 2: remaining disk space                                                     
# # Index 3: percentage of disk used                                                  
# def getDiskSpace():
#     p = os.popen("df -h /")
#     i = 0
#     while 1:
#         i = i +1
#         line = p.readline()
#         if i==2:
#             return(line.split()[1:5])


# # CPU informatiom
# CPU_temp = getCPUtemperature()
# CPU_usage = getCPUuse()

# # RAM information
# # Output is in kb, here I convert it in Mb for readability
# RAM_stats = getRAMinfo()
# RAM_total = round(int(RAM_stats[0]) / 1000,1)
# RAM_used = round(int(RAM_stats[1]) / 1000,1)
# RAM_free = round(int(RAM_stats[2]) / 1000,1)

# # Disk information
# DISK_stats = getDiskSpace()
# DISK_total = DISK_stats[0]
# DISK_used = DISK_stats[1]
# DISK_perc = DISK_stats[3]

# if __name__ == '__main__':
#   print('')
#   print('CPU Temperature = '+CPU_temp)
#   print('CPU Use = '+CPU_usage)
#   print("GPU Temperature = ",str(get_gpu_temp()))
#   print('')
#   print('RAM Total = '+str(RAM_total)+' MB')
#   print('RAM Used = '+str(RAM_used)+' MB')
#   print('RAM Free = '+str(RAM_free)+' MB')
#   print('')  
#   print('DISK Total Space = '+str(DISK_total)+'B')
#   print('DISK Used Space = '+str(DISK_used)+'B')
#   print('DISK Used Percentage = '+str(DISK_perc))