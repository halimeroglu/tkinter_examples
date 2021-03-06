from tkinter import *
from tkinter import messagebox
import math


root = Tk()
root.title('Carbon-14')
root.geometry('450x300')
root.config(bg="#74b9ff")

c12 = StringVar()
c14 = StringVar()

def age_calculate():
    if c12.get() == "" or c14.get() == "":
        messagebox.showinfo(title="Info",message="Please fill all sections")
    else:
        c12_get = float(c12.get())
        c14_get = float(c14.get())
        ratio = c14_get/c12_get
        log_ratio = math.log(ratio)
        stage_1 = log_ratio / (-0.693)
        stage_2 = stage_1 * 5736
        result = round(stage_2)
        age_label_2 = Label(root, text=str(result), bg="#74b9ff", font=('Arial', 14)).place(x=100, y=200)
def clear():
    c12.set("")
    c14.set("")
    age_label_2 = Label(root, text="_____", bg="#74b9ff", font=('Arial', 14)).place(x=100, y=200)

#widgets
c14_label = Label(root,text="C-14 Quantity",bg="#74b9ff",font=('Arial',14)).place(x=20,y=30)
c14_entry = Entry(root,textvariable=c14,font=('Arial',14)).place(x=150,y=30)
c12_label = Label(root,text="C-12 Quantity",bg="#74b9ff",font=('Arial',14)).place(x=20,y=70)
c12_entry = Entry(root,textvariable=c12,font=('Arial',14)).place(x=150,y=70)

calculate = Button(root,text="Calculate",bg="#0984e3",font=('Arial',14),width=10,command=age_calculate).place(x=100,y=125)
clear = Button(root,text="Clear",bg="#0984e3",font=('Arial',14),width=10,command=clear).place(x=225,y=125)
age_label = Label(root,text="Age",bg="#74b9ff",font=('Arial',14)).place(x=20,y=200)
age_label_2 = Label(root,text="_____",bg="#74b9ff",font=('Arial',14)).place(x=100,y=200)


root.mainloop()