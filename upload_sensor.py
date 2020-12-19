# sudo - admin previledge to create a python script
# nano - editor
# upload_sensor.py - file name
# sudo nano upload_sensor.py (used to create a python script)

import urllib.request as u # used to invoke API Request of Thingspeak
import random
import time
import arduino

write_api='https://api.thingspeak.com/update?api_key=5STFKDRBBZF3JYQ0&field1='

# upload the data to cloud
def upload_data_to_thingspeak(moisture_value):
	print('Uploading Data to Thingspeak')
	print('Soil Moisture Value: ',moisture_value)
	a=u.urlopen(write_api+str(moisture_value))
	print(a)
	print('Data Uploaded to Thingspeak')

# read the data from sensor
def read_from_esp(): # static value
	#k=random.randint(200,1000) # random value
	k=arduino.read_sensor()
	print('Sensor Value from Arduino: ',k)
	return (k)

# main logic
while -5: # True
	m=read_from_esp()
	upload_data_to_thingspeak(m)
	time.sleep(5)

