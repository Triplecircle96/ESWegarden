import RPi.GPIO as GPIO
import Base_Sensor

class Float_Switch(Base_Sensor.Base_Sensor):
    def __init__(self, sensorPinIn):
        super(Float_Switch, self).__init__(sensorPinIn)
        GPIO.setup(self.port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	#Checks whether to start in water high or low condition
	if GPIO.input(self.port):
            GPIO.add_event_detect(self.port, GPIO.FALLING, callback=self.waterLevelHigh, bouncetime=1000)
	else:
            GPIO.add_event_detect(self.port, GPIO.RISING, callback=self.waterLevelLow, bouncetime=1000)		

    def waterLevelLow(self, pin = 0):
        # Send Turn off Command
        self.event2.clear()
        self.event1.set()
        # event1 is falling water and event2 is rising
        GPIO.remove_event_detect(self.port)
        GPIO.add_event_detect(self.port, GPIO.FALLING, callback=self.waterLevelHigh, bouncetime=1000)


    def waterLevelHigh(self, pin = 0):
        # Send Turn on Command
        self.event1.clear()
        self.event2.set()
        GPIO.remove_event_detect(self.port)
        GPIO.add_event_detect(self.port, GPIO.RISING, callback=self.waterLevelLow, bouncetime=1000)
