# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:路径操作单元
# ------------------------------------------------------------------
import os


def path_create(path):
    if not os.path.exists(path):
        os.mkdir(path)
