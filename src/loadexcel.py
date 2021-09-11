# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:读取工资EXCEL并调用邮件发送
# ------------------------------------------------------------------
import xlrd
from sendmail import sendmail
from makecontent import load_css, load_sign

HEAD_ROW_COUNT = 1


def load_user_mail(file_path):
    # 打开文件
    wb = xlrd.open_workbook(file_path)
    # 获取所有sheet的名字
    # print(wb.sheet_names())
    # 获取第二个sheet的表明
    # sheet2 = wb.sheet_names()[0]
    # sheet1索引从0开始，得到sheet1表的句柄
    sheet1 = wb.sheet_by_index(0)
    rowNum = sheet1.nrows
    colNum = sheet1.ncols
    data = [sheet1.col_values(1), sheet1.col_values(colNum - 1)]
    # print(data)
    return data


def send_by_excel(file_path, subject_head):
    # 打开文件
    wb = xlrd.open_workbook(file_path)
    # 获取所有sheet的名字
    # print(wb.sheet_names())
    # 获取第二个sheet的表明
    # sheet2 = wb.sheet_names()[0]
    # sheet1索引从0开始，得到sheet1表的句柄
    sheet1 = wb.sheet_by_index(0)
    rowNum = sheet1.nrows
    # print(rowNum)
    colNum = sheet1.ncols
    # print(colNum)
    # 表格Title
    table_head = []
    for c in range(colNum):
        table_head.append(sheet1.cell(0, c).value)
    for r in range(1, HEAD_ROW_COUNT):
        for c in range(colNum):
            if table_head[c] != '':
                table_head[c] = table_head[c] + '-' + sheet1.cell(r, c).value
            else:
                table_head[c] = sheet1.cell(r, c).value
    # 读取内容
    for r in range(HEAD_ROW_COUNT, rowNum):
        html_table = load_css() + '<table border="1">\n'
        for c in range(1, colNum - 1):
            if sheet1.cell(r, c).ctype == 2:
                cellval = '%.2f' % sheet1.cell(r, c).value
            else:
                cellval = sheet1.cell(r, c).value
            html_table = html_table + '<tr>' + '<td>' + table_head[c] + '</td>' + '<td>' + cellval + '</td>' + '</tr>'

            html_table = html_table + '\n'
        html_table = html_table + load_sign()
        html_table = html_table + '\n</table>'
        subject = subject_head + '工资表-' + sheet1.cell(r, 1).value
        receivers = [sheet1.cell(r, colNum - 1).value]
        content = html_table
        # print(html_table)
        sendmail(subject, content, receivers)
        # print(subject + str(receivers))


if __name__ == '__main__':
    send_by_excel(r'demo/test.xlsx')
