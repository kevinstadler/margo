import glob, os, random, time
import RPi.GPIO as GPIO
from pygame import mixer

pin = 4 # where the arduino plugs in

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

mixer.init()

usb = glob.glob("/media/pi/*")
for dir in usb:
    if os.access(dir, os.R_OK):
       os.chdir(dir)
       break

sounds = [mixer.Sound(filename) for filename in glob.glob("*.aif")]
print(f"Loaded {len(sounds)} sound(s) from directory {os.getcwd()}")

running = False
try:
    while True:
        s = 0
        for i in range(15000):
            s = s + GPIO.input(pin)
        print(s)
        # is it currently high?
        turnon = s == 15000
        # is it high, but was low previously
        if not running and turnon:
            print("playing")
            random.choice(sounds).play()
        running = turnon
finally:
    GPIO.cleanup()

