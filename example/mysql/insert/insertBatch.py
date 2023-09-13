import pymysql
import json


# 连接到数据库
def connect_to_database():
    try:
        connection = pymysql.connect(
            host='120.27.202.176',
            user='root',
            password='A910bcOm',
            db='seraphim-exam',
            port=3100
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


# 动态生成SQL语句的方法
def generate_sql(table_name, fields):
    # 构建SQL语句
    sql = f"INSERT INTO {table_name} ({','.join(fields.keys())}) VALUES ({','.join(['%s'] * len(fields))})"
    print(sql)
    return sql


# 示例数据
table_name = "ad_visible_scope"
fields = {
    "id": 4,
    "json_user": '{"name": "John", "age": 30}'
}
# {"deptId": ["d10", "d11"], "roleId": ["r10", "r11"], "userId": ["u10", "u11"]}
# 连接到数据库
connection = connect_to_database()
if connection:
    try:
        with connection.cursor() as cursor:
            # 生成SQL语句
            # for index in range(1000000):
            #     fields = {
            #         "id": index+10,
            #         "json_user": json.dumps({
            #             "deptId": ["d10" + str(index), "d11"],
            #             "roleId": ["r10", "r11"],
            #             "userId": ["u10", "u11"]
            #         })
            #     }
            #     print(fields)
            #     sql = generate_sql(table_name, fields)
            #     # 执行SQL语句
            #     cursor.execute(sql, list(fields.values()))
            #     # 提交事务
            #     connection.commit()
            # 创建一个空列表，用于存储所有的字段字典
            all_fields = []
            for index in range(900000, 1000000):
                fields = {
                    "id": index,
                    "json_user": json.dumps({
                        "deptId": ["d" + str(index), "dd" + str(index)],
                        "roleId": ["r" + str(index), "rr" + str(index)],
                        "userId": ["u" + str(index), "uu" + str(index)]
                    })
                }
                print(index)
                all_fields.append(list(fields.values()))  # 将字段字典的值添加到列表中
            # 执行批量插入操作
            sql = generate_sql(table_name, fields)
            cursor.executemany(sql, all_fields)
            connection.commit()
            print("SQL statement executed successfully.")
    except Exception as e:
        print(f"Error executing SQL statement: {e}")
    finally:
        connection.close()
else:
    print("Failed to connect to the database.")

if __name__ == "__main__":
    table_name = "ad_visible_scope"
    fields = {
        "id": 4,
        "json_user": '{"name": "John", "age": 30}'
    }
    # generate_sql(table_name, fields)
