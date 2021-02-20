# import modules and libraries

import board
import time
import analogio
import neopixel
from simpleio import map_range

# declare neopixel object with onboard neopixel pin
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare analog input objects and variables
analog_in1 = analogio.AnalogIn(board.A1)
analog_in2 = analogio.AnalogIn(board.LIGHT)

# create a color variable and fill the pisels with the color
color = (0, 0, 0)
pixels.fill(color)

smooth_val = snalog_in.value

# make a functon to do a weighted average
def weightedSmooth(in_val, weight)
    # weight is a float between 0.0 and 1.0
    #in_val is the current reading




# repeat this code forever
while True:

    # gather input
    reading1 = analog_in1.value
    reading2 = analog_in2.value
    # do calculation
    scaled_val1 = map_range(reading1, 0, 65535, 0, 255)
    scaled_val2 = map_range(reading2, 2000, 62000, 0, 255)
    print(scaled_val1, scaled_val2)

    # set new color value
    color = (0, scaled_val1, scaled_val2)

    # do output
    pixels.fill(color)

    # sleep to prevent buffer overrun
    time.sleep(0.1)