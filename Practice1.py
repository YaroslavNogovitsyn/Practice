from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd


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
                                                    ("All files", "*.*")))
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    except FileNotFoundError:
        mb.showinfo("Внимание", "Файл не сохранён")


def delete_text():
    answer = mb.askyesno("Подтверждение", message="Вы хотите удалить текст?")
    if answer == True:
        text.delete(0.0, END)


root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="Открыть", command=insert_text)
mainmenu.add_command(label="Сохранить", command=extract_text)
menu = Menu(tearoff=0)
menu.add_command(label="Очистить", command=delete_text)
text.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

root.mainloop()