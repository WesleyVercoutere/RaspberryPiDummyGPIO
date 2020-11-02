from tkinter import *

class DummyGPIO():

    def __init__(self, tkinterApp):
        print("Project doesn't run on a Raspberry Pi.\nSimulation will start!\n")

        self.tkinterApp = tkinterApp
        self.BCM = "bcm"
        self.OUT= "out"
        self.IN = "in"
        self.HIGH = "high"
        self.LOW = "low"
        self.PUD_DOWN = "Pull down"

        self.inputs = []
        self.outputs = []

    def setwarnings(self, warning):
        print(f"Set warnings -> {warning}\n")

        if self.tkinterApp:
            self.setTopLevel()
        else:
            self.setRoot()


    def setmode(self, mode):
        print(f"Set mode -> {mode}\n")


    def setup(self, pin, typeInOut, pull_up_down=""):
        print(f"setup = {pin} {typeInOut} {pull_up_down}")

        if typeInOut == "in":
            self.addOutput(DummyInput(pin))

        if typeInOut == "out":
            self.addInput(DummyOutput(pin))


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


    def addFrames(self):
        self.dummyroot.title("Raspberry Pi dummy GPIO")
        # self.dummyroot.geometry("400x200")

        self.frameInput = LabelFrame(self.dummyroot, text="Inputs")
        self.frameOutput = LabelFrame(self.dummyroot, text="Outputs")

        self.frameInput.pack()
        self.frameOutput.pack()


    def addInput(self, input):
        self.inputs.append(input)

        btn = Button(self.frameInput, text=input.pin)
        btn.pack()


    def addOutput(self, output):
        self.outputs.append(output)

        lbl = Label(self.frameOutput, text=output.pin)
        lbl.pack()


class DummyOutput():

    def __init__(self, pin):
        self.pin = pin
        self.state = False


class DummyInput():

    def __init__(self, pin):
        self.pin = pin
        self.state = False
