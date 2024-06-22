from machine import UART
import binascii, ubinascii
import struct

#uart1 = UART(1, baudrate=4800, rx=22) #no tx
#data = uart1.read(5)         # read up to 5 bytes

uart1 = UART(1, baudrate=4800, bits=8, parity=None, stop=1, tx=4, rx=22, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=5000, timeout_char=2)
for i in range(10):
    data = uart1.read(100)
    #print(data)
    if data is not None:
        print('data: ', data)
        #data_dec = binascii.hexlify(data).decode() #data.decode("utf-8")
        #print(data_dec)
        message=str(binascii.unhexlify(data), 'utf-8')
        print(message)        
