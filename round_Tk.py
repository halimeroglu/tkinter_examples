from tkinter import *


root = Tk()
root.title('Round')
root.geometry('450x350')

number = StringVar()
digits = StringVar()

def result():
    number_get = float(number.get())
    digits_get = int(digits.get())
    round_number = round(number_get,digits_get)
    result_label_2 = Label(root, text=f"{str(round_number)}", font=("Arial", 14)).place(x=110, y=170)

def clear():
    number.set("")
    digits.set("")
    result_label_2 = Label(root, text="___________", font=("Arial", 14)).place(x=110, y=170)

#make widgets
number_label = Label(root,text="Number",font=("Arial",14)).place(x=30,y=30)
number_entry = Entry(root,textvariable=number,font=("Arial",14)).place(x=110,y=30)
digits_label = Label(root,text="Digits",font=("Arial",14)).place(x=30,y=70)
digits_entry = Entry(root,textvariable=digits,font=("Arial",14)).place(x=110,y=70)

result_button = Button(root,text="Result",font=("Arial",14),command=result).place(x=200,y=130)
clear_button = Button(root,text="Clear",font=("Arial",14),command=clear).place(x=280,y=130)

result_label = Label(root,text="Result",font=("Arial",14)).place(x=30,y=170)
result_label_2 = Label(root,text="___________",font=("Arial",14)).place(x=110,y=170)


root.mainloop()