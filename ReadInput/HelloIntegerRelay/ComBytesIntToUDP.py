# This script read bytes to relay little endian integer to a udp target
# To find them in the chaos of the stream it look about 0000 in front of the four integer bytes.

import serial
import time
from collections import deque
import socket

# Open the serial port (adjust 'COM3' to your port name)
ser = serial.Serial('COM3', 9600, timeout=1)

ipv4="127.0.0.1"
port =3615


def send_udp_little_endian(value,ipv4,port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(value.to_bytes(4, byteorder='little'), (ipv4, port))
    s.close()


array_8_bytes= deque(maxlen=8)

try:
    while True:
        # Read one byte at a time
        byte = ser.read(1)
        array_8_bytes.append(byte)
        if(len(array_8_bytes)==8):
            # if the four first bytes are zero
            if (array_8_bytes[0]==b'\x00' and array_8_bytes[1]==b'\x00' and array_8_bytes[2]==b'\x00' and array_8_bytes[3]==b'\x00'):
                # convert the last four bytes to an integer
                value = int.from_bytes(array_8_bytes[4]+array_8_bytes[5]+array_8_bytes[6]+array_8_bytes[7], byteorder='little')
                print(value)
                # Send the value to the udp listener
                send_udp_little_endian(value,ipv4,port)
                
                array_8_bytes.clear()
            
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    # Close the serial connection when done
    ser.close()
