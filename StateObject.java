/**
* A Class Used to Control the State of Threads
* @author ESW
* @version 1
*
* The state object can be used to terminate threads from other threads
* since the continuing/terminating condition is contained within the boolean
* of the state object
*/
public class StateObject {
	boolean condition;

	public StateObject(boolean cond) {
		condition = cond;
	}

	public void setTrue() {
		condition = true;
	}

	public void setFalse() {
		condition = false;
	}

	public boolean checkState() {
		return condition;
	}
}