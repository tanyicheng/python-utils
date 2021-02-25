# filename:fabric01.py

# from fabric import Connection,task

from fabric.api import *
import time

env.hosts = ['root@192.168.91.100:22']
env.password = '123456'

currentTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
# 备份数据库且下载的本地
database_path = '/home/backup/jeecg-boot'+currentTime+'.sql'


# 下载文件
def download():
    # 进入目录且。。。
    get(database_path, r'D:\1_sql\backup')


# 备份远程服务器下 docker 环境的mysql数据库
def mysql_bak():
    # result = run('mysqldump -u root -p123456 jeecg-boot > /home/jeecg-boot.sql')
    result = run('docker exec -it mysql mysqldump -u root -p123456 jeecg-boot > ' + database_path)
    print("result：" + result)


def do():
    mysql_bak()
    download()


# 执行命令，默认是在~目录下
# >fab -f fabric01.py deploy 或 execute(deploy)
# execute(download)
execute(do)
