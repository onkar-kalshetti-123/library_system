from tkinter import *
from PIL import  ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import smtplib
import datetime
from tkcalendar import *

root=Tk()
class Mainwindow():
    def __init__(self,root):
            self.root=root
            self.root.title("STAFF LOGIN")
            self.root.geometry("1200x700+200+70")
            self.root.config(bg='black')
            self.root.resizable(False,False)
            self.root.grab_set()
            self.Login_label = Label(self.root, text="Library manage system", font=("Elephant", 15, 'bold'), bg='white')
            self.Login_label.place(x=200, y=5)
            self.photo=ImageTk.PhotoImage(file="best-colors-websites-1.jpg")
            self.blabel=Label(self.root,image=self.photo)
            self.blabel.pack()
            self.frame=Frame(self.root)
            self.frame.place(x=390,y=170,width=400,height=450)

#=============LABELS AND BUTTONS ================================================#

            self.photo0 = ImageTk.PhotoImage(file="unnamed.png")
            self.blabel0 = Label(self.root, image=self.photo0,bg='gold2')
            self.blabel0.place(x=0,y=0,width=1200,height=100)


            self.label=Label(self.frame,text="UserID",font=("Andalus",15,'bold'),fg='gray',bg='#F0F8FF')
            self.label.place(x=80,y=50)

            self.Uentry=Entry(self.frame,font=('times new roman',15))
            self.Uentry.place(x=80,y=100,width=250)

            self.label = Label(self.frame, text="PASSWORD", font=("Andalus", 15,'bold'),bg='#F0F8FF',fg='gray')
            self.label.place(x=80, y=150)

            self.pentry = Entry(self.frame,show='*', font=('times new roman', 15))
            self.pentry.place(x=80, y=200,width=250)

            self.button=Button(self.frame,text="Login",bg='#F0F8FF',activebackground='#00B0F0',activeforeground="white",fg='gray',font=('Arial Rounded MT Bold',15,'bold'),cursor='hand2',command=self.admin_logindatabase)
            self.button.place(x=80,y=250,height=35,width=250)

            self.fbutton=Button(self.frame,text="Forget Password?",cursor='hand2',command=self.admin_forget_function,font=('times new roman',13,),fg='gray',bg='#F0F8FF'
                                ,bd=0,activebackground='brown',activeforeground='brown')
            self.fbutton.place(x=100,y=350,width=130)

    #===================== FORGET PASSWORD FUNCTION =========================#

    def admin_forget_function(self):
        if self.Uentry.get() == '':
            messagebox.showerror("Error", "Please Enter Email Address To Change Your Password")
        else:
            con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
            cur = con.cursor()
            print('sss coonct')
            cur = con.cursor()
            print('sss coonct')
            cur.execute('SELECT * FROM admin_data WHERE User_ID=%s', self.Uentry.get())
            row = cur.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Please Enter Valid Email Address To Change Password')
            else:
                con.commit()
                con.close()
                fscreen = Toplevel()
                self.fscrren = fscreen
                self.fscrren.title('FORGET PASSWORD')
                self.fscrren.geometry('500x400+475+140')
                self.fscrren.focus_force()
                self.fscrren.grab_set()
                self.fscrren.resizable(False, False)
                self.photo2 = ImageTk.PhotoImage(file="wooden-table-with-blurred-background_1134-14.jpg")
                self.blabel2 = Label(self.fscrren, image=self.photo2)
                self.blabel2.pack()

                self.Newpassword_label = Label(self.fscrren, text="New Password", font=("Andalus", 15), fg='black',
                                               bg='silver')
                self.Newpassword_label.place(x=150, y=50)

                self.Newpass_entry = Entry(self.fscrren, font=('times new roman', 15), bg="#ECECEC")
                self.Newpass_entry.place(x=150, y=120, width=250)

                self.confirmpass_label = Label(self.fscrren, text="Confirm Password", fg='black', font=("Andalus", 15),
                                               bg='silver')
                self.confirmpass_label.place(x=150, y=190)

                self.confpass_entry = Entry(self.fscrren, font=('times new roman', 15), bg='#ECECEC')
                self.confpass_entry.place(x=150, y=260, width=250)

                self.submitbutton = Button(self.fscrren, text="Submit", cursor='hand2',
                                           command=lambda: self.admin_reset_password(), font=('times new roman', 13),
                                           bg='brown', fg='white', bd=0, activebackground='#00B0F0',
                                           activeforeground="white")
                self.submitbutton.place(x=150, y=310, width=250)

        # =====================DATABASE QUERY FOR FORGET PASSWORD =======================#

    def admin_reset_password(self):
        if self.Newpass_entry.get == '':
            messagebox.showinfo("INFORMATION", "please Enter New Password")
        elif self.Newpass_entry.get() != self.confpass_entry.get():
            messagebox.showwarning("ERROR", "Password Does Not Match")
        else:
            con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
            cur = con.cursor()
            print('sss coonct')
            cur = con.cursor()
            cur.execute("UPDATE admin_data set Password=%s WHERE User_ID=%s",
                        (self.Newpass_entry.get(), self.Uentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("SUCCESS", "Password Change Succeessfully")
            self.fscrren.withdraw()

#================================LOgin For stafff database================================#
    def admin_logindatabase(self):
        if self.Uentry.get == '':
            messagebox.showwarning("Warning", 'Please Enter Email Address')
        elif self.pentry.get() == '':
            messagebox.showwarning("Warning", 'Please Enter Password')
        else:
            con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
            cur = con.cursor()
            print('sss coonct')

            print('ssss')
            cur.execute("SELECT * FROM admin_data WHERE User_ID=%s and Password=%s",(self.Uentry.get(),self.pentry.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showwarning("Warning", 'Please Enter Register User_Id Address Or Password')
            else:
                con.commit()
                con.close()
                self.root.withdraw()
                lastroot = Toplevel()
                self.lastroot = lastroot
                self.lastroot.title("MANAGE BOOKS")
                self.lastroot.geometry('1100x550+250+80')
                self.lastroot.configure(bg='gold2')
                self.lastroot.resizable(False,False)
                self.photo3 = ImageTk.PhotoImage(file="workbench.jpg")
                self.blabel3 = Label(self.lastroot, image=self.photo3)
                self.blabel3.place(x=0,y=50)

                self.blabels = Label(self.lastroot,text='!!!!!!!!!!!=======================!!!!!!!!!!!',bg='gold2',font=('times new roman',20,'bold'))
                self.blabels.place(x=300,y=0)

                self.AddBook= Button(self.lastroot, text="ADD BOOKS", cursor='hand2',
                                           font=('times new roman', 13,'bold'), fg='black', bg='white', bd=0,
                                           activebackground='#00B0F0', activeforeground="white",command=lambda:self.AddBook_database())
                self.AddBook.place(x=430, y=180, width=250)

                self.BorrowBook = Button(self.lastroot, text="ISSUE BOOKS", cursor='hand2',
                                      font=('times new roman', 13, 'bold'), fg='black', bg='white', bd=0,
                                      activebackground='#00B0F0', activeforeground="white",command=lambda:self.Borrow_book())
                self.BorrowBook.place(x=430, y=230, width=250)

                self.ReturnBook = Button(self.lastroot, text="Return BOOKS", cursor='hand2',
                                      font=('times new roman', 13, 'bold'), fg='black', bg='white', bd=0,
                                      activebackground='#00B0F0', activeforeground="white",command=lambda:self.returnbook())
                self.ReturnBook.place(x=430, y=270, width=250)

                self.DeleteBook = Button(self.lastroot, text="Delete BOOKS", cursor='hand2',
                                      font=('times new roman', 13, 'bold'), fg='black', bg='white', bd=0,
                                      activebackground='#00B0F0', activeforeground="white",command=lambda:self.delete_book_window())
                self.DeleteBook.place(x=430, y=310, width=250)


                self.sendreminder = Button(self.lastroot, text="Send Reminder", cursor='hand2',
                                       font=('times new roman', 13, 'bold'), bg='white', fg='black', bd=0,
                                       activebackground='#00B0F0', activeforeground="white",command=lambda:self.sendreminder1())
                self.sendreminder.place(x=430, y=350, width=250)

                self.Exitwindow = Button(self.lastroot, text="EXIT", cursor='hand2',
                font=('times new roman', 13, 'bold'), bg='white', fg='black', bd=0,
                                               activebackground='#00B0F0', activeforeground="white",command=lambda:self.exitwindow())
                self.Exitwindow.place(x=430, y=400, width=250)


# ============================ exit function =================================#
    def exitwindow(self):
        self.lastroot.withdraw()

##==================================================== ADD BOOK ===========================================##
    def AddBook_database(self):
        AddBook=Toplevel()
        self.AddBook=AddBook
        self.AddBook.title('ADD BOOKS')
        self.AddBook.geometry('900x500+350+140')
        self.AddBook.resizable(False,False)
        self.AddBook.focus_force()
        self.AddBook.grab_set()
        self.photo4 = ImageTk.PhotoImage(file="background-form-old-paper-14013296.jpg")
        self.blabel4 = Label(self.AddBook, image=self.photo4)
        self.blabel4.pack()

        self.label = Label(self.AddBook, text="Enter Book Name", font=("Andalus", 15, 'bold'), fg='gray',bg='#F0F8FF')
        self.label.place(x=330, y=110)

        self.Bookentry = Entry(self.AddBook, font=('times new roman', 15))
        self.Bookentry.place(x=330, y=160, width=250)

        self.label = Label(self.AddBook, text="Enter DEPARTMENT", font=("Andalus", 15, 'bold'), fg='gray',bg='#F0F8FF')
        self.label.place(x=330, y=210)

        self.mycombo3 = ttk.Combobox(self.AddBook, width=30, height=10,state='readonly')
        self.mycombo3['values'] = ['Select', 'Computer Science', 'IT', 'ARTS', 'Commers', 'LANGUAGE', 'OTHER']
        self.mycombo3.place(x=330, y=260)
        self.mycombo3.current(0)

        self.Submit_Name = Button(self.AddBook, text="Submit Book", cursor='hand2',
                               font=('times new roman', 13, 'bold'), fg='gray', bd=0,bg='#F0F8FF',
                               activebackground='#00B0F0', activeforeground="white",command=lambda:self.insert_books())
        self.Submit_Name.place(x=330, y=310, width=250)

#=========================== INSERT BOOK DATABASE  QUERY ========================================#
    def insert_books(self):
        if self.Bookentry.get()=='':
            messagebox.showwarning("Warning","Please Enter Book Name")
        elif self.mycombo3.get()=='':
            messagebox.showwarning("Warning", "Please Enter Book Edition")

        else:
            con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
            cur = con.cursor()
            print('sss coonct')
            print('sss coonct')
            cur.execute("SELECT * FROM books_name WHERE Book_Name=%s and DEPARTMENT=%s",(self.Bookentry.get(),self.mycombo3.get()))
            row=cur.fetchone()
            if row!=None:
                messagebox.showwarning("Warning","BOOK ALREADY SAVE IN DATABASE")
            else:
                insquery="insert into books_name(Book_Name,DEPARTMENT) values ('%s','%s')" % (self.Bookentry.get(),self.mycombo3.get())
                cur.execute(insquery)
                con.commit()
                con.close()
                messagebox.showinfo('Success','Book Add Successfully')

##============================== ISSSUE BOOOK WINDOW =========================##
    def Borrow_book(self):
        Borrowwindow=Toplevel()
        self.Borrowwindow=Borrowwindow
        self.Borrowwindow.title("ISSUE BOOKS")
        self.Borrowwindow.geometry('900x600+345+80')
        self.Borrowwindow.resizable(False,False)
        self.photo5 = ImageTk.PhotoImage(file="1426875.jpg")
        self.blabel5 = Label(self.Borrowwindow, image=self.photo5)
        self.blabel5.pack()

        self.label = Label(self.Borrowwindow, text="ISSUEE BOOKS", font=("Andalus", 15, 'bold'), fg='blue',bg='gold2')
        self.label.place(x=0, y=0,width=900,height=50)

        self.label = Label(self.Borrowwindow, text="IDCARD_NO", font=("Andalus", 15, 'bold'), fg='gray')
        self.label.place(x=150, y=120)

        self.IDCARDentry = Entry(self.Borrowwindow, font=('times new roman', 15))
        self.IDCARDentry.place(x=150, y=170, width=250)

        self.Blabel = Label(self.Borrowwindow, text="Book_NAME", font=("Andalus", 15, 'bold'), fg='gray')
        self.Blabel.place(x=150, y=220)

        self.bookaddDentry = Entry(self.Borrowwindow, font=('times new roman', 15))
        self.bookaddDentry.place(x=150, y=270, width=250)

        self.Blabel = Label(self.Borrowwindow, text="DEPARTMENT", font=("Andalus", 15, 'bold'), fg='gray')
        self.Blabel.place(x=150, y=320)

        self.mycombo2 = ttk.Combobox(self.Borrowwindow, width=30, height=20,state='readonly')
        self.mycombo2['values'] = ['Select', 'Computer Science', 'IT', 'ARTS', 'Commers', 'LANGUAGE', 'OTHER']
        self.mycombo2.place(x=150, y=370)
        self.mycombo2.current(0)

        self.Elabel = Label(self.Borrowwindow, text="EMAIL ADDRESS", font=("Andalus", 15, 'bold'), fg='gray')
        self.Elabel.place(x=150, y=420)

        self.Email_address = Entry(self.Borrowwindow, font=('times new roman', 15))
        self.Email_address.place(x=150, y=470, width=250)

        self.fromlabel = Label(self.Borrowwindow, text="SELECT DATE", font=("Andalus", 15, 'bold'), fg='gray')
        self.fromlabel.place(x=550, y=270)

        self.fromdate=DateEntry(self.Borrowwindow,font=('times new roman', 15),date_pattern='yy-mm-dd')
        self.fromdate.place(x=550,y=320, width=180)

        self.tolabel=Label(self.Borrowwindow, text="TO", font=("Andalus", 15, 'bold'), fg='gray')
        self.tolabel.place(x=550, y=370)

        self.TDateentry = DateEntry(self.Borrowwindow, font=('times new roman', 15),date_pattern='yy-mm-dd' )
        self.TDateentry.place(x=550, y=420, width=180)

        self.BOOKADD= Button(self.Borrowwindow, text="ADDBOOK", cursor='hand2',
                              font=('times new roman', 13, 'bold'), fg='black', bd=0,bg='gold2',
                              activebackground='#00B0F0', activeforeground="white",
                              command=lambda: self.addbookinStudent('ava'))
        self.BOOKADD.place(x=150, y=520, width=250)

#============= ISSUE BOOOK QUERY  ==================#
    def addbookinStudent(self,event):
        if event in('ava'):
            con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
            cur = con.cursor()
            print('sss coonct')
            print('sss coonct')
            cur.execute("SELECT * FROM student_data WHERE student_ID_Card_No=%s", (self.IDCARDentry.get()))
            row3 = cur.fetchone()
            if row3 == None:
                messagebox.showwarning("warning", 'student not found')
                con.commit()
                con.close()
            else:
                con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
                cur = con.cursor()
                print('sss coonct')
                print('sss coonct')
                cur.execute("SELECT * FROM borrow_books WHERE EMAIL_ID=%s",(self.Email_address.get()))
                row9=cur.fetchone()
                if row9!=None:
                    messagebox.showwarning("warning","Email Address Already Exists")
                else:
                     con.commit()
                     cur.execute('SELECT * FROM books_name WHERE BOOK_Name=%s and DEPARTMENT=%s',(self.bookaddDentry.get(), self.mycombo2.get()))
                     row2 = cur.fetchone()
                     if row2 == None:
                         messagebox.showwarning("Warning",'BOOK NOT avaliable')
                     else:
                         cur.execute("insert into borrow_books(STUDENT_ID,EMAIL_ID,BOOK_NAME,DEPARTMENT,FROMDATE,TODATE) values ('%s','%s','%s','%s','%s','%s')" % (self.IDCARDentry.get(),self.Email_address.get(), self.bookaddDentry.get(), self.mycombo2.get(),self.fromdate.get(),self.TDateentry.get()))
                         con.commit()
                         messagebox.showinfo("Successs", 'BOOK ADDED SUCCESSFULLY')
                         print('delete')
                         cur.execute("delete from books_name where Book_Name=%s and DEPARTMENT=%s",
                                                        (self.bookaddDentry.get(), self.mycombo2.get()))
                         con.commit()
                         con.close()
                         print("delete success")
##=====================================================================================================================##

##================================================= RETURN BOOK ========================================================###
    def returnbook(self):
        returnbooks=Toplevel()
        self.returnbooks=returnbooks
        self.returnbooks.title("RETURN BOOKS")
        self.returnbooks.geometry('1530x900+0+0')

        self.returnbooks.resizable(False,False)
        self.returnbooks.focus_force()
        self.returnbooks.grab_set()
        self.photo9 = ImageTk.PhotoImage(file="Finta+Website+Background.png")
        self.blabel9 = Label(self.returnbooks, image=self.photo9)
        self.blabel9.pack()

        self.label = Label(self.returnbooks, text="!!!!!!!!!RETURN BOOKS!!!!!!!!!", font=("Andalus", 15, 'bold'), fg='blue', bg='gold2')
        self.label.place(x=0, y=0, width=1530, height=50)

        self.frame = Frame(self.returnbooks,bg='white')
        self.frame.place(x=20, y=80, width=400, height=680)

        self.Rlabel = Label(self.returnbooks, text="IDCARD_NO", font=("Andalus", 15, 'bold'), fg='black',bg='lightgray')
        self.Rlabel.place(x=100, y=160)

        self.RIDCARDentry = Entry(self.returnbooks, font=('times new roman', 15),bg='lightgray')
        self.RIDCARDentry.place(x=100, y=210, width=250)

        self.Blabel = Label(self.returnbooks, text="Book_NAME", font=("Andalus", 15, 'bold'), fg='black',bg='lightgray')
        self.Blabel.place(x=100, y=260)

        self.RbookaddDentry = Entry(self.returnbooks, font=('times new roman', 15),bg='lightgray')
        self.RbookaddDentry.place(x=100, y=310, width=250)

        self.RBlabel = Label(self.returnbooks, text="DEPARTMENT", font=("Andalus", 15, 'bold'), fg='black',bg='lightgray')
        self.RBlabel.place(x=100, y=360)

        self.mycombo1 = ttk.Combobox(self.returnbooks, width=30, height=5,state='readonly')
        self.mycombo1['values'] = ['Select', 'Computer Science', 'IT', 'ARTS', 'Commers', 'LANGUAGE', 'OTHER']
        self.mycombo1.place(x=100, y=410)
        self.mycombo1.current(0)

        self.returnb = Button(self.returnbooks, text="SEARCH", cursor='hand2',
                              font=('times new roman', 13, 'bold'), bg='lightblue', fg='white', bd=0,
                              activebackground='#00B0F0', activeforeground="white",
                              command=lambda: self.se())
        self.returnb.place(x=100, y=460, width=250)

        self.RElabel = Label(self.returnbooks, text="EMAIL ADDRESS", font=("Andalus", 15, 'bold'), fg='black',bg='lightgray')
        self.RElabel.place(x=100, y=510)

        self.REmail_address = Entry(self.returnbooks, font=('times new roman', 15),bg='lightgray')
        self.REmail_address.place(x=100, y=560, width=250)

     #=====================  TREEVIEW ==================================================#

        self.scroll_x = ttk.Scrollbar(self.returnbooks, orient=VERTICAL)
        self.treview=ttk.Treeview(self.returnbooks,columns=(1,2,3,4,5,6),show='headings',height=36,yscrollcommand=self.scroll_x.set)
        self.scroll_x.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.treview.yview)
        self.treview.heading(1,text='STUDENT_ID')
        self.treview.heading(2, text='EMAIL_ID')
        self.treview.heading(3, text='BOOK_NAMES')
        self.treview.heading(4, text='DEPARTMENT')
        self.treview.heading(5, text='FROMDATE')
        self.treview.heading(6, text='TODATE')
        self.treview.column(1,width=180)
        self.treview.column(2, width=180)
        self.treview.column(3, width=180)
        self.treview.column(4, width=180)
        self.treview.column(5, width=180)
        self.treview.column(6, width=180)
        self.treview.place(x=440,y=80)
        style1=ttk.Style(self.treview)
        style1.theme_use("clam")
        self.returnb = Button(self.returnbooks, text="RETURNBOOK", cursor='hand2',
                              font=('times new roman', 13, 'bold'), bg='lightblue',fg='white', bd=0,
                              activebackground='#00B0F0', activeforeground="white",
                              command=lambda:self.returndata())
        self.returnb.place(x=100, y=610, width=250)
        con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
        cur = con.cursor()
        print('sss coonct')
        print('sss coonct')
        cur.execute("SELECT * FROM borrow_books")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.treview.delete(*self.treview.get_children())
            for i in rows:
                self.treview.insert('', 'end', values=i)
                con.commit()
        con.close()

    #==========================  SEARCHING STUDENT FROM DATABASE  AND UPDATING TREEVIEW ===================================#

    def se(self):
        con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
        cur = con.cursor                                                                                             ()
        print('sss coonct')
        print('sss coonct')
        cur.execute("SELECT * FROM borrow_books WHERE STUDENT_ID=%s", (self.RIDCARDentry.get()))
        row0=cur.fetchall()
        if len(row0)!=0:
            self.treview.delete(*self.treview.get_children())
            for i in row0:
                self.treview.insert('','end',values=i)
                con.commit()
#======================================  RETURN BOOK DATABASE QUERY ===========================================#

    def returndata(self):
        if self.RIDCARDentry.get() == '':
            messagebox.showwarning("Warning", 'All field are required')
        elif self.RbookaddDentry.get() == '':
            messagebox.showwarning("waening", 'All fields are required')
        elif self.mycombo1.get() == '':
            messagebox.showwarning('Warning', 'all fields are required')
        elif self.REmail_address.get() == '':
            messagebox.showwarning("warning", 'All fields are required')
        else:
            con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
            cur = con.cursor()
            print('sss coonct')
            print('sss coonct')
            cur.execute('SELECT * FROM borrow_books WHERE STUDENT_ID=%s and EMAIL_ID=%s',
                        (self.RIDCARDentry.get(), self.REmail_address.get()))
            row5 = cur.fetchall()
            if row5 == None:
                messagebox.showwarning("Warning", 'student Not borrow books')
            else:
                con.commit()
                cur.execute("insert into books_name(Book_Name,DEPARTMENT) values ('%s','%s')" % (
                self.RbookaddDentry.get(), self.mycombo1.get()))
                con.commit()
                print("inser success")
                cur.execute(
                    "delete from borrow_books  where STUDENT_ID=%s and EMAIL_ID=%s and  Book_NAME=%s and DEPARTMENT=%s",
                    (
                    self.RIDCARDentry.get(), self.REmail_address.get(), self.RbookaddDentry.get(), self.mycombo1.get()))
                con.commit()
                print("delete")
                con.close()
                messagebox.showinfo("successs", 'booK return successfully')
                con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
                cur = con.cursor()
                print('sss coonct')
                print('sss coonct')
                cur.execute("SELECT * FROM borrow_books")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.treview.delete(*self.treview.get_children())
                    for i in rows:
                        self.treview.insert('', 'end', values=i)
                        con.commit()
                con.close()
###=======================================================================================================###

###====================================== DELETE BOOK WINDOW  ===================================================###

    def delete_book_window(self):
        delete=Toplevel()
        self.delete=delete
        self.delete.title("Delete Book")
        self.delete.geometry('900x600+350+100')
        self.delete.resizable(False,False)

        self.Dlabel = Label(self.delete, text="DELETE BOOK HERE", font=("Andalus", 20, 'bold'), fg='black',
                            bg='gold2')
        self.Dlabel.place(x=0, y=10,width=900)

        self.frame1 = Frame(self.delete,bg='gray')
        self.frame1.place(x=100, y=100, width=400, height=450)


        self.Dlabel = Label(self.frame1, text="BOOK_Name", font=("Andalus", 13, 'bold'), fg='black',
                            bg='lightgray')
        self.Dlabel.place(x=100, y=100)

        self.Dbookentry = Entry(self.frame1, font=('times new roman', 13), bg='lightgray')
        self.Dbookentry.place(x=100, y=170, width=250)

        self.Dlabel1 = Label(self.frame1, text="DEPARTMENT", font=("Andalus", 13, 'bold'), fg='black',
                           bg='lightgray')
        self.Dlabel1.place(x=100, y=240)

        self.mycombo=ttk.Combobox(self.frame1,width=30,height=4,state='readonly')
        self.mycombo['values']=['Select','Computer Science','IT','ARTS','Commers','LANGUAGE','OTHER']
        self.mycombo.place(x=100,y=310)
        self.mycombo.current(0)

        self.deleteb = Button(self.frame1, text="DELETEBOOK", cursor='hand2',
                              font=('times new roman', 13, 'bold'), bg='lightblue', fg='white', bd=0,
                              activebackground='#00B0F0', activeforeground="white",command=lambda:self.delete1())
        self.deleteb.place(x=100, y=380, width=150)

        self.scroll_x = ttk.Scrollbar(self.delete, orient=VERTICAL)
        self.treview1 = ttk.Treeview(self.delete,columns=(1, 2), show='headings', height=21,yscrollcommand=self.scroll_x.set)
        self.scroll_x.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.treview1.yview)
        self.treview1.heading(1, text='BOOK_NAME')
        self.treview1.heading(2, text='DEPARTMENT')
        self.treview1.column(1, width=190)
        self.treview1.column(2, width=190)
        self.treview1.place(x=450,y=100)
        style = ttk.Style()
        style.theme_use("clam")
        con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
        cur = con.cursor()
        print('sss coonct')
        print('sss coonct')
        cur.execute("SELECT * FROM books_name")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.treview1.delete(*self.treview1.get_children())
            for i in rows:
                self.treview1.insert('', 'end', values=i)
                con.commit()
        con.close()

    #=====================  DELETEING BOOK DATABASE QUERY ===================================#

    def delete1(self):
        con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
        cur = con.cursor()
        print('sss coonct')
        print('sss coonct')
        cur.execute('DELETE FROM books_name WHERE Book_Name=%s and DEPARTMENT=%s',(self.Dbookentry.get(),self.mycombo.get()))
        data=cur.fetchall()
        if data==None:
            messagebox.showwarning("warning","book not found")
        else:
            con.commit()
            con.close()
            messagebox.showinfo("Success","BOOK DELETE SUCCESSFULLY")
            con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
            cur = con.cursor()
            print('sss coonct')
            print('sss coonct')
            cur.execute("SELECT * FROM books_name")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.treview1.delete(*self.treview1.get_children())
                for i in rows:
                    self.treview1.insert('', 'end', values=i)
                    con.commit()
            con.close()
####============================================= sending Email WINDOW ===========================================##############

    def sendreminder1(self):
        send=Toplevel()
        self.send=send
        self.send.title("SEND REMINDER")
        self.send.configure(bg='white')
        self.send.geometry("1530x900+0+0")
        self.send.resizable(False,False)

        self.label = Label(self.send, text="!!!!!!!!!SEND REMINDER!!!!!!!!!", font=("Andalus", 15, 'bold'),
                           fg='blue', bg='gold2')
        self.label.place(x=0, y=0, width=1530, height=50)

        self.SEmail = Label(self.send, text="EMAIL ADDREESS", font=("Andalus", 15, 'bold'), fg='black',
                            bg='lightgray')
        self.SEmail.place(x=80, y=130)

        self.Spassword= Label(self.send, text="PASSWORD", font=("Andalus", 15, 'bold'), fg='black',
                            bg='lightgray')
        self.Spassword.place(x=80, y=230)

        self.STo = Label(self.send, text="TO", font=("Andalus", 15, 'bold'), fg='black',
                            bg='lightgray')
        self.STo.place(x=80, y=330)

        self.Sbody= Label(self.send, text="BODY", font=("Andalus", 15, 'bold'), fg='black',
                            bg='lightgray')
        self.Sbody.place(x=80, y=430)

        self.mycombo1 = ttk.Combobox(self.send, width=30, height=4)
        self.mycombo1['values'] = ['librarymanager987@gmail.com']
        self.mycombo1.place(x=80, y=180)
        self.mycombo1.current(0)

        self.Spass_entry = Entry(self.send,show='*', font=('times new roman', 15), bg='lightgray')
        self.Spass_entry.place(x=80, y=280, width=250)

        self.Sto_entry = Entry(self.send, font=('times new roman', 15), bg='lightgray')
        self.Sto_entry.place(x=80, y=380, width=250)

        self.entry1=Entry(self.send,font=('times new roman',15),bg='lightgray')
        self.entry1.place(x=80,y=480,width=250,height=50)

        self.Ssend = Button(self.send, text="SEND", cursor='hand2',
                              font=('times new roman', 13, 'bold'), bg='lightblue', fg='white', bd=0,
                              activebackground='#00B0F0', activeforeground="white",command=lambda:self.sent())
        self.Ssend.place(x=80, y=560, width=150)

#======================= TREEVIEW ===================================#

        self.scroll_x1 = ttk.Scrollbar(self.send, orient=VERTICAL)
        self.treview2 = ttk.Treeview(self.send, columns=(1, 2,3,4,5,6), show='headings', height=34,
                                     yscrollcommand=self.scroll_x1.set)
        self.scroll_x1.pack(side=RIGHT, fill=Y)
        self.scroll_x1.config(command=self.treview2.yview)
        self.treview2.heading(1,text='STUDENT_ID')
        self.treview2.heading(2,text='EMAIL_ID')
        self.treview2.heading(3, text='BOOK_NAME')
        self.treview2.heading(4, text='DEPARTMENT')
        self.treview2.heading(5,text='FROMDATE')
        self.treview2.heading(6,text="TODATE")
        self.treview2.column(1, width=190)
        self.treview2.column(2, width=190)
        self.treview2.column(3, width=190)
        self.treview2.column(4, width=190)
        self.treview2.column(5, width=190)
        self.treview2.column(6, width=190)
        self.treview2.place(x=370, y=120)
        style2=ttk.Style(self.treview2)
        style2.theme_use("clam")

        con = pymysql.connect(host="localhost", user="root", password="OMom123@", database="student_management")
        cur = con.cursor()
        print('sss coonct')
        print('sss coonct')
        cur.execute("SELECT * FROM borrow_books")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.treview2.delete(*self.treview2.get_children())
            for i in rows:
                self.treview2.insert('', 'end', values=i)
                con.commit()
        con.close()

    #=========================== EMAIL SENDING FUNCTION ==========================================#
    def sent(self):
        try:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.login(self.mycombo1.get(),self.Spass_entry.get())
            server.sendmail(self.mycombo1.get(),self.Sto_entry.get(),self.entry1.get())
            messagebox.showinfo("Sent","Email Has Been sent")
        except:
             messagebox.showwarning("Sucesss",'Email send successfully')
##==============================================================================================##
s=Mainwindow(root)
root.mainloop()