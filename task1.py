"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
import tkinter as tk 
from tkinter import *

win = tk.Tk()


e1=''
e2=''
e3=''
out = StringVar()



def clickFunction():
    x= e1.get()
    x= str(x)
    y= e2.get()
    y= str(y)
    z= e3.get()
    z= str(z)

    e4.insert(0, "I"+ ' ' + x + ' '+ "to the store. I then sat on a" + ' ' + y + "." + ' ' + "I then saw Billy, they were" + ' ' + z + ".")








#----------------------------------
l1 = Label(win, text="I (Verb)")
e1 = Entry(win, width=20)
l2 = Label(win, text="to the store. I then sat on a(Noun)")
e2 = Entry(win, width=20)
l3 = Label(win, text="I then saw Billy, they were (Adjective)")
e3 = Entry(win, width=20)

b1 = Button(win, text="Click to create Madlib", command=clickFunction)

l4 = Label(win, text="The finished Madlib is:")
e4= Entry(win, width=80, textvariable=out)



#----------------------------------


l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
print("\n")
b1.pack()
print("\n")
l4.pack()
e4.pack()









#-------------------------
win.mainloop()