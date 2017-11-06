# Import necessary modules
import time
from tkinter import *

# Define the timer
def timer():
    seconds = e1.get()
    time.sleep(int(seconds))
    l1.destroy()
    e1.destroy()
    b1.destroy()
    l2.pack(side = TOP, pady = 25)
    b2.pack(side = BOTTOM, pady = 5)

# Create the GUI
win = Tk()
win.title('pytimer')
win.geometry('375x100')
l1 = Label(win, text = 'How long do you want to set the timer for in seconds?')
l2 = Label(win, text = 'Timer finished.')
e1 = Entry(win)
b1 = Button(win, text = 'Start Timer', command = timer)
b2 = Button(win, text = 'OK', command = quit)
l1.pack(side = TOP, pady = 5)
e1.pack(side = TOP)
b1.pack(side = BOTTOM, pady = 5)
win.mainloop()