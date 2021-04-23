import time
from math import atan2, degrees
from adafruit_clue import clue

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

def get_heading():
    magnet_x, magnet_y, _ = clue.magnetic
    return vector_2_degrees(magnet_x, magnet_y)

while True:
    print("heading: {:.2f} degrees".format(get_heading()))
    time.sleep(0.2)