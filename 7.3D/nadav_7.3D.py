from time import sleep
from gpiozero import DistanceSensor
from gpiozero import PWMLED
from signal import signal, pause
import keyboard
import sys
import RPi.GPIO as GPIO

Variable_LED=PWMLED(18)
sensor = DistanceSensor(echo=17, trigger=4 )

try:
    while True:       
        Variable_LED.on()
        Dist= sensor.value
        print(f'Distance {Dist :1.2f} M')
        distance = round(1.0 - Dist,1)            
        if distance < 0:
            distance = 0.0
        Variable_LED.value = distance
        sleep(0.1)
        
except KeyboardInterrupt:
    print("Cleaning up!")
    sys.exit(0)