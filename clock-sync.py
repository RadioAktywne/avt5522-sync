#!/usr/bin/python3

import time
import serial

#Serial port
serial_port = "/dev/ttyUSB0"

#baudrate
baud = 9600

#NMEA command template
tpl = "$GPRMC,%H%M%S,A,0000.00,N,00000.00,W,0.0,0.0,%d%m%y,004.2,W*70\r\n"

#create serial port object
tty = serial.Serial(serial_port,baud)


print("syncing with "+serial_port+"...")

#infinite loop

while True:
    #get current GMT date/time and convert to NMEA command
    nmea = time.strftime(tpl, time.gmtime())

    #send NMEA command to the clock
    tty.write(nmea.encode('ascii'))

    #print (only for debug)
    print(nmea)

    #wait (or leave when KeyboardInterrupt
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        break

#close serial port
print("closing "+serial_port)
tty.close()
