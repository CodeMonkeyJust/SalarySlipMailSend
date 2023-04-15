# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:日期处理
# ------------------------------------------------------------------
import datetime
import time

def get_specdate_last_month(specdate):
    # 获取「今天」
    # today = datetime.date.today()
    # 获取当前月的第一天
    first = specdate.replace(day=1)
    # 减一天，得到上个月的最后一天
    last_month = first - datetime.timedelta(days=1)
    return last_month.strftime("%Y%m")


def get_curdate_last_month():
    return get_specdate_last_month(datetime.date.today())

def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time

if __name__ == '__main__':
    print(get_curdate_last_month())
