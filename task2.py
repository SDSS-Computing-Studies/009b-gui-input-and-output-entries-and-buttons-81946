"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk 
from tkinter import *
import math
win = tk.Tk()
#---------------------------
out = StringVar()


def clickFunction():
    y= e1.get()
    z= e2.get()
    b= float(y)
    c= float(z)
    discriminant= (pow(b,2))-(4*1*c)
    x= str(discriminant)
    e3.insert(0, x)


l1 = Label(win, text="Please enter your 'b'")
e1 = Entry(win, width=5)
l2 = Label(win, text="And your 'c'")
e2 = Entry(win, width=5)
b1 = Button(win, text="Click to find x", command=clickFunction)

l3 = Label(win, text="x=")
e3= Entry(win, width=10, textvariable=out)





#---------------


l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()
l3.pack()
e3.pack()









#-----------------------
win.mainloop()