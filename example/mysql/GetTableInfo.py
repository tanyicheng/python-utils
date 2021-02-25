import pymysql


# 获取数据库表字段以及注释（支持所有表）
class GetMysqlTableComments():
    def __init__(self, host, user, password, database, port, charset):
        self.db = pymysql.connect(host=host, user=user, password=password, port=port, database=database,
                                  charset=charset)
        self.cursor = self.db.cursor()

    # 获取所有表结构
    def get_tables(self, database_name):
        sqlstr = ''
        # 查询mysql表名和注释
        self.cursor.execute(
            'select table_name,table_comment from information_schema.TABLES where TABLE_SCHEMA=%s order by table_name',
            database_name)
        return_tables = self.cursor.fetchall()
        for tabledata in return_tables:
            return_columns = self.get_columns(tabledata[0])
            sqlstr += '\n-- ' + tabledata[1] + '\n'  # 表注释
            sqlstr += 'select\n' + return_columns + '\n from ' + tabledata[0] + ';\n'
        return sqlstr

    # 获取指定表结构信息
    def get_columns(self, table_name):
        # 查询mysql表字段注释
        self.cursor.execute('select column_name,column_comment from information_schema.COLUMNS where TABLE_NAME=%s',
                            table_name)
        return_columns = self.cursor.fetchall()
        columnstr = ''
        for columndata in return_columns:
            # 列名加上`是为了防止列名使用了mysql关键字时会报sql语法错误
            columnstr = columnstr + "`" + columndata[0] + "`"
            if columndata[1].strip() != '':
                # 若表字段注释里含有:、-、,、空格等符号，会报sql语法错误，可以使用replace函数替换特殊符号。程序自动改虽然方便，但是注释可读性不太好，建议手动修改。
                comment = columndata[1].replace('-', '')
                comment = comment.replace(':', '，')
                comment = comment.replace(',', '，')
                comment = comment.replace(' ', '，')
                comment = comment.replace('=', '，')
                comment = comment.replace('(', '（')
                comment = comment.replace(')', '）')
                comment = comment.replace('[', '（')
                comment = comment.replace(']', '）')
                comment = comment.replace('|', '、')
                comment = comment.replace('"', '')
                comment = comment.replace('.', '、')
                comment = comment.replace('/', '、')
                comment = comment.replace('{', '（')
                comment = comment.replace('}', '）')
                comment = comment.replace('?', '？')
                # 若发现其它符号引起的sql语法错误，自己继续补充即可
                columnstr = columnstr + ' as ' + comment
            columnstr += ',\n'
        # 去掉最后一列的逗号和换行符
        return columnstr[:-2]

    def closedb(self):
        self.cursor.close()
        # 关闭数据库
        self.db.close()

    # 查询数据库中所有表是否包含某个字段（例如：查看所有表是否包含 tenant_id 字段，返回存在的表名）
    def filter_tables(self, database_name,str):
        sqlstr = ''
        # 查询mysql表名和注释
        self.cursor.execute(
            'select table_name,table_comment from information_schema.TABLES where TABLE_SCHEMA=%s order by table_name',
            database_name)
        return_tables = self.cursor.fetchall()
        for tabledata in return_tables:
            return_columns = self.filter_columns(tabledata[0],str)
            # sqlstr += '\n-- ' + tabledata[1] + '\n'
            if return_columns != '':
                sqlstr += tabledata[0] + '\n'

        return sqlstr

    # 获取指定表结构信息
    def filter_columns(self, table_name,str):
        # 查询mysql表字段注释
        self.cursor.execute('select column_name,column_comment from information_schema.COLUMNS where TABLE_NAME=%s',
                            table_name)
        return_columns = self.cursor.fetchall()
        columnstr = ''
        flag = 0;
        for columndata in return_columns:
            # 列名加上`是为了防止列名使用了mysql关键字时会报sql语法错误
            columnstr += columndata[0]
            columnstr += ',\n'
            if columndata[0] == str:
                flag = 1

        if flag == 1:
            return columnstr
        else:
            # 去掉最后一列的逗号和换行符
            return ''


if __name__ == '__main__':
    # 数据库地址
    host = '192.168.91.100'
    # 数据库端口
    port = 3306
    # 数据库用户名
    user = 'root'
    # 密码
    password = '123456'
    # 数据库名称
    database = 'jeecg-boot'
    # 字符集
    charset = 'utf8'
    my_database = GetMysqlTableComments(host, user, password, database, port, charset)
    # 获取所有表结构和注释
    # sqlstr = my_database.get_tables(database)
    # 根据表获取结构和注释
    # sqlstr = my_database.get_columns('sys_user')

    sqlstr = my_database.filter_tables(database,'tenant_id')

    my_database.closedb()
    # 生成的sql打印到控制台
    print(sqlstr)
    # 生成的sql保存到文件
    file_path = 'table.sql'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(sqlstr)
