from tkinter import *

def EntryPostalCode_builder(parent, **kwargs):
    def __trace_postal_code_w(p1, p2, p3):
        tmp_str = postal_code.get()
        if len(tmp_str) == 3 and tmp_str[0:3].isdecimal():
            ret.insert(2, '-')
        if len(tmp_str) == 6:  # copy paste variant
            if tmp_str.count('-') == 1 and tmp_str[2] == '-':
                pass
            else:
                while '-' in tmp_str:
                    tmp_str = tmp_str.replace('-', "")
                if len(tmp_str) > 2:
                    tmp_str = tmp_str[0:2] + '-' + tmp_str[2:]
                postal_code.set(tmp_str)

    def __callback_postal_code(input0: str):
        if not input0:
            return True
        if len(input0) <= 6 and (input0[-1].isdigit() or input0[-1] == '-'):
            return True
        else:
            return False

    postal_code = StringVar()
    postal_code.trace('w', __trace_postal_code_w)
    reg = parent.register(__callback_postal_code)
    ret = Entry(parent, validate="key", validatecommand=(reg, "%P"), textvariable=postal_code, width=7, **kwargs)
    return ret


if __name__ == "__main__":
    root = Tk()

    e = EntryPostalCode_builder(root, justify=CENTER)

    e.pack()
    root.mainloop()