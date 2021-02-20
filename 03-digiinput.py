import board
import time
from digitalio import DigitalInOut, Direction

switch = DigitalInOut(board.A1)
switch.direction = Direction.INPUT

while True:
    print(switch.value)
    time.sleep(0.2)