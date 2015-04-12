import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 11
ECHO = 13

while True: 
	print "distance mesurement in progress"
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(7,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)	
	GPIO.setup(18,GPIO.OUT)
	GPIO.setup(22,GPIO.OUT)
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.OUT)
	GPIO.output(TRIG, False)
	print "Waiting For Sensor to settle"
	time.sleep(0.1)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	print "Distance : ",distance, "cm"
	if distance < 10:
		print "obstacle"
		
		GPIO.output(12,False)

		
		GPIO.output(16,True) # move back

		
		GPIO.output(18,False)

		
		GPIO.output(22,False)
	
		GPIO.output(7,True) #alume red led to indicate obstacle
		time.sleep(1)
		GPIO.output(7,False)

		GPIO.output(16,False)
	GPIO.cleanup
