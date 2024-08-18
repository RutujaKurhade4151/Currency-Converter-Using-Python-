##CURRENCY CONVERTER
from currency_converter import CurrencyConverter
import tkinter as tk
root=tk.Tk()
root.geometry("500x360")

def clicked():            #function for the conversion
    amount=int(e1.get())
    cur1=e2.get()
    cur2=e3.get()
    a=CurrencyConverter()
    data=a.convert(amount,cur1,cur2)         
    l5=tk.Label(root,text=data,font="verdana 20 bold").place(x=120,y=310)

l1=tk.Label(root,text="Currency Converter",font="verdana 25 bold").place(x=85,y=10)

l2=tk.Label(root,text="Enter amount:" , font="arial 20 bold").place(x=40,y=80)

e1=tk.Entry(root)      #used for entering the amount
  
l3=tk.Label(root,text="From currency:" , font="arial 20 bold").place(x=40,y=140)
e2=tk.Entry(root)

l4=tk.Label(root,text="To currency:" , font="arial 20 bold").place(x=40,y=200)
e3=tk.Entry(root)

b1=tk.Button(root,text="Convert",font="arial 15 bold",command=clicked).place(x=180,y=270)
e1.place(x=300,y=90)
e2.place(x=300,y=150)
e3.place(x=300,y=210)


root.mainloop()