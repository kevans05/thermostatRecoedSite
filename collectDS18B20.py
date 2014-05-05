import time, urllib, os, glob, socket
from datetime import datetime

# function to read the temperature from ds18b20 temperature sensor on i2c
def read_temperature(valueX):
    tempfile = open(valueX)
    thetext = tempfile.read()
    tempfile.close()
    tempdata = thetext.split("\n")[1].split(" ")[9]
    temperature = float(tempdata[2:])
    temperature = temperature / 1000
    return round(temperature, 1)