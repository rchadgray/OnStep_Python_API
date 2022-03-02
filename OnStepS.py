import serial
import time

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)

port.write(b":Qe#\n")
time.sleep(10)

#rcv = port.read(10)
#print(rcv)

