url = 'https://www2.autoimg.cn/newsdfs/g21/M0B/C7/84/120x90_0_autohomecar__ChsEvGA4qVCANo_QAACJlKdI0Vc583.jpg'


def str1():
    start = url.rindex('/')
    name = url[start + 1:]
    print(name)


def str2():
    name= url.split('/')[-1]
    print(name)


str2()
