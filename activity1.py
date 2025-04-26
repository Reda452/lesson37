from tkinter import *

# creat window 
root = Tk()
root.title('using Place in tkinter')
root.config(bg="black")
root.geometry('250x300')
l1 = Label(root, text="tkintergeometry using place", font=("times new roman" ,12, "bold"),fg="white", bg="black")
l1.place(x=5, y=15)


root.mainloop()