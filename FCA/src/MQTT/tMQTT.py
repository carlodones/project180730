import paho.mqtt.client as mqtt #import the client1
import time
import json
import paho.mqtt.client as mqtt

#with open('./FCA/src/MQTT/message.json') as data_file:
with open ('/usr/src/app/src/MQTT/message.json') as data_file:
    send_msg = json.load(data_file)

client = mqtt.Client("P1") #create new instance
client.connect("192.168.0.55") #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic")
client.publish('de/DAB_0001/@DATA', payload=json.dumps(send_msg), qos=2, retain=False)
time.sleep(4) # wait
client.loop_stop() #stop the loop

'''
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address="192.168.1.184"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")
time.sleep(4) # wait
client.loop_stop() #stop the loop
'''