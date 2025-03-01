import tkinter as tk

from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import cv2
import numpy as np
##f=open("test.txt","w")
##f.write("sawinnnnnnnnnn")
##f.close()


v=lambda x,y : x+y

print(v(2,4))
print((lambda x: x**2)(4))

class human:
    name='sawin'
    age=29

    def __init__(self):
        print("constructor invoked")


    def sleep(self,name,age):
        print(name)
        print(age)



#human=human()
#human.sleep("brwa",33)

class cal:

    def sum(self):
         r=int(self.entry1.get())+int(self.entry2.get())
         self.Lresult1.config(text=r)
         print(" =============== ",str(r))
    def sub(self):
        r = int(self.entry1.get()) - int(self.entry2.get())
        self.Lresult1.config(text=r)
        print(" ")
    def mul(self):
        r = int(self.entry1.get()) * int(self.entry2.get())
        self.Lresult1.config(text=r)
        print("")
    def div(self):

        r = int(self.entry1.get()) / int(self.entry2.get())
        self.Lresult1.config(text=r)

    def __init__(self,root):
        self.root=root
        self.root.title('Calculator')
        self.root.geometry("250x300")
        self.root.config(padx=30,pady=30)

        #lablessssssssssss
        Lnum1 = tk.Label(self.root, text="Num 1")
        Lnum1.grid(row=0,column=0)

        Lnum2 = tk.Label(self.root, text="Num 2")
        Lnum2.grid(row=1, column=0)

        Lresult = tk.Label(self.root, text="Result")
        Lresult.grid(row=2, column=0)

        self.Lresult1 = tk.Label(self.root, text="0")
        self.Lresult1.grid(row=2, column=1)

        #Entryesssssssss
        self.entry1=tk.Entry(self.root)
        self.entry1.insert(0,"0")
        self.entry1.grid(row=0,column=1)
        self.entry2 = tk.Entry(self.root)
        self.entry2.insert(0, "0")
        self.entry2.grid(row=1, column=1)

        #buttonssssssssss
        button = tk.Button(self.root, text="+",
                           command=self.sum,padx=20,pady=20
                           )

        button1 = tk.Button(self.root, text="-",
                            command=self.sub,padx=20,pady=20
                            )

        button2 = tk.Button(self.root, text="x",
                            command=self.mul,padx=20,pady=20
                            )

        button3 = tk.Button(self.root, text="/",
                            command=self.div,padx=20,pady=20
                            )
        button.grid(row=4,column=0)
        button1.grid(row=4,column=1)
        button2.grid(row=5,column=0)
        button3.grid(row=5,column=1)
        self.root.mainloop()



root = tk.Tk()
cal=cal(root)


