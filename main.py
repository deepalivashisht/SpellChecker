import tkinter
from tkinter import *
from turtle import heading
from textblob import TextBlob

root = Tk()
root.title("Spell Checker")
root.geometry("700x400")
root.config(background="#212121")

def check_spelling():
    word=text.get()
    a=TextBlob(word)
    right=str(a.correct())
    cs=Label(root,text="Correct text is: ",font=("poppins",20),bg="#212121",fg="#fff")
    cs.place(x=150,y=250)
    spell.config(text=right)

heading = Label(root,text="Spell Checker",font=("Trebuchet MS",30,"bold"),bg="#212121",fg="#fff")
heading.pack(pady=(50,10))

text = Entry(root,justify="center",width=30,font=("poppins",25),bg="white")
text.pack(pady=10)
text.focus()

button = Button(root,text="Check",font=("arial",15,"bold"),fg="black",bg="white",command=check_spelling)
button.pack()

spell = Label(root,font=("poppins",20),bg="#212121",fg="#fff")
spell.place(x=350,y=250)

root.mainloop()