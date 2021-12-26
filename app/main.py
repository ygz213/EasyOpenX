import os 
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('EasyOpenX')

class handler():
    def __init__(self, master):
        self.apps = []

    def addApp(self):
        filename = filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('all files', '*.*'),('executables', '*.exe')))

        self.apps.append(filename)        
        self.addToCanvas(filename)
    
    def addToCanvas(self, fileName):
        self.label = tk.Label(gui_call.frame, text=fileName, bg='white').pack()

    def openApps(self):
        for path in self.apps:
            os.startfile(path)
handler_call = handler(root)


class gui():
    def __init__(self, master):
        self.canvas = tk.Canvas(master, height=700, width=700, bg='white')
        self.canvas.create_text(100, 50, text='Current Apps:', fill='black', font=('Constantia 15 bold'))   
        self.canvas.pack()
        
        self.frame = tk.Frame(self.canvas, bg='white')
        self.frame.place(x=0,y=80,relheight=0.8,relwidth=1)
        
        self.addAppButton = tk.Button(self.frame, text='Add an app!', command= handler_call.addApp)
        self.addAppButton.pack(pady=5)
        
        self.openAppsButton = tk.Button(self.frame, text='Open apps', command = handler_call.openApps)
        self.openAppsButton.pack(pady=5)

if __name__ == '__main__':
    gui_call = gui(root)
    root.mainloop()