# import modules and libraries

import board
import time
from digitalio import DigitalInOut, Direction, Pull

# declare objects and variables
led = DigitalInOut(board.A3)
led.direction = Direction.OUTPUT
ledMode = 0

button = DigitalInOut(board.A1)
button.direction = Direction.INPUT
button.pull = Pull.UP
buttonPre = True

blinkInterval = 0.25
blinkTime = time.monotonic() + blinkInterval


# loop foerver
while True:
    # gather input
    # see if the button has changed
    if button.value != buttonPre:
        # reset the previous value
        buttonPre = button.value
        if not button.value:
            ledMode += 1
            if ledMode > 2:
                ledMode = 0

    # do output based on mode
    if ledMode == 1:
        blinkInterval = 0.6
        # check if it is time to change the led
        if time.monotonic() >= blinkTime:

            # toggle led value
            led.value = not led.value

            # increament
            blinkTime += blinkInterval

    elif ledMode == 2:
        blinkInterval = 0.2
        # check if it is time to change the led
        if time.monotonic() >= blinkTime:

            # toggle led value
            led.value = not led.value

            # increament
            blinkTime += blinkInterval

    else:
        led.value = False
        blinkTime = time.monotonic()