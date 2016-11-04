import RPi.GPIO as GPIO

class Float_Switch(Base_Sensor):
    def __init__(self, sensorPinIn):
        super().__init__(sensorPinIn)
        GPIO.setup(self.sensorPin, GPIO.IN, pull_up_down=GPIO.PUD)

    def waterLevelLow(self):
        # Send Turn off Command
        this.event1.set()
        this.event2.clear()
        # event1 is falling water and event2 is rising

    def waterLevelHigh(self):
        # Send Turn on Command
        this.event1.clear()
        this.event2.set()

    GPIO.add_event_detect(self.sensorPin, GPIO.FALLING, callback=waterLevelHigh, bouncetime=50)

    GPIO.add_event_detect(self.sensorPin, GPIO.RISING, callback=waterLevelLow, bouncetime=50)