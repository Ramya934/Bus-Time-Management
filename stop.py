from tkinter import *
import mysql.connector
from tkinter import ttk

# MySQL connection configuration
con=mysql.connector.connect(user = "root",password= "",host="localhost",database="bus_schedule")

# Connect to the database
#if con:
   # print("connected")
#else:

# Function to fetch and display data based on user input
def display_data():
    input_source = source_entry.get()
    try:
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="bus_schedule")
        cursor = connection.cursor()

        # Replace 'your_table' and 'your_source_column' with your actual table name and source column name
        query = f"SELECT * FROM details WHERE source = %s"
        cursor.execute(query, (input_source,))
        data = cursor.fetchone()

        if data:
            # Clear the Treeview
            tree.delete(*tree.get_children())
            
            # Insert the data into the Treeview
            for row in cursor.fetchall():
                tree.insert("", "end", values=row)
        else:
            error_label.config(text="No data found for the provided source name")
    

       
    except mysql.connector.Error as err:
        error_label.config(text=f"Error: {err}")
    



win = Tk()
win.title("Bus time schedule using python")
win.geometry("1250x790")
win.resizable(0,0)
win.configure(bg="#FFD3B5")

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

Button(win,text="About",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(26),command=about).place(x=312,y=100)

#search
def search():
    win.destroy()
    import search
Button(win,text="Search",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(26),command=search).place(x=624,y=100)

#contact
def contact():
    win.destroy()
    import contact
Button(win,text="Contact us",width=35,height=3,bg="#FF8C94",fg="white",font=(26),bd=0,command=contact).place(x=936,y=100)

label1=Label(win, text="Stop Name",bg="#FFD3B5",font=('arial',18)).place(x=330,y=220)

source_entry = Entry(win,  width=20,font=('arial',18))
source_entry.place(x=500,y=220)


Button(win,text="Search Buses",width=15,height=1,font=(20),bg="#FF8C94",activebackground="#CACFD2",command=display_data).place(x=500,y=290)


# Create a Treeview widget
columns = ( "ID","busname", "source", "destination","timing")
tree = ttk.Treeview(win, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=250)
tree.place(x=10,y=350)


win.mainloop()
