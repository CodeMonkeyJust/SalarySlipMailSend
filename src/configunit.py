# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:INI配置文件读取
# ------------------------------------------------------------------
import configparser


def get_config(config_filename, section, item):
    cf = configparser.ConfigParser()
    cf.read(config_filename)
    if not cf.has_section(section):
        cf.add_section(section)
    if not cf.has_option(section, item):
        cf.set(section, item, "")
        cf.write(open(config_filename, 'w'))
    return (cf.get(section, item))
