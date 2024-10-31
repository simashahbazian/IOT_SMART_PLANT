# services/thingspeak_client.py

import requests
from config.config import THINGSPEAK_API_KEY, THINGSPEAK_URL

def send_to_thingspeak(temperature, humidity, moisture, light):
    payload = {
        'api_key': THINGSPEAK_API_KEY,
        'field1': temperature,
        'field2': humidity,
        'field3': moisture,
        'field4': light
    }
    response = requests.get(THINGSPEAK_URL, params=payload)
    if response.status_code == 200:
        print('Data successfully sent to ThingSpeak')
    else:
        print('Failed to send data to ThingSpeak')
