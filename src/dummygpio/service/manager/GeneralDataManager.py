from ..dto.GeneralDataDto import GeneralDataDto


class GeneralDataManager:

    def __init__(self, general_data_mapper, general_data):
        self.__generalDataMapper = general_data_mapper
        self.__generalData = general_data

    def get_general_data(self):
        dto = GeneralDataDto()

        print(type(dto))

    def set_warning(self, dto):
        self.__generalData.warnings = dto.warnings

    def set_mode(self, dto):
        self.__generalData.mode = dto.mode
