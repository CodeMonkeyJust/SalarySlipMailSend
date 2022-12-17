# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:邮件发送主GUI窗体
# ------------------------------------------------------------------
from tkinter import *
import hashlib
import time
from tkinter.filedialog import (askopenfilename,
                                askopenfilenames,
                                askdirectory,
                                asksaveasfilename)
from loadexcel import send_by_excel, load_user_mail
from configunit import get_config
from dateunit import get_curdate_last_month
import tkinter.messagebox
import os
from workspace import get_config_filename, init_file

LOG_LINE_NUM = 0
EXCEL_FILE_PATH = ''


class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("工资条发送系统 V2.1.0")  # 窗口名
        # self.init_window_name.geometry('320x160+100+100')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('800x600+10+10')
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        # 阻止Python GUI的大小调整
        self.init_window_name.resizable(0, 0)
        # 窗口图标
        # self.init_window_name.iconbitmap(r".\app.ico")
        # 标签
        self.execl_label = Label(self.init_window_name, text="工资表")
        self.execl_label.grid(row=1, column=0)
        self.excel_entry = Entry(self.init_window_name, width=80)
        self.excel_entry.grid(row=1, column=1)

        self.init_sender_label = Label(self.init_window_name, text="发件人")
        self.init_sender_label.grid(row=2, column=0)
        self.mailsender_label = Label(self.init_window_name,
                                      text=get_config(get_config_filename(), 'send', 'mail_sender'))
        self.mailsender_label.grid(row=2, column=1)

        self.init_yearmonth_label = Label(self.init_window_name, text="邮件标题")
        self.init_yearmonth_label.grid(row=3, column=0)
        self.init_data_label = Label(self.init_window_name, text="签名信息信息一")
        self.init_data_label.grid(row=4, column=0)
        self.init_data_label = Label(self.init_window_name, text="签名信息信息二")
        self.init_data_label.grid(row=5, column=0)
        self.init_data_label = Label(self.init_window_name, text="工资数据")
        self.init_data_label.grid(row=6, column=0)
        self.log_label = Label(self.init_window_name, text="发送结果")
        self.log_label.grid(row=13, column=0)
        # 文本框
        self.data_text = Text(self.init_window_name, width=100, height=18)  # 原始数据录入框
        self.data_text.grid(row=7, column=0, rowspan=5, columnspan=10)
        self.log_data_text = Text(self.init_window_name, width=100, height=18)  # 日志框
        self.log_data_text.grid(row=14, column=0, columnspan=5)

        # 输入框
        self.mailsubject_entry = Entry(self.init_window_name, width=80)
        self.mailsubject_entry.grid(row=3, column=1)
        self.mailsubject_entry.insert(0, get_curdate_last_month() + "工资条-")

        self.mailsign1_entry = Entry(self.init_window_name, width=80)
        self.mailsign1_entry.grid(row=4, column=1)
        self.mailsign1_entry.insert(0, get_config(get_config_filename(), 'send', 'sign1'))

        self.mailsign2_entry = Entry(self.init_window_name, width=80)
        self.mailsign2_entry.grid(row=5, column=1)
        self.mailsign2_entry.insert(0, get_config(get_config_filename(), 'send', 'sign2'))
        # 按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="选择工资表", width=10,
                                              command=self.choose_excel)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=0, column=0)

        self.str_trans_to_md5_button = Button(self.init_window_name, text="发送工资条", width=10,
                                              command=self.send_salary_mail)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=0, column=1)

    def choose_excel(self):
        global EXCEL_FILE_PATH
        EXCEL_FILE_PATH = askopenfilename(title='选择工资表 EXCEL', filetypes=[('XLSX', '*.xlsx'), ('XLS', '*.xls')])
        self.excel_entry.delete(0, END)
        self.excel_entry.insert(0, EXCEL_FILE_PATH)
        # 清空
        self.data_text.delete(1.0, END)
        if os.path.exists(EXCEL_FILE_PATH):
            data = load_user_mail(EXCEL_FILE_PATH)
            for j in range(len(data[0])):
                # print(data[0][j])
                # char(122288)为中文空格，修正Format格式化中文补位问题
                self.data_text.insert(END,
                                      '{0:{2}<10}|\t{1:{2}<10}\n'.format(data[0][j], data[1][j], chr(122288), end=''))

    def send_salary_mail(self):
        if os.path.exists(EXCEL_FILE_PATH):
            self.write_log_to_text('开始发送工资条')
            send_by_excel(EXCEL_FILE_PATH, self.mailsubject_entry.get(), self.mailsign1_entry.get(),
                          self.mailsign2_entry.get())
            self.write_log_to_text('工资条发送完成')
        else:
            tkinter.messagebox.showerror(title='文件错误', message='请选择工资表EXCLE文件，最后一列必须为电子邮件地址！')

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_text.delete(1.0, 2.0)
            self.log_data_text.insert(END, logmsg_in)


def gui_start():
    init_file()
    init_window = Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


if __name__ == '__main__':
    gui_start()
