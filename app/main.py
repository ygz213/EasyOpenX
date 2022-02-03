import tkinter as tk
import collection_handler as ch

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