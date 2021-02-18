# -*- coding:utf-8 -*-
import configparser
import os
import sched
import time
from ftplib import FTP

real_path = os.path.abspath(os.path.dirname(__file__))


def get_path_config():
    pro_dict = Properties(real_path + '/db.ini').get_properties()
    conf_info = ConfigInfo
    conf_info.sql_back_path = pro_dict['config']['sql_back_home']
    conf_info.dump_path = pro_dict['config']['mysql_home']
    return conf_info


class ConfigInfo(object):
    """ config path reader """

    def __init__(self, dump_path, sql_back_path):
        self.dump_path = dump_path
        self.sql_back_path = sql_back_path


class FileBack(object):
    """ ftp operator """

    def __init__(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def _connector(self):
        ftp = FTP()
        ftp.set_debuglevel(2)
        ftp.connect(self.ip, int(self.port))
        ftp.login(self.username, self.password)
        return ftp

    def list_files(self):
        ftp = self._connector()
        print(ftp.dir())

    def upload_file(self, local_file, target, filename):
        ftp = self._connector()
        try:
            ftp.cwd(target)
        except Exception as e:
            ftp.mkd(target)
            ftp.cwd(target)
        buf_size = 1024
        fp = open(local_file, 'rb')
        ftp.storbinary('STOR %s' % os.path.basename(filename), fp, buf_size)  # 上传文件
        ftp.set_debuglevel(0)
        fp.close()  # 关闭文件
        ftp.quit()


def get_db_info():
    dict_pro = Properties(real_path + '/db.ini').get_properties()
    db_info = DBInfo
    db_info.ip = dict_pro['db']['ip']
    db_info.port = dict_pro['db']['port']
    db_info.database = dict_pro['db']['database']
    db_info.username = dict_pro['db']['username']
    db_info.password = dict_pro['db']['password']
    return db_info


class DBInfo(object):
    """ database connection info """

    def __init__(self, ip, port, database, username, password):
        self.ip = ip
        self.port = port
        self.database = database
        self.username = username
        self.password = password


class Properties(object):
    """ properties reader  """

    def __init__(self, path):
        self.path = path
        self.properties = {}

    def get_properties(self):
        try:
            config = configparser.ConfigParser()
            config.read(self.path)
            db = {'ip': config.get('db', 'ip'), 'port': config.get('db', 'port'),
                  'database': config.get('db', 'database'),
                  'username': config.get('db', 'username'), 'password': config.get('db', 'password')}
            self.properties['db'] = db
            config_info = {'mysql_home': config.get('config', 'mysql_home'),
                           'sql_back_home': config.get('config', 'sql_back_home')}
            self.properties['config'] = config_info
            ftp_info = {'ip': config.get('ftp', 'ip'), 'port': config.get('ftp', 'port'),
                        'username': config.get('ftp', 'username'),
                        'password': config.get('ftp', 'password')}
            self.properties['ftp'] = ftp_info

        except Exception as e:
            raise e
        return self.properties


def main():
    db_info = get_db_info()
    config_info = get_path_config()
    time_path = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    if not os.path.isdir(config_info.sql_back_path):
        os.mkdir(config_info.sql_back_path)

    dump_cmd = config_info.dump_path + "mysqldump -u" + db_info.username + " -p" + db_info.password + " " + db_info.database + " > " + \
               config_info.sql_back_path + "/" + db_info.database + '-' + time_path + ".sql"
    os.system(dump_cmd)
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(2, 1, ftp_upload, (config_info, time_path, db_info,))
    scheduler.run()


def ftp_upload(config_info, time_path, db_info):
    ftp_info = Properties(real_path + '/db.ini').get_properties()['ftp']
    file_back = FileBack(ftp_info['ip'], ftp_info['port'], ftp_info['username'], ftp_info['password'])
    file_back.upload_file(config_info.sql_back_path + "/" + db_info.database + '-' + time_path + ".sql", 'sqlback',
                          db_info.database + '-' + time_path + ".sql")


if __name__ == '__main__':
    main()
