import fire


# fire是python中用于生成命令行界面(Command Line Interfaces, CLIs)的工具，不需要做任何额外的工作，只需要从主模块中调用fire.Fire()，
# 它会自动将你的代码转化为CLI，Fire()的参数可以说任何的python对象
class Calculator:
    def add(self, a, b):
        count = a + b
        return count

    def sub(self, a, b):
        result = a - b
        return result


class Test:
    def test(self, a, b):
        result = a * b
        return result


# 判断是否是主函数 print(__name__)
if __name__ == '__main__':
    # 指定类对象
    fire.Fire(Calculator)

# > python3 test01.py add 7 8
