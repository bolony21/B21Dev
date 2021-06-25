from os import geteuid
import tkinter
import random
from tkinter.constants import END

import pynput
import threading


root = tkinter.Tk()
root.title = "CALCULATOR 1.0"
root['bg'] ='black'
ent = tkinter.Entry(root,width=70,borderwidth=30)
ent.grid(row=0,column=0,columnspan=6,padx=10,pady=10)


def NumIn(number):
 current = ent.get()
 ent.delete(0, END)
 ent.insert(0,str(current) + str(number))

def ButtonClear():
 ent.delete(0, END)

def ButtonPlus():
 NumFi = ent.get()
 global f_Num
 global  math
 math = "Add"
 f_Num = int(NumFi)
 ent.delete(0,END)


def ButtonMinus():
 NumFi = ent.get()
 global f_Num
 global math
 math = "Min"
 f_Num = int(NumFi)
 ent.delete(0,END)

def ButtonMulti():
 NumFi = ent.get()
 global  f_Num
 global  math
 math = "Mult"
 f_Num = int(NumFi)
 ent.delete(0,END)

def ButtonDivi():
 NumFi = ent.get()
 global f_Num
 global math
 math = "Div"
 f_Num = int(NumFi)
 ent.delete(0,END)

def ButtonEqual():
 sec_num = ent.get()
 ent.delete(0,END)
 if math == "Add":
     ent.insert(0,f_Num + int(sec_num))
 if math == "Min":
     ent.insert(0,f_Num - int(sec_num))
 if math == "Div":
     ent.insert(0,f_Num / int(sec_num))
 if math == "Mult":
     ent.insert(0,f_Num * int(sec_num))
 if math == "Sqr":
     ent.insert(0,f_Num + int(sec_num))


 








myButton1 = tkinter.Button(root,text ="1",padx=40,pady=20,command=lambda: NumIn(1),fg="green",bg="black")
myButton2 = tkinter.Button(root,text ="2",command=lambda: NumIn(2),padx=40,pady=20,fg="green",bg="black")
myButton3 = tkinter.Button(root,text ="3",command=lambda: NumIn(3),padx=40,pady=20,fg="green",bg="black")
myButton4 = tkinter.Button(root,text ="4",command=lambda: NumIn(4),padx=40,pady=20,fg="green",bg="black")
myButton5 = tkinter.Button(root,text ="5",command=lambda: NumIn(5),padx=40,pady=20,fg="green",bg="black")
myButton6 = tkinter.Button(root,text ="6",command=lambda: NumIn(6),padx=40,pady=20,fg="green",bg="black")
myButton7 = tkinter.Button(root,text ="7",command=lambda: NumIn(7),padx=40,pady=20,fg="green",bg="black")
myButton8 = tkinter.Button(root,text ="8",command=lambda: NumIn(8),padx=40,pady=20,fg="green",bg="black")
myButton9 = tkinter.Button(root,text ="9",command=lambda: NumIn(9),padx=40,pady=20,fg="green",bg="black")
myButton0 = tkinter.Button(root,text ="0",command=lambda: NumIn(0),padx=40,pady=20,fg="green",bg="black")

ButtonPlus = tkinter.Button(root,text ="+",command=ButtonPlus,padx=40,pady=20,fg="green",bg="black")
ButtonMinus = tkinter.Button(root,text ="-",command=ButtonMinus,padx=40,pady=20,fg="green",bg="black")
ButtonEqual = tkinter.Button(root,text ="=",command=ButtonEqual,padx=40,pady=20,fg="green",bg="black")
ButtonMulti = tkinter.Button(root,text ="x",command=ButtonMulti,padx=40,pady=20,fg="green",bg="black")
ButtonDivi = tkinter.Button(root,text ="/",command=ButtonDivi,padx=40,pady=20,fg="green",bg="black")
ButtonClear = tkinter.Button(root,text ="Del",command=ButtonClear,padx=40,pady=20,fg="green",bg="black")


myButton0.grid(row=4,column=0)
ButtonPlus.grid(row=4,column=1)
ButtonClear.grid(row=4,column=3)
ButtonEqual.grid(row=4,column=2)
ButtonMinus.grid(row=3,column=0)
ButtonMulti.grid(row=2,column=0)
ButtonDivi.grid(row=1,column=0)

myButton1.grid(row=3,column=1)
myButton2.grid(row=3,column=2)
myButton3.grid(row=3,column=3)

myButton4.grid(row=2,column=1)
myButton5.grid(row=2,column=2)
myButton6.grid(row=2,column=3)

myButton7.grid(row=1,column=1)
myButton8.grid(row=1,column=2)
myButton9.grid(row=1,column=3)



root.mainloop()

