from tkinter import *
import mysql.connector
import os
screen = Tk()
screen.geometry("300x250")
screen.title("Account Login")
global amount

mydb=mysql.connector.connect(
host='localhost', user='root',passwd="utkarsh2000",database="d1")

def registration():
    regscreen=Toplevel(screen)
    regscreen.geometry("400x350")
    regscreen.title("Register")
    Label(regscreen, text="Enter Your Details", bg="blue", fg="white", font=("showcard gothic", 15)).pack(fill=X)
    Label(regscreen, text="*mandatory field", fg="red").pack()
    Label(regscreen, text="").pack() 
    Label(regscreen, text="").pack()
    Label(regscreen, text="Username*", font=(10)).pack()
    username=StringVar()
    password=StringVar()
    utxt=Entry(regscreen, textvariable=username).pack()
    Label(regscreen, text="").pack()
    Label(regscreen, text="Password*", font=(10)).pack()
    ptxt=Entry(regscreen, textvariable=password, show='*').pack()
    Label(regscreen, text="").pack()
    def register():
        global amount
        amount=0
        Amount= str(amount)
        uname= username.get()
        pword= password.get()
        mycursor = mydb.cursor()
        
        sql = "INSERT INTO login (user, pass, amount) VALUES (%s, %s, %s)"
        val = (uname, pword, Amount)
    
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        def reg():
            rgscr=Toplevel(regscreen)
            rgscr.geometry('200x100')
            Label(rgscr, text="Registered Successfully").pack()
            def delreg():
                rgscr.destroy()
                regscreen.destroy()
            Button(rgscr, text="OK", command=delreg).pack()
        reg()
    Button(regscreen, text="Register", width=10, height=1, font=("bold",10), command=register).pack()

def login():
    logscreen=Toplevel(screen)
    logscreen.geometry("400x350")
    logscreen.title("Login")
    Label(logscreen, text="Enter Your Details", bg="blue", fg="white", font=("showcard gothic", 15)).pack(fill=X)
    Label(logscreen, text="*mandatory field", fg='red').pack()
    Label(logscreen, text="").pack() 
    Label(logscreen, text="").pack()
    Label(logscreen, text="Login ID/Username*", font=(10)).pack()
    username1=StringVar()
    password1=StringVar()
    txt=Entry(logscreen, textvariable=username1).pack()
    Label(logscreen, text="").pack()
    Label(logscreen, text="Password*", font=(10)).pack()
    txt=Entry(logscreen, textvariable=password1, show='*').pack()
    Label(logscreen, text="").pack()
    def login_():
        uname1=username1.get()
        pword1=password1.get()
        mycursor = mydb.cursor()
        sql = "select * from login where user=%s and pass=%s"
        val = (uname1, pword1)
    
        mycursor.execute(sql, val)
        row=mycursor.fetchone()
        if row==None:
            def inpsword():
                login_scr= Toplevel(logscreen)
                login_scr.geometry('200x100')
                Label(login_scr, text="").pack()
                Label(login_scr, text="invalid password").pack()
                def delinpsword():
                    login_scr.destroy()
                    
                Button(login_scr, text="OK", command=delinpsword).pack()
            inpsword()
            
        else:
            def log():  
                loginscr= Toplevel(logscreen)
                loginscr.geometry('200x100')
                Label(loginscr, text="login successful").pack()
                def dellog():
                    loginscr.destroy()
                    logscreen.destroy()
                    window=Toplevel(screen)
                    window.geometry('350x300')
                    window.title("Credit or Debit or Check Balance")
                    Label(window, text="").pack()
                    Label(window, text="").pack()
                    def credit():
                        credit1=Toplevel(window)
                        credit1.title("Credit")
                        credit1.geometry('350x200')
                        Label(credit1, text="").pack()
                        Label(credit1, text="").pack()
                        lbl=Label(credit1, text="Enter the amount you want to credit").pack()
                        credit_amnt=StringVar()
                        atxt=Entry(credit1, width='50', textvariable=credit_amnt).pack()
                        
                        Label(credit1, text="").pack()
                        def clicked():
                            click=Toplevel(credit1)
                            click.geometry('200x150')
                            
                            global amount
                            mycursor = mydb.cursor()
                            sql = "SELECT amount FROM records WHERE user=%s and pass=%s"
                            val = (uname1,pword1)
                            mycursor.execute(sql,val)
                            amount = list(mycursor.fetchone())
                            s=int(amount[0])
                            at=credit_amnt.get()
                            amt= int(at)
                            result_amnt = s+amt
                            samnt= str(result_amnt)
                            Label(click, text="").pack()
                            Label(click, text="Transaction Done", font=(15)).pack()
                            Label(click, text="").pack()
                            res="Remaining Balance is " + samnt
                            Label(click, text= res).pack()
                            mycursor = mydb.cursor()
                            sql = "UPDATE login SET amount=%s WHERE user=%s "
                            values= (samnt,uname1)
                            
                            try:
                                mycursor.execute(sql, values)
                                mydb.commit()
                                
                                
                            except:
                                print("error")
                                
                            def destroy():
                                click.destroy()
                                credit1.destroy()
                            Button(click, text="OK", height='1', command=destroy).pack()
                        
                        Button(credit1, text='Make Transaction', height='2', command=clicked).pack()
                        
                        
                    Button(window, text="Credit", height='2', font=('forte'), command=credit).pack()
                    Label(window, text="").pack()
                    def debit():
                        debit1=Toplevel(window)
                        debit1.title("Credit")
                        debit1.geometry('300x200')
                        Label(debit1, text="").pack()
                        Label(debit1, text="").pack()
                        Label(debit1, text="Enter the amount you want to debit").pack()
                        debit_amnt=StringVar()
                        btxt=Entry(debit1, width='50', textvariable=debit_amnt).pack()
                        Label(debit1, text="").pack()
                        def clicked1():
                            click1=Toplevel(debit1)
                            click1.geometry('200x150')
                            lbl1=Label(click1, text="").pack()
                            global amount
                            mycursor = mydb.cursor()
                            sql = "SELECT amount FROM records WHERE user=%s and pass=%s"
                            val = (uname1,pword1)
                            mycursor.execute(sql,val)
                            amount = list(mycursor.fetchone())
                            s=int(amount[0])
                            at=debit_amnt.get()
                            amt=int(at)
                            result_amnt = s-amt
                            
                            samnt=str(result_amnt)
                            
                            Label(click1, text="").pack()
                            Label(click1, text="Transaction Done", font=(15)).pack()
                            res="Remaining Balance is" + samnt
                            Label(click1, text= res).pack()
                            mycursor = mydb.cursor()
                            sql = "UPDATE login SET amount=%s WHERE user=%s "
                            value= (samnt, uname1)
                            
                            try:
                                mycursor.execute(sql, value)
                                mydb.commit()
                                
                            except:
                                print("error")
                            

                            def destroy1():
                                click1.destroy()
                                debit1.destroy()
                            Button(click1, text="OK", height='1', command=destroy1).pack()
                            
                            
                        Button(debit1, text='Make Transaction', height='2', command=clicked1).pack()
                            
                    Button(window, text="Debit", height='2', font=('forte'), command=debit ).pack()
                    Label(window, text="").pack()

                    def check():
                        check1=Toplevel(window)
                        check1.geometry('200x150')
                        global amount
                        
                        Label(check1, text="").pack()
                        resultant = "Your Account Balance is " + amount
                        Label(check1, text= resultant).pack()
                    Button(window, text="Check Balance", height='2', font=('forte'), command=check ).pack()
                    
                Button(loginscr, text="OK", command=dellog).pack()
            log()
               
    Button(logscreen, text="Login", width=10, height=1, font=("bold",10), command=login_).pack()

Label(text="Choose Login Or Register", bg="blue", fg='white', font=("showcard gothic", 15)).pack(fill=X) 
Label(text="").pack()  
Label(text="").pack() 
 
Button(text="Login", height="2", width="15", font=("forte"), command=login).pack() 
Label(text="").pack() 
 
Button(text="Register", height="2", width="15", font=("forte"), command=registration).pack()
screen.mainloop()
