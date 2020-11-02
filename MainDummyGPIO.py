from tkinter import *

try:
    import RPi.GPIO as GPIO
except:
    from DummyGPIO import *
    GPIO = DummyGPIO(True)


root = Tk()
root.title("Test proggie dummy GPIO")
root.geometry("800x400")



root.mainloop()
