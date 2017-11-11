from tkinter import *  # Python 3
from time import sleep as slp # sleep imported as slp

class Timer(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        def timer(): # Define the timer
            seconds = Timer.entry.get()
            slp(int(seconds)) # sleeps for seconds

            self.label.destroy()
            self.entry.destroy()
            self.button.destroy()

            self.label2.pack(side = TOP, pady = 25)
            self.button2.pack(side = BOTTOM, pady = 5)

        vcmd = (self.register(self.onValidate), '%S') # %S is the inserted string
        Timer.label = Label(self, text = 'How long do you want to set the timer for in seconds?')
        Timer.entry = Entry(self, validate = "key", validatecommand=vcmd)
        Timer.button = Button(self, text = 'Start Timer', command = timer)

        Timer.label.pack(side = "top")
        Timer.entry.pack(side = "top")
        Timer.button.pack(side = "top")

        Timer.label2 = Label(self, text = 'Timer finished.')
        Timer.button2 = Button(self, text = 'ok', command = quit)

    def onValidate(self, input): # Used to validate the inserted text on entry
        if (input.isnumeric()):
            return True
        else:
            self.bell()
            return False
def main():
    win = Tk() # Frame used in Timer
    win.title('pytimer')
    win.geometry('375x100')
    Timer(win).pack()
    win.mainloop()

main()