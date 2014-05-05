__author__ = 'Kevans05'
#!/usr/bin/python3

from serial import Serial

def read_serial():
    ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
    ser.close()
    ser.open()
    if ser.isOpen():
        line = ser.readline()
        line = line.strip('*');
    else:
        line = 0
    return line