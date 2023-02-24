from tkinter import *
from tkinter import font
from tkinter import messagebox
import webbrowser
import os


class supermarket_start:

    def start_gui(self,root):

        root.geometry("750x500+450+100")
        root.title("supermarket")
        root.resizable(False,False)
        root.config(bg="#1A5276")
        label1=Label(root,text="super market system",bg="black",fg="#F1C40F",font=("Georgia",20))
        label1.pack(fill=X)
        frame1=Frame(root,bg="#1A5276")
        frame1.place(x=490,y=38,width=260,height=500)

        face_url="facebook.com"
        tele_url="telegram.com"
        you_url="https://www.youtube.com/watch?v=o5PdVuV-DeA"
        def ac1():
            webbrowser.open_new_tab(face_url)
        def ac2():
             webbrowser.open_new_tab(tele_url)
        def ac3():
            webbrowser.open_new_tab(you_url)

        def about_developer():
            messagebox.showinfo("about developer","osman ramadan")

        def about_project():
             messagebox.showinfo("about project","simple supermarket project to do daily tasks")  


    
        b1=Button(frame1,text="حسابنا على الفيس",height=2,fg="black",font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=ac1)
        b2=Button(frame1,text="حسابنا علي علي التليجرام",height=2,fg="black",font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=ac2)
        b3=Button(frame1,text="حسابنا علي اليوتيوب",fg="black",height=2,font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=ac3)
        b4=Button(frame1,text="لمحةعن المطور",fg="black",height=2,font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=about_developer)
        b5=Button(frame1,text="لمحة عن المشروع",fg="black",height=2,font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=about_project)
        b6=Button(frame1,text="اغلاق البرنامج",fg="black",height=3,font=("fancay",18),width=257,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=quit)
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
        b5.pack()
        b6.pack()


#image  
        user=StringVar()
        passw=StringVar()
        image1=PhotoImage(file='image.png')
        lab=Label(root,image=image1)
        lab.place(x=0,y=38,width=490,height=300)
        login=Label(root,text="enroll",bg="black",fg="white",font=("Georgia",20),width=30,height=1)
        login.place(x=2,y=338)
        lablo=Label(root,text="username:",fg="black",bg="white",font=("Georgia",15,font.BOLD))
        lablo.place(x=3,y=390)

        ent1=Entry(root,fg="blue",textvariable=user,bg="white",font=("Georgia",15))
        ent1.place(x=150,y=390)
        lablo=Label(root,text="password:",fg="black",bg="white",font=("Georgia",15,font.BOLD))
        lablo.place(x=3,y=430)
        ent2=Entry(root,show='*',fg="blue",textvariable=passw,bg="white",font=("Georgia",15))
        ent2.place(x=150,y=430)

#authintation
        username="root"
        password="root"
        def pass_or_not():
            if user.get()==username and passw.get()==password:
                
                
                os.chdir(os.getcwd())
                os.system('subsupermarket.pyc')
                
                
            else:
                messagebox.showinfo("not allowed","not allowed to enter")
        blo=Button(root,text="login",fg="white",font=("fancay",18),bg="red",height=2,relief=GROOVE,activebackground="#1A5276",activeforeground="yellow",command=pass_or_not)
        blo.place(x=1,y=460,width=490,height=38)   
        root.mainloop()
root=Tk()
s=supermarket_start()
s.start_gui(root)
#by osmanramadan
