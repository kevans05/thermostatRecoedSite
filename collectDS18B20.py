import time, urllib, os, glob, socket
from datetime import datetime


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def readsensor(input):
    raw = open(input, "r").read()
    temperature = float(raw.split("t=")[-1])/1000
    return round(temperature, 1)
