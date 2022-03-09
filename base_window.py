from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk






root = Tk()

def callback_postal_code_w(p1, p2, p3):
    tmp_str = postal_code.get()
    if len(tmp_str) < 6:
        if len(tmp_str) < 3:
            pass
        #e.insert()
        elif len(tmp_str) == 3 and tmp_str[0:3].isdecimal():
            e.insert(2, '-')
            pass
        else:
            pass
    elif len(tmp_str) == 6:  # copy paste variant
        if tmp_str.count('-') == 1 and tmp_str[2] == '-':
            pass
        else:
            while '-' in tmp_str:
                tmp_str = tmp_str.replace('-', "")
            if len(tmp_str) > 2:
                tmp_str = tmp_str[0:2] + '-' + tmp_str[2:]
            postal_code.set(tmp_str)


postal_code = StringVar()
postal_code.trace('w', callback_postal_code_w)

def callback(input0:str):
        if not input0:
            return True
        print(len(input0))
        if len(input0) <= 6 and (input0[-1].isdigit() or input0[-1] == '-'):
            return True
        else:
            return False



reg = root.register(callback)

e = Entry(root, validate="key", validatecommand=(reg, "%P"), textvariable=postal_code)
e.place(x=50, y=50)
e.pack()



root.mainloop()