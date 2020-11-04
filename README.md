# RaspberryPiDummyGPIO
Tkinter project to simulate Raspberry Pi IO pinning


## 1. Version
Vx.y.z
* x: Major version - breaks the API
* y: Minor version - Doesn't break the API
* z: Patches - Bug fixes


V0.1.0 (Development)

Implemented methods from RPi.GPIO:

* setwarnings(warning)
* setup(pin, typeInOut, pull_up_down="")
* output(pin, output):
* input(pin):


## 2. Use dummyGPIO

### 2.1 Instantiate DummyGPIO object

```python
try:
    import RPi.GPIO as GPIO
except:
    from DummyGPIO import *
    GPIO = DummyGPIO(True)
```

While instantiating the dummyGPIO class, you provide an argument (True or False).
* True: The current project has an instance of Tk(). and runs the mainloop. The DummyGPIO object will add a Toplevel widget to the project.
* False: The current project has no Tkinter frontend. The DummyGPIO object will instantiate a root and run the mainloop.


### 2.2 setwarnings

### 2.3 setup

### 2.4 output

### 2.5 input