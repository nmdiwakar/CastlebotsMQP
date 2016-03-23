/**
 * Created by dmmurray on 02/01/2016.
 * The main function
 */

var b = require('bonescript');
var Motor = require('Motor');

b.main=function(){
    Motor.initPins();
    var blueMotor = new Motor(1, Motor.motor1pin1, Motor.motor1pin2, 0);
    var yellowMotor = new Motor(1, Motor.motor2pin1, Motor.motor2pin2, 0);
    b.analogWrite(blueMotor.fowardPin, 0.5, 1000, callback);
    b.analogWrite(yellowMotor.fowardPin, 0.5, 1000, callback);
    
    for (var i = 0; i < 100000; i++) {
        b.print("The value of i is: " + i);
    }
    
    b.digitalWrite(blueMotor.forwardPin, b.LOW);
    b.digitalWrite(yellowMotor.forwardPin, b.LOW);
};

function callback() {
    b.print("We did it! Yay! (Lo hicimos)");
}

b.main();

/*setup = function() {
    Motor.initPins();
};*/

/*var loop = function() {
    b.print("running...");
};*/

/*function loop() {
    b.print("running...");
}*/
 