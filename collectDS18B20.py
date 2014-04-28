import time, urllib, os, glob, socket
from datetime import datetime


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def readsensor(input):
    tempfile = open(input, "r").read()
    thetext = tempfile.read()
    tempdata = thetext.split("\n")[1].split(" ")[9]
    temperature = float(tempdata[2:])
    temperature = temperature / 1000
    return temperature