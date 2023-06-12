from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pymysql

class Admin_window:
    def __init__(self, root):
        #----------window----------
        self.root = root
        self.root.title("Admin")	  
        self.root.attributes('-fullscreen',True)
        self.root.configure(bg="black")
                
        #----------admin label----------
        self.admin = Label(self.root, text="Admin", bg="black", fg="red", font="georgia 30 bold").place(x=700,y=150)

        #----------username entry----------
        username = Label(self.root, text="Username", bg="black", fg="white", font="georgia 15 bold").place(x=720,y=295)
        self.username_entry = Entry(self.root, font="verdana 13", bg="lightgrey")
        self.username_entry.place(x=600,y=325,width=350,height=35)

        #----------password entry----------
        passwd = Label(self.root, text="Password", bg="black", fg="white", font="georgia 15 bold").place(x=725,y=385)
        self.passwd_entry = Entry(self.root, show='*', font="verdana 13", bg="lightgrey")
        self.passwd_entry.place(x=600,y=415,width=350,height=35)

        #----------login button----------
        button_login = Button(root, command=self.admin_login, text="Login", cursor="hand2", width=20, height=1, bg="red", bd=0, fg="white", font="georgia 15 bold").place(x=690,y=525,width=180,height=40)


    def admin_login(self):
        if self.username_entry.get()=="" or self.passwd_entry.get()=="":
            messagebox.showerror("Error","All fields are required.", parent=self.root)
        else:
            try:
                mydb = pymysql.connect(user='root', host='localhost', passwd='')
                mycursor = mydb.cursor()
                mycursor.execute("create database if not exists AI_Surveillance_System")
                mycursor.execute("use AI_Surveillance_System")
                mycursor.execute("create table if not exists admin (username varchar(50), password varchar(50))")
                mycursor.execute("insert into admin values ('1','1')")
                mycursor.execute("select * from admin where username=%s and password=%s", (self.username_entry.get(),self.passwd_entry.get()))
                row = mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid username or password.", parent=self.root)
                else:
                    self.root.destroy()
                    import register
                mydb.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}", parent=self.root)


root = Tk()
obj = Admin_window(root)
root.mainloop()
