## Wesley Vercoutere
## V0.1.0

import threading
import time
from tkinter import *

try:
    import RPi.GPIO as GPIO
except:
    from dummygpio.DummyGPIO import *
    GPIO = DummyGPIO(True)


root = Tk()
root.title("Test proggie dummy GPIO")
root.geometry("800x400")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledBlue = 19
ledRed = 20
ledYellow = 21
ledGreen = 22

button1 = 23
button2 = 24
button3 = 25
button4 = 26

leds = (ledBlue, ledRed, ledYellow, ledGreen)
buttons = (button1, button2, button3, button4)

for led in leds:
    GPIO.setup(led, GPIO.OUT)

for btn in buttons:
    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


toggle = False
blink = False

def toggleLed():
    global toggle
    toggle = not toggle
    GPIO.output(ledBlue, toggle)

def blinkLed():
    global blink
    blink = not blink


btnBlue = Button(root, text="Blue led", command=toggleLed)
btnRed = Button(root, text="Red led", command=blinkLed)
btnYellow = Button(root, text="Yellow led")
btnGreen = Button(root, text="Green led")

btnBlue.place(x=10,y=10)
btnRed.place(x=10,y=60)
btnYellow.place(x=10,y=110)
btnGreen.place(x=10,y=160)


def loop():
    while True:
        # for index in range(len(buttons)):
        #     GPIO.output(leds[index], GPIO.input(buttons[index]))
        
        global blink
        if blink:
            GPIO.output(ledRed, toggle)

        
threading.Thread(target=loop).start()

root.mainloop()
