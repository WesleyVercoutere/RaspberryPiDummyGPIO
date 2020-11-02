from tkinter import *

class DummyGPIO():

    def __init__(self, tkinterApp):
        self.tkinterApp = tkinterApp

    def setTopLevel(self):
        dummyroot = Toplevel()
        dummyroot.title("Raspberry Pi dummy GPIO")
        dummyroot.geometry("400x200")

    def setRoot(self):
        pass


    

    # frameInput = LabelFrame(dummyroot, text="Inputs")
    # frameOutput = LabelFrame(dummyroot, text="Outputs")

    # frameInput.pack()
    # frameOutput.pack()

    # test = Label(dummyroot, text="test")
    # test.pack()


