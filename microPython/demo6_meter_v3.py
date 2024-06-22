from machine import UART
import binascii, ubinascii
import struct

#uart1 = UART(1, baudrate=4800, bits=8, parity=None, stop=1, tx=4, rx=22, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=1000, timeout_char=2)
# parity: N=None, Even=0, Odd=1
uart1 = UART(1, baudrate=4800, bits=8, parity=0, stop=1, tx=4, rx=22, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=1000, timeout_char=5)
for i in range(5):
    data = uart1.read(24)
    if data is not None:
        print('data: ', data)
        data_dec = binascii.hexlify(data).decode() #data.decode("utf-8")
        print(data_dec)