# Building EasyOpenX

**1-** Move `app/icons/icon.ico` and `app/icons/info.png` to `app/` directory.


**2-** Make sure that PyInstaller is installed.


**3-** Add
```python
import sys
import os

if not hasattr(sys, "frozen"):
    datafile = os.path.join(os.path.dirname(__file__), "icon.ico")
else:
    datafile = os.path.join(sys.prefix, "icon.ico")                 # stuff to show logo in .EXE properly
def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
```

lines to both `main.py` and `collection_handler.py`


**4-** Change
```python
try:
    (window).wm_iconbitmap('icons/icon.ico')
except:
    (window).wm_iconbitmap('@icons/icon.xbm')
```
and
```python
(collection_handler.py, line 33-34-35-36-37)

        self.info_frame = tk.Frame(self.add_window)
        self.info_frame.pack()

        tk.Label(self.info_frame, text = 'Collection apps:', font = 'Tahoma 10 bold').grid(column = 0, row = 0)
        self.info_icon = tk.PhotoImage(file = r'icons/info.png')
```
parts as
```python
(window).iconbitmap(default=resource_path(datafile))
```
```python
        self.info_frame = tk.Frame(self.add_window)
        self.info_frame.pack()

        if not hasattr(sys, "frozen"):
            datafilex = os.path.join(os.path.dirname(__file__), "info.png")
        else:
            datafilex = os.path.join(sys.prefix, "info.png")                 # stuff to show logo in .EXE properly
        def resource_pathx(relative_path):    
            try:       
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        tk.Label(self.info_frame, text = 'Collection apps:', font = 'Tahoma 10 bold').grid(column = 0, row = 0)
        self.info_icon = tk.PhotoImage(file = resource_pathx(datafilex))
```


**5-** `cd app/` and run `py -m PyInstaller -n fork --onefile --noconsole --add-data "icon.ico;." --add-data "info.png;." --icon=icon.ico main.py`