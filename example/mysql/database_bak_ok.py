#!/usr/bin/env python3
# filename:fabric01.py

# from fabric import Connection,task
from fabric.api import *
import time

env.hosts = ['root@192.168.91.100:22']
env.password = '123456'

currentTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
# 备份数据库且下载的本地
database_path = '/home/backup/snipe-boot' + currentTime + '.sql'
# TODO jeecg 系统数据备份
# local_path = 'D:\git\my_study\jeecg-boot\jeecg-boot\db'
local_path = '/Users/snipe/Documents/tan/git/project/jeecg-boot/jeecg-boot/db'

# 下载文件
def download():
    # 进入目录且。。。
    get(database_path, r'' + local_path)


# 备份远程服务器下 docker 环境的mysql数据库，TODO 注意不能通过Navicat导入，数据库名导入时也需要一致
def mysql_bak():
    # result = run('mysqldump -u root -p123456 jeecg-boot > /home/jeecg-boot.sql')
    # result = run('docker exec -it mysql mysqldump -uroot -p123456 -h127.0.0.1 -P3306 --databases jeecg-boot > ' + database_path)
    result = run('docker exec -it mysql mysqldump -uroot -p123456 snipe-boot > ' + database_path)
    print("result：" + result)


# linux 测试可行
# mysqldump -uroot -p123456 --databases jeecg-boot> jeecgboot.bak.sql
# mysql -uroot -p123456  jeecg-boot<jeecgboot.bak.sql

def do():
    mysql_bak()
    download()


# 执行命令，默认是在~目录下
# >fab -f fabric01.py deploy 或 execute(deploy)
# execute(download)
execute(do)

# TODO Mac 下手动执行
# docker exec -it mysql5.7  bash
# mysqldump -u root -p123456 snipe-boot > /home/snipe-boot20220510.sql
# docker cp mysql5.7:/home/snipe-boot20220510.sql /Users/snipe/Documents/tan/git/project/jeecg-boot/jeecg-boot/db

# docker exec -it w.mysql  bash
# mysqldump -u root -p123456 jeecg-boot > /home/jeecg-boot221007.sql
# 导出成功后退出，在主机执行拷贝命令，从docker复制到本机
# docker cp mysql5.7:/home/jeecg-boot221007.sql /Users/snipe/Documents/tan/git/project/jeecg-boot/jeecg-boot/db
