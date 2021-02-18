import fire


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

# > test01.py add 8 6
