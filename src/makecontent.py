# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:工资条格式
# ------------------------------------------------------------------
def load_css():
    css = ("<style type='text/css'> \n"
           "body,table{ font-size:12px;} \n"
           "table{table-layout:fixed; empty-cells:show; border-collapse: collapse;margin:0 auto; border:1px solid #cad9ea;color:#666;} \n"
           "td{border:1px solid #cad9ea;} \n"
           "</style>\n")
    return css


def load_sign(sign1, sign2):
    sign = ("<tr><td colspan='2'>" + sign1 + "</td></tr> \n"
                                             "<tr><td colspan='2'>" + sign2 + "</td></tr> \n")
    return sign
