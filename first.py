import io
import tkinter
from tkinter import messagebox
import tkinter as tk

from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import cv2
import numpy as np
from PIL import Image, ImageTk


import sys

from numpy.ma.extras import row_stack, column_stack

print(sys.version)


import PIL
from PIL import Image, ImageTk
from PIL import Image as PILImage


#root = tkinter.Tk()
#root.withdraw()

from tkinter import *
from tkinter import messagebox
#win = Tk()
#win.geometry("200x200")
#messagebox.showwarning("Warning","Proces was killed")
#messagebox.showinfo("message","time to beddddddddddddd")
#win.mainloop()
name="brwa"
#print("hello \n\t"+name)
#print(len(name))
#print(name[0])
#print(name.index('r'))

#print(name[0:3])
#print(name[-2])
#print(name.upper())
#print(name.isupper())
#print(name.replace("brwa","sawin"))

from math import *
num1=4
num2=2
num3=16
r= num1**num2

#print(r)
#print(abs(num3))
#print(min(1,9,8,4,0))
#print(round(1.6))
#print(pi)

#innnn=input("enter ur name")
#print(innnn)


#n1=int(input("enter firsrt num "))
#n2=int(input("enter second num "))
#result=n1+n2
#print(result)

'''colors=["red","blue","green"]
cars=["bmw","toyota","mersidz","nissan"]
nml=[4,2,6,1,0]
print(colors[0:4])

colors[0]="black"
#print(color,car)
colors.extend(cars)
print("New List :- ")
print(colors)

colors.append("pink")
colors.append("pink")
print(colors)

colors.insert(1,"red")
print(colors)

#colors.remove("pink")
print(colors)
#colors.clear()
#print(colors)
#d=colors.pop()

#print(colors,"\n the delete one=",d)
print(colors.index("black"))
print(colors.count("pink"))
colors.sort()
nml.sort()
print(colors)
print(nml)'''
'''cp=colors.copy()
print(cp)'''
'''print(len(colors))
print(len(nml))
#tuples & sets
tb=("ardalan","mohammed","ahmed","karwan",1,1,True,["hemn","brwa"])#it is constant u can not change and delete elements
print(tb)
s1={10,1,9,2,8,3,7,4,6,5,0,-1,1,22,33}#distinct or unique values
s2={"sawin","brwa","ahmed","cc","sawin","1"}
s2.add("mohammed")
print(s1,s2)
print("list & set together")
list1=set([55,22,33,11,10,7,4])
print(list1)
print("union & intersection")
print(s1.union(s2))
print(s1 | s2)
print(s1.difference(list1))
print(s1 - list1)
print(s1.symmetric_difference(list1))
print(s1 ^ list1)
print(s1.intersection(list1))
print(s1 & list1)

def hello(name,age):
    print("hello "+name+" ur age is "+str(age))

hello("sawin",29)

def math1(num1,num2):
    print("reult of addition ="+str(num1+num2))
    print("reult of subtraction =" + str(num1 - num2))
    print("reult of multiplication =" + str(num1 * num2))
    print("reult of division =" + str(num1/num2))
math1(5,3)

def sum(num1,num2):
    result=num1+num2
    return result

print(sum(9,1))

x=2
y=3
if x>y:
    print("x greater than y")
elif x==y:

    print("x equale y")

else:
    print("x less than y")

user="brwa"
passs="sawin"'''

'''u=input("enter user name:")
p=input("enter password:")


if u==user and p==passs:
   print("login succesful")
   messagebox.showinfo("message", "login succesful")


else:
    if u!=user:
        print("wrong username")
    else:
        print("wrong password")'''

'''myd={1:'Jan',2:'Feb',3:'Mar',4:'Apr'}
print(myd.get(0))
#messagebox.showinfo("",myd.get(9,"value not exist"))
print(myd.keys())
print(myd.values())
myd.update({5:'may'})
print(myd)
myd.pop(2)
print(myd)
myd.clear()
print(myd)'''

'''num=int(input("enter num of rows :"))
row=0
while row<num:
    star=row+1
    while star>0:
          print("*",end="")
          star=star-1
    row+=1
    print()

for i in range(1,num):
    print(i)



for i in range(len(tb)):
     print(tb[i])

def fun(bas,num):
    r=1
    for i in range (num):
        r*=bas
    return r

print("result =")
print(fun(3,3))


list2=[[1,2,3],[4,5,6,],[7,8,9]]
print("listttttt ")
for row in list2:
    for column in row:
         print(column)'''
#catching errorrrrrrrrrr
'''try:
    s=int(input("enter number"))
    print(s)

except:
    print("please enter num not str")

#reading fileeeeeeeeee
file=open("C:\\Users\\saabdullah\\Desktop\\ptest.txt","r")
#print(file.read())
#print(file.readline())
#print(file.readline())
print(file.readlines()[1])'''
def button_clicked():
    print("Button clicked!")
root=tk.Tk()
#root.geometry("600x600")
root.config(padx=30,pady=30)

def display_image(file_path):
    '''image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo
    status_label.config(text=f"Image loaded: {file_path}")'''
    # display_image(file_path)
    im= cv2.imread(file_path)
    imm=cv2.resize(im,(200,200))
    #cv2.resizeWindow("testtttt", 700, 200)
   #canvas = Canvas(root, width=1000, height=1000)
    #img = ImageTk.PhotoImage(file=file_path)
    #canvas.create_image(0, 0,  image=img,anchor=NW)
    #canvas.pack()
    #root.mainloop()

    img_rgb = cv2.cvtColor(imm, cv2.COLOR_BGR2RGB)
    print("eraaaaaaaa")
    im1 = PILImage.fromarray(img_rgb)
    im1.thumbnail((800, 800))
    # img_pil = Image.fromarray(im,mode="CMYK")
    img_tk = ImageTk.PhotoImage(im1)
    label = Label(root, image=img_tk)
   # label.pack()
    label.grid(row=1,column=0)
    root.mainloop()
    #cv2.imshow("Original",imm)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def lowpass_filtter(file_path):
    '''image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo
    status_label.config(text=f"Image loaded: {file_path}")'''
    # display_image(file_path)
    im= cv2.imread(file_path)
    imm=cv2.resize(im,(200,200))
    kernel=np.ones((12,12),np.float32)/144
    conimg=cv2.filter2D(imm,-1,kernel)
    #cv2.resizeWindow("testtttt", 700, 200)
    img_rgb = cv2.cvtColor(conimg, cv2.COLOR_BGR2RGB)
    print("eraaaaaaaa")
    im=PILImage.fromarray(img_rgb)
    im.thumbnail((800, 800))
    #img_pil = Image.fromarray(im,mode="CMYK")
    img_tk = ImageTk.PhotoImage(im)
    label = Label(root, image=img_tk)
    #label.pack()
    label.grid(row=1,column=1)
    root.mainloop()
   # label.grid(row=4,column=5)
    #cv2.imshow("LowPassResult",conimg)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def open_image_lowPass():
    file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        print("image is here")
        print(file_path)
        lowpass_filtter(file_path)

def open_image():
    file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        print("image is here")
        print(file_path)
        image=display_image(file_path)
        #image_label = tkinter.Label(root,image )
        #image_label.pack()






button=tk.Button(root,text="Original",
                 command=open_image
)

button1=tk.Button(root,text="lowPass",
                 command=open_image_lowPass
)

button2=tk.Button(root,text="heightPass",
                 command=open_image
)

button.grid(row=0,column=0)
button1.grid(row=0,column=1)
#button.pack(padx=50, pady=100)
#button1.pack(padx=50, pady=50)
#button2.pack(padx=200, pady=100)


root.mainloop()



'''class ImageViewer:
    def __init__(self, root, image_filename):
        self.root = root
        self.image_filename = image_filename

        self.root.title('ImageViewer')
        self.root.geometry('400x350')

        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.place(x=10, y=10)

        self.btnView = tk.Button(text='View', command=self.view_image)
        self.btnView.place(x=20, y=265)

        self.btnClose = tk.Button(text='close', command=self.root.destroy)
        self.btnClose.place(x=65, y=265)

    def view_image(self):
        self.img = ImageTk.PhotoImage(Image.open(self.image_filename))  # Keep ref to image.
        self.canvas.create_image(20, 20, anchor=tk.NW, image=self.img)


def main(image_filename):
    root = tk.Tk()
    ImageViewer(root, image_filename)
    root.mainloop()

if __name__ == '__main__':
    main(r"C:/Users/saabdullah/Documents/Snapchat-124690494.jpg")
    '''
