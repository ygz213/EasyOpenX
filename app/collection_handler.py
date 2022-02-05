import tkinter as tk
from tkinter import messagebox
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
    tk.Label(window, text = 'Collection apps:', font = 'Tahoma 10 bold').pack()
    collection_apps = tk.Entry(window,
                               justify = 'center',
                               width = 35,
                               bd = 4,
                               highlightthickness = 2,
                               highlightcolor = '#FFF',
                               selectforeground = 'black',
                               relief = 'flat')
    collection_apps.bind('<Return>', lambda x: send_collection())
    collection_apps.pack()


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
#     def openApps(self):
#         for path in self.apps:
#             if system() == 'Windows':
#                 os.startfile(path)
#             if system() == 'Darwin':
#                 call(('open', path))
#             if system() == 'Linux':
#                 call(('xdg-open', path))
#
#
#
# functions: platform.system(), os.startfile(), subprocess.call(), tk.filedialog.askopenfilename()