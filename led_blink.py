#Raspberry Pi GPIO led blink
#flashes led for 1 second
#B17 -> led -> 200 ohm resistor -> ground

import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM) #pins identified by BCM numbering system
    GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) #led starts as off

def main():
    while True:
        GPIO.output(17, GPIO.HIGH) #led on
        time.sleep(1)

        GPIO.output(17, GPIO.LOW) #led off
        time.sleep(1)

try:
    setup()
    main()

finally: #before quitting due to error
    print("exiting")
    GPIO.cleanup() #undo pin asignments
