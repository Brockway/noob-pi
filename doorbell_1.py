#!/usr/bin/python

import os
import time
import RPi.GPIO as GPIO
from mutagen.mp3 import MP3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)

def rndmp3 ():
	filename = random.choice(os.listdir("/opt/DoorbellChimes"))
	chime = '/opt/DoorbellChime' + filename

while True:
	if ( GPIO.input(17) == False ):
		rndmp3()
		os.system('date')
		sleeptime = int(round(audio.info.length))
		os.system('omxplayer -o alsa' + filename)
		time.sleep(sleeptime)
time.sleep(1)
