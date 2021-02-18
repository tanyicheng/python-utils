from fabric.api import *

# 全局变量
env.hosts = ['root@47.98.189.194:22']
env.password = 'Tfq.123456'


@runs_once  # 函数装饰器，标识的函数只会执行一次，不受多台主机影响
def input_raw():
    return prompt('请输入目录的名字：', default='/home')


def workask(dirname):
    run('ls -l ' + dirname)


@task  # 函数装饰器，标识的函数为fab可调用的，非标记的对fab不可见，纯业务逻辑
def go():
    print("---开始---")
    getdirname = input_raw()
    workask(getdirname)
    print('---结束---')

# >fab -f fabric01.py
