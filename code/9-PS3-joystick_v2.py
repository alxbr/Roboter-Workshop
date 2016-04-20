#!/usr/bin/python

import pygame
import sys
from time import sleep
import RPi.GPIO as GPIO
import wiringpi
import math

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set variables for the GPIO motor pins
pinMotorAForwards = 18
pinMotorABackwards = 17
pinMotorBForwards = 23
pinMotorBBackwards = 22

pygame.init()
while pygame.joystick.get_count() == 0:
	print "no joystick connected (wait 5 s.)"
	pygame.quit()
	sleep(5)
	pygame.init()
 
j = pygame.joystick.Joystick(0)
j.init()
print "joystick connected"

# How many times to turn the pin on and off each second
Frequency = 50
# How long the pin stays on each cycle, as a percent
DutyCycleA = 100
DutyCycleB = 100
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0
# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)
# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)
# Turn all motors off
def StopMotors():
        pwmMotorAForwards.ChangeDutyCycle(Stop)
        pwmMotorABackwards.ChangeDutyCycle(Stop)
        pwmMotorBForwards.ChangeDutyCycle(Stop)
        pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors forwards
def Forwards():
        pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
        pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors backwards
def Backwards():
        pwmMotorAForwards.ChangeDutyCycle(Stop)
        pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
        pwmMotorBForwards.ChangeDutyCycle(Stop)
        pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
# Turn left
def Left():
        pwmMotorAForwards.ChangeDutyCycle(Stop)
        pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
        pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
        pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn right
def Right():
        pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
        pwmMotorABackwards.ChangeDutyCycle(Stop)
        pwmMotorBForwards.ChangeDutyCycle(Stop)
        pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

try:
	while j.get_button(3) == 0:
		pygame.event.pump()
		sleep(0.01)
		speed = int(-100 * j.get_axis(1))
		helper = math.copysign(1, speed)
		direction = helper * int(100 * j.get_axis(0))
		if direction != 0.00 or speed != 0.00:
			motorA = max(min(100, speed + direction), -100)
			motorB = max(min(100, speed - direction), -100)
			if motorA > 0:
				pwmMotorAForwards.ChangeDutyCycle(motorA)
				pwmMotorABackwards.ChangeDutyCycle(0)
				sleep(0.01)
			elif motorA < 0:
				pwmMotorAForwards.ChangeDutyCycle(0)
				pwmMotorABackwards.ChangeDutyCycle(-motorA)			
				sleep(0.01)
			else:
				pwmMotorAForwards.ChangeDutyCycle(0)
				pwmMotorABackwards.ChangeDutyCycle(0)
				sleep(0.01)
			if motorB > 0:
				pwmMotorBForwards.ChangeDutyCycle(motorB)
				pwmMotorBBackwards.ChangeDutyCycle(0)
				sleep(0.01)
			elif motorB < 0:
				pwmMotorBForwards.ChangeDutyCycle(0)
				pwmMotorBBackwards.ChangeDutyCycle(-motorB)			
				sleep(0.01)
			else:
				pwmMotorBForwards.ChangeDutyCycle(0)
				pwmMotorBBackwards.ChangeDutyCycle(0)						
				sleep(0.01)			
#			print "Drive", helper, motorA, motorB		
		else:
			StopMotors()
			sleep(0.01)
except KeyboardInterrupt:
	GPIO.cleanup()	
	j.quit()
	sys.exit()
