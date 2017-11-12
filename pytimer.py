try:
    from tkinter import * # Python 3.x
except ImportError:
    from Tkinter import * # Python 2.x
from time import sleep as slp # sleep imported as slp

class Timer(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        def countDown():
            mySeconds = Timer.entry.get()
            mySeconds = mySeconds if mySeconds else 0 # Checks if there is no input
            timeleft = StringVar()

            self.label.destroy()
            self.entry.destroy()
            self.button.destroy()
            self.label3 = Label(self, text = "Time Remaining:")
            self.label4 = Label(self, textvariable = timeleft)
            self.label3.pack(side = "top", pady = 25)
            self.label4.pack(side = "top")

            # for each second from mySeconds until -1
            for t in range(int(mySeconds), 0, -1):
                # formatted as two digit numbers with zeros as fill
                # divmod() gives minutes, seconds and then hours, minutes
                m, s = divmod(t, 60)
                h, m = divmod(m, 60)
                timeleft.set("%02d:%02d:%02d" % (h, m, s))
                self.update()
                slp(1)

            self.label3.destroy()
            self.label4.destroy()
            self.label2.pack(side = TOP, pady = 20)
            self.button2.pack(side = BOTTOM, pady = 0) ## pady5

        vcmd = (self.register(self.onValidate), '%S') # %S is the inserted string
        Timer.label = Label(self, text = 'How long do you want to set the timer for in seconds?')
        Timer.entry = Entry(self, validate = "key", validatecommand = vcmd)
        Timer.button = Button(self, text = 'Start Timer', command = countDown)

        Timer.label.pack(side = "top")
        Timer.entry.pack(side = "top", pady = 5)
        Timer.button.pack(side = "top", pady = 3)

        Timer.label2 = Label(self, text = 'Timer finished.')
        Timer.button2 = Button(self, text = 'OK', command = quit)

    def onValidate(self, input): # Used to validate the inserted text on entry
        if (input.isnumeric()):
            return True
        else:
            self.bell()
            return False

def main():
    win = Tk() # Frame used in Timer
    win.title('pytimer')
    win.geometry('350x100')
    Timer(win).pack()
    win.mainloop()

main()