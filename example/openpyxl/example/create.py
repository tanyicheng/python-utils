import datetime
from random import choice
from time import time
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

# 设置文件 mingc
addr = "example.xlsx"
# 打开文件
# wb = load_workbook(addr)
wb = Workbook()
# 创建一张新表
sheet = wb.create_sheet()
# sheet = wb.active()
# 第一行输入
sheet.insert_rows(1, 4)
sheet.append(['Seraphim PV Module Serial Numbers for Belectric GmbH under Contract No. DE-TRG-20201030'])
sheet.append(['Invoice No.: WB8810C25-TZ-01      BL No.: SHAHAML07203      Container No.: EGHU9593717      PV Module Quantity: 660 PCS/CTN'])

# 输入内容（500行数据）
for i in range(10):
    barcodes = []
    for j in range(10):
        barcodes.append(str(j) + 'abc')

    sheet.append(barcodes)

# 获取最大行
row_max = sheet.max_row
# 获取最大列
con_max = sheet.max_column
# 把上面写入内容打印在控制台
for j in sheet.rows:  # we.rows 获取每一行数据
    for n in j:
        print(n.value, end="\t")  # n.value 获取单元格的值
    print()
# 保存，save（必须要写文件名（绝对地址）默认 py 同级目录下，只支持 xlsx 格式）

wb.save(addr)
