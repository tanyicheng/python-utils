import pymysql


class MysqlUtils:
    connect = None
    cur = None

    def __init__(self):
        # 创建连接
        self.connect = pymysql.connect(
            host='192.168.91.100',
            user='root',
            passwd='123456',
            database='jeecg-boot',
            port=3306)

        # 创建游标对象
        self.cur = self.connect.cursor()

    # 查询所有字段
    def list_col(self, tabls_name):
        # db = pymysql.connect(localhost, username, password, database, charset="utf8")
        # cursor = db.cursor()
        self.cur.execute("select * from %s" % tabls_name)
        col_name_list = [tuple[0] for tuple in self.cur.description]
        self.connect.close()
        return col_name_list


db = MysqlUtils()
table = db.list_col('sys_user')
print(table)
