from abc import ABC, abstractmethod


class InputOutput(ABC):

    @abstractmethod
    def __init__(self, channel):
        self.channel = channel
        self.state = False

    @abstractmethod
    def __str__(self):
        return f"pin {self.channel} = {self.state}"
    