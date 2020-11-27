import unittest
from src.dummygpio.business.DigitalInput import *


class TestDigitalInput(unittest.TestCase):

    def setUp(self):
        self.PUD_UP = "PUD_UP"
        self.PUD_DOWN = "PUD_DOWN"

    def test_init_pullUp(self):
        di = DigitalInput(1, pull_up_down=self.PUD_UP)

        self.assertEqual(1, di.channel)
        self.assertTrue(di.state)
        self.assertEqual(self.PUD_UP, di.pull_up_down)
        self.assertEqual('pin 1 = True', di.__str__())

    def test_init_pullDown(self):
        di = DigitalInput(2, pull_up_down=self.PUD_DOWN)

        self.assertEqual(2, di.channel)
        self.assertFalse(di.state)
        self.assertEqual(self.PUD_DOWN, di.pull_up_down)
        self.assertEqual('pin 2 = False', di.__str__())

    def test_init_pullValueError(self):
        with self.assertRaises(ValueError):
            di = DigitalInput(3, pull_up_down='')
