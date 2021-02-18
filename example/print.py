# 第一种方式写数据到文件
fp = open('E:\Temp\pythonText.txt', 'w')

print('奋斗成就更好的你', file=fp)
fp.close()
