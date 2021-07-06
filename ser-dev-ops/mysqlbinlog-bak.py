from fabric.api import *
import yaml

# 由于官方提示load方法存在安全漏洞，所以读取文件时会报错。加上warning忽略，就不会显示警告
yaml.warnings({'YAMLLoadWarning': False})

# 读取配置信息
f = open('conf/linux.yaml', 'r', encoding='utf-8')
cfg = f.read()
d = yaml.load(cfg)
hosts = d.get('linux44').get('hosts')
# password = d.get('linux32').get('password')

# 全局变量 root@192.168.91.100:22
env.hosts = [hosts]
# env.password = password
# 使用证书登录
env.key_filename = 'D:\\0-seraphim\\1seraphim-证书'


def dir_ls(dirname):
    run('ls -l ' + dirname)


# mes库
def bak32():
    run('scp -r root@172.16.8.32:/home/mysql/data/*.gz /home/mount-backup/binlog-backup/mes')


# report 库
def bak42():
    run('scp -r root@172.16.8.42:/home/mysql/data/*.gz /home/mount-backup/binlog-backup/report')


# other 库
def bak37():
    run('scp -r root@172.16.8.37:/home/mysql/data/*.gz /home/mount-backup/binlog-backup/other')


# TODO 执行之前，先去服务器将日志打包
@task
def go():
    print("---开始---")
    bak42()

    print('---结束---')


execute(go)
