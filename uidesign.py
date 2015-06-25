from Tkinter import *
import tkMessageBox

def doNothing():
    print("ok ok I won't...")

def QuittingWindow():
	#tkMessageBox.showinfo('Window Title','Quit')
	answer = tkMessageBox.askquestion('Quit','Are you sure you want to quit?')
	if answer == 'yes':
		root.destroy()
		#import login
		#login.QuitAll()




root = Tk()
#for full screen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
# Tkinter puts menus at the top by default
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
# Adds a drop down when "File" is clicked
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=QuittingWindow)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# ******* Creating a Toolbar *******

toolbar = Frame(root, bg="blue")

toolbut1 = Button(toolbar, text="Button 1", command=doNothing)
toolbut1.pack(side=LEFT, padx=2, pady=2)
toolbut2 = Button(toolbar, text="Button 2", command=doNothing)
toolbut2.pack(side=LEFT, padx=2, pady=2)
toolbut3 = Button(toolbar, text="Button 1", command=doNothing)
toolbut3.pack(side=LEFT, padx=2, pady=2)
toolbut4 = Button(toolbar, text="Button 2", command=doNothing)
toolbut4.pack(side=LEFT, padx=2, pady=2)
toolbut5 = Button(toolbar, text="Button 1", command=doNothing)
toolbut5.pack(side=LEFT, padx=2, pady=2)
toolbut6 = Button(toolbar, text="Button 2", command=doNothing)
toolbut6.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ******* Creating a Status Bar for the Bottom *******

# bd is border, relief is type of border
status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()