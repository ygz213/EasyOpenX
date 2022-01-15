import tkinter as tk

root = tk.Tk()
root.title('EasyOpenX')

canvas = tk.Canvas(root, height=700, width=700, bg='white')
canvas.create_text(100, 50, text='Current Collections:', fill='black', font=('Constantia 15 bold'))
canvas.pack()
frame = tk.Frame(canvas, bg='white')
frame.place(x=0,y=80,relheight=0.8,relwidth=1)

add_collection_button = tk.Button(frame, text='Create collection')
add_collection_button.pack(pady=5)

delete_collection_button = tk.Button(frame, text='Delete collection')
delete_collection_button.pack(pady=5)


root.mainloop()