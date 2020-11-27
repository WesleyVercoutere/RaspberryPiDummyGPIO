from ..dto.DigitalInputDto import DigitalInputDto
from ...business.DigitalInput import DigitalInput

class DigitalInputMapper:

    def __init__(self):
        pass

    def map_to_obj(self, dto):
        if not isinstance(dto, DigitalInputDto):
            raise TypeError("Wrong dto type.")

        general_data = GeneralData()

        general_data.warnings = dto.warnings
        general_data.mode = dto.mode

        return general_data

    def map_to_dto(self, obj):
        if not isinstance(obj, DigitalInput):
            raise TypeError("Wrong object type")

        dto = GeneralDataDto()

        dto.mode = obj.mode
        dto.warnings = obj.warnings
        dto.version = obj.version

        return dto