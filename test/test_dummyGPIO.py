import unittest
from src.dummygpio.DummyGPIO import *

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.GPIO = DummyGPIO(False)

    def test_init(self):
        GPIO1 = DummyGPIO(True)
        GPIO2 = DummyGPIO(False)

        self.assertTrue(GPIO1.tkinterApp)
        self.assertFalse(GPIO2.tkinterApp)

    def test_constants(self):
        self.BCM = "bcm"
        self.OUT= "output"
        self.IN = "input"
        self.HIGH = "high"
        self.LOW = "low"
        self.PUD_DOWN = "Pull down"

        self.assertEqual(self.GPIO.BCM, self.BCM)
        self.assertEqual(self.GPIO.OUT, self.OUT)
        self.assertEqual(self.GPIO.IN, self.IN)
        self.assertEqual(self.GPIO.HIGH, self.HIGH)
        self.assertEqual(self.GPIO.LOW, self.LOW)
        self.assertEqual(self.GPIO.PUD_DOWN, self.PUD_DOWN)








    ## Test examples
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
