from logging import root
from tkinter import *
from tkinter import font
from tkinter import messagebox
import random
import os


root=Tk()
root.geometry("1300x720+1+1")
root.title("supermarket")
root.resizable(False,False)
# Thelabel_of_page
lab_of_page=Label(root,text="ادارة المشاريع :السوبر ماركت",bg="#2980B9",font=("cooper",14,font.BOLD),fg="white",height="3")
lab_of_page.pack(fill=X)
first_frame=Frame(root,height=220,width=430,bg="#1F618D")
first_frame.place(x=890,y=58)

# thevariables_of_datauser
namo=StringVar()
veto=StringVar()
#@@@@@@@@@@@@@@@@@@@@@@@متغيرات البقوليات
q1=IntVar()
q2=IntVar()
q3=IntVar()
q4=IntVar()
q5=IntVar()
q6=IntVar()
q7=IntVar()
q8=IntVar()
q9=IntVar()
q10=IntVar()
q11=IntVar()
q12=IntVar()
q13=IntVar()
q14=IntVar()
q15=IntVar()
q16=IntVar()
q17=IntVar()
q18=IntVar()
#######################3متغيرات الادوات الكهربية
qq1=IntVar()
qq2=IntVar()
qq3=IntVar()
qq4=IntVar()
qq5=IntVar()
qq6=IntVar()
qq7=IntVar()
qq8=IntVar()
qq9=IntVar()
qq10=IntVar()
qq11=IntVar()
qq12=IntVar()
qq13=IntVar()
qq14=IntVar()
qq15=IntVar()
qq16=IntVar()
qq17=IntVar()
qq18=IntVar()
###############اللاوازم
qqq1=IntVar()
qqq2=IntVar()
qqq3=IntVar()
qqq4=IntVar()
qqq5=IntVar()
qqq6=IntVar()
qqq7=IntVar()
qqq8=IntVar()
qqq9=IntVar()
qqq10=IntVar()
qqq11=IntVar()
qqq12=IntVar()
qqq13=IntVar()
qqq14=IntVar()
qqq15=IntVar()
qqq16=IntVar()
qqq17=IntVar()
qqq18=IntVar()
qqq19=IntVar()
qqq20=IntVar()
####متغيرات الحساب

calc1=StringVar()
calc3=StringVar()
calc2=StringVar()
# متغيرات الحساب الفرعي
qc1=IntVar()
def find():
    check=False
    if not (os.path.isdir("D:\\buy\\")):
        os.mkdir("D:\\buy\\")
    for i in os.listdir("D:\\buy\\"):
            if i.split('.')[0] == veto.get():
                check=True
                f1=open(f"D:\\buy\\{i}","r",encoding="utf-8")
                text_content.delete('1.0',END)
                for d in f1:
                    text_content.insert('1.0',d)
                text_content.insert(END,'')
                f1.close()
                break
    if check:
        return
    else:
        messagebox.showerror("error","لا توجد فاتورة بهذا الاسم")


cd_l1=Label(first_frame,text=":بيانات المشتري",font=("cooper",19,font.BOLD),width=40,bg="white",fg="red")
cd_l1.place(x=1,y=0)
cd_l2=Label(first_frame,text="اسم المشتري",font=("cooper",14,font.BOLD),width=8,bg="white")
cd_l2.place(x=269,y=60)
cd_l2_entry=Entry(first_frame,justify=CENTER,textvariable=namo)
cd_l2_entry.place(x=120,y=60,height=30)
cd_l2=Label(first_frame,text="فاتورة المشتري",font=("cooper",14,font.BOLD),width=8,bg="white")
cd_l2.place(x=269,y=165)
cd_l2_entry=Entry(first_frame,justify=CENTER,textvariable=veto)
cd_l2_entry.place(x=120,y=165,height=30)
cd_search=Button(first_frame,text="بحث",command=find,width=8,height=7,font=("cooper",12,font.BOLD),activeforeground="black",fg="red")
cd_search.place(x=6,y=58)
x_scroll=Scrollbar(root,orient=HORIZONTAL)
y_scroll=Scrollbar(root,orient=VERTICAL)
text_content=Text(root,xscrollcommand=x_scroll,yscrollcommand=y_scroll,width=430,height=17)
text_content.place(x=890,y=280)
def welcome():
    text_content.delete("0.1",END)
    text_content.insert(END,"\t\tسوبر ماركت الهلال يرحب بكم")
    text_content.insert(END,"\n********************************************")
    text_content.insert(END,f"\n\n \t B_num:{veto.get()}")
    text_content.insert(END,f"\n\n \t name:{namo.get()}")
    text_content.insert(END,"\n********************************************")
    text_content.insert(END,"\n\tاسم الصنف\t\tالكمية\t\tالسعر")
    text_content.insert(END,"\n********************************************")

def ran_dom():
    o=random.randint(1,100)
    veto.set(str(o))


fr2=Frame(root,width=950,height=170,bg="#1F618D")
fr2.place(x=500,y=560)


b4=Button(fr2,text="اغلاق البرنامج",width=14,height=2,font=("cooper",14,font.BOLD),command=quit,bg="#ffbf00",fg="red")
b4.place(x=420,y=89)

l1=Label(fr2,text=":      الحساب الكلي للبقوليات",font=("cooper",14,font.BOLD),width=16,bg="#1F618D")
l2=Label(fr2,text=":الحساب الكلي للاوازم المنزلية",font=("cooper",14,font.BOLD),width=16,bg="#1F618D")
l3=Label(fr2,text=":الحساب الكلي للادوات الكهربية",font=("cooper",14,font.BOLD),width=16,bg="#1F618D")
l1.place(x=219,y=20)
l2.place(x=219,y=75)
l3.place(x=219,y=125)

enjj=Entry(fr2,width=35,textvariable=calc3)
enjj.place(x=4,y=20,height=30)
en277=Entry(fr2,width=35,textvariable=calc2)
en277.place(x=4,y=75,height=30)
en3990=Entry(fr2,width=35,textvariable=calc1)
en3990.place(x=4,y=125,height=30)

#################################
def clear():
     q1.set('0')
     q2.set('0')
     q3.set('0')
     q4.set('0')
     q5.set('0')
     q6.set('0')
     q7.set('0')
     q8.set('0')
     q9.set('0')
     q10.set('0')
     q11.set('0')
     q12.set('0')
     q13.set('0')
     q14.set('0')
##################
     qq1.set('0')
     qq2.set('0')
     qq3.set('0')
     qq4.set('0')
     qq5.set('0')
     qq6.set('0')
     qq7.set('0')
     qq8.set('0')
     qq9.set('0')
     qq10.set('0')
     qq11.set('0')
     qq12.set('0')
     qq13.set('0')
     qq14.set('0')
     
     qqq1.set('0')
     qqq2.set('0')
     qqq3.set('0')
     qqq4.set('0')
     qqq5.set('0')
     qqq6.set('0')
     qqq7.set('0')
     qqq8.set('0')
     qqq9.set('0')
     qqq10.set('0')
     qqq11.set('0')
     qqq12.set('0')
     qqq13.set('0')
     qqq14.set('0')
     qqq15.set('0')
     qqq16.set('0')
     qqq17.set('0')
     qqq18.set('0')
     qqq19.set('0')
     qqq20.set('0')

     calc3.set('0')
     calc2.set('0')
     calc1.set('0')
     b3=Button(fr2,text="افراغ الحقول",width=14,height=2,bg="#ffbf00",font=("cooper",14,font.BOLD),fg="red",command=clear)
     b3.place(x=420,y=20)

# the_first_frame
fr_b=Frame(root,height=1000,width=245,bg="#1F618D")
fr_b.place(x=0,y=110)
main_la=Label(root,text="البقوليات",font=("cooper",14,font.BOLD),fg="red")
main_la.place(x=70,y=80)
######################################################################################
l1=Label(fr_b,text="<======الطماطم",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l1.place(x=1,y=12)
l2=Label(fr_b,text="<=====الخرشوف",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l2.place(x=1,y=53)
l3=Label(fr_b,text="<======البروكل",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l3.place(x=1,y=87)
l4=Label(fr_b,text="<======القرنبيط",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l4.place(x=1,y=131)
l5=Label(fr_b,text="<======القلقاس",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l5.place(x=1,y=175)
l6=Label(fr_b,text="<======= اليام",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l6.place(x=1,y=216)
l7=Label(fr_b,text="<======البطاطا",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l7.place(x=1,y=260)
l8=Label(fr_b,text="<======الكسافا",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l8.place(x=1,y=304)
l9=Label(fr_b,text="<======الجرجير",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l9.place(x=1,y=348)
l10=Label(fr_b,text="<====== السلق",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l10.place(x=1,y=387)
l11=Label(fr_b,text="<=======اللفت",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l11.place(x=1,y=426)
l12=Label(fr_b,text="<======بروكسل",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l12.place(x=1,y=464)
l13=Label(fr_b,text="<======الباذنجان",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l13.place(x=1,y=514)
l14=Label(fr_b,text="<=======القرع",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
l14.place(x=1,y=558)
#entry
en1=Entry(fr_b,width=15,textvariable=q1)
en1.place(x=10,y=20)
en2=Entry(fr_b,width=15,textvariable=q2)
en2.place(x=10,y=53)
en3=Entry(fr_b,width=15,textvariable=q3)
en3.place(x=10,y=87)
en4=Entry(fr_b,width=15,textvariable=q4)
en4.place(x=10,y=131)
en5=Entry(fr_b,width=15,textvariable=q5)
en5.place(x=10,y=175)
en6=Entry(fr_b,width=15,textvariable=q6)
en6.place(x=10,y=216)
en7=Entry(fr_b,width=15,textvariable=q7)
en7.place(x=10,y=260)
en8=Entry(fr_b,width=15,textvariable=q8)
en8.place(x=10,y=304)
en9=Entry(fr_b,width=15,textvariable=q9)
en9.place(x=10,y=348)
en10=Entry(fr_b,width=15,textvariable=q10)
en10.place(x=10,y=387)
en=Entry(fr_b,width=15,textvariable=q11)
en.place(x=10,y=426)
en=Entry(fr_b,width=15,textvariable=q12)
en.place(x=10,y=464)
en=Entry(fr_b,width=15,textvariable=q13)
en.place(x=10,y=514)
en=Entry(fr_b,width=15,textvariable=q14)
en.place(x=10,y=558)

b3=Button(fr2,text="افراغ الحقول",width=14,height=2,bg="#ffbf00",font=("cooper",14,font.BOLD),fg="red",command=clear)
b3.place(x=420,y=20)

###########################################################################################
# the_second_frame
fr_a=Frame(root,height=1000,width=248,bg="#1F618D")
fr_a.place(x=249,y=110)
main_la=Label(root,text="الادوات الكهربية",font=("cooper",14,font.BOLD),fg="red")
main_la.place(x=300,y=80)
###########################################################################################
la1=Label(fr_a,text="<======مكنسة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la1.place(x=1,y=12)
la2=Label(fr_a,text="<=======تلفاز",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la2.place(x=1,y=53)
la3=Label(fr_a,text="<=======بتجاز",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la3.place(x=1,y=87)
la4=Label(fr_a,text="<====== غسالة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la4.place(x=1,y=131)
la5=Label(fr_a,text="<=======مروحة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la5.place(x=1,y=175)
la6=Label(fr_a,text="<=======السخان",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la6.place(x=1,y=216)
la7=Label(fr_a,text="<======ابجورة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la7.place(x=1,y=260)
la8=Label(fr_a,text="<=====كمبيوتر",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la8.place(x=1,y=304)
la9=Label(fr_a,text="<======التكيف",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la9.place(x=1,y=348)
la10=Label(fr_a,text="<====== تلاجة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la10.place(x=1,y=387)
la11=Label(fr_a,text="<=====شاشة57",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la11.place(x=1,y=426)
la12=Label(fr_a,text="<======مكنسة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la12.place(x=1,y=464)
la13=Label(fr_a,text="<======فرن غاز",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la13.place(x=1,y=514)
la14=Label(fr_a,text="<=======مكوة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=27)
la14.place(x=1,y=558)
#entry
ena1=Entry(fr_a,width=15,textvariable=qq1)
ena1.place(x=10,y=20)
ena2=Entry(fr_a,width=15,textvariable=qq2)
ena2.place(x=10,y=53)
ena3=Entry(fr_a,width=15,textvariable=qq3)
ena3.place(x=10,y=87)
ena4=Entry(fr_a,width=15,textvariable=qq4)
ena4.place(x=10,y=131)
ena5=Entry(fr_a,width=15,textvariable=qq5)
ena5.place(x=10,y=175)
ena6=Entry(fr_a,width=15,textvariable=qq6)
ena6.place(x=10,y=216)
ena7=Entry(fr_a,width=15,textvariable=qq7)
ena7.place(x=10,y=260)
ena8=Entry(fr_a,width=15,textvariable=qq8)
ena8.place(x=10,y=304)
ena9=Entry(fr_a,width=15,textvariable=qq9)
ena9.place(x=10,y=348)
ena10=Entry(fr_a,width=15,textvariable=qq10)
ena10.place(x=10,y=387)
en11a=Entry(fr_a,width=15,textvariable=qq11)
en11a.place(x=10,y=426)
en12a=Entry(fr_a,width=15,textvariable=qq12)
en12a.place(x=10,y=464)
en13a=Entry(fr_a,width=15,textvariable=qq13)
en13a.place(x=10,y=514)
en14a=Entry(fr_a,width=15,textvariable=qq14)
en14a.place(x=10,y=558)
#############################################################################################
# the_thrid_frame
fr_m=Frame(root,height=444,width=380,bg="#1F618D")
fr_m.place(x=500,y=110)
main_la=Label(root,text=" اللاوازم المنزلية",font=("cooper",14,font.BOLD),fg="red")
main_la.place(x=560,y=80)
#########################################################################################3#####
la1=Label(fr_m,text="<==مصفة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la1.place(x=1,y=12)
la2=Label(fr_m,text="<===شوك",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la2.place(x=1,y=53)
la3=Label(fr_m,text="<==اطباق",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la3.place(x=1,y=87)
la4=Label(fr_m,text="<==فايبر",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la4.place(x=1,y=131)
la5=Label(fr_m,text="<=كوبيات",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la5.place(x=1,y=175)
la6=Label(fr_m,text="<=معلقة م",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la6.place(x=1,y=216)
la7=Label(fr_m,text="<==سلة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la7.place(x=1,y=260)
la8=Label(fr_m,text="<=خلاطات",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la8.place(x=1,y=304)
la9=Label(fr_m,text="<==صنية",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la9.place(x=1,y=348)
la10=Label(fr_m,text="<==ابريق",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD),width=22)
la10.place(x=1,y=387)
lar1=Label(fr_m,text="<==امشاط",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar1.place(x=290,y=12)
lar2=Label(fr_m,text="<==احزمة",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar2.place(x=290,y=53)
lar3=Label(fr_m,text="<==توك",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar3.place(x=290,y=87)
lar4=Label(fr_m,text="<==شمع",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar4.place(x=290,y=131)
lar5=Label(fr_m,text="<==فيش",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar5.place(x=290,y=175)
lar6=Label(fr_m,text="<=بروايظ",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar6.place(x=290,y=216)
lar7=Label(fr_m,text="<==منظف",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar7.place(x=290,y=260)
lar8=Label(fr_m,text="<==معطر",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar8.place(x=290,y=304)
lar9=Label(fr_m,text="<==مرطب",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar9.place(x=290,y=348)
lar10=Label(fr_m,text="<==سكين",bg="#1F618D",fg="white",font=("cooper",14,font.BOLD))
lar10.place(x=290,y=387)
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ena1=Entry(fr_m,width=15,textvariable=qqq1)
ena1.place(x=10,y=20)
ena2=Entry(fr_m,width=15,textvariable=qqq2)
ena2.place(x=10,y=53)
ena3=Entry(fr_m,width=15,textvariable=qqq3)
ena3.place(x=10,y=87)
ena4=Entry(fr_m,width=15,textvariable=qqq4)
ena4.place(x=10,y=131)
ena5=Entry(fr_m,width=15,textvariable=qqq5)
ena5.place(x=10,y=175)
ena6=Entry(fr_m,width=15,textvariable=qqq6)
ena6.place(x=10,y=216)
ena7=Entry(fr_m,width=15,textvariable=qqq7)
ena7.place(x=10,y=260)
ena8=Entry(fr_m,width=15,textvariable=qqq8)
ena8.place(x=10,y=304)
ena9=Entry(fr_m,width=15,textvariable=qqq9)
ena9.place(x=10,y=348)
ena10=Entry(fr_m,width=15,textvariable=qqq10)
ena10.place(x=10,y=387)
enar1=Entry(fr_m,width=15,textvariable=qqq11)
enar1.place(x=200,y=20)
enar2=Entry(fr_m,width=15,textvariable=qqq12)
enar2.place(x=200,y=53)
enar3=Entry(fr_m,width=15,textvariable=qqq13)
enar3.place(x=200,y=87)
enar4=Entry(fr_m,width=15,textvariable=qqq14)
enar4.place(x=200,y=131)
enar5=Entry(fr_m,width=15,textvariable=qqq15)
enar5.place(x=200,y=175)
enar6=Entry(fr_m,width=15,textvariable=qqq16)
enar6.place(x=200,y=216)
enar7=Entry(fr_m,width=15,textvariable=qqq17)
enar7.place(x=200,y=260)
enar8=Entry(fr_m,width=15,textvariable=qqq18)
enar8.place(x=200,y=304)
enar9=Entry(fr_m,width=15,textvariable=qqq19)
enar9.place(x=200,y=348)
enar10=Entry(fr_m,width=15,textvariable=qqq20)
enar10.place(x=200,y=387)
ran_dom()
welcome()

def all_ca():

         qc1=q1.get()*1
         qc2=q2.get()*2
         qc3=q3.get()*3
         qc4=q4.get()*4
         qc5=q5.get()*5
         qc6=q6.get()*6
         qc7=q7.get()*7
         qc8=q8.get()*8
         qc9=q9.get()*9
         qc10=q10.get()*10
         qc11=q11.get()*11
         qc12=q12.get()*12
         qc13=q13.get()*13
         qc14=q14.get()*14
         b=qc1+qc2+qc3+qc4+qc5+qc6+qc7+qc8+qc9+qc10+qc11+qc12+qc13+qc14
         calc3.set(b)

         qqc1=qq1.get()*1
         qqc2=qq2.get()*2
         qqc3=qq3.get()*3
         qqc4=qq4.get()*4
         qqc5=qq5.get()*5
         qqc6=qq6.get()*6
         qqc7=qq7.get()*7
         qqc8=qq8.get()*8
         qqc9=qq9.get()*9
         qqc10=qq10.get()*10
         qqc11=qq11.get()*11
         qqc12=qq12.get()*12
         qqc13=qq13.get()*13
         qqc14=qq14.get()*14
         a=qqc1+qqc2+qqc3+qqc4+qqc5+qqc6+qqc7+qqc8+qqc9+qqc10+qqc11+qqc12+qqc13+qqc14
         calc2.set(a)
         qqqc1=qqq1.get()*1
         qqqc2=qqq2.get()*2
         qqqc3=qqq3.get()*3
         qqqc4=qqq4.get()*4
         qqqc5=qqq5.get()*5
         qqqc6=qqq6.get()*6
         qqqc7=qqq7.get()*7
         qqqc8=qqq8.get()*8
         qqqc9=qqq9.get()*9
         qqqc10=qqq10.get()*10
         qqqc11=qqq11.get()*11
         qqqc12=qqq12.get()*12
         qqqc13=qqq13.get()*13
         qqqc14=qqq14.get()*14
         x=qqqc1+qqqc2+qqqc3+qqqc4+qqqc5+qqqc6+qqqc7+qqqc8+qqqc9+qqqc10+qqqc11+qqqc12+qqqc13+qqqc14
         calc1.set(x)
         vetry=b+a+x
         
b1=Button(fr2,text="الحساب",width=14,height=2,font=("cooper",14,font.BOLD),bg="#ffbf00",fg="red",command=all_ca)
b1.place(x=605,y=20)   
################################33
def bolling():
    if namo.get()=="":
        messagebox.showerror("خطأ","يجب ملئ اسم المستخدم")
    elif calc1.get()=="" and calc2.get()=="" and calc3.get()=="":
        messagebox.showerror("خطأ","يجب اختيار احد الاصناف")

    else:
        welcome()
        if q1.get() != 0:
            text_content.insert(END,f"\n\tطماطم\t\t{q1.get()}\t\t{q1.get()*1}")

        if q2.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{q2.get()}\t\t{q2.get()*2}")
        if q3.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{q3.get()}\t\t{q3.get()*3}")    
        if q4.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{q4.get()}\t\t{q4.get()*4}")
        if q5.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{q5.get()}\t\t{q5.get()*5}")

        if q6.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{q6.get()}\t\t{q6.get()*6}")
        if q7.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{q7.get()}\t\t{q7.get()*7}")
        if q8.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{q8.get()}\t\t{q8.get()*8}")

        if q9.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{q9.get()}\t\t{q9.get()*9}")
        if q10.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{q10.get()}\t\t{q10.get()*10}")
        if q11.get() != 0:
            text_content.insert(END,f"\n\t++++++\t\t{q11.get()}\t\t{q11.get()*11}")
        if q12.get() != 0:
            text_content.insert(END,f"\n\t++++++\t\t{q12.get()}\t\t{q12.get()*12}")
        if q13.get() != 0:
            text_content.insert(END,f"\n\t++++++\t\t{q13.get()}\t\t{q13.get()*13}")
        if q14.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{q14.get()}\t\t{q14.get()*14}")

############################################3
        if qq1.get() != 0:
            text_content.insert(END,f"\n\tمكنسة\t\t{qq1.get()}\t\t{qq1.get()*1}")
        if qq2.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qq2.get()}\t\t{qq2.get()*2}")
        if qq3.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qq3.get()}\t\t{qq3.get()*3}")    
        if qq4.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qq4.get()}\t\t{qq4.get()*4}")
        if qq5.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qq5.get()}\t\t{qq5.get()*5}")
        if qq6.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qq6.get()}\t\t{qq6.get()*6}")
        if qq7.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qq7.get()}\t\t{qq7.get()*7}")
        if qq8.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qq8.get()}\t\t{qq8.get()*8}")
        if qq9.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qq9.get()}\t\t{qq9.get()*9}")
        if qq10.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qq10.get()}\t\t{qq10.get()*10}")
        if qq11.get() != 0:
            text_content.insert(END,f"\n\t++++++\t\t{qq11.get()}\t\t{qq11.get()*11}")
        if qq12.get() != 0:
            text_content.insert(END,f"\n\t++++++\t\t{qq12.get()}\t\t{qq12.get()*12}")
        if qq13.get() != 0:
            text_content.insert(END,f"\n\t++++++\t\t{qq13.get()}\t\t{qq13.get()*13}")
        if qq14.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qq14.get()}\t\t{qq14.get()*14}")
##############################################3
        if qqq1.get() != 0:
            text_content.insert(END,f"\n\tمصفة\t\t{qqq1.get()}\t\t{qqq1.get()*1}")
        if qqq2.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qqq2.get()}\t\t{qqq2.get()*2}")
        if qqq3.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq3.get()}\t\t{qqq3.get()*3}")    
        if qqq4.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq4.get()}\t\t{qqq4.get()*4}")
        if qqq5.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qqq5.get()}\t\t{qqq5.get()*5}")
        if qqq6.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qqq6.get()}\t\t{qqq6.get()*6}")
        if qqq7.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qqq7.get()}\t\t{qqq7.get()*7}")
        if qqq8.get() != 0:
            text_content.insert(END,f"\n\t++++\t\t{qqq8.get()}\t\t{qqq8.get()*8}")
        if qqq9.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq9.get()}\t\t{qqq9.get()*9}")
        if qqq10.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq10.get()}\t\t{qqq10.get()*10}")
        if qqq11.get() != 0:
            text_content.insert(END,f"\n\t++++++\t\t{qqq11.get()}\t\t{qqq11.get()*11}")
        if qqq12.get() != 0:
            text_content.insert(END,f"\n\t++++++\t\t{qqq12.get()}\t\t{qqq12.get()*12}")
        if qqq13.get() != 0:
            text_content.insert(END,f"\n\t++++++\t\t{qqq13.get()}\t\t{qqq13.get()*13}")
        if qqq14.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq14.get()}\t\t{qqq14.get()*14}")
        if qqq15.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq15.get()}\t\t{qqq15.get()*15}")
        if qqq16.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq16.get()}\t\t{qqq16.get()*16}")
        if qqq17.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq17.get()}\t\t{qqq17.get()*17}")
        if qqq18.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq18.get()}\t\t{qqq18.get()*18}")
        if qqq19.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq19.get()}\t\t{qqq19.get()*19}")
        if qqq20.get() != 0:
            text_content.insert(END,f"\n\t+++++\t\t{qqq20.get()}\t\t{qqq20.get()*20}")
        savee()
b2=Button(fr2,text="تصدير الفاتورة",width=14,height=2,font=("cooper",14,font.BOLD),bg="#ffbf00",fg="red",command=bolling)
b2.place(x=605,y=89)
def savee():
        if not (os.path.isdir("D:\\buy\\")):
            os.mkdir("D:\\buy\\")
        op = messagebox.askyesno("هل تريد حفظ الفاتورة ؟","حفظ")
        if op > 0 :
            bb= text_content.get('1.0',END)
            f1 = open('D:\\buy\\'+str(veto.get())+".txt","w",encoding="utf-8")
            f1.write(bb)
            f1.close()
        else:
            return
root.mainloop()