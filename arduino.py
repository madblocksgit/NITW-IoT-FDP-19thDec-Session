
# To read data from Arduino through Transceivers
import serial
import time

# create a serial object
ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

# Infinite Loop for debugging - done
def read_sensor():
	if(ser.inWaiting()>0):
		t=ser.readline()
		t=t.decode('utf-8') # default encoding standard in python
		t=t.split('#')[1]
		t=t[:-3] # ~,\r,\n
		print('Moisture Value from Sensor: ',t)
		return(t)

