import time
import paho.mqtt.client as mqtt
from faker import Faker

# Configuration MQTT
MQTT_BROKER_URL = "mqtt.eclipseprojects.io"
MQTT_PUBLISH_TOPIC = "temperature"

# Initialisation du client MQTT
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect(MQTT_BROKER_URL)

# Initialisation de Faker pour générer des données aléatoires
fake = Faker()

# Boucle infinie pour publier des données
try:
    while True:
        temperature = fake.random_int(min=0, max=5)  # Température entre 0 et 5
        mqttc.publish(MQTT_PUBLISH_TOPIC, temperature)
        print(f"Published new temperature measurement: {temperature}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Arrêt du capteur...")
    mqttc.disconnect()
    
# This code is a simple MQTT client that publishes random temperature measurements to a specified topic.
# It uses the Paho MQTT library for communication and the Faker library to generate random temperature values.
# The code runs in an infinite loop, publishing a new temperature value every second until interrupted by the user.
# The temperature values are generated randomly between 0 and 5 degrees Celsius.
# To stop the sensor, the user can use a keyboard interrupt (Ctrl+C).