# test ui
import board
import displayio
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.triangle import Triangle
from adafruit_clue import clue
import math
from adafruit_display_text.label import Label
import terminalio

rA = 80
rB = 20
n = 45

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
my_label = Label(terminalio.FONT, text="My Label Text", color=clue.WHITE, scale=1)


my_label.anchor_point = (0.0, 0.0)
my_label.anchored_position = (0, 8)
label_group.append(my_label)
clue_group.append(label_group)


display.show(clue_group)


while True:
    pass
