f = lambda a, b, c: a + b + c


def test(a, b, c):
    return a + b + c


# 以上2种方式一样的结果
print(f(1, 2, 3))
print(test(1, 2, 3))

# 定义一个元组，2个表达是，入参:执行逻辑
g = [lambda a: a * 2, lambda b: b * 3]

# 给第一个表达式传递值6
print(g[0](6))

# 函数也是对象
h = [test, test]
print(h[0](2, 3, 4))
