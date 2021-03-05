from fabric.api import *
import yaml

# 读取配置信息
f = open('conf/ser32.yaml', 'r', encoding='utf-8')
cfg = f.read()
d = yaml.load(cfg)
hosts = d.get('linux').get('hosts')
password = d.get('linux').get('password')

# 全局变量 root@192.168.91.100:22
env.hosts = [hosts]
# env.password = password
#使用证书登录
env.key_filename ='D:\\0-seraphim\\1seraphim-证书'


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

# >fab -f fabric01.py workask

