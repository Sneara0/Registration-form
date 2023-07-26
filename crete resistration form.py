from tkinter import*
from tkinter import messagebox
root=Tk()
root.configure(bg='midnightBlue')

label1=Label(root,text='Login form',bg='blue',fg='pink',font=('Areal',24),)
label1.place(x=50,y=24)

label2=Label(root,text='Username:',font=('Areal,20'),bg='blue',fg='white')
label2.place(x=310,y=190)

label3=Label(root,text='password:',font=('Areal,20'),bg='blue',fg='white')
label3.place(x=310,y=340)

entry1=Entry(root,font=('Areal,17'))
entry1.place(x=600,y=200)
entry1=Entry(root,font=('Areal,17'),show='*****')
entry1.place(x=600,y=350)
button=Button(root,text='login',bg='sky blue',font=('Areal',15),bd=5)
button.place(x=600,y=500)


root.mainloop()
