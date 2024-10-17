import time
import json
from faker import Faker
from kafka import KafkaProducer
from patient import Patient
from device import Device

# Initialize Faker to create fake data
fake = Faker()

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Adjust this to your Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # Serialize data to JSON
    key_serializer=lambda k: k.encode('utf-8')  # Serialize keys to UTF-8 strings
)


# Function to send data to Kafka
def send_data_to_kafka(device: Device, topic):
    try:
        data = device.generate_vital_data()
        producer.send(topic, key=device.device_id, value=data)
        producer.flush()  # Send the message immediately
        print(f"Data sent from {device.device_id}: {data}")
    except Exception as e:
        print(f"Failed to send data from {device.device_id}: {e}")


# Simulate multiple IoT devices for a single patient
def simulate_iot_devices(patient: Patient, topic, interval=1):
    while True:
        for device in patient.devices:
            send_data_to_kafka(device, topic)
        time.sleep(interval)  # Sleep for `interval` seconds before sending next batch of data


# Create a patient and multiple devices
if __name__ == "__main__":
    patient = Patient()
    num_devices = 10  # Number of devices for the patient
    for i in range(num_devices):
        device_id = f'device_{i+1:03d}'
        device = Device(device_id, patient.id)
        patient.add_device(device)

    print(f"Patient {patient.name} (ID: {patient.id}) has devices: {[d.device_id for d in patient.devices]}")
    
    # Start the simulation with the created patient and devices
    simulate_iot_devices(patient, 'patient_vitals', interval=5)
