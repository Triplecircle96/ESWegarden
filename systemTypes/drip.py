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

    def instantiateSystem(self):
        self.runSystem()

    def runSystem(self):
        # Turn on the Motor
        GPIO.output(self.motorPin, 1)
        
        # Timer Function to Turn Off
        if not self.is_running:
            self.is_running = True
            self._timer = Timer(self.offTime, self.reactivateSystem())
            self.sensor.event1.wait(self.offTime)
            if self.sensor.event1.isSet():
                self.deactivateSystem()

    def reactivateSystem(self):
        GPIO.output(self.motorPin, 0)
        self.alive = True
        # Timer Function
        if self.is_running:
            self.is_running = False;
            self._timer = Timer(self.onTime, self.runSystem())
            self._timer.start()
            self.sensor.event1.wait(onTime)
            if self.sensor.event1.isSet():
                self.deactivateSystem()

    def deactivateSystem(self):
        # Turn Off Motor
        self.alive = False
        GPIO.output(self.motorPin, 0)
        self.is_running = False
        self._timer.cancel()
        self.sensor.event2.wait()
        self.reactivateSystem()

    def diagnostic(self):
        # Prints system information for user
        print 'Time Started: ' + self.startTime + '\n'
        print 'Motor Pin Used: ' + self.motorPin + '\n'
        print 'Water Level Pin Used: ' + self.SensorPin + '\n'






