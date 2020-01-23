from tkinter import *
import mysql.connector as mysql

root = Tk()
root.geometry('1300x1000')
root.title("Registration Form")


Firstname=StringVar()
Middlename=StringVar()
Lastname=StringVar()
Email=StringVar()
var = StringVar()
c=StringVar()
var1= StringVar()
a='java'
b='python'
f='linux'
m='C'
n='C++'
o='html'
p='MySQL'
l='C#'

feedback=StringVar()
var2=StringVar()
ab='0'
bc='1'
cd='2'
de='3'
ef='4'
fg='5'

interest=StringVar()
var3=StringVar()
k='Experience must be developed'
i='Experience was good'


def database():
   name1=Firstname.get()#label1
   name2=Middlename.get()#label1a
   name3=Lastname.get()#label1b
   email=Email.get()#label2
   gender=var.get()#label3
   country=c.get()#label4
   prog=var1.get()#label5
   feed=feedback.get()#label7
   liking=interest.get()#label8
   rating=var2.get()#label9
   exp=var3.get()#label10
   conn = mysql.connect(user='root',password='jsn',host='127.0.0.1')
   d=conn.cursor()
   d.execute('use manila')
   """d.execute('create table student(FirstName varchar(255),Middlename varchar(255),Lastname varchar(255),Email varchar(255),Gender varchar(255),Country  varchar(255),Programming varchar(2255),Feedback varchar(255),Interest varchar(255),Rating varchar(255),Experience varchar(255))')"""
   d.execute('INSERT INTO student(FirstName,Middlename,Lastname,Email,Gender,Country,Programming,Feedback,Interest,Rating,Experience) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(name1,name2,name3,email,gender,country,prog,feed,liking,rating,exp))
   conn.commit()

def printo():
   print("First Name: %s\nLast Name: %s\nMiddle Name: %s\nEmail: %s\nGender: %s\nCountry: %s\nProgram: %s\nFeedback: %s\nInterest: %s\nRating: %s\nExperience: %s\n"% (Firstname.get(),Lastname.get(),Middlename.get(),Email.get(),var.get(),c.get(),var1.get(),feedback.get(),interest.get(),var2.get(),var3.get()))
#function defined here down is for printing the inputs in GUI itself 
def printoo():
    Label(root,text="Your First_name is : "+str(Firstname.get()),font=("bold",13)).place(x=90,y=520)
    Label(root,text="Your Middle_name is : "+str(Middlename.get()),font=("bold",13)).place(x=90,y=550)
    Label(root,text="Your Last_name is : "+str(Lastname.get()),font=("bold",13)).place(x=90,y=580)
    Label(root,text="Your email is : "+str(Email.get()),font=("bold",13)).place(x=90,y=610)
    Label(root,text="Your Gender is : "+str(var.get()),font=("bold",13)).place(x=90,y=640)
    Label(root,text="Your Country choice is : "+str(c.get()),font=("bold",13)).place(x=90,y=670)
    Label(root,text="Your Program choice is : "+str(var1.get()),font=("bold",13)).place(x=510,y=520)
    Label(root,text="Your Feedback is : "+str(feedback.get()),font=("bold",13)).place(x=860,y=520)
    Label(root,text="Your Interest is : "+str(interest.get()),font=("bold",13)).place(x=860,y=550)
    Label(root,text="You Rated it : "+str(var2.get()),font=("bold",13)).place(x=860,y=580)
    Label(root,text="Your Experience was : "+str(var3.get()),font=("bold",13)).place(x=860,y=610)

    
   
#labels of 1st part
label_0 = Label(root, text="Student Survey Form",width=35,font=("bold", 50))
label_0.place(x=10,y=25)


label_1 = Label(root, text="First_Name",width=20,font=("bold", 18))
label_1.place(x=20,y=140)

entry_1 = Entry(root,textvar=Firstname,bd=5)
entry_1.place(x=240,y=145)
Firstname.set('your first_name')

label_1A = Label(root, text="Middle_Name",width=20,font=("bold", 18))
label_1A.place(x=20,y=184)

entry_1A = Entry(root,textvar=Middlename,bd=5)
entry_1A.place(x=240,y=186)
Middlename.set('your middle_name')

label_1B = Label(root, text="Last_Name",width=20,font=("bold", 18))
label_1B.place(x=20,y=220)

entry_1B = Entry(root,textvar=Lastname,bd=5)
entry_1B.place(x=240,y=225)
Lastname.set('your last_name')

label_2 = Label(root, text="Email",width=20,font=("bold", 18))
label_2.place(x=20,y=260)

entry_2 = Entry(root,textvar=Email,bd=5)
entry_2.place(x=240,y=265)
Email.set('enter an email @')

label_3 = Label(root, text="Gender",width=20,font=("bold", 18))
label_3.place(x=20,y=295)

Radiobutton(root, text="Male",padx = 5, variable=var, value='male').place(x=235,y=300)
Radiobutton(root, text="Female",padx = 20, variable=var, value='female').place(x=295,y=300)

label_4 = Label(root, text="Country",width=20,font=("bold", 18))
label_4.place(x=20,y=335)

list1 = ['Canada','India','UK','Australia','Iceland','South Africa','UAE','Srilanka','Russia'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your Country') 
droplist.place(x=240,y=340)

#labels of 2nd part
label_5 = Label(root, text="Choose your Programming\n Language:",width=20,font=("bold", 19))
label_5.place(x=440,y=140)


Radiobutton(root, text="Java", variable=var1 , value=a,font=("none", 15)).place(x=480,y=220)
Radiobutton(root, text="Python", variable=var1, value=b,font=("none", 15)).place(x=582,y=220)
Radiobutton(root, text="Linux", variable=var1 ,value=f,font=("none", 15)).place(x=695,y=220)
Radiobutton(root, text="C", variable=var1 ,value=m,font=("none", 15)).place(x=550,y=270)
Radiobutton(root, text="C++", variable=var1 ,value=n,font=("none", 15)).place(x=655,y=270)
Radiobutton(root, text="html", variable=var1 ,value=o,font=("none", 15)).place(x=480,y=330)
Radiobutton(root, text="MySQL", variable=var1 ,value=p,font=("none", 15)).place(x=695,y=330)
Radiobutton(root, text="C#", variable=var1, value=l,font=("none",15)).place(x=582,y=330)






#label of 3rd part
label_7= Label(root, text="Feedback",font=("bold", 18))
label_7.place(x=880,y=140)
entry_7 = Entry(root,textvar=feedback,bd=5)

entry_7.place(x=1000,y=140)
feedback.set('your feedback in 1 line')


label_8= Label(root, text="Interest",font=("bold", 18))
label_8.place(x=880,y=190)
entry_8 = Entry(root,textvar=interest,bd=5)

entry_8.place(x=1000,y=190)
interest.set('any interest')


label_9 = Label(root, text="Rating: Rate from 0 to 5",font=("bold", 18))
label_9.place(x=880,y=240)

Radiobutton(root, text="0",font=("none", 13), variable=var2 , value=ab).place(x=990,y=270)
Radiobutton(root, text="1",font=("none", 13), variable=var2 , value=bc).place(x=1050,y=270)
Radiobutton(root, text="2",font=("none", 13), variable=var2 , value=cd).place(x=1115,y=270)
Radiobutton(root, text="3",font=("none", 13), variable=var2 , value=de).place(x=990,y=300)
Radiobutton(root, text="4",font=("none", 13), variable=var2 , value=ef).place(x=1050,y=300)
Radiobutton(root, text="5",font=("none", 13), variable=var2 , value=fg).place(x=1115,y=300)

label_10 = Label(root, text="Experience:",font=("bold", 18))
label_10.place(x=880,y=330)

Radiobutton(root, text="Experience must be developed",font=("none", 13), variable=var3 , value=k).place(x=1006,y=335)
Radiobutton(root, text="Experience is good",font=("none", 13), variable=var3 , value=i).place(x=1006,y=360)

Button(root, text='Submit',width=30,bg='brown',fg='white',font=("bold",13),command=database).place(x=160,y=450)
Button(root, text='Print in PY Shell',width=30,bg='brown',fg='white',font=("bold",13),command=printo).place(x=510,y=450)
Button(root, text='Print in GUI',width=30,bg='brown',fg='white',font=("bold",13),command=printoo).place(x=860,y=450)


root.mainloop()
