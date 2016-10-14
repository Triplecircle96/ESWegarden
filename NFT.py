import RPi.GPIO as GPIO

class NFT:
    def __init__(self, motorPin, sensorPin):
        self.motorPin = motorPin
        self.SensorPin = sensorPin

    def instantiateSystem(self):
        # Turn on the Motor

        # Instantiate Sensor

