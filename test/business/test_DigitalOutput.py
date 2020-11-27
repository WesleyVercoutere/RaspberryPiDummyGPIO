import unittest

from src.dummygpio.business.DigitalOutput import DigitalOutput


class TestDigitalOutput(unittest.TestCase):
    
    def test_init_default(self):
        do = DigitalOutput(1)

        self.assertEqual(1, do.channel)
        self.assertFalse(do.state)
        self.assertEqual('pin 1 = False', do.__str__())

    def test_init_false(self):
        do = DigitalOutput(2, initial_state=False)

        self.assertEqual(2, do.channel)
        self.assertFalse(do.state)
        self.assertEqual('pin 2 = False', do.__str__())


    def test_init_true(self):
        do = DigitalOutput(3, initial_state=True)

        self.assertEqual(3, do.channel)
        self.assertTrue(do.state)
        self.assertEqual('pin 3 = True', do.__str__())
