from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.minsize(600, 400)
root.title("Tab Widget")

print(root.keys())
root['background'] = 'red1'
root['borderwidth']=8

s = ttk.Style()
#theme_list = list(s.theme_names())
theme_names_editable = ['winnative', 'clam', 'alt', 'default', 'classic']
#print(s.theme_names())

for e in theme_names_editable:
    s.theme_use(e)
    s.configure('TNotebook', tabposition='wn', background="black")  # 'ne' as in compass direction
    s.configure('TNotebook.Tab', background='green4')  # 'ne' as in compass direction
    s.map("TNotebook.Tab", background=[("disabled", "black"), ("selected", "green3")], foreground=[("disabled", "white")])



tabControl = ttk.Notebook(root, height=0, padding=5, width=400)
print(tabControl.keys())



tab_desc = ttk.Label(tabControl)
im_PI_desc_tab = ImageTk.PhotoImage(Image.open('./asd.bmp'))
tabControl.add(tab_desc, text='Tabs', image=im_PI_desc_tab, compound="left", state="disabled")

main_tab = ttk.LabelFrame(tabControl, text="content")
im_PI_main_tab = ImageTk.PhotoImage(Image.open('./asd2.bmp'))
tabControl.add(main_tab, image=im_PI_main_tab, text='Main tab', compound="left")

doc1_tab = ttk.LabelFrame(tabControl, text="asd")
im_PI_doc1_tab = ImageTk.PhotoImage(Image.open('./asd.bmp'))
tabControl.add(doc1_tab, image=im_PI_doc1_tab, text='Doc 1', compound="left")

doc2_tab = ttk.LabelFrame(tabControl, text="kupa")
im_PI_doc2_tab = ImageTk.PhotoImage(Image.open('./asd2.bmp'))
tabControl.add(doc2_tab, image=im_PI_doc2_tab, text="Doc 2", compound="left")



tabControl.pack(expand=1, fill=BOTH)


index=0
def kolacz():
    global index
    tll = len(theme_names_editable)
    print(theme_names_editable[index % tll])
    s.theme_use(theme_names_editable[index % tll])
    #s.configure('TNotebook', tabposition='wn')
    index+=1

in_fr = LabelFrame(doc1_tab, text="hermes")

b1 = ttk.Button(main_tab, text="elo 1").pack()
b2 = ttk.Button(in_fr, text="elo 2", command=kolacz).pack()
b3 = ttk.Button(in_fr, text="elo 3").pack()
b4 = ttk.Button(doc2_tab, text="elo 4").pack()

main_tab_header = LabelFrame(main_tab, text="dane klienta")
# - - - - - - - - - - - -
header_fname_frame = Frame(main_tab_header)
header_fname_label = Label(header_fname_frame, text="imie").pack(side=LEFT)
username = StringVar()
header_fname_box = Entry(header_fname_frame, textvariable=username).pack(side=RIGHT)
header_fname_frame.grid(column=1, row=1)
# - - - - - - - - - - - -
header_sname_frame = Frame(main_tab_header)
header_sname_label = Label(header_sname_frame, text="nazwisko").pack(side=LEFT)
usersurname = StringVar()
header_sname_box = Entry(header_sname_frame, textvariable=usersurname).pack(side=RIGHT)
header_sname_frame.grid(column=2, row=1)
# - - - - - - - - - - - -
header_pesel_frame = Frame(main_tab_header)
header_pesel_label = Label(header_pesel_frame, text="pesel").pack(side=LEFT)
telephone = StringVar()
header_pesel_box = Entry(header_pesel_frame, textvariable=telephone, width=12).pack(side=RIGHT)
header_pesel_frame.grid(column=3, row=1)
# - - - - - - - - - - - -
header_tel_frame = Frame(main_tab_header)
header_tel_label = Label(header_tel_frame, text="telefon").pack(side=LEFT)
telephone = StringVar()
header_tel_box = Entry(header_tel_frame, textvariable=telephone, width=15).pack(side=RIGHT)
header_tel_frame.grid(column=4, row=1)
# - - - - - - - - - - - -
header_code_frame = Frame(main_tab_header)
header_code_label = Label(header_code_frame, text="kod pocztowy").pack(side=LEFT)
postal_code = StringVar()
header_code_box = Entry(header_code_frame, textvariable=postal_code, width=7).pack(side=RIGHT)
header_code_frame.grid(column=1, row=2)
# - - - - - - - - - - - -
header_city_frame = Frame(main_tab_header)
header_city_label = Label(header_city_frame, text="miasto").pack(side=LEFT)
city = StringVar()
header_city_box = Entry(header_city_frame, textvariable=city).pack(side=RIGHT)
header_city_frame.grid(column=2, row=2)
# - - - - - - - - - - - -
header_borough_frame = Frame(main_tab_header)
header_borough_label = Label(header_borough_frame, text="gmina").pack(side=LEFT)
telephone = StringVar()
header_borough_box = Entry(header_borough_frame, textvariable=telephone).pack(side=RIGHT)
header_borough_frame.grid(column=3, row=2)
# - - - - - - - - - - - -
header_street_frame = Frame(main_tab_header)
header_street_label = Label(header_street_frame, text="ulica").pack(side=LEFT)
telephone = StringVar()
header_street_box = Entry(header_street_frame, textvariable=telephone).pack(side=RIGHT)
header_street_frame.grid(column=4, row=2)
# - - - - - - - - - - - -


main_tab_header.pack()
in_fr.pack()

root.mainloop()
