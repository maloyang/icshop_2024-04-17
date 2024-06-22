import machine, time
from machine import Pin

relay = Pin(23, Pin.OUT)
relay.on()
time.sleep_ms(500)

for i in range(10):
    if relay.value():
        relay.off()
    else:
        relay.on()
    time.sleep_ms(1000)