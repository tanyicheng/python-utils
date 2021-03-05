from fabric.api import *
import yaml

# 由于官方提示load方法存在安全漏洞，所以读取文件时会报错。加上warning忽略，就不会显示警告
yaml.warnings({'YAMLLoadWarning': False})

# 读取配置信息
f = open('conf/linux.yaml', 'r', encoding='utf-8')
cfg = f.read()
d = yaml.load(cfg)
hosts = d.get('linux32').get('hosts')
# password = d.get('linux32').get('password')

#todo 放弃，用scp处理
# 全局变量 root@192.168.91.100:22
env.hosts = ['root@172.16.8.32:22']
# env.password = password
#使用证书登录
env.key_filename ='D:\\0-seraphim\\1seraphim-证书'


def workask(dirname):
    run('ls -l ' + dirname)


# @task  # 函数装饰器，标识的函数为fab可调用的，非标记的对fab不可见，纯业务逻辑
def go():
    print("---开始---")

    workask('/home')
    print('---结束---')


execute(go)