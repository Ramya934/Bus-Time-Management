from tkinter import *

win = Tk()
win.title("Bus time schedule using python")
win.geometry("1250x790")
win.configure(bg="#fff")
win.resizable(0,0)
titlelabel = Label(win, text="Bus Time Schedule Management",bd=20, relief = RIDGE, fg = "#FF8C94" , bg = "white", font=('arial',30))
titlelabel.pack( side=TOP , fill=X)

#home
Button(win,text="Home",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(30)).place(x=0,y=100)

#about
def about():
    
        win.destroy()
        import about
Button(win,text="About",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(30),command=about).place(x=312,y=100)

#search
def search():
    
         win.destroy()
         import search
Button(win,text="Search",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(30),command=search).place(x=624,y=100)

#contact
def contact():
   
        win.destroy()
        import contact
Button(win,text="Contact us",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(30),command=contact).place(x=936,y=100)
#Button(win,width=70,height=3,bg="#FF8C94",fg="white",bd=0,font=(30),activebackground="#FF8C94").place(x=600,y=100)

bg = PhotoImage(file = "bus2.png")
canvas = Canvas( win,width = 1250,height = 600,bg="#fff",bd=0)              
canvas.place(x=0,y=200)
canvas.create_image( 40,0, image = bg, anchor = "nw")



win.mainloop()
