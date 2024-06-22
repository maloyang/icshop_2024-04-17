from machine import UART
import binascii, ubinascii
import struct

#uart1 = UART(1, baudrate=4800, bits=8, parity=None, stop=1, tx=4, rx=22, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=1000, timeout_char=2)
uart1 = UART(1, baudrate=4800, bits=8, parity=0, stop=1, tx=4, rx=22, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=1000, timeout_char=5)
for i in range(5):
    #data = uart1.readline() # NG, block
    data = uart1.read(100)
    if data is not None:
        print('data: ', data)
        #print('str: ', str(ubinascii.unhexlify(data)))
        #data_dec = binascii.hexlify(data).decode("ascii") #data.decode("utf-8")
        #print(data_dec)
        #print(bytes.fromhex(data_dec))
