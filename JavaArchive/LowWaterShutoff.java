// import com.pi4j.io.gpio.GpioController;
// import com.pi4j.io.gpio.GpioFactory;
// import com.pi4j.io.gpio.GpioPinDigitalInput;
// import com.pi4j.io.gpio.PinPullResistance;
// import com.pi4j.io.gpio.RaspiPin;
// import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
// import com.pi4j.io.gpio.event.GpioPinListenerDigital;

/**
* A Thread Controlling Class for any Hydrosystem
* @author ESW
* @version 1
*
* The purpose of this class is to shutoff the system
* It will check the resistence of the float switch, to
* check that the water level is not too low.
*/

public class LowWaterShutoff extends Thread {
	private int monitorPin = 0;
	private double waterlevelThreshold = 0.5; //Resistance Value that reflects when system toggles
	private StateObject controlling;
	private StateObject lowWaterState;
	private boolean condition = false;

	public LowWaterShutoff(int pinNumber, StateObject system) {
		monitorPin = pinNumber;
		controlling = system;
		lowWaterState = new StateObject(false);
	}

	public void start() {
		lowWaterState.setTrue();
		while (lowWaterState.checkstate()) {
			//check the float switch resistence
			if (checkResistance(monitorPin)) {
				// ok condition do nothing
			} else {
				// bad condition
				// Terminate the system that is associated with this instance
				controlling.stop();
				// Terminate from Checking, checking will resume when
				// the system is restarted
				lowWaterState.setFalse();
				// trigger some sort of notification
			}
		}

	}

	/**
 	* Does the comparison between Resistance Value and Water Level for System
 	*
 	* @param Int of the pin to be monitoring for the float switch
 	* @return Boolean of if resistance is in threshold to keep system on or off
 	*/	
	public boolean checkResistance(int monitorPin) {
		double resistanceMeasured = 0; //TODO Measurement of Resistence from Float Switch
		if (resistanceMeasured > waterlevelThreshold) {
			return true;
		} else {
			return false;
		}
	}
	public void stop() {
		lowWaterState.setFalse();
	}
}