#!/usr/bin/python

import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27,GPIO.OUT)

print GPIO.input(17)
while True:
	if ( GPIO.input(17) == False ):
		print("Button Pressed")
		os.system('date')
		print GPIO.input(17)
		GPIO.output(27,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(27,GPIO.LOW)
	else:
		os.system('clear')
		print ("Waiting for you to press a button")
time.sleep(1)

