from fabric.api import *

# 上传文件并执行

# 全局变量
env.hosts = ['root@47.98.189.194:22']
env.password = ''

path = '/home/itcast/testdemo'


# 本地环境操作
@task
@runs_once
def tar_task():
    with lcd('D:/logs'):
        local('tar zcvf example.tar.gz example.py')


@task
def put_task():
    run('mkdir -p ' + path)
    with cd(path):
        put('D:/logs/demo.tar.gz', path + '/example.tar.gz')


@task
def check_task():
    lmd5 = ''
    rmd5 = ''

    try:
        # lmd5 = local('md5sum ' + path + '/example.tar.gz', capture=True).split(' ')[0]
        rmd5 = run('md5sum ' + path + '/example.tar.gz').split(' ')[0]
        if lmd5 == rmd5:
            print('ok ...')
        else:
            print('error...')
    except Exception as e:
        print("err  " + lmd5 + " :: " + rmd5)
        print(e)


@task
def run_task():
    with cd(path):
        run('tar zxvf example.tar.gz')
        # run('python example.py') 远程没有装python ，就执行下cat
        run('cat example.py')


@task
def go():
    tar_task()
    put_task()
    check_task()
    run_task()

# >fab -f fabric01.py -l
