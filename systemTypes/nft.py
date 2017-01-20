import RPi.GPIO as GPIO
import datetime
import time
import threading
from systemSensors import Float_Switch
import system

class NFT(system.system):
    def __init__(self, motorPin, sensorPin):
        self.debug = True
        self.motorPin = motorPin
        self.SensorPin = sensorPin
        self.startTime = datetime.datetime.now().time().isoformat()
        self.alive = True
        # Setup GPIO Pin Mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.motorPin, GPIO.OUT)
        self.sensor = Float_Switch.Float_Switch(self.SensorPin)
        if (self.debug):
            print("Creating NFT Object")


    def instantiateSystem(self):
        if (self.debug):
            print("Instantiating NFT System")
        self.runSystem()
        time.sleep(1000)
        while True:
            if not self.sensor.event1.isSet():
                self.sensor.event1.wait()
                self.deactivateSystem()
            else:
                self.sensor.event2.wait()
                self.reactivateSystem()

    def runSystem(self):
        if (self.debug):
            print("Running NFT System")
        if self.alive:
            # Turn on the Motor
            GPIO.output(self.motorPin,1)
            if (self.debug):
                print("Running NFT System : Turning ON Motor")
            # Instantiate Sensor
        else:
            GPIO.output(self.motorPin,0)
            if (self.debug):
                print("Running NFT System : Turning OFF Motor")

    def reactivateSystem(self):
        if (self.debug):
            print("Reactivating system : Turning ON Motor")
        # Turn On Motor
        self.alive = True
        self.runSystem()

    def deactivateSystem(self):
        if (self.debug):
            print("Deactivating system : Turning OFF Motor")
        # Turn Off Motor
        self.alive = False
        self.runSystem()

    def diagnostic(self):
        # Prints system information for user
        print 'Time Started: ' + self.startTime + '\n'
        print 'Motor Pin Used: ' + self.motorPin + '\n'
        print 'Water Level Pin Used: ' + self.SensorPin + '\n'