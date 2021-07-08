from openpyxl import Workbook, load_workbook

# 遍历 excel
wb = load_workbook('./demo.xlsx')
# 默认第一个sheet页
# ws = wb.active
# 选择sheet页
ws = wb.get_sheet_by_name("Sheet1")

def read():
    for row in ws:
        result_row = []
        for cell in row:
            result_row.append(str(cell.value))

        print(result_row)



# 遍历sheet页
def read2():
    # 当前的sheet页
    sheet_g = ''
    # 遍历所有表
    for sheet in wb:
        print("sheet名称："+sheet.title)
        sheet_g = sheet

    # 这里遍历的最后一页
    for row in sheet_g.rows:
        result_row = []
        for cell in row:
            result_row.append(str(cell.value))
        print(result_row)

read2()