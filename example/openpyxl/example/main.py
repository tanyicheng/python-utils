# coding=utf-8
import xlrd
import xlsxwriter
from pathlib import Path, PurePath
import time

# Excel 数据合并

def add():
    print("12313232312312")


def work(path):
    # 指定Excel源目录
    src_path = path  # 'D:/0-seraphim/1需求/表格9'

    localtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    # 指定合并完成的目录
    dst_file = 'summary'+localtime+'.xlsx'

    # 取的该目录下所有xlsx格式的文件
    p = Path(src_path)
    files = [x for x in p.iterdir() if PurePath(x).match('*.xlsx')]

    # 准备一个列表存放读取的结果
    barcodes = []

    # workbook = xlwt.Workbook(encoding='utf-8')
    workbook = xlsxwriter.Workbook(dst_file)

    format1 = workbook.add_format({
        'font_name': 'Times New Roman',
        'font_size': 24,
    })

    format2 = workbook.add_format({
        'font_name': 'Times New Roman',
        'font_size': 26,
        'bold': True
    })

    format3 = workbook.add_format({
        'font_name': 'Times New Roman',
        'font_size': 24,
        'border': 1
    })

    # 对每一个文件进行处理
    for i, f in enumerate(files):
        try:
            data = xlrd.open_workbook(filename=f)
        except Exception as e:
            print("读取失败：", e)
        else:
            barcodes = []
            table = data.sheets()[0]
            # 读取订单号
            order_no = table.cell_value(rowx=1, colx=2)
            # 读取箱号
            container_no = table.cell_value(rowx=7, colx=2)
            # 生成当前页码
            page = "Page %s/%s" % (i + 1, len(files))

            block1 = "Seraphim PV Module Serial Numbers for Belectric GmbH under Contract No. DE-TRG-20201030"
            block2 = "Invoice No.: %s      BL No.:       Container No.:%s      PV Module Quantity: 660 PCS/CTN" % (
                order_no, container_no)

            # 读取条码
            start_row = 12
            barcode = table.cell_value(rowx=start_row, colx=2)
            while barcode != '':
                barcode = table.cell_value(rowx=start_row, colx=2)
                barcodes.append(barcode)
                start_row = start_row + 1

            # 写入sheet
            # 设置样式
            sheet_name = "sheet%s" % (i + 1)
            sheet = workbook.add_worksheet(sheet_name)
            sheet.set_row(0, 21)
            sheet.set_row(1, 21)
            sheet.set_row(2, 22)
            sheet.set_row(3, 22)
            sheet.set_column('A:A', 46)
            sheet.set_column('B:B', 46)
            sheet.set_column('C:C', 46)
            sheet.set_column('D:D', 46)
            sheet.set_column('E:E', 46)
            sheet.set_column('F:F', 46)
            sheet.set_column('G:G', 46)
            # 写入logo
            sheet.insert_image('E1', 'logo.png')
            # 写入block1
            sheet.write(4, 0, block1, format2)
            # 写入block2
            sheet.merge_range(5, 0, 5, 5, block2, format1)
            # 写入page
            sheet.write(5, 6, page, format1)
            # 写入barcode
            barcode_start_row = 6
            barcode_start_col = 0
            for i, bc in enumerate(barcodes):
                if i > 0 and i % 7 == 0:
                    barcode_start_row = barcode_start_row + 1
                    barcode_start_col = 0
                sheet.write(barcode_start_row, barcode_start_col, bc, format3)
                barcode_start_col = barcode_start_col + 1

    # 写入汇总文件
    workbook.close()
    return dst_file

# work("D:/0-seraphim/1需求/表格9")