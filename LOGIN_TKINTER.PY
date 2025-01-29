
import tkinter

window= tkinter.Tk()
window.title("login form")
window.geometry('500x500')
window.configure(bg='black')

frame=tkinter.Frame(bg='black')


# creating a widgets
login_label = tkinter.Label(frame, text="U Chat",bg='black',fg='yellow',font=("bold",50))

username_label= tkinter.Label(frame, text="username",bg='black',fg='white',font=("arial",20))
username_entry=tkinter.Entry(frame)

pass_label=tkinter.Label(frame,text="Password",bg='black',fg='white',font=("arial",20))
pass_entry=tkinter.Entry(frame,show=('-'))

enter_button=tkinter.Button(frame,text="login",bg='blue',fg='white',font=("arial",35))

# placing widgets on screen by placing
login_label.grid(row=0,columnspan=2,padx=20,column=0,pady=30)
username_label.grid(row=1,column=0,sticky="e")
username_entry.grid(row=1,column=1,pady=20,padx=10,sticky="w")

pass_label.grid(row=2,column=0,sticky="e")
pass_entry.grid(row=2,column=1,pady=20,padx=10,sticky="w")

enter_button.grid(row=3,column=0,columnspan=2,pady=30)

frame.pack()

window.mainloop()
