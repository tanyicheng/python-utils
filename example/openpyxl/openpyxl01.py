from openpyxl import Workbook
import datetime

# 实例化
wb = Workbook()
# 激活 worksheet
ws = wb.active

from openpyxl import load_workbook

# 打开已有文件
# wb2 = load_workbook('D:\logs\example.xlsx')

# 存储数据
# 方式一：数据可以直接分配到单元格中(可以输入公式)
ws['A1'] = 42
# 方式二：可以附加行，从第一列开始附加(从最下方空白处，最左开始)(可以输入多行)
ws.append([1, 2, 3])
# 方式三：Python 类型会被自动转换
ws['A3'] = datetime.datetime.now().strftime("%Y-%m-%d")

# 创建表（sheet）
# 方式一：插入到最后(default)
# ws1 = wb.create_sheet("Mysheet")
# 方式二：插入到最开始的位置
# ws2 = wb.create_sheet("Mysheet", 0)

# 选择表（sheet）
# sheet 名称可以作为 key 进行索引
# ws3 = wb["New Title"]
# ws4 = wb.get_sheet_by_name("New Title")
# ws is ws3 is ws4
# 输出 True

# 显示所有表名（sheet）
print(wb.sheetnames)
sheet_g = ''
# 遍历所有表
for sheet in wb:
    print(sheet.title)
    sheet_g = sheet


for row in sheet_g.rows:
    for cell in row:
        print(cell.value)

# 保存
# wb.save('demo2.xlsx')
