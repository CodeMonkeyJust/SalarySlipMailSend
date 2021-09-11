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


def load_sign():
    sign = ("<tr><td colspan='2'>工资条内容保密，请勿外泄！</td></tr> \n"
            "<tr><td colspan='2'>本邮箱仅作为工资条发送使用，请勿回复！如有疑问，请联系综合部负责人!</td></tr> \n")
    return  sign
