# import modules and libraries
import time
from math import atan2, degrees
import board

import displayio
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.triangle import Triangle
from adafruit_clue import clue
import math
from adafruit_display_text.label import Label
import terminalio



# declare objects and variables


d = 0  # direction angle
rA = 80  # arrow dimention
rB = 20  # arrow dimention
n = 0  # arrow angle

distance = 0

# buttonPre = False  # switch

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

def get_heading():
    magnet_x, magnet_y, _ = clue.magnetic
    return vector_2_degrees(magnet_x, magnet_y)


def show(distance, n):

    a0 = rA*math.cos(n*2*math.pi/360)
    b0 = rA*math.sin(n*2*math.pi/360)

    a1 = rB*math.cos((n+90)*2*math.pi/360)
    b1 = rB*math.sin((n+90)*2*math.pi/360)

    a2 = rB*math.cos((n-90)*2*math.pi/360)
    b2 = rB*math.sin((n-90)*2*math.pi/360)

    x0 = int(a0 + 120)
    y0 = int(120 - b0)

    x1 = int(a1 + 120)
    y1 = int(120 - b1)

    x2 = int(a2 + 120)
    y2 = int(120 - b2)

    display = board.DISPLAY

    clue_group = displayio.Group(max_size=4)
    outer_circle = Circle(120, 120, 95, outline=clue.WHITE)
    clue_group.append(outer_circle)

    arrow_group = displayio.Group(max_size=1)
    arrow = Triangle(x0, y0, x1, y1, x2, y2, fill=0x00FF00)
    arrow_group.append(arrow)
    clue_group.append(arrow_group)

    label_group = displayio.Group(max_size=1)
    my_label = Label(terminalio.FONT, text=str(distance), color=clue.WHITE, scale=1)

    my_label.anchor_point = (0.0, 0.0)
    my_label.anchored_position = (0, 8)
    label_group.append(my_label)
    clue_group.append(label_group)

    display.show(clue_group)
    return

# loop foerver

while True:
    d = get_heading()
    n = 90 - d
    print(d, n)
    show(d, n)
    time.sleep(0.2)
