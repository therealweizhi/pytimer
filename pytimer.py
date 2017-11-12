try:
    from tkinter import * # Python 3.x
except ImportError:
    from Tkinter import * # Python 2.x
from time import sleep as slp # sleep imported as slp

class Timer(Frame):
    timeleft = ""
    def __init__(self, parent):
        Frame.__init__(self, parent)
        def myCountDown():
            mySeconds = Timer.entry.get()
            timeleft = StringVar()
            self.label3 = Label(self, textvariable = timeleft)
            self.label3.pack(side = "top")

            # for each second from mySeconds until -1
            for t in range(int(mySeconds), 0, -1):
                # format as 2 digit integers, fills with zero to the left
                # divmod() gives minutes, seconds
                sf = "{:02d}:{:02d}".format(*divmod(t, 60))
                timeleft.set(sf)
                self.update()
                slp(1)

            self.label3.destroy()
            self.label.destroy()
            self.entry.destroy()
            self.button.destroy()
            self.label2.pack(side = TOP, pady = 25)
            self.button2.pack(side = BOTTOM, pady = 0) ## pady5

        def timer(seconds): # Define the timer
            slp(int(seconds)) # sleeps for seconds

            self.label.destroy()
            self.entry.destroy()
            self.button.destroy()

            self.label2.pack(side = TOP, pady = 25)
            self.button2.pack(side = BOTTOM, pady = 5)

        vcmd = (self.register(self.onValidate), '%S') # %S is the inserted string
        Timer.label = Label(self, text = 'How long do you want to set the timer for in seconds?')
        Timer.entry = Entry(self, validate = "key", validatecommand=vcmd)
        Timer.button = Button(self, text = 'Start Timer', command = myCountDown)

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
    win.geometry('375x105')
    Timer(win).pack()
    win.mainloop()

main()