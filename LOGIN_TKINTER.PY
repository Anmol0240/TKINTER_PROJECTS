import tkinter

window= tkinter.Tk()
window.title("login form")
window.geometry('500x500')
window.configure(bg='#333333')

window.columnconfigure((0,1,2),weight=1)
window.rowconfigure((0,1,2,3,4,5),weight=1)

# creating a widgets
login_label = tkinter.Label(window, text="login",bg='#333333',fg='white',font=("arial",30))

username_label= tkinter.Label(window, text="username",bg='#333333',fg='white',font=("arial",15))
username_entry=tkinter.Entry(window)

pass_label=tkinter.Label(window,text="Password",bg='#333333',fg='white',font=("arial",15))
pass_entry=tkinter.Entry(window)

enter_button=tkinter.Button(window,text="login",bg='white',fg='red',font=("roman",17))

# placing widgets on screen by placing
login_label.grid(row=0, column=1,sticky="news",pady=20)

username_label.grid(row=1,column=0,padx=10,pady=10,sticky="e")
username_entry.grid(row=1,column=1,padx=10,pady=10,sticky="w")

pass_label.grid(row=2,column=0,padx=10,pady=10,sticky="e")
pass_entry.grid(row=2,column=1,padx=10,pady=10,sticky="w")

enter_button.grid(row=4,column=1,pady=10,sticky="wnes")

window.rowconfigure(3,weight=1)

window.mainloop()
