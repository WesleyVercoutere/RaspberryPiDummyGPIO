from tkinter import *

class DummyGPIO():

    def __init__(self, tkinterApp):
        print("Project doesn't run on a Raspberry Pi.\nSimulation will start!\n")

        self.tkinterApp = tkinterApp
        self.BCM = "bcm"
        self.OUT= "output"
        self.IN = "input"
        self.HIGH = "high"
        self.LOW = "low"
        self.PUD_DOWN = "Pull down"

        self._inputs = []
        self._outputs = []
        self._labels = {}

        self._rowInput = 0
        self._columnInput = 0
        self._rowOutput = 0
        self._columnOutput = 0


    def setwarnings(self, warning):
        print(f"Set warnings -> {warning}\n")

        if self.tkinterApp:
            self._setTopLevel()
        else:
            self._setRoot()


    def setmode(self, mode):
        print(f"Set mode -> {mode}\n")


    def setup(self, pin, typeInOut, pull_up_down=""):
        print(f"setup: pin {pin}, {typeInOut}, {pull_up_down}")

        if typeInOut == self.IN:
            self._addInput(DummyInput(pin))
        elif typeInOut == self.OUT:
            self._addOutput(DummyOutput(pin))
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


    def _setTopLevel(self):
        self.dummyroot = Toplevel()
        self._addFrames()


    def _setRoot(self):
        self.dummyroot = Tk()
        self._addFrames()
        self.dummyroot.mainloop()


    def _addFrames(self):
        self.dummyroot.title("Raspberry Pi dummy GPIO")

        self.frameInput = LabelFrame(self.dummyroot, text="Inputs")
        self.frameOutput = LabelFrame(self.dummyroot, text="Outputs")

        self.frameInput.grid(row=0, column=0, padx=10, pady=10)
        self.frameOutput.grid(row=0, column=1, padx=10, pady=10)


    def _addInput(self, input):
        self._inputs.append(input)

        btn = Button(self.frameInput, text=input.pin, padx=10, pady=10)
        btn.grid(row=self._rowInput, column=self._columnInput, padx=10, pady=10)
        btn.bind("<ButtonPress-1>", lambda x : self._btnToggle(input.pin))
        btn.bind("<ButtonRelease-1>", lambda x : self._btnToggle(input.pin))

        self._rowInput += 1


    def _addOutput(self, output):
        self._outputs.append(output)

        lbl = Label(self.frameOutput, text=output.pin, padx=10, pady=10)
        lbl.grid(row=self._rowOutput, column=self._columnOutput, padx=10, pady=10)

        self._labels[output.pin] = lbl

        self._rowOutput += 1


    def _btnToggle(self, pin):
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

    def __init__(self, pin):
        self.pin = pin
        self.state = False


    def __str__(self):
        return f"{self.pin}, {self.state}"

