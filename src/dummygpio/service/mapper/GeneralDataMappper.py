from src.dummygpio.business.GeneralData import GeneralData
from src.dummygpio.service.dto.GeneralDataDto import GeneralDataDto


class GeneralDataMapper:

    def __init__(self):
        pass

    def map_to_obj(self, dto):
        if not isinstance(dto, GeneralDataDto):
            raise TypeError("Wrong dto type.")

        general_data = GeneralData()

        general_data.warnings = dto.warnings
        general_data.mode = dto.mode

        return general_data

    def map_to_dto(self, obj):
        if not isinstance(obj, GeneralData):
            raise TypeError("Wrong object type")

        dto = GeneralDataDto()

        dto.mode = obj.mode
        dto.warnings = obj.warnings
        dto.version = obj.version

        return dto
