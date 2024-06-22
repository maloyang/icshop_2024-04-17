import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(27), 1)

np[0] = (255, 255, 0)
np.write()