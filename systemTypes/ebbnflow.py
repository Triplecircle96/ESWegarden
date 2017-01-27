import RPi.GPIO as GPIO
import datetime
import time
import threading
from systemSensors import Float_Switch
import system

class ebbnflow(system.system):
    def __init__(self, motorPin, sensorPin, onTime, offTime):
        self.motorPin = motorPin
        self.SensorPin = sensorPin
        self.startTime = datetime.datetime.now().time().isoformat()
        self.alive = True
        self.onTime = onTime
        self.offTime = offTime
        self.is_running = False
        # Setup GPIO Pin Mode
        GPIO.setup(self.motorPin, GPIO.OUT)
        self.sensor = Float_Switch.Float_Switch(self.SensorPin)

    def instantiateSystem(self):
        self.runSystem()

    def runSystem(self):
        # Turn on the Motor
        GPIO.output(self.motorPin, 1)
        self.alive = True
        # Timing code
        if not self.is_running:
            self.is_running = True
            self.sensor.event2.wait(self.onTime)
            if self.sensor.event2.isSet():
                self.waitSystem()

    def waitSystem(self):
        GPIO.output(self.motorPin, 0)
        # Timing code
        if self.is_running:
            self.is_running = False
            self.sensor.event1.wait(self.offTime)
            if self.sensor.event1.isSet():
                self.deactivateSystem()
            else:
                self.runSystem()

    def deactivateSystem(self):
        # Turn Off Motor
        self.alive = False
        GPIO.output(self.motorPin, 0)
        self.is_running = False
        self.sensor.event1.wait()
        self.runSystem()

    def diagnostic(self):
        # Prints system information for user
        print 'Time Started: ' + self.startTime + '\n'
        print 'Motor Pin Used: ' + self.motorPin + '\n'
        print 'Water Level Pin Used: ' + self.SensorPin + '\n'