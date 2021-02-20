# import modules and libraries

import board
import time
from digitalio import DigitalInOut, Direction, Pull

# declare objects and variables
led = DigitalInOut(board.A3)
led.direction = Direction.OUTPUT

button = DigitalInOut(board.A1)
button.direction = Direction.INPUT
button.pull = Pull.UP

blinkInterval = 0.4
blinkTime = time.monotonic() + blinkInterval


# loop foerver
while True:
    if button.value:
        led.value = False
        blinkTime = time.monotonic()
    else:
        # check if it is time to change the led
        if time.monotonic() >= blinkTime:

            # toggle led value
            led.value = not led.value

            # increament
            blinkTime += blinkInterval