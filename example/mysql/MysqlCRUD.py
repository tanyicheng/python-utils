# mysql 连接
import pymysql
import yaml


# 同步数据到多个数据库
class MysqlConnect:
    connect = None
    cur = None

    def __init__(self):
        # 创建连接 公共库 dev
        # self.connect = pymysql.connect(
        #     host='172.16.8.62',
        #     user='seraphim',
        #     passwd='seraphim',
        #     database='seraphim_material',
        #     port=3306)

        # 江赛dev
        self.connect = pymysql.connect(
            host='172.16.8.85',
            user='seraphim',
            passwd='seraphim',
            database='seraphim',
            port=3309)

        # 创建游标对象
        self.cur = self.connect.cursor()

    # 读取配置信息，数据库账号密码等
    def readYaml(self):
        # 由于官方提示load方法存在安全漏洞，所以读取文件时会报错。加上warning忽略，就不会显示警告
        yaml.warnings({'YAMLLoadWarning': False})

        # 打开文件
        f = open('conf/mysql.yaml', 'r', encoding='utf-8')
        # 读取
        cfg = f.read()
        # 将数据转换成python字典行驶输出，存在多个文件时，用load_all，单个的时候load就可以
        d = yaml.load(cfg)
        print(d)
        print(d.get('seraphim'))
        print(d.get('seraphim').get('dev').get('database'))


# INSERT INTO `cd_code_list`(`ROW_ID`, `CREATED_BY`, `CREATED_TIME`, `LAST_UPDATE_BY`, `LAST_UPDATE_TIME`, `MODIFICTION`, `IS_VALID`, `CODE_TYPE_ID`, `CODE`, `NAME`, `EN_NAME`, `SHORT_CODE`, `SHORT_NAME`, `NOTES`, `IS_DEFAULT`, `IS_SYSTEM`, `STATUS`, `XH`) VALUES (140792344028988, 162, '2020-05-12 17:32:14', NULL, '0000-00-00 00:00:00', NULL, 'Y', 20, 'SRP-340-BMB-HV', 'SRP-340-BMB-HV', NULL, NULL, NULL, NULL, 'N', 'N', 'Y', NULL);

# 执行语句 fixme 未完善
class Insert:
    def insert(self):
        insertSql = "INSERT INTO `seraphim`.`cd_code_list`(`ROW_ID`, `CREATED_BY`, `CREATED_TIME`, `LAST_UPDATE_BY`, `LAST_UPDATE_TIME`, `MODIFICTION`, `IS_VALID`, `CODE_TYPE_ID`, `CODE`, `EN_NAME`, `NAME`, `SHORT_CODE`, `SHORT_NAME`, `NOTES`, `IS_DEFAULT`, `IS_SYSTEM`, `STATUS`, `XH`) VALUES (140792344029066, 1, now(), NULL, '0000-00-00 00:00:00', NULL, 'Y', 140792027226295, 'mqy123', NULL, 'test', NULL, NULL, '1', 'N', 'N', 'Y', 1);"
        mysql = None
        try:
            mysql = MysqlConnect()
            # mysql.cur.execute(insertSql, ('李四', '18', '95.5'))
            # param = [('李四', '18', '95.5'), ('王五', '28', '65.5')]
            # 查询多条
            mysql.cur.execute(insertSql)
            # mysql.cur.executemany(insertSql, param)
            # 提交事务
            mysql.connect.commit()
            print('执行成功')
        except Exception as e:
            print(e)
            print("执行失败")
            # 出现异常，数据回滚
            mysql.connect.rollback()
        finally:
            # 关闭连接
            mysql.connect.close()


# 创建表
# c = CreateTable()
# c.create()
# 插入数据
# db = Insert()
# db.insert()

m = MysqlConnect()
m.readYaml()
