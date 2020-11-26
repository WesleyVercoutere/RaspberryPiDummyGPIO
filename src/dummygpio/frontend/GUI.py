from tkinter import Tk, Toplevel, LabelFrame


class GUI:

    __root = None
    __frameInput = None
    __frameOutput = None
    __GuiStarted = False


    def __init__(self, runMainLoop):
        print('Starting dummy gui.')

        self.__runMainLoop = runMainLoop

    
    def run(self):

        if not self.__GuiStarted:
            if self.__runMainLoop:
                self.__startMainLoop()
            
            else:
                self.__startTopLevel()

        self.__GuiStarted = True


    def __startMainLoop(self):
        self.__root = Tk()
        self.__setRoot()
        self.__setFrames()
        self.__root.mainloop()

    
    def __startTopLevel(self):
        self.__root = Toplevel()
        self.__setRoot()
        self.__setFrames()

    
    def __setRoot(self):
        print('set title')
        self.__root.title("Raspberry Pi dummy GPIO")


    def __setFrames(self):
        self.__frameInput = LabelFrame(self.__root, text="Inputs")
        self.__frameOutput = LabelFrame(self.__root, text="Outputs")

        self.__frameInput.grid(row=0, column=0, padx=10, pady=10)
        self.__frameOutput.grid(row=0, column=1, padx=10, pady=10)
