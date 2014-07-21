// bilbot.ino
//(C) Michael Moskie 2014
#include "motor.h"
#include "sensor.h"
#include <Servo.h>

//Globals for Main
String temp;
Motor right(1,true,90);
Motor left(2,true,90);
Motor hand(3,false,0);
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
//Functions
void setup() {
	Serial.begin(115200);
    inputString.reserve(200);
}

void dispatch(){
	//Basics
	if(inputString.indexOf("3") > -1){
    //Turn Right
    Serial.println("you got it");
    right.goHome();
		left.goForward();
	}

	if(inputString.indexOf("2") > -1){
    //Turn Left
    Serial.println("Yes sir");
    left.goHome();
		right.goForward();	
	}

	if(inputString.indexOf("1") > -1){
    //Go Forward
    Serial.println("proceedin");
		right.goForward();
		left.goForward();
	}
  
  if(inputString.indexOf("4") > -1){
    //Go Backward
    right.goBackward();
    left.goBackward();
  }

  if(inputString == ""){
    //We have no data, what do we do
    right.goHome();
    left.goHome();
  }

}

void loop() {
    dispatch();
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar; 
  }
}
