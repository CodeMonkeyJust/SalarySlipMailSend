# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:日志单元
# ------------------------------------------------------------------
import time


def write_log(log_filename, msg):
    fp = open(log_filename, "a", encoding="utf-8")
    fp.write(get_current_time() + ':' + str(msg) + '\n')
    fp.close()


def load_log(log_filename):
    fp = open(log_filename, "r", encoding="utf-8")
    data = fp.read()
    fp.close()
    return data


# 获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time
