# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:INI配置文件读取
# ------------------------------------------------------------------
import configparser
import os
import sys


def get_config(option, item):
    cf = configparser.ConfigParser()
    cf.read(os.path.join(os.path.expanduser('~'), 'conf', 'mail.ini'))
    #cf.read(os.path.join(os.path.dirname(sys.argv[0]), 'conf', 'mail.ini'))
    # print(os.path.join(os.path.dirname(sys.argv[0]), 'conf', 'mail.ini'))
    print(os.path.expanduser('~'))
    return (cf.get(option, item))


if __name__ == '__main__':
    print(get_config('send', 'mail_host'))
