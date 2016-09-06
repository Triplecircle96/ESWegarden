/**
* A Thread Controlling Class for Drip System
* @author ESW
* @version 1
*
* The purpose of this class is to control the continously running thread
* along with starting the monitoring for low water level shutoff.
*/

public class DripRunnable extends Thread {
	private DripThread temp;
	private StateObject dripThreadState = new StateObject(false);
	private int timeActive = 0;
	private int timeSleep = 0;
	private int waterLevelpin =0;
	private int pumppin = 0;
	private LowWaterShutoff safety;

	public DripRunnable(int timeOn, int timeOff, int controlPin, int waterpin) {
		boolean cont = true;
		dripThreadState = new StateObject(true);
		waterLevelpin = waterpin;
		pumppin = controlPin;
		// Creates a Low Water Shutoff Object associated with the pin and state object
		safety = new LowWaterShutoff(waterpin, dripThreadState);
	}
	
	public void start() {
		safety.start();
		if (dripThreadState.checkState()) {
			// Create a new thread that will actually run the looping, each time it is
			// restarted, the previous thread is abandoned and a new thread is created
			temp = new DripThread(timeOn, timeOff, dripThreadState, pumppin); 
		}
	}

	public void stop() {
		dripThreadState.setFalse();
	}
}