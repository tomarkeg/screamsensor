#!/usr/bin/env python3
########################################################################
# Filename    : SenseLED.py
# Description : Control led with infrared Motion sensor.
# Author      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import socket
from time import sleep
SERVER_IP = "192.168.68.115"
SERVER_PORT = 8888
msg = "hi"
msgsecond = "go"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (SERVER_IP,SERVER_PORT)
sock.connect(server_address)
ledPin = 12       # define ledPin
sensorPin = 11    # define sensorPin

def setup():
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)    # set ledPin to OUTPUT mode
    GPIO.setup(sensorPin, GPIO.IN)  # set sensorPin to INPUT mode

def loop():
    while True:
        if GPIO.input(sensorPin)==GPIO.HIGH:
            sock.sendall(msg.encode())
            GPIO.output(ledPin,GPIO.HIGH) # turn on led
            print ('led turned on >>>')
            sleep(1.5)
        else :
            sock.sendall(msgsecond.encode())
            GPIO.output(ledPin,GPIO.LOW) # turn off led
            print ('led turned off <<<')
            sleep(1.5)

def destroy():
    GPIO.cleanup()                     # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

