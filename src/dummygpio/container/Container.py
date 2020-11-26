from ..service.manager.GeneralDataManager import *
from ..service.manager.InputManager import *
from ..service.manager.OutputManager import *
from ..service.manager.PWMManager import *
from ..frontend.GUI import *


class Container():

    def __init__(self, runMainLoop):
        
        self.generalDataMgr = GeneralDataManager(GeneralDataMappper(), GeneralData())
        self.inputMgr = InputManager()
        self.outputMgr = OutputManager()
        self.pwmManager = PWMManager()
        self.GUI = GUI(runMainLoop)
