# -*- encoding=utf-8 -*-
__author__ = "Moltapy"

from ControlForm import *

# Handle Functions
## open directory
def open_directory(args):
    directory_path = filedialog.askdirectory()
    if directory_path:
        if os.path.isdir(directory_path):
            if args:
                args.set(directory_path)
            else:
                messagebox.showerror("错误","请设置回调函数的返回对象")
        else:
            messagebox.showerror("错误","文件夹无效")
## open subwindow
def open_subwindow(basedwindow,width,height,title):
    subwindow = SubWindowForm(title=title,upwindow=basedwindow)
    subwindow.setwindow(width=width,height=height)
    return subwindow