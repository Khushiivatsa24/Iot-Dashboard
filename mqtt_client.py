from app import app
from extensions import db
from models import SensorReading
import paho.mqtt.client as mqtt
import json

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

def on_connect(client, userdata, flags, rc, properties):
    client.subscribe("sensor/data")
    print("Connected to MQTT broker")
    

def on_message(client, userdata, message):
    print("Message received!")
    data = json.loads(message.payload.decode())
    with app.app_context():
        new_reading = SensorReading(temp = data['temp'], humidity=data['humidity'])
        db.session.add(new_reading)
        db.session.commit()
    
   

client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883)
client.loop_forever()