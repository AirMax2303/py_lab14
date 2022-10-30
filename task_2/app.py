# Задание 2. Напишите программу, которая отображает случайное слово
# на русском языке (тип данных dict). Пользователь пытается угадать его на
# английском (или другом языке). Дополнительно ограничить работу
# программы по числу неправильно угаданных слов.
# ToDo: Переделать!
import tkinter
import random
from tkinter import messagebox
import os
import sys
 
d={'машина':'car', 'вертолет':'helicopter', 'самолет':'plane', 'автобус':'bus', 'поезд':'train'}
window = tkinter.Tk()
window.geometry('300x200')
window.title('Dictionary')
lbl1=tkinter.Label(window, text='Write the English word for:', font=("Arial Bold", 15))
lbl2=tkinter.Label(window)
lbl3=tkinter.Label(window)
lbl4=tkinter.Label(window)
 
# функция выбора случайного слова из словаря
def random_word():
    word=random.choice(list(d.keys()))
    lbl2.configure(text=word)
    lbl3.configure(text='')
    return word
random_word()
 
lbl1.pack()
lbl2.pack()
txt = tkinter.Entry(window, width=10)
txt.focus()
txt.pack()
lbl3.pack()
lbl4.pack()
 
# функция рестарта программы
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
 
# функция проверки ввода
def click():
    a=txt.get()
    if d[lbl2.cget('text')]==a:
        result='You are right.'
    else:
        result='You are wrong.'
        click.invocations-=1
        lbl4.configure(text=f'Attempts left: {click.invocations}.')
        if click.invocations==0:
            result='You lost.'
            msg=messagebox.showinfo(title="You lost!", message="The game will restart.")
            if msg=='ok':
                restart_program() # при трех ошибках возникает сообщение о том, Вы проиграли и что игра начнется заново.
    lbl3.configure(text=result)
click.invocations=3 #обратный счетчик ошибок
 
btn1 = tkinter.Button(window, text="Check", command=click)
btn1.pack()
btn2 = tkinter.Button(window, text="Next", command=random_word)
btn2.pack()
window.mainloop()