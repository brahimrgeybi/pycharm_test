from tkinter import *
from PIL import Image, ImageTk
import webview

app = Tk()
app.geometry('1000x600+200+50')
app.title("Python Project")
icon_path = 'C:\\Users\\HP ELITEBOOK\\PycharmProjects\\pythonProject1\\ph\\icone.ico'

img = Image.open(icon_path)
icon = ImageTk.PhotoImage(img)
app.tk.call('wm', 'iconphoto', app._w, icon)
app.configure(background='whitesmoke')


def facebook():
    url = 'https://web.facebook.com/'

    webview.create_window(
        '[Facebook]',
        url,
        width=815,
        height=560,
        resizable=True,
        background_color='#D8D8D8',
        x=390, y=120, zoomable=True
    )
    webview.start()


def tiktok():
    url = 'https://www.tiktok.com/'

    webview.create_window(
        '[tiktok]',
        url,
        width=815,
        height=560,
        resizable=True,
        background_color='#D8D8D8',
        x=390, y=120, zoomable=True
    )
    webview.start()


def Github():
    url = 'https://github.com/login'
    webview.create_window(
        '[Github]',
        url,
        width=815,
        height=560,
        resizable=True,
        background_color='#D8D8D8',
        x=390, y=120, zoomable=True
    )
    webview.start()


def youtube():
    url = 'https://www.youtube.com/'
    webview.create_window(
        '[youtube]',
        url,
        width=815,
        height=560,
        resizable=True,
        background_color='#D8D8D8',
        x=390, y=120, zoomable=True
    )
    webview.start()


title1 = Label(app, text=' social Application Systeme',
               fg='black', bg='white',
               font=('Courier', 16))
title1.pack(fill=X)

img = Image.open('C:\\Users\\HP ELITEBOOK\\PycharmProjects\\pythonProject1\\ph\\light2x.png')
logo = ImageTk.PhotoImage(img)
label = Label(app, image=logo, bg='whitesmoke')
label.place(x=2400, y=85, width=700, height=400)

label.pack()

title2 = Label(app, text='Application de médias sociaux',
               fg='black', bg='whitesmoke',
               font=('Courier', 26, 'bold'))
title2.place(x=290, y=520)

title2.pack(fill=X)

# --------------Sidbar-------------------
side = Frame(app, width=180, height=590, bg='white',
             bd=0, relief=GROOVE)
side.place(x=0, y=24)

side_title = Label(side, text='DrRako.io', fg='black',
                   bg='white',
                   font=('Courier', 13))
side_title.place(x=5, y=10)

# -----------------------IMAGE ----------
profil = Image.open('C:\\Users\\HP ELITEBOOK\\PycharmProjects\\pythonProject1\\ph\\user.png')
profil1 = ImageTk.PhotoImage(profil)

fb = Image.open('C:\\Users\\HP ELITEBOOK\\PycharmProjects\\pythonProject1\\ph\\fc1.png')
fb1 = ImageTk.PhotoImage(fb)

tik = Image.open('C:\\Users\\HP ELITEBOOK\\PycharmProjects\\pythonProject1\\ph\\tik.png')
tik1 = ImageTk.PhotoImage(tik)

git = Image.open('C:\\Users\\HP ELITEBOOK\\PycharmProjects\\pythonProject1\\ph\\github.png')
git1 = ImageTk.PhotoImage(git)

you = Image.open('C:\\Users\\HP ELITEBOOK\\PycharmProjects\\pythonProject1\\ph\\you.png')
you1 = ImageTk.PhotoImage(you)

B = Button(side, text='Pool d’applications', cursor='hand2',
           image=profil1, compound=TOP,
           width=120,
           bd=0,
           relief=RIDGE,
           bg='white')
B.place(x=25, y=50)

side_title2 = Label(side, text='social app', fg='black',
                    bg='white',
                    font=('Courier', 12))
side_title2.place(x=25, y=190)

B1 = Button(side, text='Facebook',
            cursor='hand2',
            image=fb1, compound=TOP,
            width=130,
            bd=0,
            relief=RIDGE, command=facebook,
            )
B1.place(x=20, y=220)

B2 = Button(side, text='tiktok', cursor='hand2',
            image=tik1, compound=TOP,
            width=130,
            bd=0,
            relief=RIDGE, command=tiktok,
            )

B2.place(x=20, y=280)

B3 = Button(side, text='Github', cursor='hand2',
            image=git1, compound=TOP,
            width=130,
            bd=0,
            relief=RIDGE, command=Github,
            )
B3.place(x=20, y=340)

B4 = Button(side, text='Youtube', cursor='hand2',
            image=you1, compound=TOP,
            width=130,
            bd=0,
            relief=RIDGE, command=youtube
            )
B4.place(x=20, y=400)

app.mainloop()
