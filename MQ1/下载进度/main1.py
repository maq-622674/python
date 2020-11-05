
from urllib.request import urlretrieve
 
#这是在百度图片里找到一张图片的地址
url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1555478103570&di=105c8451bd007dd31fd4abc4a550f339&imgtype=0&src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_bt%2F0%2F8583539165%2F1000'
 
#下面的go是自定义的回调函数，每次调用它都会打印出当前下载进度
def go(blocknum,blocksize,totalsize):
    percent=blocknum*blocksize/totalsize
    #blocknum是数据块的数量，我只下载一张图片，所以它等于1；blocksize是已经下载的文件大小，totalsize是图片总大小。
    if percent>1:
        percent=1
    #这里用了格式化字符串，输出的格式是小数点后保留两位的百分数 
    print('已下载{:.2%}'.format(percent))
    
progress=urlretrieve(url,'GJL.jpg',go)