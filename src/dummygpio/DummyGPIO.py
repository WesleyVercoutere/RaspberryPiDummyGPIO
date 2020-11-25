from tkinter import Tk, Toplevel, LabelFrame, Button, Label

class DummyGPIO():

    def __init__(self, runMainLoop):
        print("Project doesn't run on a Raspberry Pi.\nSimulation started!\n")

        self.__tkinterStarted = False
        self.__runMainloop = runMainLoop

        self.__setConstants()
        

    ## RPi.GPIO api

    def setwarnings(self, warning):
        print(f"Set warnings -> {warning}\n")
        self.__initFrontEnd()


    def setmode(self, mode):
        print(f"Set mode -> {mode}\n")
        self.__initFrontEnd()


    def getmode(self):
        pass


    def setup(self, pin, typeInOut, pull_up_down="", initial=""):
        # setup with arrays and tuples!!
        '''
        GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
        chan_list = [11,12]    # add as many channels as you want!
            # you can tuples instead i.e.:
            #   chan_list = (11,12)
        GPIO.setup(chan_list, GPIO.OUT) 
        '''
        pass


    def output(self, pin, output):
        '''
        chan_list = [11,12]                             # also works with tuples
        GPIO.output(chan_list, GPIO.LOW)                # sets all to GPIO.LOW
        GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW
        GPIO.output(12, not GPIO.input(12))
        '''
        pass


    def input(self, pin):
        pass


    def cleanup(self):
        '''
        GPIO.cleanup(channel)
        GPIO.cleanup( (channel1, channel2) )
        GPIO.cleanup( [channel1, channel2] )
        '''
        pass


    def wait_for_edge(self, pin, type, timeout=0):
        pass


    def add_event_detect(self, pin, type, callback="", bouncetime=0):
        '''
        callback returns channel
        '''
        pass


    def add_event_callback(self, pin, my_callback="", bouncetime=0):
        pass


    def event_detected(self, pin):
        '''
        GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel
        do_something()
        if GPIO.event_detected(channel):
            print('Button pressed')
        '''
        pass


    def remove_event_detect(self, pin):
        pass


    def PWM(self, pin, frequency):
        pass


    def gpio_function(self, pin):
        '''
        gpio_function(channel)
        Shows the function of a GPIO channel.
        For example:

        import RPi.GPIO as GPIO

        GPIO.setmode(GPIO.BOARD)
        func = GPIO.gpio_function(pin)
        will return a value from:
        GPIO.IN, GPIO.OUT, GPIO.SPI, GPIO.I2C, GPIO.HARD_PWM, GPIO.SERIAL, GPIO.UNKNOWN
        '''
        pass


    ## Private methods

    def __setConstants(self):
        self.BCM = "bcm"
        self.BOARD = "board"
        self.OUT= "output"
        self.IN = "input"
        self.HIGH = True
        self.LOW = False
        self.PUD_UP = "PUD_UP"
        self.PUD_DOWN ="PUD_DOWN"
        self.FALLING = "falling"
        self.RISING = "rising"
        self.BOTH = "both"
        self.VERSION = "Dummy GPIO V1.0.0"


    def __initFrontEnd(self):
        
        if not self.__tkinterStarted:
            if self.__runMainloop:
                pass

            else:
                pass

        self.__tkinterStarted = True




    



'''

        

        self.tkinterApp = tkinterApp
        self.BCM = "bcm"
        self.OUT= "output"
        self.IN = "input"
        self.HIGH = True
        self.LOW = False
        self.PUD_UP = "PUD_UP"
        self.PUD_DOWN ="PUD_DOWN"

        self._inputs = []
        self._outputs = []
        self._labels = {}

        self._rowInput = 0
        self._columnInput = 0
        self._rowOutput = 0
        self._columnOutput = 0




    def setup(self, pin, typeInOut, pull_up_down=""):
        print(f"setup: pin {pin}, {typeInOut}, {pull_up_down}")

        if typeInOut == self.IN:
            self.__addInput(DummyInput(pin, pull_up_down))
        elif typeInOut == self.OUT:
            self.__addOutput(DummyOutput(pin))
        else:
            raise ValueError("type not known")


    def output(self, pin, output):
        # print(f"output pin number {pin} {output}")

        for index in range(len(self._outputs)):
            if self._outputs[index].pin == pin:
                self._outputs[index].state = output

        self.__updateOutputs()


    def input(self, pin):
        # print(f"input pin number {pin}")

        for input in self._inputs:
            if input.pin == pin:
                return input.state


    def cleanup(self):
        print('Cleanup')


    def __setTopLevel(self):
        self.dummyroot = Toplevel()
        self.__addFrames()


    def __setRoot(self):
        self.dummyroot = Tk()
        self.__addFrames()
        self.dummyroot.mainloop()


    def __addFrames(self):
        self.dummyroot.title("Raspberry Pi dummy GPIO")

        self.frameInput = LabelFrame(self.dummyroot, text="Inputs")
        self.frameOutput = LabelFrame(self.dummyroot, text="Outputs")

        self.frameInput.grid(row=0, column=0, padx=10, pady=10)
        self.frameOutput.grid(row=0, column=1, padx=10, pady=10)


    def __addInput(self, input):
        self._inputs.append(input)

        btn = Button(self.frameInput, text=input.pin, padx=10, pady=10)
        btn.grid(row=self._rowInput, column=self._columnInput, padx=10, pady=10)
        btn.bind("<ButtonPress-1>", lambda x : self.__btnToggle(input.pin))
        btn.bind("<ButtonRelease-1>", lambda x : self.__btnToggle(input.pin))

        self._rowInput += 1


    def __addOutput(self, output):
        self._outputs.append(output)

        lbl = Label(self.frameOutput, text=output.pin, padx=10, pady=10)
        lbl.grid(row=self._rowOutput, column=self._columnOutput, padx=10, pady=10)

        self._labels[output.pin] = lbl

        self._rowOutput += 1


    def __btnToggle(self, pin):
        print(f"push/release btn {pin}")

        for index in range(len(self._inputs)):
            if self._inputs[index].pin == pin:
                self._inputs[index].state = not self._inputs[index].state

        ## Only for debugging
        # for input in self.inputs:
        #     print(input)


    def __updateOutputs(self):

        for output in self._outputs:
            lbl = self._labels.get(output.pin)
            
            if output.state:
                lbl['bg'] = 'red'
            else:
                lbl['bg'] = 'green'


class DummyOutput():

    def __init__(self, pin):
        self.pin = pin
        self.state = False


class DummyInput():

    def __init__(self, pin, pull_up_down):
        self.pin = pin

        if pull_up_down == 'PUD_UP':
            self.state = True
        else:
            self.state = False    


    def __str__(self):
        return f"{self.pin}, {self.state}"

'''
