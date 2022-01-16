import tkinter as tk
from tkinter import filedialog
from subprocess import call
from platform import system
import os

def add_collection():
    window = tk.Toplevel()
    try:
        window.wm_iconbitmap('icons/icon.ico')
    except:
        window.wm_iconbitmap('@icons/icon.xbm')

    tk.Label(window, text = 'Collection name:', font = 'Tahoma 10 bold').pack()
    collection_name = tk.Entry(window,
                               justify = 'center',
                               width = 35,
                               bd = 4,
                               highlightthickness = 2,
                               highlightcolor = '#FFF',
                               selectforeground = 'black',
                               relief = 'flat')    #TODO: command = database.stuff()
    collection_name.pack()


class handler():
    def __init__(self, master):
        self.apps = []

    def addApp(self):
        filename = filedialog.askopenfilename(initialdir=f'{os.getcwd()}', title='Select file...', filetypes=([("All files", "*.*")]))

        self.apps.append(filename)
        self.addToCanvas(filename)

    def addToCanvas(self, fileName):
        self.label = tk.Label(frame, text=fileName, bg='white').pack()

    def openApps(self):
        for path in self.apps:
            if system() == 'Windows':
                os.startfile(path)
            if system() == 'Darwin':
                call(('open', path))
            if system() == 'Linux':
                call(('xdg-open', path))