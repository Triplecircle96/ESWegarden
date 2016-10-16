import RPi.GPIO as GPIO
import datetime

class NFT:
    def __init__(self, motorPin, sensorPin):
        self.motorPin = motorPin
        self.SensorPin = sensorPin
        self.startTime = datetime.datetime.now().time().isoformat()

    def instantiateSystem(self):
        # Setup GPIO Pin Mode
        GPIO.setup(self.motorPin, GPIO.OUT)
        # Turn on the Motor
        GPIO.output(self.motorPin,1)
        # Instantiate Sensor

    def deactivateSystem(self):
        # Turn Off Motor
        GPIO.output(self.motorPin,0)

    def diagnostic(self):
        # Prints system information for user
        print 'Time Started: ' + self.startTime + '\n'
        print 'Motor Pin Used: ' + self.motorPin + '\n'
        print 'Water Level Pin Used: ' + self.SensorPin + '\n'


