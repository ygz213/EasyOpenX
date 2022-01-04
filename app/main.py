import os
import tkinter as tk
from platform import system
from subprocess import call
from tkinter import filedialog

root = tk.Tk()
root.title('EasyOpenX')


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
handler_call = handler(root)


canvas = tk.Canvas(root, height=700, width=700, bg='white')
canvas.create_text(100, 50, text='Current Apps:', fill='black', font=('Constantia 15 bold'))
canvas.pack()
frame = tk.Frame(canvas, bg='white')
frame.place(x=0,y=80,relheight=0.8,relwidth=1)

addAppButton = tk.Button(frame, text='Add an app!', command= handler_call.addApp)
addAppButton.pack(pady=5)

openAppsButton = tk.Button(frame, text='Open apps', command = handler_call.openApps)
openAppsButton.pack(pady=5)


root.mainloop()