import tkinter as tk
from tkinter import messagebox
from os import startfile
from platform import system
from subprocess import call
import database_handler as dbh

collection_repo = []

def add_collection_gui():
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
                               relief = 'flat')
########
    def send_collection():
        if len(collection_name.get()) == 0 or len(collection_apps.get()) == 0:
            messagebox.showerror('ERROR', 'Invalid data.')
            return
        collection_repo.clear()
        collection_repo.extend([collection_name.get(), collection_apps.get()])
        dbh.dbhandler.create_collection()
        window.destroy()
    collection_name.pack()
########
    info_frame = tk.Frame(window)
    info_frame.pack()

    tk.Label(info_frame, text = 'Collection apps:', font = 'Tahoma 10 bold').grid(column = 0, row = 0)
    info_icon = tk.PhotoImage(file = r'icons/info.png')
    info_button = tk.Button(info_frame, relief = 'flat', image = info_icon, command = lambda: messagebox.showinfo('EasyOpenX', '''FORMAT:

C:/EasyOpenX/app/main.py | C:/pdfs/linux.pdf | C:/secret.txt'''))
    info_button.image = info_icon
    info_button.grid(column = 1, row = 0)


    collection_apps = tk.Entry(window,
                               justify = 'center',
                               width = 70,
                               bd = 4,
                               highlightthickness = 2,
                               highlightcolor = '#FFF',
                               selectforeground = 'black',
                               relief = 'flat')
    collection_apps.bind('<Return>', lambda x: send_collection())
    collection_apps.pack()


def run_collection(collection_name):
    try:
        app_paths = ''.join(dbh.dbhandler.search_collection(collection_name)[0][1:])
    except IndexError:
        messagebox.showerror('ERROR', 'No collection found.')

    for app in app_paths.split(' | '):
        if system() == 'Windows':
            startfile(app)
        if system() == 'Darwin':
            call(('open', app))
        if system() == 'Linux':
            call(('xdg-open', app))  


# class handler():                (codes taken from upstream, may be used in the future)
#     def __init__(self, master):
#         self.apps = []
#
#     def addApp(self):
#         filename = filedialog.askopenfilename(initialdir=f'{os.getcwd()}', title='Select file...', filetypes=([('All files', '*.*')]))
#
#         self.apps.append(filename)
#         self.addToCanvas(filename)
#
#     def addToCanvas(self, fileName):
#         self.label = tk.Label(frame, text=fileName, bg='white').pack()
#
#
#
# functions: platform.system(), os.startfile(), subprocess.call(), tk.filedialog.askopenfilename()