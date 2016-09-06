/**
* A Class for Drip System
* @author ESW
* @version 1
*
* The purpose of this class is to act as a link between the user and the 
* thread that controls the drip system. UI communication should not occur
* in the DripRunnable or DripThread threads!
*/

import java.util.Scanner;
import java.util.stream.IntStream;

public class Drip extends HydroSystem {
	private static Scanner kybd = new Scanner(System.in);
	private int timeOn = 0;
	private int timeOff = 0;
	private int pumpPin = 0;
	private int waterLevelPin = 0;
	private DripRunnable dripSystem;

    /**
    * Drip System Object Constructor
    * @param condition Whether to create system or placeholder
    */
	public Drip(boolean condition) {
		if (condition) {
			System.out.println("Setting up Drip System");
			adjustSystemParam();
		}
	}

    /**
    * Creates the Drip System, this object is what the user interfaces to. 
    */
	public void initiateSystem() {
		// Creates Runnable Drip Object - This thread controls the continous thread
		dripSystem = new DripRunnable(timeOn, timeOff, pumpPin, waterLevelPin);
		dripSystem.start();
	}

    /**
    * Prompts the user through the system parameters that they want to change for the
    * drip system. 
    */
	public void adjustSystemParam() {
		System.out.println("What parameters of the Drip System would you like to change?");
		System.out.println("1. Time System is On");
		System.out.println("2. Time System is Off");
		System.out.println("3. Pump Controlling pin");
		System.out.println("4. Water Level Shutoff Pin (Float Switch)");
		int choice = kybd.nextInt();
		switch (choice) {
			case 1:
				System.out.println();
		}
	}

    /**
    * Turns off the Drip System
    */
	public void terminateSystem() {
		dripSystem.stop();
	}

		/**
 	* Validates that the proposed pin number is valid, upon which pin assignment will occur
 	*
 	* @param Int of the new proposed pin number, int assigning which sensor to reconfigure
 	* @return void 
 	*/
	private void validateSignalPin(int pinAssignment, int pinControlNumber) {
		int[] rpiSignalPins = {2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21};
		boolean contains = IntStream.of(rpiSignalPins).anyMatch(x -> x == 4);
		if (contains) {
			changeSignalPin(pinAssignment, pinControlNumber);
		} else {
			System.out.println("Invalid Signal Pin Assignment!");
			System.out.println("Please reference the Raspberry Pi Documentation");
		}
	}

}