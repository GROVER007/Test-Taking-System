from tkinter import * 
from tkinter import messagebox
from dbmodule import *


#  function assigned to commit button
def commit():
    databases = checkdb()
    print(databases)
    question = str(question_entry.get())
    answer = str(answer_entry.get())
    option2 = str(option2_entry.get())
    option3 = str(option3_entry.get())
    option4 = str(option4_entry.get())

    if len(question)==0 or len(answer)==0 or len(option2)==0 or len(option3)==0 or len(option4)==0:
        messagebox.showerror("Error","You Cant Leave Any Cell Empty")

    elif "vishu_mcq" not in databases:
        createdb()
        addrow(question,answer,option2,option3,option4)
        messagebox.showinfo("New Database Created","New Database 'vishu_mcq' Is Created In Your Sql where your entered data is stored")
        question_entry.delete(0,END)
        answer_entry.delete(0,END)
        option2_entry.delete(0,END)
        option3_entry.delete(0,END)
        option4_entry.delete(0,END)
        
    else:   
        addrow(question,answer,option2,option3,option4)
        messagebox.showinfo("Data Saved","Your Data Is Saved Successfully !")
        question_entry.delete(0,END)
        answer_entry.delete(0,END)
        option2_entry.delete(0,END)
        option3_entry.delete(0,END)
        option4_entry.delete(0,END)
    

root= Tk()

#  root configurations
root.geometry("900x470")
root.maxsize(900,470)
root.minsize(750,470)
root.title("Teacher's Interface")

#  heading interface
heading_frame = Frame(root)
heading_frame.pack(fill = "both",side="top",expand="yes")
heading_label = Label(heading_frame,text="TEACHER'S INTERFACE",font=("Helvetica",40,"bold"),bg = "blue",fg = "yellow",relief = SUNKEN,borderwidth=5)
heading_label.pack(fill="both")

#  question interface
question_frame = Frame(root)
question_frame.pack(fill = "both",side = "top",expand="yes")
question_label = Label(question_frame,font=("verdana",20,"bold"),text="Question :")
question_label.pack()
question_entry = Entry(question_frame,width=70 ,font=("Times",15))
question_entry.pack(ipady=30)

#  options interface
option_frame = Frame(root)
option_frame.pack(expand = "yes")

answer_label = Label(option_frame,text = "answer",font = ("verdana",15,"bold"))
answer_label.grid(column = 0,row = 0,ipadx =30)
answer_entry = Entry(option_frame,font=("Times",15))
answer_entry.grid(column=1,row=0)

option2_label = Label(option_frame,text="option 2",font=("verdana",15,"bold"))
option2_label.grid(column=2,row=0,ipadx = 20,padx =10)
option2_entry = Entry(option_frame,font=("Times",15))
option2_entry.grid(column=3,row=0)

option3_label = Label(option_frame,text="option 3",font=("verdana",15,"bold"))
option3_label.grid(column=0,row=1,ipadx = 30,)
option3_entry = Entry(option_frame,font=("Times",15))
option3_entry.grid(column=1,row=1)

option4_label = Label(option_frame,text="option 4",font=("verdana",15,"bold"))
option4_label.grid(column=2,row=1,ipadx = 20,padx =10)
option4_entry = Entry(option_frame,font=("Times",15))
option4_entry.grid(column=3,row=1)

#  commit button interface
commit = Button(root,text="COMMIT",font=("verdana",15,"bold"),command=commit)
commit.pack(expand = "yes")


root.mainloop()