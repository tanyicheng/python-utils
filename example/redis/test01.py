import redis


class RedisConnect:
    # redis连接
    redisCon = None

    def __init__(self, host, port, password):
        self.redisCon = redis.Redis(host=host, port=port, password=password)

    # 清空所有key
    def del_all(self):
        for key in self.redisCon.keys():
            self.redisCon.delete(key)

    # map形式保存 (key,属性,value)
    def set_hash_map(self, key, id, val):
        self.redisCon.hset(key, id, val)

    def set_data(self, key, val):
        self.redisCon.set(key, val)

    # 获取hashmap形式的key
    def get_hash_map(self, key, id):
        val = self.redisCon.hget(key, id)
        print(val.decode('utf-8'))

    def get_data(self, key):
        val = self.redisCon.get(key)
        print(val.decode('utf-8'))


redis = RedisConnect('172.16.8.63', 6379, 'redis@2019')

# redis.set_hash_map('name', 1, '张三')
# redis.get_hash_map('name', 1)
# redis.set_data("abc", '阿斯蒂芬')
# redis.get_data('abc')

# redis.del_all()