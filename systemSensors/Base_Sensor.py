import threading

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Base_Sensor(object):

    def __init__(self, portnum):
        self.port = portnum
        # self.value = 0
        self.event1 = threading.Event()
        self.event2 = threading.Event()
        # event2 used to block opposite of event1
        self.event1.set()
        # implicit self.event2.clear()

    def read_data(self):
        raise NotImplementedError()
        
	def checkWater(self):
		raise NotImplementedError()
