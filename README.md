# RaspberryPiDummyGPIO
Tkinter project to simulate Raspberry Pi IO pinning


## 1. Version
Vx.y.z
* x: Major version - breaks the API
* y: Minor version - Doesn't break the API
* z: Patches - Bug fixes

V1.0.0 (Development)

* split code in multiple classes
* complete RPi.GPIO api

V0.2.0 (Development)

* add cleanup method

V0.1.1 (Development)

* pull_up and pull_down added in setmode
* output with True and False
* update test


V0.1.0 (Development)

Implemented methods from RPi.GPIO:

* setwarnings(warning)
* setup(pin, typeInOut, pull_up_down="")
* output(pin, output):
* input(pin):


## 2. Use dummyGPIO

### 2.1 Instantiate DummyGPIO object

While instantiating the dummyGPIO class, you provide an argument (True or False).
* True: The current project has an instance of Tk(). and runs the mainloop. The DummyGPIO object will add a Toplevel widget to the project.
* False: The current project has no Tkinter frontend. The DummyGPIO object will instantiate a root and run the mainloop.

```python
try:
    import RPi.GPIO as GPIO
except:
    from DummyGPIO import *
    GPIO = DummyGPIO(True)
```


### 2.2 setwarnings

If the current project has an instance of Tk() run the setwarnings method after the instantiation of tkinter.

```python
root = Tk()
root.title("Test proggie dummy GPIO")
root.geometry("800x400")

GPIO.setwarnings(False)
```


### 2.3 setup

Setting up the pins according to the RPi.GPIO library.


### 2.4 output

Set the output pin according to the RPi.GPIO library.


### 2.5 input

Read the state of the input pin according to the RPi.GPIO library.

