//motor.h
//Michael Moskie 2014
#ifndef MOTOR_H
#define MOTOR_H
#include "Arduino.h"
class Motor{
	public:
		Motor(int id, bool wheel, int home); //Expects ID to be the motor ID from the PCB
		void goTo(int degree); //Expects degree to move motor to.
		void goHome(); //Returns to 0, or other defined variable for home.
		void goForward();
		void goBackward();
		void setDegree(int deg);
	
	private:
		int myHome;
		int position;
		int direction;
		bool isWheel;
};
#endif
