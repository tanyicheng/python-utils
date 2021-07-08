from openpyxl import Workbook, load_workbook
import os

path = 'D:/0-seraphim/1需求/表格/'
fileNames = os.listdir(path)
# 设置文件名
addr = "example.xlsx"
# 创建文件
c_wb = Workbook()
total = len(fileNames)

def read():
    wb = load_workbook('D:/0-seraphim/1需求/表格/SS8810C25-TZ-1_EGLV142151687228_SRP-410-BMA-HV_6002921-C_660PCS_SRP2021.4.5.xlsx')
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
    num=1
    for name in fileNames:
        readCell(name,num)
        num+=1

    c_wb.save(addr)

def readCell(fileName,num):
    print(path+fileName)
    wb = load_workbook(path+fileName)
    # 默认第一个sheet页
    sheet = wb.active
    # 获取指定单元格的值
    orderNumber = sheet.cell(2, 3).value
    containerNo = sheet.cell(8, 3).value
    barcodes = []
    for i in range(13, sheet.max_row):
        val = sheet.cell(i, 3).value
        barcodes.append(val)

    # print(barcodes)
    create(orderNumber, containerNo, barcodes,num)


def create(orderNumber, containerNo, list,num):
    # 创建一张新表
    c_sheet = c_wb.create_sheet()
    # sheet = wb.active()
    # 从第一行开始往下3行插入空
    c_sheet.insert_rows(1, 3)
    c_sheet.append(['Seraphim PV Module Serial Numbers for Belectric GmbH under Contract No. DE-TRG-20201030'])
    c_sheet.append([
        'Invoice No.: ' + orderNumber + '      BL No.: SHAHAML07203      Container No.: ' + containerNo + '      PV Module Quantity: 660 PCS/CTN'])
    # 合并单元格
    c_sheet.merge_cells('A6:F6')
    # 指定位置插入
    c_sheet.cell(row=6, column=7, value='Page '+str(num)+'/'+str(total))

    i = 1
    line = []
    for barcode in list:
        line.append(barcode)
        if (i % 7 == 0):
            c_sheet.append(line)
            line = []
        i += 1



doWork()
# read()
