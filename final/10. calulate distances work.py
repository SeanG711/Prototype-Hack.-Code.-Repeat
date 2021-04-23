# import modules and libraries
import time
import math

LongCurrent = -118.100708
LatiCurrent = 34.140682
distance = [0, 0, 0, 0, 0]
t0 = [34.147195, -118.102073]  # Vons
t1 = [34.145869, -118.094245]  # Shell
t2 = [34.128910, -118.114172]  # HuntingtonLib
t3 = [34.127797, -118.147915]  # SouthCampus
t4 = [34.105209, -118.094296]  # SanGabGolfCourse

Lati_list = [t0[0], t1[0], t2[0], t3[0], t4[0]]
Long_list = [t0[1], t1[1], t2[1], t3[1], t4[1]]

R = 6371  # radious of earth
Delta_lati = [0, 0, 0, 0, 0]
Delta_long = [0, 0, 0, 0, 0]
a = [0, 0, 0, 0, 0]
c = [0, 0, 0, 0, 0]


while True:
    # calculate distances
    for i in range(5):

        Delta_lati[i] = (Lati_list[i] - LatiCurrent)*math.pi/180
        Delta_long[i] = (Long_list[i] - LongCurrent)*math.pi/180

        a[i] = math.sin(Delta_lati[i]/2) * math.sin(Delta_lati[i]/2)
        + math.cos(LatiCurrent*math.pi/180) * math.cos(Lati_list[i]*math.pi/180) * math.sin(Delta_long[i]/2) * math.sin(Delta_long[i]/2)

        c[i] = 2 * math.atan2(math.sqrt(a[i]), math.sqrt(1-a[i]))

        distance[i] = R * c[i]

    print(distance)

    time.sleep(0.05)