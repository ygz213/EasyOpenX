from shutil import rmtree
import tkinter as tk
import collection_handler as ch
import database_handler as dbh

root = tk.Tk()
root.title('EasyOpenX')
try:
    root.wm_iconbitmap('icons/icon.ico')
except:
    root.wm_iconbitmap('@icons/icon.xbm')

canvas = tk.Canvas(root, height=700, width=700, bg='white')
canvas.create_text(100, 50, text='   Current Collections:', fill='black', font=('Tahoma 15 bold'))
canvas.pack()
frame = tk.Frame(canvas, bg='white')
frame.place(x=0,y=80,relheight=0.8,relwidth=1)

########
def print_collections():
    if dbh.dbhandler.check_collections() is not None:
        collectionnames_as_string = [' '.join(l) for l in dbh.dbhandler.check_collections()]
        collection_data.set(' '.join(str(x) for x in collectionnames_as_string).replace(' ', ' | '))
        collections.after(1000,  print_collections)
########

collection_data = tk.StringVar()
collections = tk.Label(frame, bg = '#FFF', textvariable = collection_data)
collections.pack()
print_collections()

add_collection_button = tk.Button(frame,
                                  bg = '#598D9C',
                                  fg = '#FFF',
                                  activebackground = '#416873',
                                  activeforeground = '#FFF',
                                  relief = 'flat',
                                  text = 'Create collection',
                                  command = ch.add_collection_gui)
add_collection_button.pack(pady=5)

edit_collection_button = tk.Button(frame,
                                   bg = '#A29E74',
                                   activebackground = '#838058',
                                   relief = 'flat',
                                   text = 'Edit collections',
                                   command = ch.edit_collection_gui)
edit_collection_button.pack()

delete_collection_button = tk.Button(frame,
                                     bg = '#D62B47',
                                     fg = '#FFF',
                                     activebackground = '#96323C',
                                     activeforeground = '#FFF',
                                     relief = 'flat',
                                     text = 'Delete collection',
                                     command = ch.delete_collection_gui)
delete_collection_button.pack(pady=5)

tk.Label(frame, text = 'Enter collection name.', bg = '#FFF').pack(pady = (35,7))
collection_name_to_run = tk.Entry(frame,
                                  justify = 'center',
                                  width = 60,
                                  bg = '#DEDEDE',
                                  selectforeground = 'black',
                                  relief = 'flat')
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