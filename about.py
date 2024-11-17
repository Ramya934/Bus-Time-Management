from tkinter import *

win = Tk()

win.title("Bus time schedule using python")
win.resizable(0,0)
win.geometry("1250x790")
win.configure(bg="white")

frame =Frame(win,width=669,height=325,bg="#fff" ,highlightthickness=0)
frame.place(x=0,y=200)

text=Label(frame ,bg="#fff",text="Welcome you !!",font=(20)).place(x=30,y=30)
text=Label(frame ,bg="#fff",text="Local bus time management aims to provide better public",font=(20)).place(x=70,y=80)
text=Label(frame ,bg="#fff",text="transportation services to residents and visitors. It helps create ",font=(20)).place(x=10,y=120)
text=Label(frame ,bg="#fff",text="a more efficient and user-friendly transportation network.",font=(20)).place(x=10,y=160)
text=Label(frame ,bg="#fff",text="By accurately tracking bus arrival times and optimizing schedules, ",font=(20)).place(x=10,y=200)
text=Label(frame ,bg="#fff",text="local bus time management systems reduce passenger waiting times",font=(20)).place(x=10,y=240)
text=Label(frame ,bg="#fff",text="at bus stops. This enhances the overall passenger experience.",font=(20)).place(x=10,y=280)

img2 = PhotoImage(file="aboutimg2.png")
Label(win,image=img2,bd=0).place(x=10,y=530)

frame1 =Frame(win,width=700,height=200,bg="#fff" ,highlightthickness=0)
frame1.place(x=500,y=550)

text=Label(frame1 ,bg="#fff",text="Many bus time management systems offer real-time updates to passenger",font=(20)).place(x=10,y=20)
text=Label(frame1 ,bg="#fff",text="allowing them to track buses in real - time using mobile apps or websites.",font=(20)).place(x=10,y=60)
text=Label(frame1 ,bg="#fff",text="This feature is especially  valuable during  adverse weather conditions or",font=(20)).place(x=10,y=100)
text=Label(frame1 ,bg="#fff",text="unexpected delays",font=(20)).place(x=10,y=140)


titlelabel = Label(win, text="Bus Time Schedule Management",bd=20, relief = RIDGE, fg = "#FF8C94" , bg = "white", font=('arial',30))
titlelabel.pack( side=TOP , fill=X)

#home
def home():
    win.destroy()
    import home
Button(win,text="Home",width=35,height=3,bg="#FF8C94",fg="white",font=(30),bd=0,command=home).place(x=0,y=100)

#about
Button(win,text="About",width=35,height=3,bg="#FF8C94",fg="white",font=(26),bd=0).place(x=312,y=100)
#search
def search():
    win.destroy()
    import search
Button(win,text="Search",width=35,height=3,bg="#FF8C94",fg="white",font=(26),bd=0,command=search).place(x=624,y=100)

#contact
def contact():
    win.destroy()
    import contact
Button(win,text="Contact us",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(26),command=contact).place(x=936,y=100)

img = PhotoImage(file="aboutimg3.png")
Label(win,image=img,bd=0).place(x=670,y=220)



win.mainloop()
