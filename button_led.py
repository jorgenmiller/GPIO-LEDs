#Raspberry Pi GPIO buton activated led (continous polling)
#led turns on when button pressed
#B18 -> led -> 200 ohm resistor -> ground
#3.3V -> button -> 10K ohm resistor -> B17

import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM) #BCM pin numbering
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pin 17 is input and is set to off when button not pressed
    GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

def main():
    while True:
        if GPIO.input(17) == GPIO.HIGH: #button pressed
            GPIO.output(18, GPIO.HIGH)
        else: #button not pressed
            GPIO.output(18,GPIO.LOW)
        time.sleep(.1)

try:
    setup()
    main()

finally:
    print("exiting")
    GPIO.cleanup()
