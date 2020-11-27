from ..business.GeneralData import GeneralData
from ..repository.DigitalInputRepository import DigitalInputRepository
from ..repository.DigitalOutputRepository import DigitalOutputRepository
from ..service.manager.GeneralDataManager import *
from ..service.manager.DigitalInputManager import DigitalInputManager
from ..service.manager.DigitalOutputManager import DigitalOutputManager
from ..service.manager.PWMManager import *
from ..frontend.GUI import *
from ..service.mapper.GeneralDataMappper import GeneralDataMapper
from ..service.mapper.DigitalInputMapper import DigitalInputMapper
from ..service.mapper.DigitalOutputMapper import DigitalOutputMapper


class Container:

    def __init__(self, run_main_loop):
        
        self.generalDataMgr = GeneralDataManager(GeneralDataMapper(), GeneralData())
        self.inputMgr = DigitalInputManager(DigitalInputMapper(), DigitalInputRepository())
        self.outputMgr = DigitalOutputManager(DigitalOutputMapper(), DigitalOutputRepository())
        self.pwmManager = PWMManager()
        self.GUI = GUI(run_main_loop)
