const int ledPin = 13;

const int motorPin1 = 6; //green - M2
const int motorPin2 = 5; //white - M1

const int motorPin3 = 10; //grey - M1
const int motorPin4 = 9; //yellow - M2

void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
  //Serial.println("Pins Configured");
}

void loop(){
  if (Serial.available())  {
    Serial.println("Connected");
    char Command = Serial.read();
    if (Command == 'B'){
      //Serial.println("Got B");
      driveBackward();
    }
    if (Command == 'F'){
      //Serial.println("Got F");
      driveForward();
    }
    if (Command == 'L'){
      turnLeft();
    }
    if (Command == 'R'){
      turnRight();
    }
  }
}

void driveForward(){
  drive(motorPin1);
  drive(motorPin3);
  delay(250);
  motorStop(motorPin1);
  motorStop(motorPin3);
  delay(250);
  Serial.println("Finished forward");
}

void drive(int motorpin){
  analogWrite(motorpin, 50);
}

void motorStop(int motorpin){
  analogWrite(motorpin, 0);
}

void driveBackward(){
  drive(5);
  drive(9);
  delay(250);
  motorStop(5);
  motorStop(9);
  delay(250);
  Serial.println("Finished backward");
}

void turnRight(){
  drive(motorPin2);
  drive(motorPin3);
  delay(250);
  motorStop(motorPin2);
  motorStop(motorPin3);
  delay(250);
}

void turnLeft(){
  drive(motorPin1);
  drive(motorPin4);
  delay(250);
  motorStop(motorPin1);
  motorStop(motorPin4);
  delay(250);
}

/*void runMotor(){
  analogWrite(motorPin1, 100); //f
  delay(4000);
  analogWrite(motorPin1, 0);
  delay(4000);
  analogWrite(motorPin2, 100); //b
  delay(4000);
  analogWrite(motorPin2, 0);
  delay(4000);
  analogWrite(motorPin3, 100); //f
  delay(4000);
  analogWrite(motorPin3, 0);
  delay(4000);
  analogWrite(motorPin4, 100); //b
  delay(4000);
  analogWrite(motorPin4, 0);
  delay(4000);
}*/

void PleaseBlink(int numberOfTimes){
  for (int i = 0; i < numberOfTimes; i++)  {
    digitalWrite(ledPin, HIGH);
    delay(100);
    digitalWrite(ledPin, LOW);
    delay(100);
  }
  //runMotor();
}
