#include "UnoJoy.h"
#include <Wire.h>

#define SLAVE_ADDRESS 0x05

int byteCount = 0;
char temp[32];
int led = 13;
int ledState = 0;

#define numberOfDigits 3
char theNumberString[numberOfDigits + 1];

int triangleOn = 0;
int circleOn = 0;
int squareOn = 0;
int crossOn = 0;
int dpadUpOn = 0;
int dpadDownOn = 0;
int dpadLeftOn = 0;
int dpadRightOn = 0;
int l1On = 0;
int l2On = 0;
int l3On = 0;
int r1On = 0;
int r2On = 0;
int r3On = 0;
int selectOn = 0;
int startOn = 0;
int homeOn = 0;
int leftStickX = 128;
int leftStickY = 128;
int rightStickX = 128;
int rightStickY = 128;
int digit0 = 1;
int digit1 =  2;
int digit2 =  8;


void setup(){
  setupUnoJoy();
  //Serial.begin();
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
}

void receiveData(int byteCount) {
    while ( Wire.available()) {
      for (int i = 0; i < byteCount; i++) {
        temp[i] = Wire.read();
        temp[i + 1] = '\0';
      }
      for (int i = 0; i < byteCount; ++i)
        temp[i] = temp[i + 1];

      if ( byteCount > 3){
        int digit0 = temp[1];
        int digit1 =  temp[2];
        int digit2 =  temp[3];
        theNumberString[0] = digit0;
        theNumberString[1] = digit1;
        theNumberString[2] = digit2;
        theNumberString[3] = 0x00;
      }
      if (temp[0] == '*') {
        Wire.flush();
        forceReset();
      }
      else if (temp[0] == 'T') {
        triangleOn = temp[1];
      }
      else if (temp[0] == 'O') {
        circleOn = temp[1];
      }
      else if (temp[0] == 'S') {
        squareOn = temp[1];
      }
      else if (temp[0] == 'X') {
        crossOn = temp[1];
      }
      else if (temp[0] == 'U') {
        dpadUpOn = temp[1];
      }
      else if (temp[0] == 'D') {
        dpadDownOn = temp[1];
      }
      else if (temp[0] == 'F') {
        dpadLeftOn = temp[1];
      }
      else if (temp[0] == 'G') {
        dpadRightOn = temp[1];
      }
      else if (temp[0] == '[') {
        l1On = temp[1];
      }
      else if (temp[0] == '{') {
        l2On = temp[1];
      }
      else if (temp[0] == '<') {
        l3On = temp[1];
      }
      else if (temp[0] == ']') {
        r1On = temp[1];
      }
      else if (temp[0] == '}') {
        r2On = temp[1];
      }
      else if (temp[0] == '>') {
        r3On = temp[1];
      }
      else if (temp[0] == 'Z') {
        selectOn = temp[1];
      }
      else if (temp[0] == 'Y') {
        startOn = temp[1];
      }
      else if (temp[0] == 'P') {
        Serial.print("home");
        homeOn = temp[1];
      }
      else if (temp[0] == 'L') {
        leftStickX = atoi(theNumberString);

      }
      else if (temp[0] == 'l') {
        leftStickY = atoi(theNumberString);
      }
      else if (temp[0] == 'R') {
        rightStickX = atoi(theNumberString);

      }
      else if (temp[0] == 'r') {
        rightStickY = atoi(theNumberString);

      }
      dataForController_t controllerData = getControllerData();
      setControllerData(controllerData);
      digitalWrite(13, LOW);
    }
}


dataForController_t getControllerData(void){
  dataForController_t controllerData = getBlankDataForController();
  controllerData.triangleOn = triangleOn;
  controllerData.circleOn = circleOn;
  controllerData.squareOn = squareOn;
  controllerData.crossOn = crossOn;
  controllerData.dpadUpOn = dpadUpOn;
  controllerData.dpadDownOn = dpadDownOn;
  controllerData.dpadLeftOn = dpadLeftOn;
  controllerData.dpadRightOn = dpadRightOn;
  controllerData.l1On = l1On;
  controllerData.l2On = l2On;
  controllerData.l3On = l3On;
  controllerData.r1On = r1On;
  controllerData.r2On = r2On;
  controllerData.r3On = r3On;
  controllerData.selectOn = selectOn;
  controllerData.startOn = startOn;
  controllerData.homeOn = homeOn;

  controllerData.leftStickX = leftStickX;
  controllerData.leftStickY = leftStickY;
  controllerData.rightStickX = rightStickX;
  controllerData.rightStickY = rightStickY;

  // And return the data!
  return controllerData;
}

void forceReset() {
  triangleOn = 0;
  circleOn = 0;
  squareOn = 0;
  crossOn = 0;
  dpadUpOn = 0;
  dpadDownOn = 0;
  dpadLeftOn = 0;
  dpadRightOn = 0;
  l1On = 0;
  l2On = 0;
  l3On = 0;
  r1On = 0;
  r2On = 0;
  r3On = 0;
  selectOn = 0;
  startOn = 0;
  homeOn = 0;
  leftStickX = 128;
  leftStickY = 128;
  rightStickX = 128;
  rightStickY = 128;
}

void loop() {
}