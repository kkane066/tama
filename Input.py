#!/usr/bin/python
import RPi.GPIO as GPIO
import subprocess
import os
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
input = GPIO.input(17)

while True:
    if (GPIO.input(17)):
        print("Camera Works")
        os.system("python /home/pi/Desktop/camera.py")
    
    else:
        print("Camera doesn't work")
