import unittest

from src.dummygpio.business.GeneralData import GeneralData


class TestGeneralData(unittest.TestCase):

    def test_init_pullUp(self):
        gd = GeneralData()

        gd.warnings = True
        gd.mode = "Test"

        self.assertTrue(gd.warnings)
        self.assertEqual("Test", gd.mode)
        self.assertEqual("V1.0.0", gd.version)
        