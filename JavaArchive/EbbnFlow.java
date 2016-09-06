// import com.pi4j.io.gpio.GpioController;
// import com.pi4j.io.gpio.GpioFactory;
// import com.pi4j.io.gpio.GpioPinDigitalInput;
// import com.pi4j.io.gpio.PinPullResistance;
// import com.pi4j.io.gpio.RaspiPin;
// import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
// import com.pi4j.io.gpio.event.GpioPinListenerDigital;

/**
* A Class for Ebb and Flow System
* @author ESW
* @version 1
*/
public class EbbnFlow extends HydroSystem {

    /**
    * EbbnFlow System Object Constructor
    * @param condition Whether to create system or placeholder
    * @param pumpSetPin Pin number for Pump Control
    * @param waterLevelSetpin Pin number of Water Low Level Set Pin
    * @param waterHighPin Water High Level detection for Ebb and Flow System
    */	
	public EbbnFlow(boolean condition, int pumpSetPin, int waterLevelSetpin, int waterHighPin) {
		if (condition) {
			System.out.println("Setting up Ebb and Flow System");
			adjustSystemParam();
		}
	}

	public void initiateSystem() {

	}

	public void adjustSystemParam() {

	}

	public void terminateSystem() {
		
	}

}