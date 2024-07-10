# -*- encoding=utf-8 -*-
__author__ = "Molta"

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
Threads = None
Process = None


# Classes
## Background
class BackGroundLabel:
    def __init__(self,upwindow,init_path:str):
        self.windowform = upwindow
        self.path = os.path.join(os.path.dirname(__file__)+init_path)
    def place():
        image = Image.open(self.path).convert('RGBA')
        alpha=128
        image.inputalpha(alpha)
        image_resized =image.resize((self.windowform.winfo_width(),self.windowform.winfo_height()),Image.Resampling.LANCZOS)


## Main_Window
class WindowForm:
    def __init__(self, title: str):
        self.root = tk.Tk()
        self.title = title
        self.root.title(title)
        self.background = None

    def setbackground(self, background: str):
        dirname = os.path.dirname(__file__)
        bg_path = os.path.join(dirname, background)
        image = Image.open(bg_path).convert('RGBA')
        alpha = 128
        image.putalpha(alpha)
        image_resized = image.resize((self.root.winfo_width(), self.root.winfo_height()), Image.Resampling.LANCZOS)
        bg_object = ImageTk.PhotoImage(image_resized)
        self.background = tk.Label(self.root, image=bg_object)
        self.background.place(relx=0, rely=0, relheight=1, relwidth=1)

    def setwindow(self, width, height):
        self.root.geometry(f"{width}x{height}")
        self.root.mainloop()


## Sub_Window
class SubWindowForm(WindowForm):
    def __init__(self, title: str, upwindow):
        self.root = tk.Toplevel(upwindow.root)
        super().__init__(title)


## Labels
class LabelForm:
    def __init__(self, content: str, window_belong):
        self.string = tk.StringVar(window_belong)
        self.string.set(content)
        self.root = tk.Label(window_belong, textvariable=self.string, padx=10, pady=10)
    # use relative position directly

    def place(self, x, y, width, height):
        self.root.place(relx=x, rely=y, relwidth=width, relheight=height)


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
