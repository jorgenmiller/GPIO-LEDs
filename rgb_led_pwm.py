#Raspberry Pi GPIO cathode rgb led pwm
#lights rgb led of variable color with pwm
#GPIO -> red lead -> 2 parallel 410 ohm resistors
#3.3V -> cathode lead
#GPIO -> green lead -> 410 ohm resistor
#GPIO -> blue lead -> 410 ohm resistor

import RPi.GPIO as GPIO
import time
from threading import Thread

pins = {
    'redPin' : 3 ,
    'greenPin' : 7,
    'bluePin' : 5 ,
} #physical pins for anode leads

GPIO.setmode(GPIO.BOARD) #pins identified by physical numbering system
GPIO.setwarnings(False)
GPIO.setup(pins['redPin'], GPIO.OUT, initial=GPIO.HIGH) #led starts as off
GPIO.setup(pins['bluePin'], GPIO.OUT, initial=GPIO.HIGH) #led starts as off
GPIO.setup(pins['greenPin'], GPIO.OUT, initial=GPIO.HIGH) #led starts as off
red = GPIO.PWM(pins['redPin'], 100) #star pwm at 100Hz
green = GPIO.PWM(pins['greenPin'], 100)
blue = GPIO.PWM(pins['bluePin'], 100)

def main(pins, red, green, blue):
    red.start(100) #100% of cycle applyig voltage, starts as off
    green.start(100)
    blue.start(100)
    while True:
        redColor = int(input('red 0-100: ')) #ask for individual rgb
        greenColor = int(input('green 0-100: '))
        blueColor = int(input('blue 0-100: '))
        red.ChangeDutyCycle(100 - redColor) #change active percents, inverse due to 3.3V->cathode
        green.ChangeDutyCycle(100 - greenColor)
        blue.ChangeDutyCycle(100 - blueColor)
        print()

try:
    main(pins, red, green, blue)

finally: #before quitting due to error
    print("exiting")
    red.stop() #stop pwm
    blue.stop()
    green.stop()
    GPIO.cleanup() #undo pin asignments
