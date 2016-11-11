import RPi.GPIO as GPIO
import Base_Sensor

class Float_Switch(Base_Sensor.Base_Sensor):
    def __init__(self, sensorPinIn):
        super(Float_Switch, self).__init__(sensorPinIn)
        GPIO.setup(self.port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.port, GPIO.FALLING, callback=Float_Switch.waterLevelHigh, bouncetime=50)
		
    def waterLevelLow(self, pin = 0):
        # Send Turn off Command
        if not self.event1.isSet():
			self.event1.set()
			self.event2.clear()
        # event1 is falling water and event2 is rising

    def waterLevelHigh(self, pin = 0):
        # Send Turn on Command
        if not self.event2.isSet():
			self.event1.clear()
			self.event2.set()
