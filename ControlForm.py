# -*- encoding=utf-8 -*-
__author__ = "Moltapy"

# Modules
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from airtest.core.api import *
from PIL import Image, ImageTk

import os
import shutil
import win32gui
import subprocess

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator

import numpy as np

import ctypes

# Global Vars
Simulation_Mode = {"mode": None, "condition": None}
Mapping = {"祝者": "chara", "陨星之忆": "weapon"}
Rarity = {"辰级": "third-rarity", "星级": "forth-rarity", "月级": "fifth-rarity", "日级": "sixth-rarity"}
Dirname = os.path.dirname(__file__)
Threads = None
Process = None


# Classes
## Main_Window
class WindowForm(tk.Frame):
    def __init__(self, title: str,master=None):
        super().__init__(master)
        self.master = master
        self.settitle(title=title)
        self.setposition(0,0,1,1)
        

    def setwindow(self, width, height):
        self.master.geometry(f"{width}x{height}")

    def settitle(self,title):
        self.master.title(title)

    def setposition(self,x,y,h,w):
        self.place(relx=x,rely=y,relheight=h,relwidth=w)

## Sub_Window
class SubWindowForm(tk.Frame):
    def __init__(self, title: str, upwindow): 
        self.master = tk.Toplevel(upwindow.master)
        super().__init__(self.master)
        self.settitle(title=title)
        self.setposition(0,0,1,1)
        

    def setwindow(self, width, height):
        self.master.geometry(f"{width}x{height}")

    def settitle(self,title):
        self.master.title(title)

    def setposition(self,x,y,h,w):
        self.place(relx=x,rely=y,relheight=h,relwidth=w)


## Labels
class LabelForm:
    def __init__(self, content: str, window_belong):
        self.string = tk.StringVar(window_belong)
        self.string.set(content)
        self.root = tk.Label(window_belong, textvariable=self.string, padx=10, pady=10)
    # use relative position directly

    def place(self, x, y, width, height):
        self.root.place(relx=x, rely=y, relwidth=width, relheight=height)

class BackgroundLabel:
    def __init__(self,content:str,window_belong):
        self.content_path = os.path.join(Dirname,content)
        self.belong_window = window_belong
        self.bkgd_object = self.process_picture(content)
        self.root = tk.Label(window_belong,image= self.bkgd_object)
       
    def process_picture(self,origin_path,alpha = 128):
        origin_image = Image.open(origin_path).convert('RGBA')
        origin_image.putalpha(alpha)
        resized_image = origin_image.resize((self.belong_window.winfo_screenwidth(),self.belong_window.winfo_screenheight()),Image.Resampling.LANCZOS)
        processed_image = ImageTk.PhotoImage(resized_image)
        return processed_image
    
    def place(self,x,y,height,width):
         self.root.place(relx=x, rely=y, relheight=height, relwidth=width)



## Entry_InputBox
class EntryForm:
    def __init__(self, window_belong, init_width):
        self.string = tk.StringVar(window_belong)
        self.root = tk.Entry(window_belong, textvariable=self.string, width=init_width)

    def place(self, x, y, width, height):
        self.root.place(relx=x, rely=y, relwidth=width, relheight=height)


## Buttons
class ButtonForm:
    def __init__(self, window_belong, init_text: str, func_handle):
        self.string = init_text
        self.handle = func_handle
        self.root = tk.Button(window_belong, text=self.string, command=self.handle)

    def place(self, x, y, width, height):
        self.root.place(relx=x, rely=y, relwidth=width, relheight=height)


## OptionMenus
class OptionForm:
    def __init__(self, window_belong, init_option, *args):
        self.string = tk.StringVar(window_belong)
        self.string.set(init_option)
        self.options = args
        self.root = tk.OptionMenu(window_belong, self.string, *self.options)

    def place(self, x, y, width, height):
        self.root.place(relx=x, rely=y, relwidth=width, relheight=height)
    
## MessageWindows

class MessageWindows:
    def __init__(self,title,image):
        self.