from tkinter import *

win = Tk()
win.title("Bus time schedule using python")
win.geometry("1250x790")
win.resizable(0,0)
win.configure(bg="#FFD3B5")
titlelabel = Label(win, text="Bus Time Schedule Management",bd=20, relief = RIDGE, fg = "#FF8C94" , bg = "white", font=('arial',30))
titlelabel.pack( side=TOP , fill=X)


label=Label(win,text="Search Buses",bg="#FFD3B5",font=('Script MT Bold', 46, 'bold')).place(x=450,y=300)

#home
def home():
    win.destroy()
    import home
Button(win,text="Home",width=35,height=3,bg="#FF8C94",fg="white",font=(30),bd=0,command=home).place(x=0,y=100)

#about
def about():
    win.destroy()
    import about
Button(win,text="About",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(26),command=about).place(x=312,y=100)
Button(win,text="Search",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(26)).place(x=624,y=100)

#contact
def contact():
    win.destroy()
    import contact
Button(win,text="Contact us",width=35,height=3,bg="#FF8C94",fg="white",font=(26),bd=0,command=contact).place(x=936,y=100)

def search_stop():
    win.destroy()
    import stop
Button(win,text="Search Buses By Stop",width=20,height=2,font=(24),bg="#FF8C94",activebackground="#CACFD2",command=search_stop).place(x=290,y=500)

def search_time():
    win.destroy()
    import timecpy
Button(win,text="Search Buses By Departure Time",width=30,height=2,font=(24),bg="#FF8C94",activebackground="#CACFD2",command=search_time).place(x=690,y=500)

win.mainloop()
