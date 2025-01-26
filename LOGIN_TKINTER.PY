import tkinter

window= tkinter.Tk()
window.title("login form")
window.geometry('500x500')
window.configure(bg='#333333')

# creating a widgets
    login_label = tkinter.Label(window, text="login",bg='#333333',fg='white',font="arial",30)

username_label= tkinter.Label(window, text="username",bg='#333333',fg='white',)
username_entry=tkinter.Entry(window)

pass_label=tkinter.Label(window,text="Password",bg='#333333',fg='white')
pass_entry=tkinter.Entry(window)

enter_label=tkinter.Button(window,text="login",bg='white',fg='red',font='roman')

# placing widgets on screen by placing
login_label.grid(row=0, column=3,sticky="news")

username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1)

pass_label.grid(row=2,column=0)
pass_entry.grid(row=2,column=1)

enter_label.grid(row=4,column=3)

window.mainloop()