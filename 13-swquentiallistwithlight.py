# import modules
import board
import time
import neopixel

# declare objects and variables
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

# declare list of 10
# look up table
colors = [(0, 0, 255), (28, 0, 224),
        (56, 0, 196), (84, 0, 168),
        (112, 0, 140), (140, 0, 112),
        (168, 0, 84), (196, 0, 56),
        (224, 0, 28), (255, 0, 0)]

for x in range(len(pixels)):
    pixels[x] = colors[x]

pixels.show()

time.sleep(0.25)

# repeat forever
while True:
    # do calculations
    popColor = colors.pop(0)
    colors.append(popColor)
    # do output

    for x in range(len(pixels)):
        pixels[x] = colors[x]

    pixels.show()

    time.sleep(0.25)