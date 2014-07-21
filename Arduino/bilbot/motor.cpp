//motor.cpp
//Michael Moskie 2014
#include "motor.h"
#include <Servo.h>
Servo s;
Motor::Motor(int id, bool wheel, int home){
	s.attach(id+1);
	isWheel = wheel;
	myHome = home;
}


void Motor::goTo(int degree){
	s.write(degree);
	position = degree;
}

void Motor::goHome(){
	s.write(myHome);
}

void Motor::goForward(){
	//Expected functionality is to move a 360 degree rotational servo forward, or increase a non continuious servo by one.
	if(isWheel){
		s.write(myHome+10);
		return;
	}goTo(position++);
}

void Motor::goBackward(){
	if(isWheel){
		s.write(myHome-10);
		return;
	}goTo(position--);
}

void Motor::setDegree(int deg){
	s.write(deg);
}
