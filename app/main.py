from shutil import rmtree
import tkinter as tk
import ttkbootstrap as ttk
import collection_handler as ch
import database_handler as dbh

root = ttk.Window(themename = 'flatly')
root.title('EasyOpenX')
try:
    root.wm_iconbitmap('icons/icon.ico')
except:
    root.wm_iconbitmap('@icons/icon.xbm')

canvas = tk.Canvas(root, height=700, width=700, bg = 'white')
canvas.create_text(100, 50, text='   Current Collections:', fill='black', font=('Tahoma 15 bold'))
canvas.pack()
frame = tk.Frame(canvas, bg = 'white')
frame.place(x=0,y=80,relheight=0.8,relwidth=1)

########
def print_collections():
    if dbh.dbhandler.check_collections() is not None:
        collectionnames_as_string = [' '.join(l) for l in dbh.dbhandler.check_collections()]
        collection_data.set(' | '.join(collectionnames_as_string))
        collections.after(1000,  print_collections)
########

collection_data = tk.StringVar()
collections = tk.Label(frame, bg = '#FFF', textvariable = collection_data)
collections.pack()
print_collections()

add_collection_button = ttk.Button(frame,
                                  text = 'Create collection',
                                  bootstyle = 'warning',
                                  command = ch.add_collection_gui)
add_collection_button.pack(pady=5)

edit_collection_button = ttk.Button(frame,
                                   text = 'Edit collections',
                                   bootstyle = 'secondary',
                                   command = ch.edit_collection_gui)
edit_collection_button.pack()

delete_collection_button = ttk.Button(frame,
                                     text = 'Delete collection',
                                     bootstyle = 'danger',
                                     command = ch.delete_collection_gui)
delete_collection_button.pack(pady=5)

tk.Label(frame, text = 'Enter collection name.', bg = '#FFF').pack(pady = (35,7))
collection_name_to_run = ttk.Entry(frame,
                                  justify = 'center',
                                  width = 60)
collection_name_to_run.bind('<Return>', lambda x: ch.run_collection(collection_name_to_run.get()))
collection_name_to_run.pack(ipady = 5)


########
def delete_cache():
    try:
        rmtree('__pycache__')
    except FileNotFoundError:
        pass
    root.destroy()
########

root.protocol("WM_DELETE_WINDOW", delete_cache)
root.mainloop()