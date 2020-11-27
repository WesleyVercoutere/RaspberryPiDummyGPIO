import unittest

from src.dummygpio.business.GeneralData import GeneralData
from src.dummygpio.service.dto.GeneralDataDto import GeneralDataDto
from src.dummygpio.service.mapper.GeneralDataMappper import GeneralDataMapper


class TestGeneralDataMapper(unittest.TestCase):

    def setUp(self) -> None:
        self.mapper = GeneralDataMapper()

    def test_map_to_obj(self):
        dto = GeneralDataDto()
        dto.warnings = False
        dto.mode = "test"

        obj = self.mapper.map_to_obj(dto)
        self.assertFalse(obj.warnings)
        self.assertEqual(obj.mode, "test")

    def test_map_to_obj_type_error(self):
        dto = "Hello World"

        with self.assertRaises(TypeError):
            obj = self.mapper.map_to_obj(dto)

    def test_map_to_dto(self):
        obj = GeneralData()
        obj.warnings = False
        obj.mode = "test"

        dto = self.mapper.map_to_dto(obj)
        self.assertFalse(dto.warnings)
        self.assertEqual(dto.mode, "test")

    def test_map_to_dto_type_error(self):
        obj = "Hello World"

        with self.assertRaises(TypeError):
            dto = self.mapper.map_to_dto(obj)
