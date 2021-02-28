# Use a Potentiometer or a LDR light sensor to change the brightness of your neopixels.

# import modules and libraries

import board
import time
import analogio
import neopixel


# declare neopixel object with onboard neopixel pin
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare analog input objects and variables
analog_in = analogio.AnalogIn(board.A1)

# create a color variable and fill the pisels with the color
color = (0, 0, 0)
pixels.fill(color)


# repeat this code forever
while True:

    # gather input
    reading = analog_in.value

    # do calculation
    scaled_val = reading >> 8
    print(scaled_val)

    # set new color value
    color = (0, scaled_val, scaled_val)

    # do output
    pixels.fill(color)

    # sleep to prevent buffer overrun
    time.sleep(0.1)