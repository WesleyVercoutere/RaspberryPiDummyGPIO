from .InputOutput import *


class DigitalInput(InputOutput):
    
    def __init__(self, channel, pull_up_down = ''):
        super().__init__(channel)

        if pull_up_down == 'PUD_UP':
            self.state = True
