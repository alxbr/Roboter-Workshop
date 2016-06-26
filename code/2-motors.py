# CamJam EduKit 3 - Robotics
# Worksheet 2 - Motor Test Code
import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO Pin mode
# changed by Alex for the Ryanteck Board
GPIO.setup(17, GPIO.OUT) # right motor +
GPIO.setup(18, GPIO.OUT) # right motor -
GPIO.setup(22, GPIO.OUT) # left motor +
GPIO.setup(23, GPIO.OUT) # left motor -

print "Turn all motors off"
GPIO.output(17, 0)
GPIO.output(18, 0)
GPIO.output(22, 0)
GPIO.output(23, 0)

print "Turn the right motor forwards"
GPIO.output(17, 1)
GPIO.output(18, 0)

print "Wait for 1 second"
time.sleep(1)

print "Turn the left motor forwards"
GPIO.output(22, 1)
GPIO.output(23, 0)

print "Wait for 1 second"
time.sleep(1)

print "Reset the GPIO pins (turns off motors too)"
GPIO.cleanup()
