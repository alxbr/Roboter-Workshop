#!/usr/bin/python

import pygame
import sys
from time import sleep
import RPi.GPIO as GPIO
import wiringpi

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set variables for the GPIO motor pins
pinMotorAForwards = 18
pinMotorABackwards = 17
pinMotorBForwards = 23
pinMotorBBackwards = 22

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
if j.get_init():
	print "Joystick connected"

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
		print j.get_button(4)," ", j.get_button(5), " ", j.get_button(6), " ", j.get_button(7), " ", j.get_axis(1)
		sleep(1)
		pygame.event.pump()
		if j.get_axis(1) == 0.00:
			StopMotors()
			sleep(0.01)
#			print "Stop"
		elif j.get_axis(1) != 0.00:
#			DutyCycleA = 100 * j.get_axis(1)
#			DutyCycleB = 100 * j.get_axis(1)
			sleep(0.01)			
			print DutyCycleA
			if j.get_button(4) != 0 :	#VOR	
				Forwards()
#				print "Vor"
				sleep(0.01)
			elif j.get_button(5) != 0  :	#RECHTS
				Right()
#				print "Rechts"
				sleep(0.01)			
			elif j.get_button(7) != 0	:	#LINKS
				Left()
#				print "Links"
				sleep(0.01)			
			elif j.get_button(6) != 0	:	#ZURUECK
				Backwards()
#				print "Zurueck"
				sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()	
	j.quit()
	sys.exit()
