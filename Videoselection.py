#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24.1
#  in conjunction with Tcl version 8.6
#    Nov 21, 2019 08:45:54 PM IST  platform: Windows NT

import sys
import os
from tkinter import filedialog
from tkinter import *
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Videoselection_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Videoselection_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Videoselection_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def encr1(self):
        os.system("EncryptionProcess.py")
        exit()
    def brws(self):
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir="C:/Users/jithu/PycharmProjects/j/MAJOR/", title="Select file",
                                                   filetypes=(("Video files", "*.mp4"), ("All files", "*.*")))
        print(root.filename)
        self.Entry1.insert(10,root.filename)
        self.Button2.configure(state=ACTIVE)
        file=open("binpath.txt","w+")
        file.write(root.filename)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font15 = "-family {Times New Roman} -size 20 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font18 = "-family {Times New Roman} -size 16 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("1044x469+377+150")
        top.title("Video Selection")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.096, rely=0.277, height=43, width=179)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font15)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Select Video''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.326, rely=0.277,height=44, relwidth=0.368)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=384)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.728, rely=0.256, height=53, width=168)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font18)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Browse''',command=self.brws)
        self.Button1.configure(width=168)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.402, rely=0.597, height=63, width=201)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font18)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Continue''',command=self.encr1)
        self.Button2.configure(width=201)
        self.Button2.configure(state=DISABLED)

if __name__ == '__main__':
    vp_start_gui()





