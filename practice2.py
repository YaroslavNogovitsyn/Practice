from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import sys
import shutil
import os
import time

file_path = 'file2.txt'
try:
    fp = open(file_path)
except IOError:
    # If not exists, create the file
    fp = open(file_path, 'w+')
_stored = dict()
def is_modified(name):
    with open(name) as f:
        t = os.path.getmtime(name)
        if name in _stored:
            reply = not _stored[name] == t
            _stored.update({name: t})
            return reply
        else:
            _stored.update({name: t})
            return False


def send():
    intered_text = tk_object_text.get("1.0", "end")
    f = open('file1.txt', 'w')
    f1 = open("file_history1.txt", 'a')
    try:
        f1.write(intered_text)
        f.write(intered_text)
        tk_object_text.delete("1.0", "end")
    finally:
        f.close()


def change_file():
    if is_modified("file2.txt"):
        x = open('file2.txt', 'r')
        x = x.read()
        txt.insert("1.0", x)
tk = Tk()

def change_loop():
    change_file()
    tk.after(1000, change_loop)


change_loop()
tk.after(2000, change_file)
tk.title('Добро пожаловать в приложение PythonRu')
tk.geometry('1020x500')
tk.resizable(0, 0)
tk_object_text = Text(tk, width=1000, height=500, wrap=WORD)
tk_object_text.place(x=530, y=100, width=1000, height=500)
intered_text = tk_object_text.get("1.0", "end")
scroll = Scrollbar(tk, command=tk_object_text.yview)
scroll.place(x=1000, y=0, width=20, height=500)
tk_object_text.config(yscrollcommand=scroll.set)

l1 = Label(width=5, height=10)
l1.pack(expand=1, fill=Y)

txt = Text(tk, width=1000, height=500, wrap=WORD)
txt.place(x=0, y=100, width=450, height=500)

btn = Button(tk, text="Отправить", command=send)
btn.place(x=930, y=460)

l4 = Label(bg="lightgreen", width=5, height=2, text="Откуда:")
l4.place(x=0, y=0)
e1 = Entry(width=50)
e1.place(x=45, y=10)
l3 = Label(bg='yellow', width=5, height=2, text="Куда:")
l3.place(x=0, y=35)
e2 = Entry(width=50)
e2.place(x=45, y=45)


def get_name_file():
    e1.insert(0, fd.askopenfilename())


def send_name_file():
    e2.insert(0, fd.askdirectory())


get_name_file = Button(tk, text="Выберите файл", command=get_name_file)
get_name_file.place(x=300, y=5)

send_name_file = Button(tk, text="Выберите папку", command=send_name_file)
send_name_file.place(x=300, y=45)


def get_file():
    shutil.copy(e1.get(), e2.get())


b1 = Button(text="Отправить файл", command=get_file)
b1.place(x=0, y=70)


def insert_text():
    try:
        file_name = fd.askopenfilename()
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    except FileNotFoundError:
        mb.showinfo("Внимание", "Файл не загружен")


def extract_text():
    try:
        file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                    ("HTML files", "*.html; *.htm"),
                                                    ("Python files", "*.py; *.pyw"),
                                                    ("All files", "*.*")))
        f = open(file_name, 'w')
        s = text.get("1.0", "end")
        f.write(s)
        f.close()
    except FileNotFoundError:
        mb.showinfo("Внимание", "Файл не сохранён")

def exit():
    sys.exit()


def clear():
    global text
    text.delete(1.0, END)


def th():
    global text

    def bth():
        global text
        texts = text.get(1.0, END)
        text = Text(tk, width=1000, height=500, bg="#DDD", fg='#F05', wrap=WORD)
        text.place(x=0, y=0, width=1000, height=500)
        text.insert(1.0, texts)
        scroll = Scrollbar(tk, command=text.yview)
        scroll.place(x=1000, y=0, width=20, height=500)
        text.config(yscrollcommand=scroll.set)

    def dth():
        global text
        texts = text.get(1.0, END)
        text = Text(tk, width=1000, height=500, bg="#111", fg='#F05', wrap=WORD)
        text.place(x=0, y=0, width=1000, height=500)
        text.insert(1.0, texts)
        scroll = Scrollbar(tk, command=text.yview)
        scroll.place(x=1000, y=0, width=20, height=500)
        text.config(yscrollcommand=scroll.set)

    def oth():
        global text
        texts = text.get(1.0, END)
        text = Text(tk, width=1000, height=500, bg="#0AA", fg='#05D', wrap=WORD)
        text.place(x=0, y=0, width=1000, height=500)
        text.insert(1.0, texts)
        scroll = Scrollbar(tk, command=text.yview)
        scroll.place(x=1000, y=0, width=20, height=500)
        text.config(yscrollcommand=scroll.set)

    def cth():
        global text
        texts = text.get(1.0, END)
        text = Text(tk, width=1000, height=500, bg="#555", fg='#222', wrap=WORD)
        text.place(x=0, y=0, width=1000, height=500)
        text.insert(1.0, texts)
        scroll = Scrollbar(tk, command=text.yview)
        scroll.place(x=1000, y=0, width=20, height=500)
        text.config(yscrollcommand=scroll.set)

    def fth():
        global text
        texts = text.get(1.0, END)
        text = Text(tk, width=1000, height=500, bg="#F30", fg='#DD0', wrap=WORD)
        text.place(x=0, y=0, width=1000, height=500)
        text.insert(1.0, texts)
        scroll = Scrollbar(tk, command=text.yview)
        scroll.place(x=1000, y=0, width=20, height=500)
        text.config(yscrollcommand=scroll.set)

    def gth():
        global text
        texts = text.get(1.0, END)
        text = Text(tk, width=1000, height=500, bg="#0A4", fg='#0FA', wrap=WORD)
        text.place(x=0, y=0, width=1000, height=500)
        text.insert(1.0, texts)
        scroll = Scrollbar(tk, command=text.yview)
        scroll.place(x=1000, y=0, width=20, height=500)
        text.config(yscrollcommand=scroll.set)

    thw = Tk()
    thw.title('')
    thw.geometry('300x100')
    thw.resizable(0, 0)
    btn = Button(thw, text='Bright theme', bg="#DDD", fg="#F05", command=bth)
    btn.place(x=0, y=0, width=100, height=50)
    btn = Button(thw, text='Dark theme', bg="#111", fg="#F05", command=dth)
    btn.place(x=100, y=0, width=100, height=50)
    btn = Button(thw, text='Cry theme', bg="#555", fg="#222", command=cth)
    btn.place(x=200, y=0, width=100, height=50)
    btn = Button(thw, text='Ocean theme', bg="#0AA", fg="#05D", command=oth)
    btn.place(x=0, y=50, width=100, height=50)
    btn = Button(thw, text='Fire theme', bg="#F30", fg="#DD0", command=fth)
    btn.place(x=100, y=50, width=100, height=50)
    btn = Button(thw, text='Grass theme', bg="#0A4", fg="#0FA", command=gth)
    btn.place(x=200, y=50, width=100, height=50)


mainmenu = Menu(tk)
tk.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новый", command=clear)
filemenu.add_command(label="Открыть", command=insert_text)
filemenu.add_command(label="Сохранить", command=extract_text)
filemenu.add_command(label="Выход", command=exit)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Тема", command=th)
menu = Menu(tearoff=0)

tk.mainloop()
