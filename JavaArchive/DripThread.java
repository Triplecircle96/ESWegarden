/**
* The Running thread Class for Drip System
* @author ESW
* @version 1
*
* The purpose of this class is to directly control the pumppin
* on the time on and time off cycle needed for the Drip System.
*/

// import com.pi4j.io.gpio.GpioController;
// import com.pi4j.io.gpio.GpioFactory;
// import com.pi4j.io.gpio.GpioPinDigitalInput;
// import com.pi4j.io.gpio.PinPullResistance;
// import com.pi4j.io.gpio.RaspiPin;
// import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
// import com.pi4j.io.gpio.event.GpioPinListenerDigital;

public class DripThread extends Thread {
	private int timeActive = 0;
	private int timeSleep = 0;
	private int pummppin = 0;
	private StateObject o = new StateObject(false);

	public DripThread(int timeOn, int timeoff, StateObject ob, int controlPin) {
		o = ob;
		pummppin = controlPin;
		timeActive = 1000 * timeOn; // Seconds converted to Milliseconds
		timeSleep = 1000 * timeOff; // Seconds converted to Milliseconds
		gotime();
	}

    /**
    * Method that starts the continious timer cycle, this can be terminated by
    * setting the state object to false outside of this scope 
    */
	private void gotime() {
		while(o.checkState()) {
			// turn the control pin on
			try {
    			Thread.sleep(timeSleep);                 //1000 milliseconds is one second.
			} catch(InterruptedException ex) {
    			Thread.currentThread().interrupt();
			}
		}
	}
}