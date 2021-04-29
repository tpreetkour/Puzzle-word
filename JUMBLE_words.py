from tkinter import *
from tkinter import messagebox
import random
import time


root=Tk()


answers=['python','swift','java','fortran','pascal','keyboard','kotlin','computer','software','monitor']

words=['yhnpto (HINT:Interpreted language)','fsitw (HINT:Developed by Apple)','vaaj (HINT:Object oriented)','ofatrrn (HINT:Formula translation)','acaslp (HINT:Niklaus Wirth)','ebadroyk (HINT:Input device)','olnitk (HINT:Jet brains)','optreumc (HINT: Machine)','otaerwfs (HINT:Set of instructions)','oiortnm (HINT:Output device)']

num=random.randrange(0,10,1)

ans=StringVar()


def checkans():
    global words
    global answers
    global num
    
    var=e1.get()
    
    if (var==answers[num]):
        
        messagebox.showinfo("Correct answer",'correct answer')
        reset()
    else:
        messagebox.showerror(" Incorrect answer",'Incorrect answer')
        e1.delete(0,END)

def reset():
    global words
    global answers
    global num
    num=random.randrange(0,10,1)
    l1.config(text=words[num])
    e1.delete(0,END)
def default():
    global words
    global answers
    global num
    l1.config(text=words[num])
    
    


l1=Label(root,text="Start Here",font=("verdana",19))

l1.pack()

e1=Entry(root,font=("verdana",17),width=35)
e1.pack()

b1=Button(root,text="Check",font=("comic sans ms",17),width=35,bg='lime',relief=GROOVE,command=checkans)
b1.pack()

b2=Button(root,text="Reset",font=("comic sans ms",17),width=35,bg='pink',relief=GROOVE,command=reset)
b2.pack()

c1=Canvas(root,height=550,width=550)
c1.pack()

root.geometry("500x500")
root.title('Jumble words')

i=PhotoImage(file='C:\\Users\\gurjinder\\Downloads\\SHAREit\\puzzle.PNG')


c1.create_image(100,0,anchor=NW,image=i)

default()
root.mainloop()
