# import modules
import board
from digitalio import DigitalInOut, Direction
import time

# declare object and variables

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# variables for blinking
onTime = 0.5
offTime = 0.25

# loop forever
while True:
    # turn the led on
    led.value = True
    time.sleep(onTime)
    # turn the led off
    led.value = False
    time.sleep(offTime)