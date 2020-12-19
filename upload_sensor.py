# sudo - admin previledge to create a python script
# nano - editor
# upload_sensor.py - file name
# sudo nano upload_sensor.py (used to create a python script)

import paho.mqtt.client as mqtt
import time
import arduino

# upload the data to cloud
def upload_data_to_colab(moisture_value):
	print('Uploading Data to colab')
	print('Soil Moisture Value: ',moisture_value)
	client=mqtt.Client()
	client.connect('broker.hivemq.com',1883)
	client.publish('nitw/iot',moisture_value)
	print('Data Uploaded to Colab')

# read the data from sensor
def read_from_esp(): # static value
	#k=random.randint(200,1000) # random value
	k=arduino.read_sensor()
	print('Sensor Value from Arduino: ',k)
	return (k)

# main logic
while -5: # True
	m=read_from_esp()
	upload_data_to_colab(m)
	time.sleep(5)

