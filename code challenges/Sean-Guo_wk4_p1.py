# Use all seven capacitive touch pads and NeoPixels
# to make a color picking machine

# import modules
import board
import time
import neopixel
import touchio

# declare objects and variables
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
touchPin1 = touchio.TouchIn(board.A1)
touchPin2 = touchio.TouchIn(board.A2)
touchPin3 = touchio.TouchIn(board.A3)
touchPin4 = touchio.TouchIn(board.A4)
touchPin5 = touchio.TouchIn(board.A5)
touchPin6 = touchio.TouchIn(board.A6)
touchPin7 = touchio.TouchIn(board.TX)

touchPins = [touchPin1, touchPin2, touchPin3, touchPin4,
            touchPin5, touchPin6, touchPin7]
touchVals = [False, False, False, False, False, False, False]
touchPin1Pre = False

# create a color variable and fill the pisels with the color
R = 64
G = 64
B = 64
color = [R, G, B]
COLOR = [0, 0, 0]
ledMode = 0
# increament value
i = 20

# repeat forever
while True:
    # gather input
    # see if A1 has changed
    for x in range(7):
        touchVals[x] = touchPins[x].value
    # print(touchVals)
    # see if A1 has changed
    if touchVals[0] != touchPin1Pre:
        # reset the previous value
        touchPin1Pre = touchVals[0]
        if touchVals[0]:
            ledMode += 1
            if ledMode > 1:
                ledMode = 0

        # else:
            # ledMode = 0

    print(ledMode)

    if ledMode == 1:

        # do calculation
        if touchVals[1]:
            R += i
            if R > 255:
                R = 255
        if touchVals[2]:
            R -= i
            if R < 0:
                R = 0
        if touchVals[3]:
            G += i
            if G > 255:
                G = 255
        if touchVals[4]:
            G -= i
            if G < 0:
                G = 0
        if touchVals[5]:
            B += i
            if B > 255:
                B = 255
        if touchVals[6]:
            B -= i
            if B < 0:
                B = 0
        # set new color value
        color = [R, G, B]
        pixels.fill(color)
        pixels.show()
    # fill empty
    else:
        pixels.fill(COLOR)
        pixels.show()
    print(R, G, B)

    time.sleep(0.2)


