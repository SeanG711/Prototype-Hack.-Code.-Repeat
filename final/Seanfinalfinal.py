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
import adafruit_gps


# declare objects and variables

# list of coordinates (target = [latitude, longitude])
t0 = [34.147195, -118.102073]  # Vons
t1 = [34.145869, -118.094245]  # Shell
t2 = [34.128910, -118.114172]  # HuntingtonLib
t3 = [34.127797, -118.147915]  # SouthCampus
t4 = [34.105209, -118.094296]  # SanGabGolfCourse
Lati_list = [t0[0], t1[0], t2[0], t3[0], t4[0]]
Long_list = [t0[1], t1[1], t2[1], t3[1], t4[1]]

# current location
LongCurrent = -118.100708
LatiCurrent = 34.140682

# for calculation
distance = [0, 0, 0, 0, 0]
bearing = [0, 0, 0, 0, 0]
a = [0, 0, 0, 0, 0]
c = [0, 0, 0, 0, 0]
e = [0, 0, 0, 0, 0]
f = [0, 0, 0, 0, 0]
g = [0, 0, 0, 0, 0]
R = 3958.8  # radious of earth in miles
Delta_lati = [0, 0, 0, 0, 0]
Delta_long = [0, 0, 0, 0, 0]

# gps
i2c = board.I2C()
gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False)  # Use I2C interface
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")
last_print = time.monotonic()

# for ui
d = 0  # direction angle
rA = 80  # arrow dimention
rB = 20  # arrow dimention
n = 0  # arrow angle
n_list = [0, 0, 0, 0, 0]
number = 0
t = 1

# button
buttonPre = False  # switch


# angle
def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

def get_heading():
    magnet_x, magnet_y, _ = clue.magnetic
    return vector_2_degrees(magnet_x, magnet_y)

# draw the arrow
def show(number, n):

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
    my_label = Label(terminalio.FONT, text=str(number), color=clue.WHITE, scale=1)

    my_label.anchor_point = (0.0, 0.0)
    my_label.anchored_position = (0, 8)
    label_group.append(my_label)
    clue_group.append(label_group)

    display.show(clue_group)
    return

# loop foerver
while True:

    d = get_heading()   # get compass direction
    gps.update()
    current = time.monotonic()

    if current - last_print >= 1.0:
        last_print = current
        LongCurrent = gps.longitude    # update location
        LatiCurrent = gps.latitude
        if not gps.has_fix:
            print("Waiting for fix...")
            continue
        # print(LatiCurrent)
        # print(LongCurrent)
    if clue.button_b != buttonPre:    # toggle
        buttonPre = clue.button_b
        if clue.button_b:
            t += 1

    # calculate
    for i in range(5):
        # calculate distances
        Delta_lati[i] = (Lati_list[i] - LatiCurrent)*math.pi/180
        Delta_long[i] = (Long_list[i] - LongCurrent)*math.pi/180
        a[i] = math.sin(Delta_lati[i]/2) * math.sin(Delta_lati[i]/2)
        + math.cos(LatiCurrent*math.pi/180) * math.cos(Lati_list[i]*math.pi/180) * math.sin(Delta_long[i]/2) * math.sin(Delta_long[i]/2)
        c[i] = 2 * math.atan2(math.sqrt(a[i]), math.sqrt(1-a[i]))
        distance[i] = R * c[i]

        # calculate bearings
        e[i] = math.sin(Long_list[i]-LongCurrent)*math.cos(Lati_list[i])
        f[i] = math.cos(LatiCurrent)*math.sin(Lati_list[i])-math.sin(LatiCurrent)*math.cos(Lati_list[i])*math.cos(Long_list[i]-LongCurrent)
        g[i] = math.atan2(e[i], f[i])
        bearing[i] = (g[i]*180/math.pi+360) % 360


        n_list[i] = 90 - d + bearing[i]    # match bearings with arrow
        n = n_list[t % 5]  # get an angle for ui
        number = distance[t % 5]  # get a distance

    show(number, n)
    print(n, t)

    time.sleep(0.05)