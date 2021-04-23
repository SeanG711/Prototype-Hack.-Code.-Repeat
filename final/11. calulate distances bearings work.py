# import modules and libraries
import time
import math
# from math import atan2, degrees

LongCurrent = -118.100708
LatiCurrent = 34.140682
distance = [0, 0, 0, 0, 0]
bearing = [0, 0, 0, 0, 0]
a = [0, 0, 0, 0, 0]
c = [0, 0, 0, 0, 0]
e = [0, 0, 0, 0, 0]
f = [0, 0, 0, 0, 0]
g = [0, 0, 0, 0, 0]

t0 = [34.147195, -118.102073]  # Vons
t1 = [34.145869, -118.094245]  # Shell
t2 = [34.128910, -118.114172]  # HuntingtonLib
t3 = [34.127797, -118.147915]  # SouthCampus
t4 = [34.105209, -118.094296]  # SanGabGolfCourse

Lati_list = [t0[0], t1[0], t2[0], t3[0], t4[0]]
Long_list = [t0[1], t1[1], t2[1], t3[1], t4[1]]

R = 3958.8  # radious of earth in miles
Delta_lati = [0, 0, 0, 0, 0]
Delta_long = [0, 0, 0, 0, 0]

while True:

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

    print(bearing)

    time.sleep(0.05)