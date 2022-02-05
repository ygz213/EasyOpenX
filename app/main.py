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
                                  command = lambda: ch.add_collection_gui())
add_collection_button.pack(pady=5)

delete_collection_button = tk.Button(frame,
                                     bg = '#D62B47',
                                     fg = '#FFF',
                                     activebackground = '#96323C',
                                     activeforeground = '#FFF',
                                     relief = 'flat',
                                     text='Delete collection')
delete_collection_button.pack(pady=5)


root.mainloop()