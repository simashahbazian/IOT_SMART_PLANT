# services/mqtt_client.py

import paho.mqtt.client as mqtt 
from config.config import MQTT_BROKER, MQTT_PORT

client = mqtt.Client()

def connect_mqtt():
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

def publish(topic, payload):
    client.publish(topic, payload)
