'''
deebin10
https://www.cnblogs.com/syrgdm/p/12854186.html
1.执行sh脚本文件
例如:./test.sh

2.可显示电脑以及操作系统的相关信息
uname -a


3.批处理文件,shell脚本文件
touch test.sh
vim test.sh

4.创建文件夹
mkdir 文件夹
创建文件
touch 文件


5.-r 就是向下递归，不管有多少级目录，一并删除
-f 就是直接强行删除，不作任何提示的意思
删除文件
rm -f 文件
删除文件夹
rm -rf 文件夹

6.查看文件内容
cat 文件

7.重启命令
reboot -f
sudo reboot -f

8.查看文件的权限
ls -l

9.配置yum
更新源列表
sudo apt-get -y update
更新软件
sudo apt-get dist-upgrade
此时我们的root还没有初始化,所以下一步就是初始化root密码
sudo passwd
然后输入当前密码
然后再输入新的root的密码再次确认
su root然后输入刚刚设置的root密码切换到root权限
安装及配置yum源
sudo apt-get install build-essential
sudo apt-get install yum
cd /etc/yum.repos.d
vi 163.repo(i键编辑 esc键退出编辑模式 输入:wq保存并退出 出现异常退不出去 ctrl+z)
然后使用
yum clean all
yum repolist all
yum makecache
yum list

10.开启远程服务
安装ssh服务
sudo apt-get install openssh-serve
配置端口
vi /etc/ssh/sshd_config
重启ssh服务端
sudo /etc/init.d/ssh start或者service ssh start
查看本机ip
ipconfig
ip add

11.给文件增加权限
chmod +x 文件位置

12.没有chkconfig命令怎么处理
有网的情况下可直接yum安装命令
先下载yum
再yum install chkconfig
没有用网络的情况下可从安装光盘下复制chkconfig的rpm包
执行rpm命令安装
假设复到了/tmp/chkconfig-1.3.30.2-2.el5.x86_64.rpm
命令如下
rpm -ivh /tmp/chkconfig-1.3.30.2-2.el5.x86_64.rpm
然后chkconfig命令就可以用了。
http://www.maersk.com.cn/
'''
