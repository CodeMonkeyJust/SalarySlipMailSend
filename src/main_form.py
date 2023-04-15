# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:邮件发送主GUI窗体
# ------------------------------------------------------------------
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, messagebox
import time
from tkinter.filedialog import (askopenfilename,
                                askopenfilenames,
                                askdirectory,
                                asksaveasfilename)
from loadexcel import send_by_excel, load_user_mail
from config_unit import get_config
from date_unit import get_curdate_last_month
import tkinter.messagebox
import os
from workspace import get_config_filename, init_file

LOG_LINE_NUM = 0
EXCEL_FILE_PATH = ''


class WindowsMain(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__()
        init_file()
        # 全局变量
        self.VER = 'V3.0.0'
        self.init_form()
        self.load_default_config
        self.mainloop()

    # 设置窗口
    def init_form(self):
        # setting title
        self.title("工资条发送工具 " + self.VER)
        # setting window size
        width = 800
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        # 菜单，MacOS下根菜单不显示，所以不使用根菜单
        menu_main = tk.Menu(self)
        menu_file = tk.Menu(menu_main, tearoff=False)
        menu_file.add_command(label='选择工资表', command=self.choose_excel)
        # menu_file.add_command(label='选择图像', command=self.button_choose_image_dir_command)
        # 添加一条分割线
        menu_file.add_separator()
        menu_file.add_command(label="退出", command=self.destroy)
        menu_main.add_cascade(label='文件', menu=menu_file)
        menu_help = tk.Menu(menu_main, tearoff=False)
        menu_help.add_command(label='关于', command=self.show_about_author)
        menu_main.add_cascade(label='帮助', menu=menu_help)
        self.config(menu=menu_main)

        # 工资表
        label_execl = tk.Label(self, text="工资表:")
        label_execl["justify"] = "right"
        label_execl.place(x=20, y=20, width=90, height=30)

        self.entry_excel = tk.Entry(self, width=80)
        self.entry_excel["justify"] = "right"
        self.entry_excel.place(x=130, y=20, width=460, height=30)

        self.str_trans_to_md5_button = tk.Button(self, text="...", width=10,
                                                 command=self.choose_excel)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.place(x=600, y=20, width=40, height=30)

        self.str_trans_to_md5_button = tk.Button(self, text="发送工资条", width=10,
                                                 command=self.send_salary_mail)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.place(x=660, y=20, width=100, height=30)

        # 发件人
        init_sender_label = tk.Label(self)
        init_sender_label["text"] = "发件人："
        init_sender_label["justify"] = "right"
        init_sender_label.place(x=20, y=60, width=90, height=30)
        self.mailsender_label = tk.Label(self,
                                         text=get_config(get_config_filename(), 'send', 'mail_sender'))
        self.mailsender_label.place(x=130, y=60, width=630, height=30)

        init_yearmonth_label = tk.Label(self)
        init_yearmonth_label["text"] = "邮件标题："
        init_yearmonth_label["justify"] = "right"
        init_yearmonth_label.place(x=20, y=100, width=90, height=30)
        self.mailsubject_entry = tk.Entry(self,)
        self.mailsubject_entry.place(x=130, y=100, width=630, height=30)
        self.mailsubject_entry.insert(0, get_curdate_last_month() + "工资条-")

        label_mailsign1 = tk.Label(self, text="签名一：")
        label_mailsign1["justify"] = "right"
        label_mailsign1.place(x=20, y=140, width=90, height=30)
        self.entry_mailsign1 = tk.Entry(self)
        self.entry_mailsign1.place(x=130, y=140, width=630, height=30)

        label_mailsign2 = tk.Label(self, text="签名二：")
        label_mailsign2["justify"] = "right"
        label_mailsign2.place(x=20, y=180, width=90, height=30)
        self.entry_mailsign2 = tk.Entry(self)
        self.entry_mailsign2.place(x=130, y=180, width=630, height=30)

        init_data_label = tk.Label(self, text="工资数据：")
        init_data_label["justify"] = "right"
        init_data_label.place(x=20, y=220, width=90, height=30)
        self.data_text = tk.Text(self )  # 原始数据录入框
        self.data_text.place(x=130, y=220, width=630, height=200)
        #
        log_label = tk.Label(self, text="发送结果：")
        log_label["justify"] = "right"
        log_label.place(x=20, y=430, width=90, height=30)
        self.log_data_text = tk.Text(self)  # 日志框
        self.log_data_text.place(x=130, y=430, width=630, height=100)


    def load_default_config(self):
        self.mailsign1_entry.insert(0, get_config(get_config_filename(), 'send', 'sign1'))
        self.mailsign2_entry.insert(0, get_config(get_config_filename(), 'send', 'sign2'))

    def choose_excel(self):
        global EXCEL_FILE_PATH
        EXCEL_FILE_PATH = askopenfilename(title='选择工资表 EXCEL', filetypes=[('XLSX', '*.xlsx'), ('XLS', '*.xls')])
        self.excel_entry.delete(0, tk.END)
        self.excel_entry.insert(0, EXCEL_FILE_PATH)
        # 清空
        self.data_text.delete(1.0, tk.END)
        if os.path.exists(EXCEL_FILE_PATH):
            data = load_user_mail(EXCEL_FILE_PATH)
            for j in range(len(data[0])):
                # print(data[0][j])
                # char(122288)为中文空格，修正Format格式化中文补位问题
                self.data_text.insert(tk.END,
                                      '{0:{2}<10}|\t{1:{2}<10}\n'.format(data[0][j], data[1][j], chr(122288), end=''))

    def send_salary_mail(self):
        if os.path.exists(EXCEL_FILE_PATH):
            self.write_log_to_text('开始发送工资条')
            send_by_excel(EXCEL_FILE_PATH, self.mailsubject_entry.get(), self.mailsign1_entry.get(),
                          self.mailsign2_entry.get())
            self.write_log_to_text('工资条发送完成')
        else:
            tkinter.messagebox.showerror(title='文件错误', message='请选择工资表EXCLE文件，最后一列必须为电子邮件地址！')

    # 日志动态打印
    def write_log_to_text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_text.insert(tk.END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_text.delete(1.0, 2.0)
            self.log_data_text.insert(tk.END, logmsg_in)

    def show_about_author(self):
        messagebox.showinfo('关于', '工资条发送工具.\n\rzlj20@163.com\n\r' + self.VER)


def gui_start():
    gwindowsMain = WindowsMain()


if __name__ == '__main__':
    gui_start()
