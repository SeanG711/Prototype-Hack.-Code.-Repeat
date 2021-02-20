# import modules
import board
import time
import neopixel
import touchio

# declare objects and variables
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
touchPin1 = touchin.TouchIn(board.A1)
touchPin2 = touchin.TouchIn(board.A2)
touchPin3 = touchin.TouchIn(board.A3)
touchPin4 = touchin.TouchIn(board.A4)
touchPin5 = touchin.TouchIn(board.A5)
touchPin6 = touchin.TouchIn(board.A6)
touchPin7 = touchin.TouchIn(board.A7)

touchPins = [touchPin1, touchPin2, touchPin3, touchPin4, touchPin5, touchPin6, touchPin7]
touchVals = [False, False, False, False, False, False, False]



COLOR = (0,100,100)
CLEAR = (0, 0, 0)


# repeat forever
while True:
    # capture touch input
    for x in range(7):
        touchVals[x] = touchPins[x].value


    # do output

    for x in range(7):
        if touchValss[x] == True
            pixels[x]. = COLOR
        else:
            pixels[x] = CLEAR



    time.sleep(0.25)