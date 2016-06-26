#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinMotorAForwards = 17
pinMotorABackwards = 18
pinMotorBForwards = 22
pinMotorBBackwards = 23
pinLineFollowerL = 9 # left sensor
pinLineFollowerR = 25 # right sensor
Frequency = 50
DutyCycleA = 100
DutyCycleB = 100
Stop = 0
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
GPIO.setup(pinLineFollowerR, GPIO.IN)
GPIO.setup(pinLineFollowerL, GPIO.IN)
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)
def StopMotors():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
def Forwards():
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
def Backwards():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
def Right():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
def Left():
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
def Line():
	if GPIO.input(pinLineFollowerR) == 0 and GPIO.input(pinLineFollowerL) == 0:
		print "Line detected by both sensors: L=", GPIO.input(pinLineFollowerL), " ,R=", GPIO.input(pinLineFollowerR), " go back"
		Backwards()
		time.sleep(0.25)
	while GPIO.input(pinLineFollowerR) == 0:
		#print "Line detected by the right sensor: L=", GPIO.input(pinLineFollowerL), " ,R=", GPIO.input(pinLineFollowerR), " turn left"
		Left()
	while GPIO.input(pinLineFollowerL) == 0:
                #print "Line detected by the left sensor: L=", GPIO.input(pinLineFollowerL), " ,R=", GPIO.input(pinLineFollowerR), " turn right"
		Right()
	return True
try:
	while Line() == True:
		if GPIO.input(pinLineFollowerR) == 1 and GPIO.input(pinLineFollowerL) == 1: Forwards()
except KeyboardInterrupt: StopMotors()
GPIO.cleanup()
