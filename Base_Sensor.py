import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Base_Sensor:

    value = 0
    port = []

    def __init__(self, portnum):
        self.port = portnum

    def read_data(self):
        raise NotImplementedError()