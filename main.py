import os 
import tkinter as tk
from tkinter import filedialog


class handler:
    def __init__(self, master):
        self.apps = []
        
        
        self.canvas = tk.Canvas(master, height=700, width=700, bg="white")
        self.canvas.create_text(100, 50, text="Current Apps:", fill="black", font=('Constantia 15 bold'))   
        self.canvas.pack()
        
        self.frame = tk.Frame(self.canvas, bg="white")
        self.frame.place(x=0,y=80,relheight=0.8,relwidth=1)
        
        self.addAppButton = tk.Button(master, text="Add an app!", command= self.addApp)
        self.addAppButton.pack(pady=5)
        
        self.openAppsButton = tk.Button(master, text="Open apps", command = self.openApps)
        self.openAppsButton.pack(pady=5)
           
    def addApp(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("all files", "*.*"),("executables", "*.exe")))

        self.apps.append(filename)        
        self.addToCanvas(filename)
    
    def addToCanvas(self, fileName):
        self.label = tk.Label(self.frame, text=fileName, bg='white').pack()
        
    def openApps(self):
        for path in self.apps:
            os.startfile(path)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("EasyOpenX")
    main_call = handler(root)

    root.mainloop()