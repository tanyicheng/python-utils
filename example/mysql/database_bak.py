# !/usr/bin/python
###########################################################
#
# This python script is used for mysql database backup
# using mysqldump and tar utility.
#
# Written by : Rahul Kumar
# Website: http://tecadmin.net
# Created date: Dec 03, 2013
# Last modified: Aug 17, 2018
# Tested with : Python 2.7.15 & Python 3.5
# Script Revision: 1.4
#
##########################################################

import os
import time
import pipes

"""
1.MySQL database details to which backup to be done. 
  Make sure below user having enough privileges to take databases backup.
2.To take multiple databases backup, create any file like /backup/dbnames.
  txt and put databases names one on each line and assigned to DB_NAME variable.
"""
DB_HOST = '192.168.91.100'
DB_USER = 'root'
DB_USER_PASSWORD = '123456'
# DB_NAME = '/backup/dbnameslist.txt'
DB_NAME = 'jeecg-boot'
BACKUP_PATH = 'D:\\1_sql\\backup'

# Getting current DateTime to create the separate backup folder like "20180817-123433".
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '\\' + DATETIME

# Checking if backup folder already exists or not. If not exists will create it.
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.makedirs(TODAYBACKUPPATH)

# Code for checking if you want to take single database backup or assigned multiple backups in DB_NAME.
print("checking for databases names file.")
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print("发现数据库文件...")
    print("Starting backup of all dbs listed in file " + DB_NAME)
else:
    print("没有发现数据库文件...")
    print("Starting backup of database " + DB_NAME)
    multi = 0

# Starting actual database backup process.
if multi:
    in_file = open(DB_NAME, "r")
    flength = len(in_file.readlines())
    in_file.close()
    p = 1
    dbfile = open(DB_NAME, "r")

    while p <= flength:
        db = dbfile.readline()  # reading database name from file
        db = db[:-1]  # deletes extra line
        dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(
            TODAYBACKUPPATH) + "\\" + db + ".sql"
        os.system(dumpcmd)
        gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "\\" + db + ".sql"
        os.system(gzipcmd)
        p = p + 1
    dbfile.close()
else:
    db = DB_NAME
    dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(
        TODAYBACKUPPATH) + "\\" + db + ".sql"
    os.system(dumpcmd)
    # gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "\\" + db + ".sql"
    # os.system(gzipcmd)

print("")
print("Backup script completed")
print("Your backups have been created in '" + TODAYBACKUPPATH + "' directory")

# fixme 有异常，输出乱码
# 指定ip地址备份数据 docker exec -it mysql mysqldump -h 192.168.91.100 -u root -p123456 jeecg-boot > /home/jeecg-boot.sql
# 可以执行 docker exec -it mysql mysqldump -u root -p123456 jeecg-boot > /home/jeecg-boot.sql