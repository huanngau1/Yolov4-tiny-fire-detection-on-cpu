import random
import time
import os
from paho.mqtt import client as mqtt_client


broker = 'test.mosquitto.org'
port = 1883
topic = "canhbao"
topic2 ='phanhoi'
#topic3 ="Image"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg1):
        print(f"Received `{msg1.payload.decode()}` from `{msg1.topic}` topic")	
    client.subscribe(topic2)
    client.on_message = on_message



def publish(client):
    #while True:
    #time.sleep(1)
    msg = 'chay'
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:print(f"Failed to send message to topic {topic}")

        
    #f=open("cam.jpg", "rb") #3.7kiB in same folder
    #fileContent = f.read()
    #byteArr = bytes(fileContent)


    #result1 = client.publish(topic3, byteArr)
    #status1 = result1[0]
    #if status1 == 0:
    #    print(f"Send anh to topic `{topic3}`")

client = connect_mqtt()
client.loop_start()
subscribe(client)
def run():
    publish(client)


