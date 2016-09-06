import java.util.Scanner;
import java.util.stream.IntStream;

/**
* Driver Class for Egarden System
* @author ESW
* @version 1
*/

public class Egarden {
	private static Scanner kybd = new Scanner(System.in);
	public static int pump1pin = 15;
	public static int pump2pin = 18;
	public static int floatSwitch1 = 21;
	public static int floatSwitch2 = 24;
	public static int floatSwitch3 = 26;
	private static HydroSystem outlet1 = new NFT(false, pump1pin, floatSwitch1);
	private static HydroSystem outlet2 = new NFT(false, pump2pin, floatSwitch2);

	public static void main(String args[]) {
		System.out.println();
		System.out.println("Welcome to eGarden");
		System.out.println("eGarden is an interface to controlling your hydroponics systems");
		System.out.println("Made by Mo Alshihabi, James Li, and Siva Movva");
		System.out.println();
		System.out.println("Currently only two outputs on Box are supported (Ones with RED LEDs next to them");
		System.out.println("Using System Default Pin Assignments:");
		System.out.println("Pump 1 Control Signal:" + pump1pin);
		System.out.println("Pump 2 Control Signal:" + pump2pin);
		System.out.println("Float Switch 1 Signal:" + floatSwitch1);
		System.out.println("Float Switch 2 Signal:" + floatSwitch2);
		System.out.println("Float Switch 3 Signal:" + floatSwitch3);
		boolean cont = true; // This should not be set false, DEBUG

		while (cont) {
			System.out.println("");
			System.out.println("What would you like to do?");
			System.out.println("1. Alter Outlet 1");
			System.out.println("2. Alter Outlet 2");
			System.out.println("3. Change Control Signal Pins");
			System.out.println("4. Exit");
			int choice = kybd.nextInt();
			switch (choice) {
				case 1:
					System.out.println("");
					System.out.println("Changing Outlet 1");
					System.out.println("What would you like to change?");
					System.out.println("1. Set System Type");
					System.out.println("2. Change System Parameters");
					System.out.println("3. Return to Previous Menu");
					int decision = kybd.nextInt();
					switch (decision) {
						case 1:
							System.out.println("");
							System.out.println("What System would you like to set up?");
							System.out.println("1. NFT System");
							System.out.println("2. Drip System");
							System.out.println("3. Ebb and Flow");
							System.out.println("4. Return to Previous Menu");
							int decisionSystemType = kybd.nextInt();
							initiateSystem(choice, decisionSystemType);
						case 2:
							outlet1.adjustSystemParam();
						default:
							break;
						}
					break;
				case 2:
					System.out.println("");
					System.out.println("Changing Outlet 2");
					System.out.println("What would you like to change?");
					System.out.println("1. Set System Type");
					System.out.println("2. Change System Parameters");
					System.out.println("3. Return to Previous Menu");
					int decision = kybd.nextInt();
					switch (decision) {
						case 1:
							System.out.println("");
							System.out.println("What System would you like to set up?");
							System.out.println("1. NFT System");
							System.out.println("2. Drip System");
							System.out.println("3. Ebb and Flow");
							System.out.println("4. Return to Previous Menu");
							int decisionSystemType = kybd.nextInt();
							initiateSystem(choice, decisionSystemType);
							break;
						case 2:
							outlet2.adjustSystemParam();
							break;
					}
					break;
				case 3:
					System.out.println("");
					System.out.println("Which Pin Would you like to edit?");
					System.out.println("1. Pump 1 Control Signal (Currently on Pin " + pump1pin + ")");	
					System.out.println("2. Pump 2 Control Signal (Currently on Pin " + pump2pin + ")");	
					System.out.println("3. Float Switch 1 Signal (Currently on Pin " + floatSwitch1 + ")");	
					System.out.println("4. Float Switch 2 Signal (Currently on Pin " + floatSwitch2 + ")");	
					System.out.println("5. Float Switch 3 Signal (Currently on Pin " + floatSwitch3 + ")");
					System.out.println("6. Return to Previous Menu");
					int signalEdit = kybd.nextInt();
					System.out.format("Editing Pump %d Control Signal Pin", signalEdit);
					System.out.println("What is the new pin assignment?");
					validateSignalPin(signalEdit, signalEdit);
					break;
				case 4:
					cont = false;
					break;
				default:
					cont = true;
					break;
			}
		}
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

	/**
 	* Changes the Signal Pin Assignement after Validation
 	*
 	* @param Int of the new proposed pin number, int assigning which sensor to reconfigure
 	* @return void 
 	*/
	public void changeSignalPin(int pinAssignment, int pinControlNumber) {
		switch (pinNumber) {
			case 1:
				pump1pin = pinAssignment;
				break;
			case 2:
				pump2pin = pinAssignment;
				break;
			case 3:
				floatSwitch1 = pinAssignment;
				break;
			case 4:
				floatSwitch2 = pinAssignment;
				break;
			case 5:
				floatSwitch3 = pinAssignment;
				break;
			default:
				System.out.println("Error: Did not Change Pin Assignment");
		}				
	}

    /**
    * Initiate's the system based on user input and system type
    */
	private void initiateSystem(int outletNumber, int systemType) {
		System.out.println();
		System.out.println("Which pump would you like to use?");
		System.out.println("1. Pump 1 Pin is on:" + pump1pin);
		System.out.println("2. Pump 2 Pin is on:" + pump2pin);
		System.out.println("3. Exit");
		int pumpDecision = kybd.nextInt;
		System.out.println("What pin will be used for Water Low Level Detection?");
		int waterSensorPin = sensorAssignment();
		switch (pumpDecision) {
			case 1:
				switch (systemType) {
					case 1:				
						outlet1 = new NFT(true, 1, waterSensorPin);
						break;
					case 2:
						outlet1 = new Drip(true, 1, waterSensorPin);
						break;			
					case 3:
						System.out.println("What pin will be used for High Water Detection?");
						int waterHeightPin = sensorAssignment();
						outlet1 = new EbbnFlow(true, 1, waterSensorPin, waterHeightPin);
						break;	
					default:
						break;
				}
			case 2:
				switch (systemType) {
					case 1:
						outlet2 = new NFT(true, 2, waterSensorPin);
						break;
					case 2:
						outlet2 = new Drip(true, 2, waterSensorPin);
						break;				
					case 3:
						System.out.println("What pin will be used for High Water Detection?");
						int waterHeightPin = sensorAssignment();
						outlet2 = new EbbnFlow(true, 2, waterSensorPin, waterHeightPin);
						break;	
					default:
						break;
				}
			default:
				System.out.println("Error when setting Water Level Detection Pin");
				break;		
		}
	}

    /**
    * Goes through dialogue of setting up which pin is going to be used
    * @return Sensor Pin Number that has been selected by user
    */
	private int sensorAssignment() {
		System.out.println();
		System.out.println("1. Float Switch 1 Signal (Currently on Pin " + floatSwitch1 + ")");	
		System.out.println("2. Float Switch 2 Signal (Currently on Pin " + floatSwitch2 + ")");	
		System.out.println("3. Float Switch 3 Signal (Currently on Pin " + floatSwitch3 + ")");
		int floatKeyboard = kybd.nextInt();
		int returning = 0;
			switch (floatKeyboard) {
				case 1:
					returning = floatSwitch1;
					break;
				case 2:
					returning = floatSwitch2;
					break;
				case 3:
					returning = floatSwitch3;
					break;
				default:
					System.out.println("Input not Valid");
					break;
			}
		return returning;
	}
}