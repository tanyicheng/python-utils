from fabric.api import *
import yaml

# 由于官方提示load方法存在安全漏洞，所以读取文件时会报错。加上warning忽略，就不会显示警告
yaml.warnings({'YAMLLoadWarning': False})

# 读取配置信息
f = open('conf/linux.yaml', 'r', encoding='utf-8')
cfg = f.read()
d = yaml.load(cfg)
hosts = d.get('linux43').get('hosts')
# password = d.get('linux32').get('password')

# 全局变量 root@192.168.91.100:22
env.hosts = [hosts]
# env.password = password
# 使用证书登录
env.key_filename = 'D:\\0-seraphim\\1seraphim-证书'


def dir_ls(dirname):
    run('ls -l ' + dirname)

#指定目录打包
def tar(dirname):

    # run('cd /home ')
    with cd(dirname):
        # run('tar -zcvf tomcat7-material.tar tomcat7-material/ --exclude=tomcat7-material/logs')
        run('tar -zcvf tomcat7-mes.tar tomcat7-mes/ --exclude=tomcat7-mes/logs')
        run('tar -zcvf tomcat7-mq.tar tomcat7-mq/ --exclude=tomcat7-mq/logs')
        run('tar -zcvf tomcat7-newmes.tar tomcat7-newmes/ --exclude=tomcat7-newmes/logs')
        run('tar -zcvf tomcat7-report.tar tomcat7-report/ --exclude=tomcat7-report/logs')
        run('tar -zcvf tomcat7-user.tar tomcat7-user/ --exclude=tomcat7-user/logs')
        run('tar -zcvf tomcat7-wms.tar tomcat7-wms/ --exclude=tomcat7-wms/logs')


# TODO 执行之前，先去服务器将日志打包
@task
def go():
    print("---开始---")
    tar('/home/erp/apps')

    print('---结束---')


execute(go)
