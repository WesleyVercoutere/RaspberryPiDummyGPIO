from .InputOutput import *


class DigitalInput(InputOutput):
    
    def __init__(self, channel, pull_up_down):
        super().__init__(channel)

        self.pull_up_down = pull_up_down
        self.__setInitialState()


    def __setInitialState(self):
        PUD_UP = "PUD_UP"
        PUD_DOWN ="PUD_DOWN"

        if self.pull_up_down == PUD_DOWN:
            self.state = False

        elif self.pull_up_down == PUD_UP:
            self.state = True

        else :
            raise ValueError('Wrong value for pull up/down parameter!')
