/**
 * Created by dmmurray on 01/26/16.
 * The motor class
 */
 
 var b = require('bonescript');
 
 //var P8_34 = GPIO63; /*global GPIO63*/ // EHRPWM1B
 //var P8_36 = GPIO37; /*global GPIO37*/ // EHRPWM1A
 //var P8_45 = GPIO70; /*global GPIO70*/ // EHRPWM2A
 //var P8_46 = GPIO71; /*global GPIO71*/ // EHRPWM2B or not 2b
 var motor1pin1 = "P8_34";
 var motor1pin2 = "P8_36";
 var motor2pin1 = "P8_45";
 var motor2pin2 = "P8_46";
 
/**
 * Makes a motor
 * @constructor
 * @param portnum, the motor's port number
 * @param forwardPin, the number of the pin for forward motion
 * @param backwardPin, the number of the pin for backward motion
 * @param reversed, flag for reversal of one motor
 * @param encoder, the encoder attached to this motor
 */
function Motor(portnum, forwardPin, backwardPin, reversed, encoder) {
    this.portnum = portnum;
    //this.speed = 0;
    this.forwardPin = forwardPin;
    b.pinMode(this.forwardPin, b.OUTPUT);
    this.backwardPin = backwardPin;
    b.pinMode(this.backwardPin, b.OUTPUT);
    this.reversed = reversed;
    this.encoder = encoder;
}

/**
 * Stops the motor
 */
Motor.prototype.stop = function() {
    this.speed = 0;
};

/**
 * Drives the motor at the given speed in the given direction for the given
 * distance
 * @param speed, the motor's speed
 * @param distance, the distance for the motor to drive
 * @param direction, the direction for the motor to drive
 */
Motor.prototype.drive = function(speed, distance, direction) {
    var time = 1000 * distance / speed;
    if (direction == "forward") {
        // set forward pin to speed
        //b.pinMode(this.forwardPin, b.OUTPUT);
        b.digitalWrite(this.forwardPin, b.HIGH);
        b.analogWrite(this.fowardPin, 0.5, 1000, callback);
    }
    else if (direction == "backward") {
        // set backward pin to speed
        //b.pinMode(this.backwardPin, b.OUTPUT);
        b.digitalWrite(this.backwardPin, b.HIGH);
    }
    else {
        console.log("direction must be forward or backward");
        return;
    }
    setTimeout(this.stop(), time);
};

var callback = 4;

/**
 * Initializes the motor pins
 */
 Motor.prototype.initPins = function() {
     b.digitalWrite(motor1pin1, b.LOW);
     b.digitalWrite(motor1pin2, b.LOW);
     b.digitalWrite(motor2pin1, b.LOW);
     b.digitalWrite(motor2pin2, b.LOW);
 };
