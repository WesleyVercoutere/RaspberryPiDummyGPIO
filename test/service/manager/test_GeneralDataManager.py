import unittest

from src.dummygpio.service.manager.GeneralDataManager import GeneralDataManager
from src.dummygpio.service.mapper.GeneralDataMappper import GeneralDataMapper
from src.dummygpio.business.GeneralData import GeneralData


class TestGeneralDataManager(unittest.TestCase):

    def setUp(self):
        pass

    # def test_get_general_data(self):
    #     mgr = GeneralDataManager(GeneralDataMapper(), GeneralData())
    #     mgr.get_general_data()
    #
    # def test_get_general_data_value_error(self):
    #     mgr = GeneralDataManager(GeneralDataMapper(), GeneralData())
    #     mgr.get_general_data()
