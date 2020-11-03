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

        self.inputs = []
        self.outputs = []

        self.rowInput = 0
        self.columnInput = 0
        self.rowOutput = 0
        self.columnOutput = 0


    def setwarnings(self, warning):
        print(f"Set warnings -> {warning}\n")

        if self.tkinterApp:
            self.setTopLevel()
        else:
            self.setRoot()


    def setmode(self, mode):
        print(f"Set mode -> {mode}\n")


    def setup(self, pin, typeInOut, pull_up_down=""):
        print(f"setup: pin {pin}, {typeInOut}, {pull_up_down}")

        if typeInOut == self.IN:
            self.addOutput(DummyInput(pin))
        elif typeInOut == self.OUT:
            self.addInput(DummyOutput(pin))
        else:
            raise ValueError("type not known")


    def output(self, pin, output):
        print(f"output pin number {pin} {output}")


    def input(self, pin):
        print(f"input pin number {pin}")


    def setTopLevel(self):
        self.dummyroot = Toplevel()
        self.addFrames()


    def setRoot(self):
        self.dummyroot = Tk()
        self.addFrames()
        self.dummyroot.mainloop()


    def addFrames(self):
        self.dummyroot.title("Raspberry Pi dummy GPIO")

        self.frameInput = LabelFrame(self.dummyroot, text="Inputs")
        self.frameOutput = LabelFrame(self.dummyroot, text="Outputs")

        self.frameInput.grid(row=0, column=0, padx=10, pady=10)
        self.frameOutput.grid(row=0, column=1, padx=10, pady=10)


    def addInput(self, input):
        self.inputs.append(input)

        btn = Button(self.frameInput, text=input.pin, padx=10, pady=10)
        btn.grid(row=self.rowInput, column=self.columnInput, padx=10, pady=10)

        self.rowInput += 1


    def addOutput(self, output):
        self.outputs.append(output)

        lbl = Label(self.frameOutput, text=output.pin, padx=10, pady=10)
        lbl.grid(row=self.rowOutput, column=self.columnOutput, padx=10, pady=10)

        self.rowOutput += 1


class DummyOutput():

    def __init__(self, pin):
        self.pin = pin
        self.state = False


class DummyInput():

    def __init__(self, pin):
        self.pin = pin
        self.state = False
