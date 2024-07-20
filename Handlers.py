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
def open_subwindow(basedwindow,width,height,title,window_varname:str):
    exec(f"global {window_varname}")
    subwindow = SubWindowForm(title=title,upwindow=basedwindow)
    subwindow.setwindow(width=width,height=height)
    exec(f"{window_varname} = subwindow")

## check directory
def check_directory(label):
    if not os.path.isdir(label.string.get()):
         messagebox.showerror("错误","请先选择资源文件夹")
    else:
        os.startfile(label.string.get())

## show search results

def combine_filename(*args):
    if len(args) == 2:
        filename = f"{Mapping[args[0].string.get()]}_{args[1].string.get()}"
    else:
        filename ="error"
    return filename


def search_out(*args):
    