import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(27), 1)

np[0] = (255, 255, 0)
np.write()

#-- show1
for i in range(10):
    for j in range(3):
        if j==0:
            np[0] = (100, 0, 0)
        elif j==1:
            np[0] = (0, 100, 0)
        elif j==2:
            np[0] = (0, 0, 100)
        np.write()
        time.sleep_ms(500)

