# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:日志单元
# ------------------------------------------------------------------
import time
import os
import sys


def get_log_file_name():
    curent_date = time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    return os.path.join(os.path.expanduser('~'), 'log', curent_date)


def write_log(log_file_name, msg):
    fp = open(log_file_name, "a", encoding="utf-8")
    fp.write(get_current_time() + ':' + str(msg) + '\n')
    fp.close()


def load_log(log_file_name):
    fp = open(log_file_name, "r", encoding="utf-8")
    data = fp.read()
    fp.close()
    return data


# 获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time


if __name__ == '__main__':
    print(get_log_file_name())
