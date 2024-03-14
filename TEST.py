import os
import r1
from tkinter import *
from tkinter import messagebox
import cv2
root = Tk()
root.geometry('290x500')
root.title('Screen lock[Rakwan]')
root.iconbitmap('icon.ico')
root.resizable(False,False)
root.attributes('-alpha',0.9)

#---- Define ----

def one(enent=None):
    one = 1
    En1.insert(END,one)
def tow(enent=None):
    tow =2
    En1.insert(END,tow)
def three(enent=None):
     three= 3
     En1.insert(END,three)
def four(enent=None):
     four=4
     En1.insert(END,four)
def five(enent=None):
     five=5
     En1.insert(END,five)
def six(enent=None):
     six=6
     En1.insert(END,six)
def seven(enent=None):
     seven=7
     En1.insert(END,seven)
def eight(enent=None):
     eight=8
     En1.insert(END,eight)
def nine(enent=None):
     nine=9
     En1.insert(END,nine)
def zero(enent=None):
     zero=0
     En1.insert(END,zero)
def reset(enent=None):
    En1.delete('0',END)
    error1.place(x=1200,y=1200)


def ok(enent=None):
    passow = En1.get()

    if passow == '123456':
        os.startfile('C:\\Users\\HP ELITEBOOK\\PycharmProjects\\pythonProject1\\r1.py')
    if passow != '123456':
        global error1
        error1 = Label(F1,text='Error Password !!',fg='red',bg='white')
        error1.place(x=100,y=100)
        s = cv2.VideoCapture(0)
        ret, image = s.read()
        cv2.imwrite('lock.png', image)
        del (s)
#---- title ----

title = Label(root,text='Screen Lock',fg='white',bg='#D82148',font=('Stencil',21))
title.pack(fill=X)

#---- Frame tools ----

F1 = Frame(root,bg='white')
F1.place(x=1,y=38,width=298,height=460)

title1 = Label(F1,text='Enter Password',fg='black',bg='white',font=('Stencil',15))
title1.place(x=55,y=10)
En1 = Entry(F1,justify=CENTER,font=('Impact',25),bd=2,relief=RIDGE,width=10,bg='white',fg='#D82148')
En1.place(x=50,y=50)

#---- Buttons ----

b1 = Button(F1,text='1',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=one)
b1.place(x=20,y=130)
b2 = Button(F1,text='2',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=tow)
b2.place(x=110,y=130)
b3 = Button(F1,text='3',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=three)
b3.place(x=200,y=130)

b4 = Button(F1,text='4',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=four)
b4.place(x=20,y=215)
b5 = Button(F1,text='5',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=five)
b5.place(x=110,y=215)
b6 = Button(F1,text='6',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=six)
b6.place(x=200,y=215)

b7 = Button(F1,text='7',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=seven)
b7.place(x=20,y=300)
b8 = Button(F1,text='8',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=eight)
b8.place(x=110,y=300)
b9 = Button(F1,text='9',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=nine)
b9.place(x=200,y=300)

b0 = Button(F1,text='0',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=zero)
b0.place(x=110,y=385)
bR = Button(F1,text='X',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',fg='#D82148',command=reset)
bR.place(x=20,y=385)
bOk = Button(F1,text='ok',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',fg='green',command=ok)
bOk.place(x=200,y=385)



root.mainloop()