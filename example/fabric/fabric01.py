# filename:fabric01.py

# from fabric import Connection,task

from fabric.api import *

env.hosts = ['root@47.98.189.194:22']
env.password = 'Tfq.123456'


def task1():
    print("hello")


def hello():
    print("hello world")


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

def upload():
    put(r'D:\logs\service_log.txt','/home/tan')

# 执行命令，默认是在~目录下
# >fab -f fabric01.py deploy
