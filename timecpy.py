import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import *

# Function to fetch and display data within a time range
def display_data():
    input_source = source_entry.get()
    input_time_from = entry_time_from.get()
    input_time_to = entry_time_to.get()
    try:
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="bus_schedule")
        cursor = connection.cursor()

        # Replace 'your_table' and 'your_time_column' with your actual table name and time column name
        query = "SELECT * FROM details WHERE source = %s AND time BETWEEN %s AND %s"
        cursor.execute(query, (input_source,input_time_from, input_time_to))

        # Clear the Treeview
        for item in tree.get_children():
            tree.delete(item)

          
        
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)

    except mysql.connector.Error as err:
        error_label.config(text=f"Error: {err}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create the main window
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

def search():
    win.destroy()
    import search
Button(win,text="Search",width=35,height=3,bg="#FF8C94",fg="white",bd=0,font=(26),command=search).place(x=624,y=100)

#contact
def contact():
    win.destroy()
    import contact
Button(win,text="Contact us",width=35,height=3,bg="#FF8C94",fg="white",font=(26),bd=0,command=contact).place(x=936,y=100)

label1= Label(win, text="From",bg="#FFD3B5",font=('arial',18)).place(x=330,y=250)
source = StringVar()
source_entry = Entry(win, textvariable=source, width=20,font=('arial',18))
source_entry.place(x=500,y=250)

label2= Label(win, text="To",bg="#FFD3B5",font=('arial',18)).place(x=330,y=310)
to =StringVar()
to_entry=Entry(win, textvariable=to, width=20,font=('arial',18)).place(x=500,y=310)

# Label and entry widgets for user input
label3= Label(win, text="Time",bg="#FFD3B5",font=('arial',18)).place(x=330,y=370)
entry_time_from = tk.Entry(win,width=9,font=('arial',18))
entry_time_from.place(x=500,y=370)


label_time_to = tk.Label(win,  text="to",bg="#FFD3B5",font=('arial',18)).place(x=620,y=370)
entry_time_to = tk.Entry(win, width=9,font=('arial',18))
entry_time_to.place(x=650,y=370)

# Button to trigger data retrieval
search_button = tk.Button(win, text="Search", command=display_data,width=15,height=1,font=(20),bg="#FF8C94",activebackground="#CACFD2")
search_button.place(x=950,y=250)


# Label for displaying errors
error_label = tk.Label(win, text="", fg="red",bg="#FFD3B5")
error_label.place(x=950,y=350)

# Create a Treeview widget
columns = ("ID", "BuaName", "Source", "Destination", "Time")
tree = ttk.Treeview(win, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=250)
tree.place(x=0,y=450)

win.mainloop()
