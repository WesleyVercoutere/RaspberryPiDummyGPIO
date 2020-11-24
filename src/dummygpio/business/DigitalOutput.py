from .InputOutput import *


class DigitalOutput(InputOutput):
    
    def __init__(self, channel, initial_state=False):
        super().__init__(channel)
        self.state = initial_state
