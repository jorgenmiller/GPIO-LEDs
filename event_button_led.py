#Raspberry Pi GPIO buton activated led (event based)
#led turns on the first time a button is pressed
#B18 -> led -> 200 ohm resistor -> ground
#3.3V -> button -> 10K ohm resistor -> B17

import RPi.GPIO as GPIO

def button_pushed(event): #receives information about event
    if GPIO.input(18) == 0: #if led is off
        GPIO.output(18, GPIO.HIGH)
    else: #if led is on
        GPIO.output(18, GPIO.LOW)

def setup():
    GPIO.setmode(GPIO.BCM) #BCM pin numbering
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(17, GPIO.RISING, callback=button_pushed) #call button_pushed on rising edge (button pushed)
    GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

try:
    setup()
    message = raw_input("Press ENTER to quit") #wait for user while listening for button

finally:
    print("exiting")
    GPIO.cleanup()
