__author__ = 'Kevans05'

import serial
import re

serial_pattern = r"T: (\d+\.\d*)\n";
serial_port = '/dev/ttyACM0';
serial_bauds = 9600;

def open_serial_port() :
  s = serial.Serial(serial_port, serial_bauds);
  line = s.readline();
  return s

def read_temperature(s):
  line = s.readline();
  m = re.match(serial_pattern, line);
  return float(m.group(1))


