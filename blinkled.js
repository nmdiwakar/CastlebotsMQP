var b = require('bonescript');
var led = "USR3";
var state = 0;

b.pinMode(led, 'out');
var toggleLED = function() {
    state = state ? 0 : 1;
    b.digitalWrite(led, state);
};

var timer = setInterval(toggleLED, 100);

var stopTimer = function() {
    clearInterval(timer);
};

setTimeout(stopTimer, 3000);