from tkinter import *

win = Tk()
win.resizable(0,0)
win.title("Bus time schedule using python")
win.configure(bg="white")
win.geometry("1250x790")

titlelabel = Label(win, text="Bus Time Schedule Management",bd=20, relief = RIDGE, fg = "#FF8C94" , bg = "white", font=('arial',30))
titlelabel.pack( side=TOP , fill=X)

#home
def home():
    win.destroy()
    import home
Button(win,text="Home",width=35,height=3,bg="#FF8C94",fg="white",font=(30),bd=0,command=home).place(x=0,y=100)

#about
def about():
    win.destroy()
    import about
Button(win,text="About",width=35,height=3,bg="#FF8C94",fg="white",font=(26),bd=0,command=about).place(x=312,y=100)

#search
def search():
    win.destroy()
    import search
Button(win,text="Search",width=35,height=3,bg="#FF8C94",fg="white",font=(26),bd=0,command=search).place(x=624,y=100)


Button(win,text="Contact us",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(26)).place(x=936,y=100)

img2 = PhotoImage(file="contactimg.png")
Label(win,image=img2,bd=0).place(x=0,y=200)

frame=Frame(win,width=450,height=180,bg="lightgrey")
frame.place(x=115,y=550)
text=Label(frame ,text="Contact Us" ,font=(28),bg="lightgrey", fg="red").place(x=160,y=10)
text=Label(frame ,text="Phone No" ,font=(24),bg="lightgrey", fg="black").place(x=70,y=50)
text=Label(frame ,text="123-4567-890" ,font=(24),bg="white", fg="black").place(x=250,y=50)
text=Label(frame ,text="Email" ,font=(22),bg="lightgrey", fg="black").place(x=70,y=90)
text=Label(frame ,text="bus@gmail.com" ,font=(22),bg="white", fg="black").place(x=250,y=90)

frame2=Frame(win,width=450,height=180,bg="lightgrey")
frame2.place(x=680,y=550)
text=Label(frame2 ,text="Social Media" ,font=(28),bg="lightgrey", fg="red").place(x=160,y=10)
text=Label(frame2 ,text="Linkedin" ,font=(24),bg="lightgrey", fg="black").place(x=50,y=50)
text=Label(frame2 ,text="www.linkedin.com/in/localbus" ,font=(24),bg="white", fg="black").place(x=180,y=50)
text=Label(frame2 ,text="Twitter" ,font=(22),bg="lightgrey", fg="black").place(x=50,y=90)
text=Label(frame2 ,text=" @localbus" ,font=(22),bg="white", fg="black").place(x=180,y=90)

win.mainloop()

