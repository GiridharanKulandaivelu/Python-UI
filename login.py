from Tkinter import *
import os

#def QuitAll():
#	master.destroy()
#	master.protocol("WM_DELETE_WINDOW", on_closing)

master =Tk()

def validate(event):
	print("success")
	#print(d_username.get())
	#(d_password.get())
	if d_username.get() == "gt" and d_password.get() == "gt":
		print("logged in")
		os.system('uidesign.py')




l_username = Label(master, text="Name")
l_password = Label(master, text="Password")

d_username = Entry(master)
d_password = Entry(master, show="*")

l_username.grid(row=0)
l_password.grid(row=1)

d_username.grid(row=0, column=1)
d_password.grid(row=1, column=1)

loginButt = Button(master, text="Login")
loginButt.grid(columnspan=2)
loginButt.bind("<Button-1>",validate)



master.mainloop()