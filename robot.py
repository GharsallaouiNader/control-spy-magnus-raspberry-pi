#author : gharsallaoui nader & rami selmi
#comment : 
import os
from socket import * # fo socket
import RPi.GPIO as GPIO # to use gpio
import time 


def marche():
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12,True)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16,False)
    time.sleep(0.1)
    
    return
def back():
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12,False)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16,True)
    time.sleep(0.1)
    return
def left():
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18,True)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22,False)
    time.sleep(0.1)
    return
def right():
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22,True)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18,False)
    time.sleep(0.1)
    return
def auto(pin):  #not ready yet 
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12,True)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16,False)
    time.sleep(0.1)
    return

def stop():
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12,True)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16,True)
    GPIO.setup(18, GPIO.OUT)   
    GPIO.output(18,True)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22,True)
    time.sleep(0.1)
    return
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT) #set gpio 12,16,18,22 as outputs
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)


host = ""
port = 13000
buf = 1024
addr = (host, port) #address "" to get all socket from any ip address
UDPSock = socket(AF_INET, SOCK_DGRAM) #
UDPSock.bind(addr)
print "Waiting to receive messages..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print "Received message: " + data
    if data == "r":
        print "running"
        marche()
    if data == "s":
        print "stoped"
        stop()
    if data == "l":
        print "leftmove"
        left()
    if data == "i":
        print "rightmove"
        right()
    if data == "b":
        print "return back"
        back()
    
        
        
    if data == "exit":
       break
GPIO.cleanup()
UDPSock.close()
os._exit(0)
