# 单例模式

class Singleton:
    __obj = None  # 类属性
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if (cls.__obj == None):
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        #增加初始化的标记，使对象只会初始化一次
        if self.__init_flag:
            print('对象初始化...')
            self.name = name
            self.__init_flag = False


a = Singleton("aa")
b = Singleton("bb")

print(a)
print(b)
