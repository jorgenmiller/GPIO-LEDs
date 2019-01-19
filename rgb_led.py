#Raspberry Pi GPIO rgb cathode led
#lights rgb led to specified rgb 1/0 color
#red lead -> 3 parallel 410 ohm resistors -> GPIO
#3.3V -> cathode lead
#green lead -> 2 parallel 410 ohm resistors -> GPIO
#blue lead -> 410 ohm resistor -> GPIO

import RPi.GPIO as GPIO
import time

pins = {
    'redPin' : 3 ,
    'greenPin' : 7,
    'bluePin' : 5 ,
} #physical pins for anode leads

def setup(pins):
    GPIO.setmode(GPIO.BOARD) #pins identified by physical numbering system
    GPIO.setup(pins['redPin'], GPIO.OUT, initial=GPIO.HIGH) #red led starts as off
    GPIO.setup(pins['bluePin'], GPIO.OUT, initial=GPIO.HIGH) #blue led starts as off
    GPIO.setup(pins['greenPin'], GPIO.OUT, initial=GPIO.HIGH) #green led starts as off

def main(pins):
    while True:
        color = str(raw_input("rgb color? ((rgb) 1 or 0): ")) #111 white, 000 off, 010 green
        if color[0] == '1': #1 in r position
            GPIO.output(pins['redPin'], GPIO.LOW) #red led on
        else:
            GPIO.output(pins['redPin'], GPIO.HIGH) #red led off
        if color[1] == '1': #1 in g position
            GPIO.output(pins['greenPin'], GPIO.LOW) #green led on
        else:
            GPIO.output(pins['greenPin'], GPIO.HIGH) #green led off
        if color[2] == '1': #1 in b position
            GPIO.output(pins['bluePin'], GPIO.LOW) #blue led on
        else:
            GPIO.output(pins['bluePin'], GPIO.HIGH) #blue led off

try:
    setup(pins)
    main(pins)

finally: #before quitting due to error
    print("exiting")
    GPIO.cleanup() #undo pin asignments
