#!/usr/bin/env python
# Written by Limor "Ladyada" Fried for Adafruit Industries, (c) 2015
# This code is released into the public domain
import time
import os
import RPi.GPIO as GPIO

store_mic_audio = []
store_mic_env = []
store_mic_gate = []

GPIO.setmode(GPIO.BCM)
DEBUG = 1

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
	if ((adcnum > 7) or (adcnum < 0)):
		return -1
	GPIO.output(cspin, True)

	GPIO.output(clockpin, False) # start clock low
	GPIO.output(cspin, False) # bring CS low

	commandout = adcnum
	commandout |= 0x18 # start bit + single-ended bit
	commandout <<= 3 # we only need to send 5 bits here

	for i in range(5):
		if (commandout and 0x80):
			GPIO.output(mosipin, True)
		else:
			GPIO.output(mosipin, False)
		commandout <<= 1
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)

	adcout = 0

	# read in one empty bit, one null bit and 10 ADC bits
	for i in range(12):
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)
		adcout <<= 1
		if (GPIO.input(misopin)):
			adcout |= 0x1

	GPIO.output(cspin, True)

	adcout >>= 1 # first bit is 'null' so drop it
	return adcout

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

# Analog rep of wave connected to adc #0
mic_audio = 0;		
# Analog voltage of amplitude connected to adc #1
mic_envelope = 1;
# Binary representation of presence connected to adc #2
mic_gate = 2;

#last_read = 0 # this keeps track of the last potentiometer value
tolerance = 5 # to keep from being jittery we'll only report when the reading has changed 5+

while True:

	# we'll assume that the mic didn't move
	audio_changed = False
	envelope_changed = False
	gate_changed = False
	# read the analog pin
	audio_output = readadc(mic_audio, SPICLK, SPIMOSI, SPIMISO, SPICS)
	envelope_output = readadc(mic_envelope, SPICLK, SPIMOSI, SPIMISO, SPICS)
	gate_output = readadc(mic_gate, SPICLK, SPIMOSI, SPIMISO, SPICS)
	# how much has it changed since the last read?
	audio_adjust = abs(audio - audio_last_read)
	envelope_adjust = abs(envelope - env_last_read)
	gate_adjust = abs(gate - gate_last_read)

	if DEBUG:
		print "mic_audio:", audio
		print "mic_envelope:", envelope
		print "mic_gate:", gate

	if ( audio_adjust > tolerance ):
		audio_changed = True

	if ( envelope_adjust > tolerance ):
		envelope_changed = True

	if ( gate_adjust != 0 ):
		gate_changed = True


	# save the potentiometer reading for the next loop
	audio_last_read = audio
	env_last_read = envelope
	gate_last_read = gate

	store_mic_audio.append(audio)
	store_mic_env.append(envelope)
	store_mic_gate.append(gate)
	
# hang out and do nothing for a half second
time.sleep(0.5)

# USE ALL THREE TO START DETECTION
# WHEN AMPLITUDE DROPS, END SAMPLING

if (audio_changed and gate_changed and envelope_changed):
	reading = 1;
	
