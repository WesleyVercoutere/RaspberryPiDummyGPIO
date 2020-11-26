from ..mapper.GeneralDataMappper import *
from ...business.GeneralData import *


class GeneralDataManager:

    def __init__(self, generalDataMapper, generalData):
        self.__generalDataMapper = generalDataMapper
        self.__generalData = generalData


    def setWarning(self, dto):
        self.__generalData.warnings = dto.warnings


    def setMode(self, dto):
        self.__generalData.mode = dto.mode
        