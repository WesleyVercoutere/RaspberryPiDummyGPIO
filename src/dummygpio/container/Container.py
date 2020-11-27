from ..business.GeneralData import GeneralData
from ..repository.InputRepository import InputRepository
from ..repository.OutputRepository import OutputRepository
from ..service.manager.GeneralDataManager import *
from ..service.manager.InputManager import *
from ..service.manager.OutputManager import *
from ..service.manager.PWMManager import *
from ..frontend.GUI import *
from ..service.mapper.GeneralDataMappper import GeneralDataMapper
from ..service.mapper.InputMapper import InputMapper
from ..service.mapper.OutputMapper import OutputMapper


class Container:

    def __init__(self, run_main_loop):
        
        self.generalDataMgr = GeneralDataManager(GeneralDataMapper(), GeneralData())
        self.inputMgr = InputManager(InputMapper(), InputRepository())
        self.outputMgr = OutputManager(OutputMapper(), OutputRepository())
        self.pwmManager = PWMManager()
        self.GUI = GUI(run_main_loop)
