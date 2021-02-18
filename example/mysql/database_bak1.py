#!/usr/bin env python3
import os
import time
import datetime

# fixme 没有dbnames.txt 配置文件
# 定义服务器，用户名、密码、数据库名称（多个库分行放置）和备份的路径
DB_HOST = '192.168.91.100'
DB_USER = 'root'
DB_USER_PASSWD = '123456'
DB_NAME = 'D:\\1_sql\\dbbackup\\dbnames.txt'
BACKUP_PATH = 'D:\\1_sql\\dbbackup\\mysql\\'

DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + DATETIME

print("createing backup folder!")
# 创建备份文件夹
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)

print("checking for databases names file")


# 定义执行备份脚本，读取文件中的数据库名称，注意按行读写，不校验是否存在该库
def run_backup():
    in_file = open(DB_NAME, "r")
    for dbname in in_file.readlines():
        dbname = dbname.strip()
        print("now starting backup database %s" % dbname)
    dumpcmd = "mysqldump -u" + DB_USER + " -p" + DB_USER_PASSWD + " " + dbname + " > " + TODAYBACKUPPATH + "/" + dbname + ".sql"
    print(dumpcmd)
    os.system(dumpcmd)

    file1.close()


# 执行压缩的函数
def run_tar():
    compress_file = TODAYBACKUPPATH + ".tar.gz"
    compress_cmd = "tar -czvf " + compress_file + " " + DATETIME
    os.chdir(BACKUP_PATH)
    os.system("pwd")
    os.system(compress_cmd)
    print("compress complete!")
    # 删除备份文件夹
    remove_cmd = "rm -rf " + TODAYBACKUPPATH
    os.system(remove_cmd)


# 备份数据库文件存在就执行备份和压缩，否则退出
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    print("starting backup of all db listed in file " + DB_NAME)
    run_backup()
    run_tar()
    print("backup success!")
else:
    print("database file not found..")
    exit()
