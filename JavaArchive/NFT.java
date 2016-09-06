// import com.pi4j.io.gpio.GpioController;
// import com.pi4j.io.gpio.GpioFactory;
// import com.pi4j.io.gpio.GpioPinDigitalInput;
// import com.pi4j.io.gpio.PinPullResistance;
// import com.pi4j.io.gpio.RaspiPin;
// import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
// import com.pi4j.io.gpio.event.GpioPinListenerDigital;

/**
* A Class for NFT System
* @author ESW
* @version 1
*/
public class NFT extends HydroSystem {
	private int pumpPin = 0;
	private int waterLevelPin = 0;

    /**
    * EbbnFlow System Object Constructor
    * @param condition Whether to create system or placeholder
    * @param pumpSetPin Pin number for Pump Control
    * @param waterLevelSetpin Pin number of Water Low Level Set Pin
    */	
	public NFT(boolean condition, int pumpSetPin, int waterLevelSetpin) {
		if (condition) {
			System.out.println("Setting up Drip System");
			initiateSystem(pumpSetPin, waterLevelSetpin);
		}		
	}

	public void initiateSystem(int pumpSetPin, int waterLevelSetpin) {

	}

	public void initiateSystem(int pumpSetPin) {
		
	}

	public void adjustSystemParam() {

	}

	public void terminateSystem() {

	}

}