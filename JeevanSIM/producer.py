import random
import time
import json
from faker import Faker
from kafka import KafkaProducer

# Initialize Faker to create fake data
fake = Faker()

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Adjust this to your Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # Serialize data to JSON
    key_serializer=lambda k: k.encode('utf-8')  # Serialize keys to UTF-8 strings
)

class Device:
    def __init__(self, device_id, patient_id):
        self.device_id = device_id
        self.patient_id = patient_id

    def generate_vital_data(self):
        return {
            "device_id": self.device_id,
            "patient_id": self.patient_id,
            "heart_rate": random.randint(60, 100),  # Random heart rate between 60 and 100 bpm
            "blood_pressure": {
                "systolic": random.randint(110, 140),
                "diastolic": random.randint(70, 90)
            },
            "oxygen_level": random.randint(95, 100),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }

class Patient:
    def __init__(self):
        self.id = fake.uuid4()  # Random UUID for patient ID
        self.name = fake.name()  # Random name
        self.age = random.randint(18, 90)  # Random age between 18 and 90
        self.gender = random.choice(["Male", "Female"])  # Random gender
        self.address = fake.address()  # Random address
        self.devices = []  # List to hold devices

    def add_device(self, device):
        self.devices.append(device)

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
    num_devices = 1  # Number of devices for the patient
    for i in range(num_devices):
        device_id = f'device_{i+1:03d}'
        device = Device(device_id, patient.id)
        patient.add_device(device)

    print(f"Patient {patient.name} (ID: {patient.id}) has devices: {[d.device_id for d in patient.devices]}")
    
    # Start the simulation with the created patient and devices
    simulate_iot_devices(patient, 'patient_vitals', interval=5)
