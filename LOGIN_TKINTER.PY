import tkinter

window= tkinter.Tk()
window.title("login form")
window.geometry('500x700')
window.configure(bg='black')

frame=tkinter.Frame(bg='black')


# creating a widgets
login_label = tkinter.Label(frame, text="U Chat",bg='black',fg='yellow',font=("bold",50))

username_label= tkinter.Label(frame, text="username",bg='black',fg='white',font=("arial",20))
username_entry=tkinter.Entry(frame)

pass_label=tkinter.Label(frame,text="Password",bg='black',fg='white',font=("arial",20))
pass_entry=tkinter.Entry(frame,show=('-'))

enter_button=tkinter.Button(frame,text="login",bg='blue',fg='white',font=("arial",35),activebackground='red')

# placing widgets on screen by placing
login_label.grid(row=0,columnspan=2,padx=20,column=0,pady=30)
username_label.grid(row=1,column=0,sticky="e")
username_entry.grid(row=1,column=1,pady=20,padx=10,sticky="w")

pass_label.grid(row=2,column=0,sticky="e")
pass_entry.grid(row=2,column=1,pady=20,padx=10,sticky="w")

enter_button.grid(row=8,column=0,columnspan=2,pady=30)


# creating a check button 
age =tkinter.Checkbutton(frame,text='I am above 18 age',foreground='red',background='black',font=('arial',10))
age_label=tkinter.Label(frame,text='select your gender',font=('arial',12),fg='white',bg='black')


# placing the checkbutton 
age.grid(row=3,column=0,columnspan=2,pady=10)
age_label.grid(row=4,column=0,columnspan=2)

# creating a radio button to select the user gender
gender1=tkinter.Radiobutton(frame,text='male',value=1,foreground='red',background='black',activebackground='grey',font=('arial',12))
gender2=tkinter.Radiobutton(frame,text='female',value=2,foreground='red',background='black',activebackground='grey',font=('arial',12))
gender3=tkinter.Radiobutton(frame,text='none of these',value=3,foreground='red',background='black',activebackground='grey',font=('arial',12))


# placing the radio button
gender1.grid(row=5,column=0,columnspan=2,padx=10,pady=10)
gender2.grid(row=6,column=0,columnspan=2,padx=10,pady=10)
gender3.grid(row=7,column=0,columnspan=2,padx=10,pady=10)




frame.pack()

window.mainloop()
