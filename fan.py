#!/usr/bin/python

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
import re
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def measure_temp():
    raw = os.popen('vcgencmd measure_temp').readline()
    m = re.match("temp=(\d+\.?\d*)'C", raw)
    if not m:
        raise ValueError("Unexpected temperature string: " + raw)
    return float(m.group(1))

while True:
    temp = measure_temp()
    print 'Temperature from vcgencmd: {}'.format(temp)

    if temp > 45:
        print 'Turning ON GPIO 18!'
        GPIO.output(18, True)
    else:
        print 'Turning OFF GPIO 18!'
        GPIO.output(18, False)

    time.sleep(3)

