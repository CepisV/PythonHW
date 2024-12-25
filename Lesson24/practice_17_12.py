from tkinter import *
from tkinter import ttk


def clicked():
    lbl.configure(text='Кнопка нажата')

def finish():
    window.destroy()
    print('Приложение закрыто')

def get_text():
    lbl['text'] = entry.get()

window = Tk()
window.title('Добро пожаловать в ITStep')
window.geometry('400x250+200+200')
# window.attributes("-fullscreen", True) Весь экран
# window.attributes("-alpha", 0.5) Прозрачность
# window.attributes('-toolwindow', True) Убрать свернуть
# window.attributes('-disabled', True) Отключить нажатие
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", finish)
icon = PhotoImage(file='icon.png')
window.iconphoto(False, icon)
# lbl = Label(window, text='Приветствую', font=('Arial Bold', 15))
# lbl.grid(column=0, row=0)
# btn = Button(window, text='Нажми меня', command=clicked)
# btn.grid(column=0, row=1)

btn = ttk.Button(text='Нажми меня', command=get_text)
btn.pack()
entry = ttk.Entry()
entry.pack(anchor=NW, padx=10, pady=10)
lbl = ttk.Label(text='', font=('Arial Bold', 15))
lbl.pack(anchor=NW)
enabled = IntVar()
enabled_checkbutton = ttk.Checkbutton(text='Включить', variable=enabled)
enabled_checkbutton.pack()
# btn = Button(text='Вторая кнопка') Второнй метод отрисовки интерфейса
# btn.pack()
window.mainloop()
