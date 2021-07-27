from openpyxl.styles import Font
from openpyxl import Workbook, load_workbook
import os
# from PIL import Image
from openpyxl.drawing.image import Image
from openpyxl.utils import get_column_letter

# Excel 数据合并
path = 'D:/0-seraphim/1需求/表格9/'
fileNames = os.listdir(path)
# 导出的文件名
addr = "example_9.xlsx"
# 创建文件
c_wb = Workbook()
total = len(fileNames)


def read():
    wb = load_workbook(
        'D:/0-seraphim/1需求/表格/SS8810C25-TZ-1_EGLV142151687228_SRP-410-BMA-HV_6002921-C_660PCS_SRP2021.4.5.xlsx')
    # 默认第一个sheet页
    sheet = wb.active
    orderNumber = ''
    containerNo = ''
    # 循环行
    i = 1
    for row in sheet:
        result_row = []
        # 每行的单元格
        j = 1
        for cell in row:
            if (i == 2 and j == 3):
                orderNumber = cell.value
            if (i == 8 and j == 3):
                containerNo = cell.value
            if (i >= 13 and j == 3):
                result_row.append(str(cell.value))
            j += 1

        print(result_row)
        i += 1

    print(orderNumber, containerNo)


def doWork():
    num = 1
    for name in fileNames:
        readCell(name, num)
        num += 1

    c_wb.save(addr)


def readCell(fileName, num):
    print(str(num) + ' ' + path + fileName)
    orderNumber = ''
    containerNo = ''
    barcodes = []
    try:
        wb = load_workbook(path + fileName)
        # 默认第一个sheet页
        sheet = wb.active
        # 获取指定单元格的值
        orderNumber = sheet.cell(2, 3).value
        containerNo = sheet.cell(8, 3).value
        for i in range(13, sheet.max_row):
            val = sheet.cell(i, 3).value
            barcodes.append(val)

    except Exception as e:
        print('出现异常',e)

    create(orderNumber, containerNo, barcodes, num)


def create(orderNumber, containerNo, list, num):
    # 创建一张新表
    c_sheet = c_wb.create_sheet()
    insertImage(c_sheet)
    # sheet = wb.active()
    # 从第一行开始往下3行插入空
    c_sheet.insert_rows(1, 3)
    c_sheet.append(['Seraphim PV Module Serial Numbers for Belectric GmbH under Contract No. DE-TRG-20201030'])
    c_sheet.append([
        'Invoice No.: ' + orderNumber + '      BL No.: SHAHAML07203      Container No.: ' + containerNo + '      PV Module Quantity: 660 PCS/CTN'])

    c_sheet["A5"].font = Font(name="Times New Roman", size=26, bold=True)
    c_sheet["A6"].font = Font(name="Times New Roman", size=24, bold=True)
    # 合并单元格
    c_sheet.merge_cells('A6:F6')
    # 指定位置插入
    c_sheet.cell(row=6, column=7, value='Page ' + str(num) + '/' + str(total))
    c_sheet["G6"].font = Font(name="Times New Roman", size=24, bold=True)

    i,j = 1,7

    line = []
    for barcode in list:
        line.append(barcode)
        if (i % 7 == 0):
            c_sheet.append(line)
            # 设置样式
            for column in range(1,8):
                c_sheet.cell(row=j, column=column).font=Font(name="Times New Roman", size=24)

            line = []
            j+=1
        i += 1


    c_sheet["A6"].font = Font(name="Times New Roman", size=24, bold=True)
    # 设置宽高
    setWidthHeight(c_sheet)


def setWidthHeight(c_sheet):
    # 单列调整列宽
    # ws.column_dimensions['A'].width = 20.0
    # 单行调整行高
    # ws.row_dimensions[1].height = 40
    # 调整行高
    for i in range(1, c_sheet.max_row + 1):
        c_sheet.row_dimensions[i].height = 29
    # 列宽
    for i in range(1, c_sheet.max_column + 1):
        c_sheet.column_dimensions[get_column_letter(i)].width = 42


def insertImage(sheet):
    # fileName = os.path.join(os.getcwd(), './img.png')
    # img = Image.open(path).convert("RGB")
    # sheet.add_image(fileName , 'E1')
    img = Image('./logo.png')
    img.width, img.height = 830, 135
    sheet.add_image(img, 'E1')


def image():
    img = Image('./logo.png')
    img.width, img.height = 830, 140


# image()
doWork()
