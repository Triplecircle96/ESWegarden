import RPi.GPIO as GPIO

class Float_Switch(Base_Sensor):
    def __init__(self, sensorPinIn):
        super().__init__(sensorPinIn)
        GPIO.setup(self.sensorPin, GPIO.IN, pull_up_down=GPIO.PUD)

    def waterLevelLow(self):
        # Send Turn off Command

    def waterLevelHigh(self):
        # Send Turn on Command

    GPIO.add_event_detect(self.sensorPin, GPIO.FALLING, callback=waterLevelHigh, bouncetime=50)

    GPIO.add_event_detect(self.sensorPin, GPIO.RISING, callback=waterLevelLow, bouncetime=50)