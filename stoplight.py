#Raspberry Pi GPIO led stoplight
#runs through a stop light pattern (green, yellow, red)
#B27 -> green led -> 200 ohm resistor -> ground
#B18 -> yellow led -> 200 ohm resistor -> ground
#B17 -> red led -> 200 ohm resistor -> ground

import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM)
    led_pins = [17,18,27]
    GPIO.setup(led_pins,GPIO.OUT,initial=GPIO.LOW) #initialize all 3 pins

def main():
    while True:
        GPIO.output(27,GPIO.HIGH) #green led
        time.sleep(4)
        GPIO.output(27,GPIO.LOW)

        GPIO.output(18,GPIO.HIGH) #yellow led
        time.sleep(2)
        GPIO.output(18,GPIO.LOW)

        GPIO.output(17,GPIO.HIGH) #red led
        time.sleep(4)
        GPIO.output(17,GPIO.LOW)

try:
    setup()
    main()

finally:
    print("exiting")
    GPIO.cleanup()
