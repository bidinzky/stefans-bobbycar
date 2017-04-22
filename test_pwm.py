#!/usr/bin/env python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([10,9,11,25,8,7],GPIO.OUT)
r1 = GPIO.PWM(10,50)
b1 = GPIO.PWM(9,50)
g1 = GPIO.PWM(11,50)

r2 = GPIO.PWM(25,50)
b2 = GPIO.PWM(8,50)
g2 = GPIO.PWM(7,50)
r1.start(50)
b1.start(50)
g1.start(50)

r2.start(50)
b2.start(50)
g2.start(50)
while 1==1:
	input()
