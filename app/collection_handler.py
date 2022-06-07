from os import path, getcwd
from platform import system
from subprocess import Popen
from tkinter import filedialog
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
import database_handler as dbh
if system() == 'Windows':
    from os import startfile

def check_collection_apps(collection_apps):
    bool_list = []
    for paths in collection_apps.split(' | '):       # Checks if file/folder paths exists
        bool_list.append(path.exists(rf'{paths}'))
    return False in bool_list       # If function returns True, this means there are broken paths or entry format is not valid (split(' | ') checks this)

def check_format(collection_name, collection_apps):
    if len(collection_name) == 0 or len(collection_apps) == 0 or check_collection_apps(collection_apps):
        Messagebox.show_error('Invalid data.', title = 'ERROR')
        return True

def insert_path(collection_apps):
    path = filedialog.askopenfilename(initialdir = f'{getcwd()}', title = 'Select file...', filetypes = ([('All files', '*.*')]))

    if not bool(collection_apps.get()):       # When entry box is empty
        collection_apps.insert('end', f'{path} | ')
    elif collection_apps.get()[-1] == '|':       # When it is like "C:/EasyOpenX/app/main.py |"
        collection_apps.insert('end', f' {path} | ')
    elif collection_apps.get()[-1] == ' ':       # When it is like "C:/EasyOpenX/app/main.py | " (This can be hacked "C:/EasyOpenX/app/main.py ")
        collection_apps.insert('end', f'{path} | ')
    else:       # When it is like "C:/EasyOpenX/app/main.py" or anything else
        collection_apps.insert('end', f' | {path} | ')

    collection_apps.focus()
    collection_apps.xview_moveto(1)


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

        tk.Label(self.add_window,
                 text = 'Collection name:',
                 font = 'Tahoma 10 bold').pack()
        self.collection_name = ttk.Entry(self.add_window,
                                         justify = 'center',
                                         width = 35)
        self.collection_name.pack()

        self.info_frame = tk.Frame(self.add_window)
        self.info_frame.pack()

        tk.Label(self.info_frame,
                 text = 'Collection apps:',
                 font = 'Tahoma 10 bold').grid(column = 0, row = 0)
        self.info_icon = tk.PhotoImage(file = r'icons/info.png')
        self.info_button = tk.Button(self.info_frame,
                                     image = self.info_icon,
                                     command = lambda: Messagebox.show_info('''FORMAT:

C:/EasyOpenX/app/main.py | C:/pdfs/linux.pdf | C:/secret.txt''', title = 'EasyOpenX'))
        self.info_button.configure(bg = 'white')
        self.info_button.image = self.info_icon
        self.info_button.grid(column = 1, row = 0)

        ttk.Button(self.info_frame,
                   text = 'Select file',
                   bootstyle = 'warning-outline',
                   command = lambda: insert_path(self.collection_apps)).grid(column = 2, row = 0, padx = (5, 0))

        self.collection_apps = ttk.Entry(self.add_window,
                                         justify = 'center',
                                         width = 70)
        self.collection_apps.bind('<Return>', lambda x: None if check_format(self.collection_name.get(), self.collection_apps.get()) else self.create_collection())        # Do nothing if check_format returns True, else create collection
        self.collection_apps.pack()


    def create_collection(self):
        dbh.dbhandler.create_collection(self.collection_name.get(), self.collection_apps.get())
        self.add_window.destroy()



def run_collection(collection_name):
    try:
        app_paths = ''.join(dbh.dbhandler.search_collection(collection_name)[0][1:])
    except IndexError:
        Messagebox.show_error('No collection found.', title = 'ERROR')
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
        Messagebox.show_error('No collection found.', title = 'ERROR')
        return

    delete_window = tk.Toplevel()
    delete_window.attributes('-topmost', True)
    delete_window.resizable(False, False)
    delete_window.focus()
    try:
        delete_window.wm_iconbitmap('icons/icon.ico')
    except:
        delete_window.wm_iconbitmap('@icons/icon.xbm')

    tk.Label(delete_window,
             text = 'Select the collection you want to delete.',
             font = 'Tahoma 10 bold').pack()
    for collection in [' '.join(l) for l in dbh.dbhandler.check_collections()]:
        ttk.Button(delete_window,
                   text = f'{collection}',
                   bootstyle = 'danger-outline',
                   command = lambda collection = collection: [dbh.dbhandler.delete_collection(f'{collection}'), delete_window.destroy()]).pack(pady = 4)



class edit_collection_gui():
    def __init__(self):
        if not dbh.dbhandler.check_collections():
            Messagebox.show_error('No collection found.', title = 'ERROR')
            return

        self.edit_window = tk.Toplevel()
        self.edit_window.bind('<FocusOut>', lambda x: self.edit_window.destroy())
        self.edit_window.resizable(False, False)
        self.edit_window.focus()
        try:
            self.edit_window.wm_iconbitmap('icons/icon.ico')
        except:
            self.edit_window.wm_iconbitmap('@icons/icon.xbm')

        tk.Label(self.edit_window,
                 text = 'Select the collection you want to edit.',
                 font = 'Tahoma 10 bold').pack()
        for collection in [' '.join(l) for l in dbh.dbhandler.check_collections()]:
            ttk.Button(self.edit_window,
                       text = f'{collection}',
                       bootstyle = 'secondary-outline',
                       command = lambda collection = collection: self.edit_collection(f'{collection}')).pack(pady = 4)


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
        self.edited_collection_name = ttk.Entry(self.collection_edit_window,
                                                textvariable = self.edited_collectionname_data,
                                                justify = 'center',
                                                width = 35)
        self.edited_collection_name.pack()

        self.info_frame = tk.Frame(self.collection_edit_window)
        self.info_frame.pack()

        tk.Label(self.info_frame,
                 text = 'Collection apps:',
                 font = 'Tahoma 10 bold').grid(column = 0, row = 0)

        ttk.Button(self.info_frame,
                   text = 'Select file',
                   bootstyle = 'secondary-outline',
                   command = lambda: insert_path(self.edited_collection_apps)).grid(column = 2, row = 0, padx = (5, 0))

        self.edited_collection_apps = ttk.Entry(self.collection_edit_window,
                                                textvariable = self.edited_collectionapps_data,
                                                justify = 'center',
                                                width = 70)
        self.edited_collection_apps.bind('<Return>', lambda x: None if check_format(self.edited_collection_name.get(), self.edited_collection_apps.get()) else self.update_collection(collection_name_to_edit))
        self.edited_collection_apps.pack()


    def update_collection(self, collection_name_to_edit):
        dbh.dbhandler.update_collection(collection_name_to_edit, self.edited_collection_name.get(), self.edited_collection_apps.get())
        self.collection_edit_window.destroy()