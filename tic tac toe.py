from tkinter import*

window=Tk()
window.title('TIC TAC TOE')
window.geometry('700x700')
window.configure(bg='cyan')


frame1= Frame(window,bg='cyan')
frame1.pack()

name=Label(frame1, text='Tic Tac Toe',bg='cyan',foreground='red',font=('Arial',30))
name.grid(row=1,column=0,columnspan=2,pady=20)

frame2=Frame(window)
frame2.pack()


turn= "x"

def play(event):
    global turn
    button=event.widget

    
    if turn=="x":
        button["text"]="X"
        turn="O"
    
    else:
        button["text"]="O"
        turn="x"




# button creation
# first row

button1=Button(frame2,text=' ',font=('Arial',31),width=4,height=2,fg='red',bg='purple',activebackground='blue')
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button1=Button(frame2,text=' ',font=('Arial',31),width=4,height=2,fg='red',bg='purple',activebackground='blue')
button1.grid(row=0,column=1)
button1.bind("<Button-1>",play)


button1=Button(frame2,text=' ',font=('Arial',31),width=4,height=2,fg='red',bg='purple',activebackground='blue')
button1.grid(row=0,column=2)
button1.bind("<Button-1>",play)

# 2nd row

button1=Button(frame2,text=' ',font=('Arial',31),width=4,height=2,fg='red',bg='purple',activebackground='blue')
button1.grid(row=1,column=0)
button1.bind("<Button-1>",play)

button1=Button(frame2,text=' ',font=('Arial',31),width=4,height=2,fg='red',bg='purple',activebackground='blue')
button1.grid(row=1,column=1)
button1.bind("<Button-1>",play)


button1=Button(frame2,text=' ',font=('Arial',31),width=4,height=2,fg='red',bg='purple',activebackground='blue')
button1.grid(row=1,column=2)
button1.bind("<Button-1>",play)

# 3rd row

button1=Button(frame2,text=' ',font=('Arial',31),width=4,height=2,fg='red',bg='purple',activebackground='blue')
button1.grid(row=2,column=0)
button1.bind("<Button-1>",play)

button1=Button(frame2,text=' ',font=('Arial',31),width=4,height=2,fg='red',bg='purple',activebackground='blue')
button1.grid(row=2,column=1)
button1.bind("<Button-1>",play)


button1=Button(frame2,text=' ',font=('Arial',31),width=4,height=2,fg='red',bg='purple',activebackground='blue')
button1.grid(row=2,column=2)
button1.bind("<Button-1>",play)




window.mainloop()