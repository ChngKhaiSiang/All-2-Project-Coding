from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import pyttsx3
from tkinter import filedialog
import os
import threading
from googletrans import Translator,LANGUAGES
from PIL import ImageTk,Image
import pygame
import tkinter as tk
import speech_recognition as sr
from pytesseract import pytesseract
from tkinter.filedialog import askopenfilename
from gtts import gTTS
ws = tk.Tk()
ws.geometry('1920x1080')
ws.resizable(0,0)
ws.rowconfigure(0,weight=1)
ws.columnconfigure(0,weight=1)

registerpage=Frame(ws)
loginpage=Frame(ws)
forgotpage=Frame(ws)
mainpage=Frame(ws,bg='black')
askttspage=Frame(ws,bg='light pink')
bahasattspage=Frame(ws,bg='light pink')
ttspage=Frame(ws,bg='light pink')
engttspage=Frame(ws,bg='light pink')
asksttpage=Frame(ws,bg='#dcb8ff')
engsttpage=Frame(ws,bg='#dcb8ff')
chisttpage=Frame(ws,bg='#dcb8ff')
bahasasttpage=Frame(ws,bg='#dcb8ff')
asktranslatepage=Frame(ws,bg='#81D8D0')
translatepage=Frame(ws,bg='#81D8D0')
primarytranslatepage=Frame(ws,bg='#81D8D0')
imagetotextpage=Frame(ws,bg='#D8759B')
askquizpage=Frame(ws,bg='light blue')
quizpage=Frame(ws,bg='light blue')
engquiz1page=Frame(ws,bg='#002EA6')
engquiz2page=Frame(ws,bg='#002EA6')
engquiz3page=Frame(ws,bg='#002EA6')
engquiz4page=Frame(ws,bg='#002EA6')
engquiz5page=Frame(ws,bg='#002EA6')
engquiz6page=Frame(ws,bg='#002EA6')
engquiz7page=Frame(ws,bg='#002EA6')
engquiz8page=Frame(ws,bg='#002EA6')
engquiz9page=Frame(ws,bg='#002EA6')
engquiz10page=Frame(ws,bg='#002EA6')
engscorepage=Frame(ws,bg='#002EA6')
chiquiz1page=Frame(ws,bg='#002EA6')
chiquiz2page=Frame(ws,bg='#002EA6')
chiquiz3page=Frame(ws,bg='#002EA6')
chiquiz4page=Frame(ws,bg='#002EA6')
chiquiz5page=Frame(ws,bg='#002EA6')
chiquiz6page=Frame(ws,bg='#002EA6')
chiquiz7page=Frame(ws,bg='#002EA6')
chiquiz8page=Frame(ws,bg='#002EA6')
chiquiz9page=Frame(ws,bg='#002EA6')
chiquiz10page=Frame(ws,bg='#002EA6')
chiscorepage=Frame(ws,bg='#002EA6')
for frame in (registerpage,loginpage,forgotpage,mainpage,askttspage,bahasattspage,ttspage,engttspage,asksttpage,engsttpage,chisttpage,bahasasttpage,asktranslatepage,translatepage,primarytranslatepage,imagetotextpage,askquizpage,quizpage,engquiz1page,
              engquiz2page,engquiz3page,engquiz4page,engquiz5page,engquiz6page,engquiz7page,engquiz8page,engquiz9page,engquiz10page,engscorepage,chiquiz1page,chiquiz2page,chiquiz3page,chiquiz4page,chiquiz5page,chiquiz6page
              ,chiquiz7page,chiquiz8page,chiquiz9page,chiquiz10page,chiscorepage):
    frame.grid(row=0,column=0,sticky='nsew')

def show_frame(frame):
    frame.tkraise()

loginbg=Image.open("loginbg.png")
loginbg = loginbg.resize((1920,1080))
loginbg=ImageTk.PhotoImage(loginbg)

registerbg=Image.open("registerbg.png")
registerbg = registerbg.resize((1920,1080))
registerbg=ImageTk.PhotoImage(registerbg)

soundicon=Image.open("soundicon.png")
soundicon = soundicon.resize((100,100))
soundicon=ImageTk.PhotoImage(soundicon)

downloadicon=Image.open("downloadicon.png")
downloadicon = downloadicon.resize((100,100))
downloadicon=ImageTk.PhotoImage(downloadicon)

clearicon=Image.open("clearicon.png")
clearicon = clearicon.resize((100,100))
clearicon=ImageTk.PhotoImage(clearicon)

translatebutton=Image.open("translate.png")
translatebutton = translatebutton.resize((100,100))
translatebutton=ImageTk.PhotoImage(translatebutton)



ttsicon=Image.open("ttsicon.png")
ttsicon = ttsicon.resize((300,300))
ttsicon=ImageTk.PhotoImage(ttsicon)

stticon=Image.open("stticon.png")
stticon = stticon.resize((300,300))
stticon=ImageTk.PhotoImage(stticon)

transicon=Image.open("translatoricon.png")
transicon = transicon.resize((300,300))
transicon=ImageTk.PhotoImage(transicon)

imagetotexticon=Image.open("imagetotext.png")
imagetotexticon = imagetotexticon.resize((300,300))
imagetotexticon=ImageTk.PhotoImage(imagetotexticon)

quizicon=Image.open("quiz.png")
quizicon = quizicon.resize((300,300))
quizicon=ImageTk.PhotoImage(quizicon)

recognizationbutton=Image.open("sttbutton.png")
recognizationbutton = recognizationbutton.resize((150,150))
recognizationbutton=ImageTk.PhotoImage(recognizationbutton)

good=Image.open("good.png")
good= good.resize((100,100))
good=ImageTk.PhotoImage(good)
#Register page--------------------------------------------------------------------------------------------------------------
def backlogin():
    show_frame(loginpage)

def backmain():
    show_frame(mainpage)

    
def sign_up():
    signup_pass = signup_passwordentry.get()
    signup_passcomfirm = signup_confirmpasswordentry.get()
    if usernameentry.get()==""or signup_emailentry.get()==""or sec_signup_question.get()==""or signup_answerentry.get()==""or signup_passwordentry.get()==""or signup_confirmpasswordentry.get()=="":
        messagebox.showerror("Error","All Fields Are Required")
    elif signup_pass != signup_passcomfirm :
        messagebox.showerror('Error', 'Password and confirm password must be the same!')
    elif sec_signup_question.get()=="Select":
        messagebox.showerror('Error', 'Please choose the Security Questions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
            cursor=con.cursor()
            cursor.execute('Select * from users where Email_Address=%s',signup_emailentry.get())
            row=cursor.fetchone()
            if row!=None:
                messagebox.showerror('Error', 'Email Address already exist')
            else:
                cursor.execute('insert into users(Username,Gender,Email_Address,Security_Questions,Answer,Password)values(%s,%s,%s,%s,%s,%s)',
                              (usernameentry.get(),
                                gendervalue.get(),
                                signup_emailentry.get(),
                                sec_signup_question.get(),
                                signup_answerentry.get(),
                                signup_passwordentry.get()
                                ))
                messagebox.showinfo(title='Welcome', message='You have successfully signed up!')
                show_frame(loginpage)
            con.commit()
            con.close()
            
                    

        except Exception as es:
            messagebox.showerror('Error',f'Error due to:{str(es)}')
        
Label(registerpage,image=registerbg).place(x=0,y=0)        
#frame_reg
frame_reg = Frame(registerpage,bg='white')
frame_reg.place(x=1050,y=170,height=700,width=800)


# Title
title= Label(frame_reg,text="Registeration Form", font=("Times New Roman",35, 'bold'),fg='#00a8f3',bg='white')
title.place(x=180,y=10)

 #Field
    
username = Label(frame_reg, text="Username:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')
signup_gender = Label(frame_reg, text="Gender:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')
signup_email = Label(frame_reg, text="Email address:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')
signup_question= Label(frame_reg,text='Security Question:',font=('Times New Roman',20,'bold'),fg='grey',bg='white')
signup_answer= Label(frame_reg,text='Answer:',font=('Times New Roman',20,'bold'),fg='grey',bg='white')
signup_password = Label(frame_reg, text="Password:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')
signup_confirmpassword = Label(frame_reg, text="Confirm password:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')

    
username.place(x=50,y=120)
signup_gender.place(x=50,y=180)
signup_email.place(x=50,y=240)
signup_question.place(x=50,y=300)
signup_answer.place(x=50,y=360)
signup_password.place(x=50,y=420)
signup_confirmpassword.place(x=50,y=480)
    
usernamevalue = StringVar()
signup_emailvalue = StringVar()
gendervalue = IntVar()
signup_questionvalue = StringVar()
signup_answervalue = StringVar()
signup_passwordvalue = StringVar()
signup_confirmpasswordvalue = StringVar()
    
    
usernameentry = Entry(frame_reg, textvariable =usernamevalue,font=('Times New Roman',15,'bold'),fg='black',bg='#00a8f3')
signup_emailentry = Entry(frame_reg, textvariable =signup_emailvalue,font=('Times New Roman',15,'bold'),fg='black',bg='#00a8f3')
#sec question
ques=['Select','In what city were you born?','What is the name of your favorite pet?','What high school did you attend?','What is the name of your first school?',
     'What was the make of your first car?','What was your favorite food as a child?']
sec_signup_question=ttk.Combobox(frame_reg,value=ques,font=('Times New Roman',15,'bold'))
sec_signup_question.current(0)
signup_answerentry = Entry(frame_reg,textvariable =signup_answervalue,font=('Times New Roman',15,'bold'),fg='black',bg='#00a8f3')
signup_passwordentry = Entry(frame_reg, textvariable =signup_passwordvalue,show='*',font=('Times New Roman',15,'bold'),fg='black',bg='#00a8f3')
signup_confirmpasswordentry = Entry(frame_reg, textvariable =signup_confirmpasswordvalue,show='*',font=('Times New Roman',15,'bold'),fg='black',bg='#00a8f3')
    
    
usernameentry.place(x=300,y=120,width=400,height=35)
signup_emailentry.place(x=300,y=240,width=400,height=35)
sec_signup_question.place(x=300,y=300,height=35,width=400)
signup_answerentry.place(x=300,y=360,width=400,height=35)
signup_passwordentry.place(x=300,y=420,width=400,height=35)
signup_confirmpasswordentry.place(x=300,y=480,width=400,height=35)

#Creating Checkbox
agree=Label(frame_reg,text="Submit and Agree To The Terms & Conditions", font=("Times New Roman",10, 'bold'),bg='white').place(x=270,y=550,height=40,width=300)
#Radio button
Radiobutton(frame_reg, text="Male",font=("Times New Roman",15, 'bold'), variable=gendervalue,value=1,bg='white').place(x=300,y=180)
Radiobutton(frame_reg, text="Female",font=("Times New Roman",15, 'bold'), variable=gendervalue,value=2,bg='white').place(x=400,y=180)

def show_hide2():
    if signup_passwordentry.cget('show') == '':
        signup_passwordentry.config(show='*')
        show2_button.config(text='show')
    else:
        signup_passwordentry.config(show='')
        show2_button.config(text='hide')

def show_hide3():
    if signup_confirmpasswordentry.cget('show') == '':
        signup_confirmpasswordentry.config(show='*')
        show3_button.config(text='show')
    else:
        signup_confirmpasswordentry.config(show='')
        show3_button.config(text='hide')
#hide btn
show2_button = Button(frame_reg,text='show',borderwidth=5,bg='white',command=show_hide2)
show2_button.place(x=655,y=420)

show3_button = Button(frame_reg,text='show',borderwidth=5,bg='white',command=show_hide3)
show3_button.place(x=655,y=480)
#Submit button
submitbtn = Button(frame_reg,text="Submit",font=("Times New Roman",20, 'bold'),borderwidth=10,bg='#00a8f3',fg='white',command=sign_up)
submitbtn.place(x=300,y=600,height=60,width=240)

Button(registerpage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backlogin).place(x=80,y=80,height=50,width=150)

#Forgot page------------------------------------------------------------------------------------------------------------
def forgot_password():
    if ftext_email.get()=='' or fsec_question.get()==''or ftext_answer.get()==''or ftext_new_password.get()=='':
        messagebox.showerror("Error","All Fields Are Required")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
            cursor=con.cursor()
            cursor.execute('Select * from users where Email_Address=%s',ftext_email.get())
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid Email Address to reset your password")
            else:
                con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
                cursor=con.cursor()
                cursor.execute('Select * from users where Email_Address=%s and Security_Questions=%s and Answer=%s',(ftext_email.get(),fsec_question.get(),ftext_answer.get()))
                row=cursor.fetchone()
                if row==None:
                    messagebox.showerror(title='Error', message='Please select correct Security Questions/Enter correct Answer!')
                else:
                    cursor.execute('update users set Password=%s where Email_Address=%s',(ftext_new_password.get(),ftext_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success','Password has been reset')
                    show_frame(loginpage)
        except Exception as es:
            messagebox.showerror('Error',f'Error due to:{str(es)}')

Label(forgotpage,image=registerbg).place(x=0,y=0)  
#frame_for
frame_for = Frame(forgotpage,bg='white')
frame_for.place(x=1200,y=200,height=600,width=500)
    
#title
title = Label(frame_for,text='Forgot Password',font=('Times New Roman',35,'bold'),fg='#00a8f3',bg='white')
title.place(x=80,y=20)
 
#email
email = Label(frame_for,text='Email Address :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
email.place(x=50,y=120)
 
ftext_email = Entry(frame_for,font=('Times New Roman',15,'bold'),fg='black',bg='#00a8f3')
ftext_email.place(x=50,y=150,width=400,height=35)

#sec question
question= Label(frame_for,text='Security Question :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
question.place(x=50,y=210)
ques=['Select','In what city were you born?','What is the name of your favorite pet?','What high school did you attend?','What is the name of your first school?','What was the make of your first car?','What was your favorite food as a child?']
fsec_question=ttk.Combobox(frame_for,value=ques,font=('Times New Roman',15,'bold'))
fsec_question.current(0)
fsec_question.place(x=50,y=240,height=40,width=300)

#answer
answer= Label(frame_for,text='Answer :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
answer.place(x=50,y=300)
  
ftext_answer = Entry(frame_for,font=('Times New Roman',15,'bold'),fg='black',bg='#00a8f3')
ftext_answer.place(x=50,y=330,width=400,height=35)

#password
new_password = Label(frame_for,text='New Password :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
new_password.place(x=50,y=390,width=400,height=35)

ftext_new_password = Entry(frame_for,font=('Times New Roman',15,'bold'),fg='black',bg='#00a8f3',show='*')
ftext_new_password.place(x=50,y=420,width=400,height=35)

def show_hide():
    if ftext_new_password.cget('show') == '':
        ftext_new_password.config(show='*')
        show_button.config(text='show')
    else:
        ftext_new_password.config(show='')
        show_button.config(text='hide')
        
#hide btn
show_button = Button(frame_for,text='show',borderwidth=5,bg='white',command=show_hide)
show_button.place(x=404,y=420) 
 
    
#reset password button
reset_password_button = Button(frame_for,text='RESET PASSWORD',font=('Times New Roman',15,'bold'),borderwidth=10,bg='#00a8f3',fg='white',command=forgot_password)
reset_password_button.place(x=130,y=500,height=60,width=240)

Button(forgotpage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backlogin).place(x=80,y=80,height=50,width=150)
#Login Page--------------------------------------------------------------------------------------------------------
def user_login():
    user_email = text_email.get()
    user_password = text_password.get()
    if text_email.get()==''or text_password.get()=='':
       messagebox.showerror("Error","All Fields Are Required")
    elif text_email.get()=='Admin111'or text_password.get()=='Admin111':
       messagebox.showinfo("Success","Welcome,Admin")
       
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
            cursor=con.cursor()
            cursor.execute('Select * from users where Email_Address=%s and Password=%s',(text_email.get(),text_password.get()))
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Email Address & Password!")
            else:
                messagebox.showinfo(title='Welcome', message='Login Successful')

                show_frame(mainpage)
            con.close()
        except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}')

Label(loginpage,image=loginbg).place(x=0,y=0)
                
#Login Frame
frame_login = Frame(loginpage,bg='white')
frame_login.place(x=200,y=200,height=500,width=500)
 
#title
title = Label(frame_login,text='Login',font=('Times New Roman',35,'bold'),fg='#1cc29c',bg='white')
title.place(x=190,y=20)
 
#email
email = Label(frame_login,text='Email Address :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
email.place(x=50,y=120)
text_email = Entry(frame_login,font=('Times New Roman',15,'bold'),fg='black',bd=2)
text_email.place(x=50,y=150,width=400,height=35)

#password
password = Label(frame_login,text='Password :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
password.place(x=50,y=210)
text_password = Entry(frame_login,font=('Times New Roman',15,'bold'),fg='black',bd=2,show='*')
text_password.place(x=50,y=240,width=400,height=35)

def show_hide1():
    if text_password.cget('show') == '':
        text_password.config(show='*')
        show1_button.config(text='show')
    else:
        text_password.config(show='')
        show1_button.config(text='hide')
        
#hide btn
show1_button = Button(frame_login,text='show',borderwidth=5,bg='white',command=show_hide1)
show1_button.place(x=410,y=240)

#register Frame
frame_register = Frame(loginpage,bg='white')
frame_register.place(x=200,y=720,height=100,width=500)

#new user
newuser = Label(frame_register,text='New user?',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
newuser.place(x=125,y=35)

#login button
login_button = Button(frame_login,text='LOGIN',font=('Times New Roman',15,'bold'),borderwidth=10,bg='#1cc29c',fg='white',command=user_login)
login_button.place(x=130,y=390,height=60,width=240)

#forget pass btn
forget_button = Button(frame_login,text='Forgot Password?',font=('Times New Roman',15,'bold','underline'),borderwidth=0,bg='white',fg='#1cc29c',command=lambda:show_frame(forgotpage))
forget_button.place(x=50,y=290)

#create an acc btn
acc_button = Button(frame_register,text='Create an account',font=('Times New Roman',15,'bold','underline'),borderwidth=0,bg='white',fg='#1cc29c',command=lambda:show_frame(registerpage))
acc_button.place(x=220,y=33)

#Main page-----------------------------------------------------------------------------------------------------

Label(mainpage,text='Welcome',font=('Ink Free',70,'bold'),bg='black',fg='white').place(x=800,y=80)

tts_button = Button(mainpage,text='Text To Speech',font=('Times New Roman',15,'bold'),borderwidth=5,bg='#e44100',fg='black',command=lambda:show_frame(askttspage))
tts_button.place(x=150,y=300,height=80,width=200)
Label(mainpage,image=ttsicon).place(x=100,y=500)

stt_button = Button(mainpage,text='Speech To Text',font=('Times New Roman',15,'bold'),borderwidth=5,bg='#e44100',fg='black',command=lambda:show_frame(asksttpage))
stt_button.place(x=500,y=300,height=80,width=200)
Label(mainpage,image=stticon).place(x=450,y=500)

trans_button = Button(mainpage,text='Translator',font=('Times New Roman',15,'bold'),borderwidth=5,bg='#e44100',fg='black',command=lambda:show_frame(asktranslatepage))
trans_button.place(x=850,y=300,height=80,width=200)
Label(mainpage,image=transicon).place(x=800,y=500)

file_button = Button(mainpage,text='Image To Text',font=('Times New Roman',15,'bold'),borderwidth=5,bg='#e44100',fg='black',command=lambda:show_frame(imagetotextpage))
file_button.place(x=1200,y=300,height=80,width=200)
Label(mainpage,image=imagetotexticon).place(x=1150,y=500)

quiz_button = Button(mainpage,text='Learning Quiz',font=('Times New Roman',15,'bold'),borderwidth=5,bg='#e44100',fg='black',command=lambda:show_frame(askquizpage))
quiz_button.place(x=1550,y=300,height=80,width=200)
Label(mainpage,image=quizicon).place(x=1500,y=500)

Button(mainpage,text="Log Out",font=("Times New Roman",20, 'bold'),bg='#e44100',bd=5,command=backlogin).place(x=80,y=80,height=50,width=150)
#ask tts page-----------------------------------------------------------------------------------------------------------------
Label(askttspage,text='Text To Speech',font=('Ink Free',70,'bold'),bg='light pink',fg='white').place(x=680,y=80)

engtts = Button(askttspage,text='English',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(engttspage))
engtts.place(x=850,y=350,height=100,width=280)

chitts = Button(askttspage,text='Chinese',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(ttspage))
chitts.place(x=850,y=550,height=100,width=280)

bahasatts = Button(askttspage,text='Malay',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(bahasattspage))
bahasatts.place(x=850,y=750,height=100,width=280)

Button(askttspage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)
#English TTS Page----------------------------------------------------------------------------------------------------------
engine = pyttsx3.init()
def engspeaknow():
    text=engtts_entry.get(1.0,END)
    gender=enggender_combobox.get()
    spe=engspeed.get()
    volume_=engvolume.get()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    
    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.setProperty('volume',(volume_)/100)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.setProperty('volume',(volume_)/100)
            engine.say(text)
            engine.runAndWait()

    if(text):
        engine.setProperty('rate',spe)
        setvoice()


engine = pyttsx3.init()    
def engdownload():
    downtext=engtts_entry.get(1.0,END)
    gender=enggender_combobox.get()
    spe=engspeed.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            tts=gTTS(text=downtext,lang='en')
            tts.save('eng.mp3')
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            tts=gTTS(text=downtext,lang='en')
            tts.save('eng.mp3')

    if(downtext):
       engine.setProperty('rate',spe)
       setvoice()
        
def engclear():
    engtts_entry.delete(1.0,END)


Label(engttspage,bg='#00a8f3').place(x=100,y=50,height=160,width=1700)
Label(engttspage,text='Text To Speech(English)',font=('Ink Free',50,'bold'),bg='#00a8f3',fg='white').place(x=600,y=80)
Label(engttspage,bg='#00a8f3').place(x=100,y=250,height=750,width=1700)

engtts_entry = Text(engttspage,font=('Times News Roman',30))
engtts_entry.place(x=140,y=290,height=650,width=850)

engscrolltts=ttk.Scrollbar(engttspage,orient='vertical',command=engtts_entry.yview)
engscrolltts.place(x=995,y=290,height=650,width=30)
engtts_entry['yscrollcommand']=engscrolltts.set

engspeed=Scale(engttspage,length=300,label='Voice Speed',bg='white',font=('Times New Roman',15,'bold'),from_=0,to=300,resolution=1,orient=HORIZONTAL)
engspeed.set(150)
engspeed.place(x=1200,y=450)

engvolume=Scale(engttspage,length=300,label='Volume',bg='white',font=('Times New Roman',15,'bold'),from_=0,to=100,resolution=1,orient=HORIZONTAL)
engvolume.set(50)
engvolume.place(x=1200,y=600)

engspeak_button = Button(engttspage,text='Speak',font=('Times New Roman',15,'bold'),bg='white',bd=4,image=soundicon,command=engspeaknow)
engspeak_button.place(x=1200,y=800)


engdownload_button = Button(engttspage,text='Download',font=('Times New Roman',15,'bold'),bg='white',bd=4,image=downloadicon,command=engdownload)
engdownload_button.place(x=1400,y=800)

engclear_button = Button(engttspage,text='Clear',font=('Times New Roman',15,'bold'),bg='white',bd=4,image=clearicon,command=engclear)
engclear_button.place(x=1600,y=800)

enggen=['Male','Female']
enggender_combobox=ttk.Combobox(engttspage,font=('Times New Roman',15,'bold'))
enggender_combobox['values']=enggen
enggender_combobox.place(x=1200,y=350)
enggender_combobox.set('Male')

Button(engttspage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=120,y=102,height=50,width=150)
#Chinese TTS Page---------------------------------------------------------------------------------------------------------
engine = pyttsx3.init()
def speaknow():
    text=tts_entry.get(1.0,END)
    gender=gender_combobox.get()
    spe=speed.get()
    volume_=volume.get()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    
    def setvoice():
        if(gender=='Female'):
            engine.setProperty('voice',voices[2].id)
            engine.setProperty('volume',(volume_)/100)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[2].id)
            engine.setProperty('volume',(volume_)/100)
            engine.say(text)
            engine.runAndWait()

    if(spe):
        engine.setProperty('rate',speed.get())
        setvoice()


    
def download():
    downtext=tts_entry.get(1.0,END)
    gender=gender_combobox.get()
    spe=speed.get()
    volume_=volume.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            tts=gTTS(text=downtext,lang='zh')
            tts.save('chi.mp3')
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            tts=gTTS(text=downtext,lang='zh')
            tts.save('chi.mp3')

    if(spe):
        engine.setProperty('rate',speed.get())
        setvoice()

def clear():
    tts_entry.delete(1.0,END)


Label(ttspage,bg='#00a8f3').place(x=100,y=50,height=160,width=1700)
Label(ttspage,text='Text To Speech(Chinese)',font=('Ink Free',50,'bold'),bg='#00a8f3',fg='white').place(x=600,y=80)
Label(ttspage,bg='#00a8f3').place(x=100,y=250,height=750,width=1700)

tts_entry = Text(ttspage,font=('Times News Roman',30))
tts_entry.place(x=140,y=290,height=650,width=850)

scrolltts=ttk.Scrollbar(ttspage,orient='vertical',command=tts_entry.yview)
scrolltts.place(x=995,y=290,height=650,width=30)
tts_entry['yscrollcommand']=scrolltts.set

speed=Scale(ttspage,length=300,label='Voice Speed',bg='white',font=('Times New Roman',15,'bold'),from_=0,to=300,resolution=1,orient=HORIZONTAL)
speed.set(150)
speed.place(x=1200,y=450)

volume=Scale(ttspage,length=300,label='Volume',bg='white',font=('Times New Roman',15,'bold'),from_=0,to=100,resolution=1,orient=HORIZONTAL)
volume.set(50)
volume.place(x=1200,y=600)

speak_button = Button(ttspage,text='Speak',font=('Times New Roman',15,'bold'),bg='white',bd=4,image=soundicon,command=speaknow)
speak_button.place(x=1200,y=800)



download_button = Button(ttspage,text='Download',font=('Times New Roman',15,'bold'),bg='white',bd=4,image=downloadicon,command=download)
download_button.place(x=1400,y=800)

clear_button = Button(ttspage,text='Clear',font=('Times New Roman',15,'bold'),bg='white',bd=4,image=clearicon,command=clear)
clear_button.place(x=1600,y=800)

gen=['Male','Female']
gender_combobox=ttk.Combobox(ttspage,font=('Times New Roman',15,'bold'))
gender_combobox['values']=gen
gender_combobox.place(x=1200,y=350)
gender_combobox.set('Male')

Button(ttspage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=120,y=102,height=50,width=150)
#bahasa tts------------------------------------------------------------------------------------------------------------------------------------
pygame.mixer.init()
def speakbahasa():
    try:
        bahasagender=bahasagender_combobox.get()
        con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
        cursor=con.cursor()
        cursor.execute('Select * from bahasa where Word=%s',bahasatts_entry.get())
        row=cursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Not available word')
        elif bahasatts_entry.get()=='saya' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\saya.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='tidur' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\tidur.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='mandi' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\mandi.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='makan' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\makan.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='duduk' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\duduk.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='keluar' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\keluar.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='nyanyi' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\nyanyi.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='bayar' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\bayar.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='ambil' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\ambil.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='hantar' and bahasagender=='Female':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\hantar.mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='saya' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\saya(1).mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='tidur' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\tidur (1).mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='mandi' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\mandi (1).mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='makan' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\makan (1).mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='duduk' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\duduk (1).mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='keluar' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\keluar (1).mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='nyanyi' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\nyanyi (1).mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='bayar' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\bayar (1).mp3')
            pygame.mixer.music.play(loops=1)
        elif bahasatts_entry.get()=='ambil' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\ambil (1).mp3')
            pygame.mixer.music.play(loops=1)
        elif row!='hantar' and bahasagender=='Male':
            pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\hantar (1).mp3')
            pygame.mixer.music.play(loops=1)
        else:
            messagebox.showerror('Error','Not available word')
                                
        con.commit()
        con.close()
    except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}')
            

Label(bahasattspage,bg='#00a8f3').place(x=100,y=50,height=160,width=1700)
Label(bahasattspage,text='Text To Speech(Malay)',font=('Ink Free',50,'bold'),bg='#00a8f3',fg='white').place(x=620,y=80)
Label(bahasattspage,bg='#00a8f3').place(x=100,y=250,height=750,width=1700)


bahasatts_entry = Entry(bahasattspage,font=('Times News Roman',30))
bahasatts_entry.place(x=140,y=290,height=650,width=850)


bahasaspeak_button = Button(bahasattspage,text='Speak',font=('Times New Roman',20,'bold'),bg='white',bd=4,image=soundicon,command=speakbahasa)
bahasaspeak_button.place(x=1200,y=800)


bahasagen=['Male','Female']
bahasagender_combobox=ttk.Combobox(bahasattspage,font=('Times New Roman',20,'bold'))
bahasagender_combobox['values']=bahasagen
bahasagender_combobox.place(x=1200,y=350)
bahasagender_combobox.set('Male')

Button(bahasattspage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=120,y=102,height=50,width=150)
#ask stt page-----------------------------------------------------------------------------------------------------------------
Label(asksttpage,text='Speech To Text',font=('Ink Free',70,'bold'),bg='#dcb8ff',fg='white').place(x=680,y=80)

engstt = Button(asksttpage,text='English',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(engsttpage))
engstt.place(x=850,y=350,height=100,width=280)

chistt = Button(asksttpage,text='Chinese',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(chisttpage))
chistt.place(x=850,y=550,height=100,width=280)

bahasastt = Button(asksttpage,text='Malay',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(bahasasttpage))
bahasastt.place(x=850,y=750,height=100,width=280)

Button(asksttpage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)
#English Stt page--------------------------------------------------------------------------------------------------------------------------------------
Label(engsttpage, text='English',font=('Ink Free',50,'bold'),bg='#dcb8ff',fg='white').place(x=800,y=80)
def sttengclear():
    engtext.delete(1.0,END)
    
def engrecordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source, 3, 3)
            try:    
                text1 = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text1
engrecordbutton = Button(engsttpage,image=recognizationbutton,command=lambda: engtext.insert(END, engrecordvoice()))
engrecordbutton.place(x=850, y=800)

engtext = Text(engsttpage,font=('Times New Roman',30,'bold'), height=10, width=75)
engtext.place(x=180, y=280)

stteng = Button(engsttpage,text='Clear',font=('Times New Roman',15,'bold'),bg='white',bd=4,image=clearicon,command=sttengclear)
stteng.place(x=1150,y=825)

Button(engsttpage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)
#Chinese Stt page--------------------------------------------------------------------------------------------------------------------------------------
Label(chisttpage, text='Chinese',font=('Ink Free',50,'bold'),bg='#dcb8ff',fg='white').place(x=800,y=80)
def sttchiclear():
    chitext.delete(1.0,END)
    
def chirecordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source, 3,3)
            try:    
                text1 = r.recognize_google(audio,language="zh")
            except:
                pass
            return text1
chirecordbutton = Button(chisttpage,image=recognizationbutton,command=lambda: chitext.insert(END, chirecordvoice()))
chirecordbutton.place(x=850, y=800)

chitext = Text(chisttpage,font=('Times New Roman',30,'bold'), height=10, width=75)
chitext.place(x=180, y=280)

sttchi = Button(chisttpage,text='Clear',font=('Times New Roman',15,'bold'),bg='white',bd=4,image=clearicon,command=sttchiclear)
sttchi.place(x=1150,y=825)

Button(chisttpage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)
#Malay Stt page--------------------------------------------------------------------------------------------------------------------------------------
Label(bahasasttpage, text='Malay',font=('Ink Free',50,'bold'),bg='#dcb8ff',fg='white').place(x=830,y=80)
def sttbahasaclear():
    bahasatext.delete(1.0,END)
    
def bahasarecordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio,language="ms-MY")
            except:
                pass
            return text1
bahasarecordbutton = Button(bahasasttpage,image=recognizationbutton,command=lambda: bahasatext.insert(END, bahasarecordvoice()))
bahasarecordbutton.place(x=850, y=800)

bahasatext = Text(bahasasttpage,font=('Times New Roman',30,'bold'), height=10, width=75)
bahasatext.place(x=180, y=280)

sttchi = Button(bahasasttpage,text='Clear',font=('Times New Roman',15,'bold'),bg='white',bd=4,image=clearicon,command=sttbahasaclear)
sttchi.place(x=1150,y=825)

Button(bahasasttpage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)
#ask translate page------------------------------------------------------------------------------------------------------------------------------------
Label(asktranslatepage,text='Translator',font=('Ink Free',70,'bold'),bg='#81D8D0',fg='white').place(x=720,y=80)

Button(asktranslatepage,text='Primary Translator',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(primarytranslatepage)).place(x=800,y=350,height=100,width=280)


Button(asktranslatepage,text='Advanced Translator',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(translatepage)).place(x=800,y=550,height=100,width=280)

Button(asktranslatepage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)
#Translate Page---------------------------------------------------------------------------------------------------------------------------------------


def show():
    v1=choose1.get()
    v2=choose2.get()
    text1.config(text= v1)
    text2.config(text= v2)
    translatepage.after(1000,show)

def translate():
    trans=Translator()
    trans_lang=trans.translate(input_text.get(1.0,END),src=choose1.get(),dest=choose2.get())

    output_text.delete(1.0,END)
    output_text.insert(END,trans_lang.text)
        
def clear():
    output_text.delete(1.0,END)
    input_text.delete(1.0,END)

Label(translatepage,text='Translator',font=('Ink Free',40,'bold'),bg='#81D8D0',fg='white').place(x=790,y=80)

text1=Label(translatepage,text='english',font=('Ink Free',30,'bold'),bg='#81D8D0',fg='white')
text1.place(x=300,y=200)

text2=Label(translatepage,text='chinese (simplified)',font=('Ink Free',30,'bold'),bg='#81D8D0',fg='white')
text2.place(x=1250,y=200)

language=list(LANGUAGES.values())

choose1=ttk.Combobox(translatepage,values=language,font=('Times New Roman',20,'bold'))
choose1.place(x=300,y=260)
choose1.set('english')

choose2=ttk.Combobox(translatepage,values=language,font=('Times New Roman',20,'bold'))
choose2.place(x=1250,y=260)
choose2.set('chinese (simplified)')

input_text=Text(translatepage,font=('Times New Roman',20,'bold'),height=15,width=45)
input_text.place(x=150,y=350)

output_text=Text(translatepage,font=('Times New Roman',20,'bold'),height=15,width=45)
output_text.place(x=1100,y=350)
        
translate=Button(translatepage,text='Translate',bd=5,image=translatebutton,command=translate)
translate.place(x=900,y=520)

clear=Button(translatepage,text='Clear',bd=5,image=clearicon,command=clear)
clear.place(x=900,y=700)

Button(translatepage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)

show()
# primary Translate Page---------------------------------------------------------------------------------------------------------------------------------------
def show2():
    vv=prichoose1.get()
    pritext1.config(text= vv)
    primarytranslatepage.after(1000,show2)


def ptranslate():
    if prichoose1.get()=='English':
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
            cursor=con.cursor()
            cursor.execute('Select * from translate where English=%s',pinput_text.get())
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Not Available Word!")   
            else:
                poutput_text.insert(END,row)
            con.commit()
            con.close()
        except Exception as es:
            messagebox.showerror('Error',f'Error due to:{str(es)}')
    elif prichoose1.get()=='Chinese':
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
            cursor=con.cursor()
            cursor.execute('Select * from translate where Chinese=%s',pinput_text.get())
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Not Available Word!")   
            else:
                poutput_text.insert(END,row)
            con.commit()
            con.close()
        except Exception as es:
            messagebox.showerror('Error',f'Error due to:{str(es)}')
    elif prichoose1.get()=='Malay':
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
            cursor=con.cursor()
            cursor.execute('Select * from translate where Malay=%s',pinput_text.get())
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Not Available Word!")   
            else:
                poutput_text.insert(END,row)
            con.commit()
            con.close()
        except Exception as es:
            messagebox.showerror('Error',f'Error due to:{str(es)}')
    else:
        messagebox.showerror("Error","Not Available Word!")
def pclear():
    poutput_text.delete(1.0,END)
    
Label(primarytranslatepage,text='Translator',font=('Ink Free',40,'bold'),bg='#81D8D0',fg='white').place(x=790,y=80)

pritext1=Label(primarytranslatepage,text='English',font=('Ink Free',30,'bold'),bg='#81D8D0',fg='white')
pritext1.place(x=300,y=200)

ptext2=Label(primarytranslatepage,text='English , Chinese , Malay',font=('Ink Free',30,'bold'),bg='#81D8D0',fg='white')
ptext2.place(x=1200,y=200)

languages=['English','Chinese','Malay']

prichoose1=ttk.Combobox(primarytranslatepage,values=languages,font=('Times New Roman',20,'bold'))
prichoose1.place(x=300,y=260)
prichoose1.set('English')

pinput_text=Entry(primarytranslatepage,font=('Times New Roman',30,'bold'))
pinput_text.place(x=150,y=350,height=480,width=660)

poutput_text=Text(primarytranslatepage,font=('Times New Roman',30,'bold'))
poutput_text.place(x=1100,y=350,height=480,width=660)

        
ptranslate=Button(primarytranslatepage,text='Translate',bd=5,image=translatebutton,command=ptranslate)
ptranslate.place(x=900,y=520)

pclear=Button(primarytranslatepage,text='Clear',bd=5,image=clearicon,command=pclear)
pclear.place(x=900,y=700)

Button(primarytranslatepage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)

show2()
#image to text page------------------------------------------------------------------------------------
Label(imagetotextpage,text='Image To Text',font=('Ink Free',40,'bold'),bg='#D8759B',fg='#F9F3E9').place(x=800,y=80)

def upload_file():
    f_types=[('Jpg files','*.jpg'),('Png files','*.png'),('All Files','*.*')]
    filename=tk.filedialog.askopenfilename(filetypes=f_types)
    imgtotext = Image.open(filename)
    imgtotext=imgtotext.resize((400,400))
    imgtotext=ImageTk.PhotoImage(imgtotext)
    el=Label(imagetotextpage)
    el.place(x=1250,y=390)
    el.image=imgtotext
    el['image']=imgtotext



def image():
    path_to_tesseract = r'C:\\Users\\User\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
    f_types=[('Jpg files','*.jpg'),('Png files','*.png'),('All Files','*.*')]
    filename=tk.filedialog.askopenfilename(filetypes=f_types)
    path_to_images = Image.open(filename)

    pytesseract.tesseract_cmd = path_to_tesseract

    imagetext = pytesseract.image_to_string(path_to_images)
    
    return (imagetext)


imagebutton = Button(imagetotextpage, text='start',font=("Times New Roman",20, 'bold'),bg='#F9F3E9',fg='#D8759B',bd=5, command=lambda:ptext.insert(END,image()))
imagebutton.place(x=930,y=520,height=100,width=150)

ptext = Text(imagetotextpage,font=("Times New Roman",20, 'bold'),bg='#F9F3E9', height=20, width=52)
ptext.place(x=220,y=350,height=480,width=620)

Label(imagetotextpage,bg='#F9F3E9').place(x=1200,y=350,height=480,width=500)

uploadbutton = Button(imagetotextpage, text='upload',font=("Times New Roman",20, 'bold'),bg='#F9F3E9',fg='#D8759B',bd=5, command=upload_file)
uploadbutton.place(x=930,y=700,height=100,width=150)

Button(imagetotextpage,text="Back",font=("Times New Roman",20, 'bold'),bg='#F9F3E9',fg='#D8759B',bd=5,command=backmain).place(x=80,y=80,height=50,width=150)
#ask Quiz Page-----------------------------------------------------------------------------------------------------------------------
Label(askquizpage,text='Learning Quiz',font=('Ink Free',70,'bold'),bg='light blue',fg='white').place(x=650,y=80)
Label(askquizpage,text='Username:',font=('Times New Roman',30,'bold'),bg='light blue',fg='black').place(x=500,y=420)

quizuser_entry = Entry(askquizpage,font=('Times New Roman',30,'bold'))
quizuser_entry.place(x=800,y=350,height=200,width=550)
Button(askquizpage,text='Submit',width=15,command=lambda:show_frame(quizpage)).place(x=800,y=700,height=100,width=250)

Button(askquizpage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)
#Quiz Page-----------------------------------------------------------------------------------------------------------------------
Label(quizpage,text='Learning Quiz',font=('Ink Free',70,'bold'),bg='light blue',fg='white').place(x=650,y=80)

Button(quizpage,text='Learn English',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(engquiz1page)).place(x=800,y=350,height=100,width=280)


Button(quizpage,text='Learn Chinese',font=('Times New Roman',15,'bold'),borderwidth=5,bg='white',fg='black',command=lambda:show_frame(chiquiz1page)).place(x=800,y=550,height=100,width=280)

Button(quizpage,text="Back",font=("Times New Roman",20, 'bold'),bd=5,command=backmain).place(x=80,y=80,height=50,width=150)
#english quiz---------------------------------------------------------------------------------------------------------------
Label(engquiz1page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz1page,text='Quiz 1',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz1page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

global counter

counter=0
def score():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 1', message='Correct!')
    show_frame(engquiz2page)

Button(engquiz1page,text='猥琐',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz2page)).place(x=1100,y=350,height=80,width=200)
Button(engquiz1page,text='帅气',font=('Times New Roman',15,'bold'),command=score).place(x=1100,y=500,height=80,width=200)
Button(engquiz1page,text='漂亮',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz2page)).place(x=1100,y=650,height=80,width=200)
Button(engquiz1page,text='丑陋',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz2page)).place(x=1100,y=800,height=80,width=200)

play_btn=ImageTk.PhotoImage(Image.open("C:\\Users\\User\\OneDrive\\Desktop\\All 2\\playbutton.png"))
pygame.mixer.init()
def engquiz1():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\handsome.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz1page,image=play_btn,bg='#fcc630',bd=5,command=engquiz1).place(x=450,y=450)
       
       
Label(engquiz2page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz2page,text='Quiz 2',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz2page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

def score1():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 2', message='Correct!')
    show_frame(engquiz3page)
Button(engquiz2page,text='耐心',font=('Times New Roman',15,'bold'),command=score1).place(x=1100,y=350,height=80,width=200)
Button(engquiz2page,text='暴躁',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz3page)).place(x=1100,y=500,height=80,width=200)
Button(engquiz2page,text='焦急',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz3page)).place(x=1100,y=650,height=80,width=200)
Button(engquiz2page,text='放纵',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz3page)).place(x=1100,y=800,height=80,width=200)

def engquiz2():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\patient.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz2page,image=play_btn,bg='#fcc630',bd=5,command=engquiz2).place(x=450,y=450)

Label(engquiz3page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz3page,text='Quiz 3',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz3page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)
def score2():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 3', message='Correct!')
    show_frame(engquiz4page)
Button(engquiz3page,text='情侣',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz4page)).place(x=1100,y=350,height=80,width=200)
Button(engquiz3page,text='学生',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz4page)).place(x=1100,y=500,height=80,width=200)
Button(engquiz3page,text='朋友',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz4page)).place(x=1100,y=650,height=80,width=200)
Button(engquiz3page,text='家庭',font=('Times New Roman',15,'bold'),command=score2).place(x=1100,y=800,height=80,width=200)

def engquiz3():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\family.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz3page,image=play_btn,bg='#fcc630',bd=5,command=engquiz3).place(x=450,y=450)

Label(engquiz4page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz4page,text='Quiz 4',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz4page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)
def score3():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 4', message='Correct!')
    show_frame(engquiz5page)
Button(engquiz4page,text='杯子',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz5page)).place(x=1100,y=350,height=80,width=200)
Button(engquiz4page,text='拖把',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz5page)).place(x=1100,y=500,height=80,width=200)
Button(engquiz4page,text='牙刷',font=('Times New Roman',15,'bold'),command=score3).place(x=1100,y=650,height=80,width=200)
Button(engquiz4page,text='牙膏',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz5page)).place(x=1100,y=800,height=80,width=200)

def engquiz4():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\toothbrush.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz4page,image=play_btn,bg='#fcc630',bd=5,command=engquiz4).place(x=450,y=450)

Label(engquiz5page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz5page,text='Quiz 5',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz5page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)
def score4():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 5', message='Correct!')
    show_frame(engquiz6page)
Button(engquiz5page,text='医院',font=('Times New Roman',15,'bold'),command=score4).place(x=1100,y=350,height=80,width=200)
Button(engquiz5page,text='餐厅',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz6page)).place(x=1100,y=500,height=80,width=200)
Button(engquiz5page,text='酒店',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz6page)).place(x=1100,y=650,height=80,width=200)
Button(engquiz5page,text='超市',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz6page)).place(x=1100,y=800,height=80,width=200)

def engquiz5():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\hospital.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz5page,image=play_btn,bg='#fcc630',bd=5,command=engquiz5).place(x=450,y=450)

Label(engquiz6page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz6page,text='Quiz 6',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz6page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)
def score5():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 6', message='Correct!')
    show_frame(engquiz7page)
Button(engquiz6page,text='厕所',font=('Times New Roman',15,'bold'),command=score5).place(x=1100,y=350,height=80,width=200)
Button(engquiz6page,text='房间',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz7page)).place(x=1100,y=500,height=80,width=200)
Button(engquiz6page,text='客厅',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz7page)).place(x=1100,y=650,height=80,width=200)
Button(engquiz6page,text='厨房',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz7page)).place(x=1100,y=800,height=80,width=200)

def engquiz6():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\toilet.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz6page,image=play_btn,bg='#fcc630',bd=5,command=engquiz6).place(x=450,y=450)

Label(engquiz7page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz7page,text='Quiz 7',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz7page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)
def score6():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 7', message='Correct!')
    show_frame(engquiz8page)
Button(engquiz7page,text='相机',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz8page)).place(x=1100,y=350,height=80,width=200)
Button(engquiz7page,text='照片',font=('Times New Roman',15,'bold'),command=score6).place(x=1100,y=500,height=80,width=200)
Button(engquiz7page,text='电影',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz8page)).place(x=1100,y=650,height=80,width=200)
Button(engquiz7page,text='影片',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz8page)).place(x=1100,y=800,height=80,width=200)

def engquiz7():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\photo.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz7page,image=play_btn,bg='#fcc630',bd=5,command=engquiz7).place(x=450,y=450)

Label(engquiz8page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz8page,text='Quiz 8',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz8page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)
def score7():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 8', message='Correct!')
    show_frame(engquiz9page)
Button(engquiz8page,text='健身',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz9page)).place(x=1100,y=350,height=80,width=200)
Button(engquiz8page,text='运动',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz9page)).place(x=1100,y=500,height=80,width=200)
Button(engquiz8page,text='操劳',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz9page)).place(x=1100,y=650,height=80,width=200)
Button(engquiz8page,text='休息',font=('Times New Roman',15,'bold'),command=score7).place(x=1100,y=800,height=80,width=200)

def engquiz8():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\rest.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz8page,image=play_btn,bg='#fcc630',bd=5,command=engquiz8).place(x=450,y=450)

Label(engquiz9page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz9page,text='Quiz 9',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz9page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)
def score8():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 9', message='Correct!')
    show_frame(engquiz10page)
Button(engquiz9page,text='安全',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz10page)).place(x=1100,y=350,height=80,width=200)
Button(engquiz9page,text='安宁',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz10page)).place(x=1100,y=500,height=80,width=200)
Button(engquiz9page,text='危险',font=('Times New Roman',15,'bold'),command=score8).place(x=1100,y=650,height=80,width=200)
Button(engquiz9page,text='小心',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engquiz10page)).place(x=1100,y=800,height=80,width=200)

def engquiz9():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\dangerous.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz9page,image=play_btn,bg='#fcc630',bd=5,command=engquiz9).place(x=450,y=450)

Label(engquiz10page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(engquiz10page,text='Quiz 10',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(engquiz10page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)


def score9():
    global counter
    counter +=1
    engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 10', message='Correct!')
    show_frame(engscorepage)
    
Button(engquiz10page,text='人民',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engscorepage)).place(x=1100,y=350,height=80,width=200)
Button(engquiz10page,text='员工',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engscorepage)).place(x=1100,y=500,height=80,width=200)
Button(engquiz10page,text='政府',font=('Times New Roman',15,'bold'),command=score9).place(x=1100,y=650,height=80,width=200)
Button(engquiz10page,text='亲戚',font=('Times New Roman',15,'bold'),command=lambda:show_frame(engscorepage)).place(x=1100,y=800,height=80,width=200)

def engquiz10():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\government.mp3')
       pygame.mixer.music.play(loops=1)

Button(engquiz10page,image=play_btn,bg='#fcc630',bd=5,command=engquiz10).place(x=450,y=450)
#english score page------------------------------------------------------------------------------------------------------------
engscore=Label(engscorepage,text=counter,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
Label(engscorepage,text='Your Score : ',font=('Times New Roman',30,'bold'),bg='#002EA6').place(x=450,y=450)
Label(engscorepage,text='Nice Try',font=('Ink Free',50,'bold'),bg='#002EA6').place(x=700,y=100)
Label(engscorepage,image=good,bg='#002EA6').place(x=1000,y=90)
def saveengscore():
    try:
        con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
        cursor=con.cursor()
        cursor.execute('insert into test(Username,Score)values(%s,%s)',(quizuser_entry.get(),counter))
        con.commit()
        con.close()
        
    except Exception as es:
         messagebox.showerror('Error',f'Error due to:{str(es)}')
    show_frame(mainpage)

Button(engscorepage,text='Done',font=('Times New Roman',20,'bold'),bg='white',bd=5,command=saveengscore).place(x=800,y=750,height=100,width=250)
#Chinese Quiz-------------------------------------------------------------------------------------------------------------
Label(chiquiz1page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz1page,text='Quiz 1',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz1page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)
global counter1
counter1=0
def score10():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 1', message='Correct!')
    show_frame(chiquiz2page)
Button(chiquiz1page,text='carelessness',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz2page)).place(x=1100,y=350,height=80,width=200)
Button(chiquiz1page,text='attention',font=('Times New Roman',15,'bold'),command=score10).place(x=1100,y=500,height=80,width=200)
Button(chiquiz1page,text='inattention',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz2page)).place(x=1100,y=650,height=80,width=200)
Button(chiquiz1page,text='neglect',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz2page)).place(x=1100,y=800,height=80,width=200)

def chiquiz1():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\关注.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz1page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz1).place(x=450,y=450)

Label(chiquiz2page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz2page,text='Quiz 2',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz2page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

def score11():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 2', message='Correct!')
    show_frame(chiquiz3page)
Button(chiquiz2page,text='criticize',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz3page)).place(x=1100,y=350,height=80,width=200)
Button(chiquiz2page,text='blame',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz3page)).place(x=1100,y=500,height=80,width=200)
Button(chiquiz2page,text='condemn',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz3page)).place(x=1100,y=650,height=80,width=200)
Button(chiquiz2page,text='praise',font=('Times New Roman',15,'bold'),command=score11).place(x=1100,y=800,height=80,width=200)

def chiquiz2():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\赞扬.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz2page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz2).place(x=450,y=450)

Label(chiquiz3page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz3page,text='Quiz 3',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz3page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

def score12():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 3', message='Correct!')
    show_frame(chiquiz4page)
Button(chiquiz3page,text='lecturer',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz4page)).place(x=1100,y=350,height=80,width=200)
Button(chiquiz3page,text='classroom',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz4page)).place(x=1100,y=500,height=80,width=200)
Button(chiquiz3page,text='instructor',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz4page)).place(x=1100,y=650,height=80,width=200)
Button(chiquiz3page,text='lecture',font=('Times New Roman',15,'bold'),command=score12).place(x=1100,y=800,height=80,width=200)

def chiquiz3():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\讲座.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz3page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz3).place(x=450,y=450)

Label(chiquiz4page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz4page,text='Quiz 4',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz4page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

def score13():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 4', message='Correct!')
    show_frame(chiquiz5page)
Button(chiquiz4page,text='bath',font=('Times New Roman',15,'bold'),command=score13).place(x=1100,y=350,height=80,width=200)
Button(chiquiz4page,text='sweep',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz5page)).place(x=1100,y=500,height=80,width=200)
Button(chiquiz4page,text='run',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz5page)).place(x=1100,y=650,height=80,width=200)
Button(chiquiz4page,text='play',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz5page)).place(x=1100,y=800,height=80,width=200)

def chiquiz4():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\洗澡.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz4page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz4).place(x=450,y=450)

Label(chiquiz5page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz5page,text='Quiz 5',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz5page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)
def score14():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 5', message='Correct!')
    show_frame(chiquiz6page)
Button(chiquiz5page,text='careless',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz6page)).place(x=1100,y=350,height=80,width=200)
Button(chiquiz5page,text='rude',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz6page)).place(x=1100,y=500,height=80,width=200)
Button(chiquiz5page,text='careful',font=('Times New Roman',15,'bold'),command=score14).place(x=1100,y=650,height=80,width=200)
Button(chiquiz5page,text='irritable',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz6page)).place(x=1100,y=800,height=80,width=200)

def chiquiz5():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\小心.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz5page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz5).place(x=450,y=450)

Label(chiquiz6page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz6page,text='Quiz 6',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz6page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

def score15():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 6', message='Correct!')
    show_frame(chiquiz7page)
Button(chiquiz6page,text='play',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz7page)).place(x=1100,y=350,height=80,width=200)
Button(chiquiz6page,text='rest',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz7page)).place(x=1100,y=500,height=80,width=200)
Button(chiquiz6page,text='travel',font=('Times New Roman',15,'bold'),command=score15).place(x=1100,y=650,height=80,width=200)
Button(chiquiz6page,text='sleep',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz7page)).place(x=1100,y=800,height=80,width=200)

def chiquiz6():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\旅游.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz6page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz6).place(x=450,y=450)

Label(chiquiz7page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz7page,text='Quiz 7',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz7page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

def score16():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 7', message='Correct!')
    show_frame(chiquiz8page)
Button(chiquiz7page,text='photo',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz8page)).place(x=1100,y=350,height=80,width=200)
Button(chiquiz7page,text='movie',font=('Times New Roman',15,'bold'),command=score16).place(x=1100,y=500,height=80,width=200)
Button(chiquiz7page,text='drama',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz8page)).place(x=1100,y=650,height=80,width=200)
Button(chiquiz7page,text='mime',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz8page)).place(x=1100,y=800,height=80,width=200)

def chiquiz7():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\电影.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz7page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz7).place(x=450,y=450)

Label(chiquiz8page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz8page,text='Quiz 8',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz8page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

def score17():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 8', message='Correct!')
    show_frame(chiquiz9page)
Button(chiquiz8page,text='language',font=('Times New Roman',15,'bold'),command=score17).place(x=1100,y=350,height=80,width=200)
Button(chiquiz8page,text='number',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz9page)).place(x=1100,y=500,height=80,width=200)
Button(chiquiz8page,text='font',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz9page)).place(x=1100,y=650,height=80,width=200)
Button(chiquiz8page,text='book',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz9page)).place(x=1100,y=800,height=80,width=200)

def chiquiz8():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\语言.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz8page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz8).place(x=450,y=450)

Label(chiquiz9page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz9page,text='Quiz 9',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz9page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

def score18():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 9', message='Correct!')
    show_frame(chiquiz10page)
Button(chiquiz9page,text='environment',font=('Times New Roman',15,'bold'),command=score18).place(x=1100,y=350,height=80,width=200)
Button(chiquiz9page,text='situation',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz10page)).place(x=1100,y=500,height=80,width=200)
Button(chiquiz9page,text='encounter',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz10page)).place(x=1100,y=650,height=80,width=200)
Button(chiquiz9page,text='status',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiquiz10page)).place(x=1100,y=800,height=80,width=200)

def chiquiz9():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\环境.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz9page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz9).place(x=450,y=450)

Label(chiquiz10page,bg='#fcc630').place(x=100,y=50,height=160,width=1700)
Label(chiquiz10page,text='Quiz 10',font=('Ink Free',50,'bold'),bg='#fcc630',fg='white').place(x=850,y=80)
Label(chiquiz10page,bg='#fcc630').place(x=100,y=250,height=750,width=1700)

def score19():
    global counter1
    counter1 +=1
    chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
    messagebox.showinfo(title='Quiz 10', message='Correct!')
    show_frame(chiscorepage)
Button(chiquiz10page,text='wrong',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiscorepage)).place(x=1100,y=350,height=80,width=200)
Button(chiquiz10page,text='incorrect',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiscorepage)).place(x=1100,y=500,height=80,width=200)
Button(chiquiz10page,text='correct',font=('Times New Roman',15,'bold'),command=score19).place(x=1100,y=650,height=80,width=200)
Button(chiquiz10page,text='improper',font=('Times New Roman',15,'bold'),command=lambda:show_frame(chiscorepage)).place(x=1100,y=800,height=80,width=200)

def chiquiz10():
       pygame.mixer.music.load('C:\\Users\\User\\OneDrive\\Desktop\\All 2\\正确.mp3')
       pygame.mixer.music.play(loops=1)

Button(chiquiz10page,image=play_btn,bg='#fcc630',bd=5,command=chiquiz10).place(x=450,y=450)
#chinese score page-------------------------------------------------------------------------------------------------------------
chiscore=Label(chiscorepage,text=counter1,font=('Times New Roman',40,'bold'),bg='#002EA6').place(x=900,y=450)
Label(chiscorepage,text='Your Score : ',font=('Times New Roman',30,'bold'),bg='#002EA6').place(x=450,y=450)
Label(chiscorepage,text='Nice Try',font=('Ink Free',50,'bold'),bg='#002EA6').place(x=700,y=100)
Label(chiscorepage,image=good,bg='#002EA6').place(x=1000,y=90)
def savechiscore():
    try:
        con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
        cursor=con.cursor()
        cursor.execute('insert into test(Username,Score)values(%s,%s)',(quizuser_entry.get(),counter1))
        con.commit()
        con.close()
        
    except Exception as es:
         messagebox.showerror('Error',f'Error due to:{str(es)}')
    show_frame(mainpage)

Button(chiscorepage,text='Done',font=('Times New Roman',20,'bold'),bg='white',bd=5,command=savechiscore).place(x=800,y=750,height=100,width=250)

show_frame(loginpage)
ws.mainloop()

