import RPi.GPIO as GPIO
import datetime
import threading
from threading import Timer
from eGardenPackage.systemSensors import *

class drip(system):
    def __init__(self, motorPin, sensorPin, onTime):
        self.motorPin = motorPin
        self.SensorPin = sensorPin
        self.onTime = onTime
        self.startTime = datetime.datetime.now().time().isoformat()
        self.alive = True
        # Variables for Timer
        self._timer = None
        self.is_running = False
        # Setup GPIO Pin Mode
        GPIO.setup(self.motorPin, GPIO.OUT)
        self.sensor = Float_Switch(self.SensorPin)

    def runSystem(self):
            # Turn on the Motor
            GPIO.output(self.motorPin,1)
            # Instantiate Sensor

            # Timer Function to Turn Off
            if self.is_running:


    def reactivateSystem(self):
        # Turn On Motor
        self.alive = True
        self.runSystem()
        # Timer Function
        if not self.is_running:
                self._timer = Timer(self.onTime,runSystem)
                self._timer.start()
                self.is_running = True;

    def deactivateSystem(self):
        # Turn Off Motor
        GPIO.output(self.motorPin, 0)
        self.is_running = False

    def diagnostic(self):
        # Prints system information for user
        print 'Time Started: ' + self.startTime + '\n'
        print 'Motor Pin Used: ' + self.motorPin + '\n'
        print 'Water Level Pin Used: ' + self.SensorPin + '\n'






