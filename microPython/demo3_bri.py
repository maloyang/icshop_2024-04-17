import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(27), 1)

np[0] = (255, 255, 0)
np.write()

#-- show2
for i in range(10):
    for j in range(0, 200, 10):
        np[0] = (0, 0, j)
        np.write()
        time.sleep_ms(50)

    for j in range(200, 0, -10):
        np[0] = (0, 0, j)
        np.write()
        time.sleep_ms(50)

    np[0] = (0, 0, 0)
    np.write()
    time.sleep_ms(500)