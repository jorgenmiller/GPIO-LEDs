#Raspberry Pi GPIO led rave
#flashes through multiple leds
#GPIO -> led -> 410 ohm resistor -> ground

import RPi.GPIO as GPIO
import time

gpio_pins = [11, 12, 13, 15, 16, 18, 38, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37] #pins for leds, in order

def setup(gpio_pins):
    GPIO.setmode(GPIO.BOARD) #pins identified by physical numbering system
    GPIO.setup(gpio_pins, GPIO.OUT, initial=GPIO.LOW) #all leds starts as off

def main(gpio_pins):
    while True:
        for n in range(0, len(gpio_pins)-1, 1): #move down the line
            GPIO.output(gpio_pins[n], GPIO.HIGH) #led on
            time.sleep(.1)
            GPIO.output(gpio_pins[n], GPIO.LOW) #led off, comment out for bouncing progress bar
            time.sleep(.01)
        for n in range(len(gpio_pins)-1, 0, -1): #go the other way
            GPIO.output(gpio_pins[n], GPIO.HIGH) #led on
            time.sleep(.1)
            GPIO.output(gpio_pins[n], GPIO.LOW) #led off
            time.sleep(.01)
try:
    setup(gpio_pins)
    main(gpio_pins)

finally: #before quitting due to error
    print("exiting")
    GPIO.cleanup() #undo pin asignments
