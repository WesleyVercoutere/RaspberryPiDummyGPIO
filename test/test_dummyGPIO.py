import unittest
from tkinter import *
from src.dummygpio.DummyGPIO import *

class TestDummyGPIO(unittest.TestCase):

    def setUp(self):
        pass


    def test_init(self):
        GPIO1 = DummyGPIO(True)
        GPIO2 = DummyGPIO(False)

        self.assertTrue(GPIO1.tkinterApp)
        self.assertFalse(GPIO2.tkinterApp)


    def test_constants(self):
        self.GPIO = DummyGPIO(False)
        
        BCM = "bcm"
        OUT= "output"
        IN = "input"
        HIGH = True
        LOW = False
        PUD_UP = "PUD_UP"
        PUD_DOWN ="PUD_DOWN"

        self.assertEqual(self.GPIO.BCM, BCM)
        self.assertEqual(self.GPIO.OUT, OUT)
        self.assertEqual(self.GPIO.IN, IN)
        self.assertEqual(self.GPIO.HIGH, HIGH)
        self.assertEqual(self.GPIO.LOW, LOW)
        self.assertEqual(self.GPIO.PUD_UP, PUD_UP)
        self.assertEqual(self.GPIO.PUD_DOWN, PUD_DOWN)


    def test_setwarnings1(self):
        root = Tk()
        GPIO = DummyGPIO(True)
        GPIO.setwarnings(False)
        guiType = str(GPIO.dummyroot)
        root.destroy()

        self.assertEqual(guiType, ".!toplevel")


    # def test_setwarnings2(self):
    #     GPIO2 = DummyGPIO(False)
    #     GPIO2.setwarnings(False)
    #     # guiType = GPIO2.dummyroot
    #     GPIO2.root.destroy()
    #     # print(guiType)
    #     # self.assertEqual(guiType, ".!toplevel")


    def test_setmode(self):
        #this method contains no logic in the simulation library
        pass


    def test_setup(self):
        pass


    def test_output(self):
        pass


    def test_input(self):
        pass
