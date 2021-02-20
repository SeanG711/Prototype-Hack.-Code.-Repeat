# import modules
import board
from digitalio import DigitalInOut, Direction
import time

# declare object and variables

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# variables for blinking
onTime_dot = 0.3
onTime_dash = 1
offTime = 0.2

# loop forever
while True:
    # sos
    led.value = True
    time.sleep(onTime_dot)
    led.value = False
    time.sleep(offTime)
    led.value = True
    time.sleep(onTime_dot)
    led.value = False
    time.sleep(offTime)
    led.value = True
    time.sleep(onTime_dot)
    led.value = False
    time.sleep(offTime)

    led.value = True
    time.sleep(onTime_dash)
    led.value = False
    time.sleep(offTime)
    led.value = True
    time.sleep(onTime_dash)
    led.value = False
    time.sleep(offTime)
    led.value = True
    time.sleep(onTime_dash)
    led.value = False
    time.sleep(offTime)

    led.value = True
    time.sleep(onTime_dot)
    led.value = False
    time.sleep(offTime)
    led.value = True
    time.sleep(onTime_dot)
    led.value = False
    time.sleep(offTime)
    led.value = True
    time.sleep(onTime_dot)
    led.value = False
    time.sleep(offTime*2)

