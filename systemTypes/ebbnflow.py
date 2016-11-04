import RPi.GPIO as GPIO
import datetime
import threading
from eGardenPackage.systemSensors import *

class ebbnflow(system):
    def __init__(self, motorPin, sensorPin):
        self.motorPin = motorPin
        self.SensorPin = sensorPin
        self.startTime = datetime.datetime.now().time().isoformat()
        self.alive = True
        # Setup GPIO Pin Mode
        GPIO.setup(self.motorPin, GPIO.OUT)
        self.sensor = Float_Switch(self.SensorPin)

    def runSystem(self):
        if self.alive:
            # Turn on the Motor
            GPIO.output(self.motorPin,1)
            # Instantiate Sensor
        else:
            GPIO.output(self.motorPin,0)

    def reactivateSystem(self):
        # Turn On Motor
        self.alive = True
        self.runSystem()

    def deactivateSystem(self):
        # Turn Off Motor
        self.alive = False
        self.runSystem()

    def diagnostic(self):
        # Prints system information for user
        print 'Time Started: ' + self.startTime + '\n'
        print 'Motor Pin Used: ' + self.motorPin + '\n'
        print 'Water Level Pin Used: ' + self.SensorPin + '\n'






