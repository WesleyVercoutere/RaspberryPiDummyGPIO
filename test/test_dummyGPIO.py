import unittest
from src.dummygpio.DummyGPIO import *

class TestDummyGPIO(unittest.TestCase):

    def setUp(self):
        self.GPIO = DummyGPIO(False)

    def test_init(self):
        GPIO1 = DummyGPIO(True)
        GPIO2 = DummyGPIO(False)

        self.assertTrue(GPIO1.tkinterApp)
        self.assertFalse(GPIO2.tkinterApp)

    def test_constants(self):
        BCM = "bcm"
        OUT= "output"
        IN = "input"
        HIGH = True
        LOW = False
        PUD_DOWN = ""

        self.assertEqual(self.GPIO.BCM, BCM)
        self.assertEqual(self.GPIO.OUT, OUT)
        self.assertEqual(self.GPIO.IN, IN)
        self.assertEqual(self.GPIO.HIGH, HIGH)
        self.assertEqual(self.GPIO.LOW, LOW)
        self.assertEqual(self.GPIO.PUD_DOWN, PUD_DOWN)



    # test_setwarnings
    # test_setmode
    # test_setup
    # test_output
    # test_input




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
