import paho.mqtt.client as mqtt
import time

client=mqtt.Client()
client.connect('broker.hivemq.com',1883)
client.subscribe('nitw/iot')

def notification(client,userdata,msg):
  print(msg.payload)

client.on_message=notification
client.loop_forever()
