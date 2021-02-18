# filename:fabric01.py

# from fabric import Connection,task

from fabric.api import *

env.hosts = ['root@192.168.91.100:22']
env.password = '123456'


def deploy():
    run('cd /home && ls')
    with cd('/home'):
        run('pwd')
        run('ls')


# 从远程下载文件
def get_file():
    with cd('/root/chengLogs/system'):
        get('system_logger_2021-02-07.log', r'D:\logs')

    # run('ls')

# 上传文件
def upload():
    put(r'D:\logs\service_log.txt', '/home/')


# 下载文件
def download():
    # 进入目录且。。。
    with cd('/home'):
        get('jeecg-boot.sql', r'D:\logs')


# 备份远程服务器下 docker 环境的mysql数据库
def mysql_bak():
    # result = run('mysqldump -u root -p123456 jeecg-boot > /home/jeecg-boot.sql')
    result = run('docker exec -it mysql mysqldump -u root -p123456 jeecg-boot > /home/jeecg-boot.sql')
    print("result："+result)


# 执行命令，默认是在~目录下
# >fab -f fabric01.py deploy 或 execute(deploy)
# execute(download)
execute(mysql_bak)
