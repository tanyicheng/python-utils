# mysql 连接
import pymysql


class MysqlConnect:
    connect = None
    cur = None

    def __init__(self):
        # 创建连接
        self.connect = pymysql.connect(
            host='172.16.8.62',
            user='seraphim',
            passwd='seraphim',
            database='barrett',
            port=3306)

        # 创建游标对象
        self.cur = self.connect.cursor()


# 注意创建数据时要指定字符编码
# 如果为指定utf8，无法插入中文，另外执行：alter database barrett character set utf8 collate utf8_general_ci;
class CreateTable:

    def create(self):
        # 测试连接
        # print(con)
        # 创建表
        createTableSql = '''
        create table t_student(
            sno int primary  key auto_increment,
            sname varchar(30) not null,
            age int(2) ,
            score float(3,1) 
        )
        '''

        mysql = None
        try:
            mysql = MysqlConnect()
            mysql.cur.execute(createTableSql)
            print('执行成功')
        except Exception as e:
            print(e)
            print("执行失败")
        finally:
            # 关闭连接
            mysql.connect.close()


class Insert:
    def insert(self):
        insertSql = '''
            insert into t_student(sname,age,score)values(%s,%s,%s)
            '''
        mysql = None
        try:
            mysql = MysqlConnect()
            # mysql.cur.execute(insertSql, ('李四', '18', '95.5'))
            param = [('李四', '18', '95.5'), ('王五', '28', '65.5')]
            # 查询多条
            mysql.cur.executemany(insertSql, param)
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


class SearchAll:
    def searchAll(self):
        sql = '''
            select * from t_student
            '''
        mysql = None
        try:
            mysql = MysqlConnect()
            cur = mysql.cur
            cur.execute(sql)
            # 处理结果集
            lists = cur.fetchall()
            # print(lists)
            for stu in lists:
                print("{0},{1},{2}".format(stu[0], stu[1], stu[2]))
        except Exception as e:
            print(e)
            print("执行失败")
        finally:
            # 关闭连接
            mysql.connect.close()

    def searchOne(self):
        sql = '''
            select * from t_student where sno=1
            '''
        mysql = None
        try:
            mysql = MysqlConnect()
            cur = mysql.cur
            cur.execute(sql)
            # 处理结果集
            stu = cur.fetchone()
            print(stu)
        except Exception as e:
            print(e)
            print("执行失败")
        finally:
            # 关闭连接
            mysql.connect.close()


class Update:
    def updateOrDelete(self):
        sql = '''
            update t_student set sname=%s where sno=%s
            '''
        delSql = '''
            delete from t_student where sno = %s
        '''
        mysql = None
        try:
            mysql = MysqlConnect()
            cur = mysql.cur
            param = 5
            # cur.execute(sql, param)
            cur.execute(delSql, param)

            # 提交事务
            mysql.connect.commit()
            print('操作成功')
        except Exception as e:
            print(e)
            print("执行失败")
        finally:
            # 关闭连接
            mysql.connect.close()


# 创建表
# c = CreateTable()
# c.create()
# 插入数据
# db = Insert()
# db.insert()
# 查询所有数据
db = SearchAll()
db.searchOne()
# db = Update()
# db.updateOrDelete()
