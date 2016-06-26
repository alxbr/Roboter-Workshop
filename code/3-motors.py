#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# CamJam EduKit 3 - Robotics
# Worksheet 3 – Driving and Turning
import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
# changed by Alex for the Ryanteck Board
pinMotorAForwards = 17	# right motor +
pinMotorABackwards = 18	# right motor -
pinMotorBForwards = 22	# left motor +
pinMotorBBackwards = 23	# left motor -

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off
def StopMotors():
	GPIO.output(pinMotorAForwards, 0)
	GPIO.output(pinMotorABackwards, 0)
	GPIO.output(pinMotorBForwards, 0)
	GPIO.output(pinMotorBBackwards, 0)
    
# Turn both motors forwards
def Forwards():
	GPIO.output(pinMotorAForwards, 1)
	GPIO.output(pinMotorABackwards, 0)
	GPIO.output(pinMotorBForwards, 1)
	GPIO.output(pinMotorBBackwards, 0)
    
# Turn both motors backwards
def Backwards():
	GPIO.output(pinMotorAForwards, 0)
	GPIO.output(pinMotorABackwards, 1)
	GPIO.output(pinMotorBForwards, 0)
	GPIO.output(pinMotorBBackwards, 1)
	
# Turn left
def Right():
	GPIO.output(pinMotorAForwards, 0)
	GPIO.output(pinMotorABackwards, 1)
	GPIO.output(pinMotorBForwards, 1)
	GPIO.output(pinMotorBBackwards, 0)
    
# Turn Right
def Left():
	GPIO.output(pinMotorAForwards, 1)
	GPIO.output(pinMotorABackwards, 0)
	GPIO.output(pinMotorBForwards, 0)
	GPIO.output(pinMotorBBackwards, 1)

print "Turn both motors forwards for one second"
Forwards()
time.sleep(1) # Pause for 1 second

print "Turn left for one second"
Left()
time.sleep(1) # Pause for half a second

print "Turn both motors forwards for one second"
Forwards()
time.sleep(1)

print "Turn right for one second"
Right()
time.sleep(1)

print "Turn both motors backwards for one second"
Backwards()
time.sleep(1)

print "Stop"
StopMotors()
GPIO.cleanup()
