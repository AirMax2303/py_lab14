# Задание 1. Напишите программу, переводящую градусы по Фаренгейту в градусы по Цельсию.
from cProfile import label
from curses import window
import tkinter

def transference():
    try:
        result=((float(entry.get())-32)/1.8)
        labelResult.config(text=result)
        checker = True
        # labelResult.pack() - если использовать pack() внутри функции, то результат выводится после кнопок. ToDo
        window.update() # Не перерисовывает страницу полностью, if не срабатывает. ToDO
    except:
        labelResult.config(text='Введите корректное значение!')

checker = False

window = tkinter.Tk()

frame = tkinter.Frame(window)

window.title("Перевод температурных значений от Максима Андреевича")

label = tkinter.Label(frame, text = 'Введите значение в фарингейтах: ',font=17)
entry = tkinter.Entry(frame, width = 30)
entry.focus()
label2 = tkinter.Label(frame)
labelResult = tkinter.Label(frame)
buttonConvert = tkinter.Button(frame, text = 'Перевести', command = transference)
buttonQuit = tkinter.Button(frame, text = 'Выйти', command = window.destroy)

frame.pack()
label.pack()
entry.pack()
label.pack()
if checker == True:
    labelResult.pack()
buttonConvert.pack()
buttonQuit.pack()

window.mainloop()



