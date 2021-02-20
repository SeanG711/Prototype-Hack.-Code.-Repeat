# import modules and libraries

import board
import time
import analogio

# declare analog input objects and variables
analog_in = analogio.AnalogIn(board.A1)

# repeat this code forever
while True:

    # gather input
    reading = analog_in.value



    # print output
    print(reading)


    # sleep to prevent buffer overrun
    time.sleep(0.1)