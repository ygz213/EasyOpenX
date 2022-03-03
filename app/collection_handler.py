from tkinter import messagebox
from subprocess import Popen
from platform import system
import tkinter as tk
import database_handler as dbh
if system() == 'Windows':
    from os import startfile

collection_repo = []

class add_collection_gui():
    def __init__(self):
        self.add_window = tk.Toplevel()
        self.add_window.attributes('-topmost', True)
        self.add_window.resizable(False, False)
        self.add_window.focus()
        try:
            self.add_window.wm_iconbitmap('icons/icon.ico')
        except:
            self.add_window.wm_iconbitmap('@icons/icon.xbm')

        tk.Label(self.add_window, text = 'Collection name:', font = 'Tahoma 10 bold').pack()
        self.collection_name = tk.Entry(self.add_window,
                                   justify = 'center',
                                   width = 35,
                                   bd = 4,
                                   highlightthickness = 2,
                                   highlightcolor = '#FFF',
                                   selectforeground = 'black',
                                   relief = 'flat')
        self.collection_name.pack()

        self.info_frame = tk.Frame(self.add_window)
        self.info_frame.pack()

        tk.Label(self.info_frame, text = 'Collection apps:', font = 'Tahoma 10 bold').grid(column = 0, row = 0)
        self.info_icon = tk.PhotoImage(file = r'icons/info.png')
        self.info_button = tk.Button(self.info_frame, relief = 'flat', image = self.info_icon, command = lambda: messagebox.showinfo('EasyOpenX', '''FORMAT:

C:/EasyOpenX/app/main.py | C:/pdfs/linux.pdf | C:/secret.txt'''))
        self.info_button.image = self.info_icon
        self.info_button.grid(column = 1, row = 0)


        self.collection_apps = tk.Entry(self.add_window,
                                       justify = 'center',
                                       width = 70,
                                       bd = 4,
                                       highlightthickness = 2,
                                       highlightcolor = '#FFF',
                                       selectforeground = 'black',
                                       relief = 'flat')
        self.collection_apps.bind('<Return>', lambda x: self.send_collection())
        self.collection_apps.pack()


    def send_collection(self):      # This extends collection names and apps to collection_repo and database_handler gets datas from there
        if len(self.collection_name.get()) == 0 or len(self.collection_apps.get()) == 0:
            messagebox.showerror('ERROR', 'Invalid data.')
            return
        collection_repo.clear()
        collection_repo.extend([self.collection_name.get(), self.collection_apps.get()])
        dbh.dbhandler.create_collection()
        self.add_window.destroy()



def run_collection(collection_name):
    try:
        app_paths = ''.join(dbh.dbhandler.search_collection(collection_name)[0][1:])
    except IndexError:
        messagebox.showerror('ERROR', 'No collection found.')
        return

    for app in app_paths.split(' | '):
        if system() == 'Windows':
            startfile(app)
        if system() == 'Darwin':
            Popen(('open', app))
        if system() == 'Linux':
            Popen(('xdg-open', app))



def delete_collection_gui():
    if not dbh.dbhandler.check_collections():
        messagebox.showerror('ERROR', 'No collection found.')
        return

    delete_window = tk.Toplevel()
    delete_window.attributes('-topmost', True)
    delete_window.resizable(False, False)
    delete_window.focus()
    try:
        delete_window.wm_iconbitmap('icons/icon.ico')
    except:
        delete_window.wm_iconbitmap('@icons/icon.xbm')

    tk.Label(delete_window, text = 'Select the collection you want to delete.', font = 'Tahoma 10 bold').pack()
    for collection in [' '.join(l) for l in dbh.dbhandler.check_collections()]:
        tk.Button(delete_window,
                  text = f'{collection}',
                  bg = '#51706D',
                  fg = '#FFF',
                  activebackground = '#37524F',
                  activeforeground = '#FFF',
                  relief = 'flat',
                  command = lambda: [dbh.dbhandler.delete_collection(f'{collection}'), delete_window.destroy()]).pack(pady = 4)



class edit_collection_gui():
    def __init__(self):
        if not dbh.dbhandler.check_collections():
            messagebox.showerror('ERROR', 'No collection found.')
            return

        self.edit_window = tk.Toplevel()
        self.edit_window.bind('<FocusOut>', lambda x: self.edit_window.destroy())
        self.edit_window.resizable(False, False)
        self.edit_window.focus()
        try:
            self.edit_window.wm_iconbitmap('icons/icon.ico')
        except:
            self.edit_window.wm_iconbitmap('@icons/icon.xbm')

        tk.Label(self.edit_window, text = 'Select the collection you want to edit.', font = 'Tahoma 10 bold').pack()
        for collection in [' '.join(l) for l in dbh.dbhandler.check_collections()]:
            tk.Button(self.edit_window,
                      text = f'{collection}',
                      bg = '#51706D',
                      fg = '#FFF',
                      activebackground = '#37524F',
                      activeforeground = '#FFF',
                      relief = 'flat',
                      command = lambda: self.edit_collection(f'{collection}')).pack(pady = 4)


    def edit_collection(self, collection_name_to_edit):
        self.collection_edit_window = tk.Toplevel()
        self.collection_edit_window.attributes('-topmost', True)
        self.collection_edit_window.resizable(False, False)
        self.collection_edit_window.focus()
        try:
            self.collection_edit_window.wm_iconbitmap('icons/icon.ico')
        except:
            self.collection_edit_window.wm_iconbitmap('@icons/icon.xbm')

        self.edited_collectionname_data = tk.StringVar()
        self.edited_collectionname_data.set(f'{collection_name_to_edit}')
        self.edited_collectionapps_data = tk.StringVar()     # These are for pasting current apps and datas to entry boxes, and being used to get edited collection names and data
        self.edited_collectionapps_data.set(f'{dbh.dbhandler.search_collection(collection_name_to_edit)[0][1]}')

        tk.Label(self.collection_edit_window, text = 'Collection name:', font = 'Tahoma 10 bold').pack()
        self.edited_collection_name = tk.Entry(self.collection_edit_window,
                                               textvariable = self.edited_collectionname_data,
                                               justify = 'center',
                                               width = 35,
                                               bd = 4,
                                               highlightthickness = 2,
                                               highlightcolor = '#FFF',
                                               selectforeground = 'black',
                                               relief = 'flat')
        self.edited_collection_name.pack()

        tk.Label(self.collection_edit_window, text = 'Collection apps:', font = 'Tahoma 10 bold').pack()
        self.edited_collection_apps = tk.Entry(self.collection_edit_window,
                                               textvariable = self.edited_collectionapps_data,
                                               justify = 'center',
                                               width = 70,
                                               bd = 4,
                                               highlightthickness = 2,
                                               highlightcolor = '#FFF',
                                               selectforeground = 'black',
                                               relief = 'flat')

        self.edited_collection_apps.bind('<Return>', lambda x: [dbh.dbhandler.update_collection(collection_name_to_edit, self.edited_collection_name.get(), self.edited_collection_apps.get()), self.collection_edit_window.destroy()])
        self.edited_collection_apps.pack()



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