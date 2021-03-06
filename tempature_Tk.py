from tkinter import *

root = Tk()
root.geometry('380x250')
root.config(bg="#D980FA")
root.title("Temperature Scales")


#variables
celcius = IntVar()
fahrenheit = IntVar()
kelvin = IntVar()

def c_to_k():
    new_window = Toplevel(root)
    new_window.geometry('300x250')
    new_window.title("Celcius to Kelvin")
    def result():
        celcius_get = celcius.get()
        to_kelvin = celcius_get + 273
        lbl = Label(new_window,text=f"{str(celcius.get())} Celcius = {to_kelvin} Kelvin",font=("Arial 10 bold")).place(x=35,y=110)
    label = Label(new_window,text="Celcius",font=("Arial 10 bold")).place(x=35,y=30)
    entry = Entry(new_window, textvariable=celcius, font=("Arial 10 bold")).place(x=135, y=30)
    button = Button(new_window,text="Result",font=("Arial 10 bold"),command=result).place(x=70,y=70)

def k_to_c():
    new_window = Toplevel(root)
    new_window.geometry('300x250')
    new_window.title("Kelvin to Celcius")
    def result():
        kelvin_get = kelvin.get()
        to_celcius = kelvin_get - 273
        lbl = Label(new_window,text=f"{str(kelvin.get())} Kelvin = {to_celcius} Celcius",font=("Arial 10 bold")).place(x=35,y=110)
    label = Label(new_window,text="Kelvin",font=("Arial 10 bold")).place(x=35,y=30)
    entry = Entry(new_window, textvariable=kelvin, font=("Arial 10 bold")).place(x=135, y=30)
    button = Button(new_window,text="Result",font=("Arial 10 bold"),command=result).place(x=70,y=70)

def c_to_f():
    new_window = Toplevel(root)
    new_window.geometry('300x250')
    new_window.title("Celcius to Fahrenheit")
    def result():
        celcius_get = celcius.get()
        stage_1 = (9 * celcius_get) / 5
        to_fahrenheit = stage_1 + 32
        round_fahrenheit = round(to_fahrenheit)
        lbl = Label(new_window,text=f"{str(celcius.get())} Celcius = {round_fahrenheit} Fahrenheit",font=("Arial 10 bold")).place(x=35,y=110)
    label = Label(new_window,text="Celcius",font=("Arial 10 bold")).place(x=35,y=30)
    entry = Entry(new_window, textvariable=celcius, font=("Arial 10 bold")).place(x=135, y=30)
    button = Button(new_window,text="Result",font=("Arial 10 bold"),command=result).place(x=70,y=70)

def f_to_c():
    new_window = Toplevel(root)
    new_window.geometry('300x250')
    new_window.title("Fahrenheit to Celcius")
    def result():
        fahrenheit_get = fahrenheit.get()
        stage_1 = fahrenheit_get - 32
        to_celcius = (5 * stage_1) / 9
        round_celcius = round(to_celcius)
        lbl = Label(new_window,text=f"{str(fahrenheit.get())} Celcius = {round_celcius} Fahrenheit",font=("Arial 10 bold")).place(x=35,y=110)
    label = Label(new_window,text="Fahrenheit",font=("Arial 10 bold")).place(x=35,y=30)
    entry = Entry(new_window, textvariable=fahrenheit, font=("Arial 10 bold")).place(x=135, y=30)
    button = Button(new_window,text="Result",font=("Arial 10 bold"),command=result).place(x=70,y=70)

#widgets
btn1 = Button(root,text="Celcius to Kelvin",bg="#6F1E51",width=17,font=("Arial 10 bold"),command=c_to_k).place(x=35,y=30)
btn2 = Button(root,text="Kelvin to Celcius",bg="#6F1E51",width=17,font=("Arial 10 bold"),command=k_to_c).place(x=200,y=30)
btn3 = Button(root,text="Celcius to Fahrenheit",bg="#6F1E51",width=17,font=("Arial 10 bold"),command=c_to_f).place(x=35,y=100)
btn4 = Button(root,text="Fahrenheit to Celcius",bg="#6F1E51",width=17,font=("Arial 10 bold"),command =f_to_c).place(x=200,y=100)



root.mainloop()