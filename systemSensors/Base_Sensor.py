import threading

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Base_Sensor:

    def __init__(self, portnum):
        self.port = portnum
        self.value = 0
        self.event = threading.Event()

    def read_data(self):
        raise NotImplementedError()