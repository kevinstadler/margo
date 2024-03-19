#include <Adafruit_MotorShield.h>
#include <Wire.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

Adafruit_DCMotor *myMotor = AFMS.getMotor(1);
void setup() {
  AFMS.begin(1000);  
 
}

void loop() {
 myMotor->setSpeed(255);
  myMotor->run(FORWARD);
  delay(2500);
  myMotor->setSpeed(0);
  myMotor->run(FORWARD);
  delay(2700);
}
