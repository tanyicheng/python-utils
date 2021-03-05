class Student:
    #定义属性
    add = "http://www.baidu.com"

    #构造函数
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #定义普通方法
    def say(self,content):
        print(content)


    def printScore(self):
        print('{0},{1}'.format(self.name,self.age))


stu = Student("snipe",18)
stu.address="江苏省"
stu.say("hello")
stu.printScore()
print(stu.address)

print(dir(stu))
