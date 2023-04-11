from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector
form2=Tk()
form=Tk()
formR=Tk()
def register():
    #buraya üye kayıt kodları gelecek
   
    formR.title('Veritabanı Örnek Üye Kayıt')
    formR.geometry("400x600")
    formR.configure(bg="AntiqueWhite1")
    formR.resizable(False,False)
    e3=Label(formR,font=('Arial 12'),text="Adınız Soyadınız:")
    e3['bg'] = formR['bg']
    e3.place(x=120,y=40)
    name = Entry(formR, bd =2,  width=22, font=('Arial 12'),justify='left')
    name.place(x=80, y=70)
    e1=Label(formR,font=('Arial 12'),text="E-Posta Adresiniz:")
    e1['bg'] = formR['bg']
    e1.place(x=120,y=120)
    email = Entry(formR, bd =2,  width=22, font=('Arial 12'),justify='left')
    email.place(x=80, y=160)
    e2=Label(formR,font=('Arial 12'),text="Şifreniz:")
    e2['bg'] = formR['bg']
    e2.place(x=140,y=200)
    password = Entry(formR, bd =2, show="*",  width=22, font=('Arial 12'),justify='left')
    password.place(x=80, y=250)
    email.focus()    
    registerBtn = tk.Button(formR, text="Üye Ol", font="Arial 11 bold", width=6)
    registerBtn.place(x=80, y=300)
    loginBtn = tk.Button(formR, text="Giriş", font="Arial 11 bold", width=6,command=loginForm)
    loginBtn.place(x=220, y=300)
    forgetBtn = tk.Button(formR, text="Şifremi Unuttum", font="Arial 11 bold", width=21)
    forgetBtn.place(x=80, y=350)
    
    form.withdraw()
    formR.deiconify()
def loginForm():
    formR.withdraw()
    form.deiconify()
def anasayfa():    
    form2.title('Veritabanı Örnek Anasayfa')
    form2.geometry("1000x600")
    form2.configure(bg="AntiqueWhite1")
    form.withdraw()
    form2.mainloop()
def login():
    if(email.get()=="" or password.get()==""):
        messagebox.showinfo("Hata" , "Veri Girmediniz")
    else:
        db = mysql.connector.connect(host ="localhost",user ='root',password='',db ="yurtseven")
        cursor = db.cursor()
        sorgu = 'SELECT * FROM users WHERE email = %s and password = %s'
        vals = (email.get(), password.get(),)
        cursor.execute(sorgu, vals)
        user = cursor.fetchone()
        if user is not None:
             anasayfa()
        else:
            email.delete(0,END)
            password.delete(0,END)
            email.focus()
            messagebox.showinfo("Hata" , "Kullanıcı bulunamadı")   
     
    

form.title('Veritabanı Örnek V 1.0')
form.geometry("400x400")
form.configure(bg="gray")
form.resizable(False,False)
e1=Label(form,font=('Arial 15'),text="E-Posta Adresiniz:")
e1['bg'] = form['bg']
e1.place(x=120,y=40)
email = Entry(form, bd =2,  width=22, font=('Arial 15'),justify='left')
email.place(x=80, y=70)
e2=Label(form,font=('Arial 15'),text="Şifreniz:")
e2['bg'] = form['bg']
e2.place(x=160,y=120)
password = Entry(form, bd =2, show="*",  width=22, font=('Arial 15'),justify='left')
password.place(x=80, y=150)
email.focus()
loginBtn = tk.Button(form, text="Giriş", font="Arial 11 bold", width=6,command=login)
loginBtn.place(x=80, y=200)
registerBtn = tk.Button(form, text="Üye Ol", font="Arial 11 bold", width=6,command=register)
registerBtn.place(x=145, y=200)
forgetBtn = tk.Button(form, text="Şifremi Unuttum", font="Arial 11 bold", width=12)
forgetBtn.place(x=210, y=200)
exitBtn = tk.Button(form, text="Programı Kapat", font="Arial 10 bold", width=30,command=form.destroy)
exitBtn.place(x=80, y=250)
form2.withdraw()
formR.withdraw()
form.mainloop()
