import time
import json
from faker import Faker
from kafka import KafkaProducer
from patient import Patient
from device import Device
import logging

# Configure logging for better error visibility
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Faker to create fake data
fake = Faker()

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Adjust this to your Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # Serialize data to JSON
    key_serializer=lambda k: k.encode('utf-8')  # Serialize keys to UTF-8 strings
)

# Retry configuration
MAX_RETRIES = 5
INITIAL_RETRY_INTERVAL = 2  # Seconds (initial backoff time)


# Function to send data to Kafka
def send_data_to_kafka(device: Device, topic, simulate_abnormal, max_retries=MAX_RETRIES):
    attempt = 0
    retry_interval = INITIAL_RETRY_INTERVAL

    if device.device_failure():
        print(f"Device {device.device_id} is failing. Skipping data send.")
        return
    
    while attempt < max_retries:
        try:
            data = device.generate_vital_data(simulate_abnormal=simulate_abnormal)
            producer.send(topic, key=device.device_id, value=data)
            producer.flush()  # Send the message immediately
            print(f"Data sent from {device.device_id}: {data}")
            return  # Exit the function if successful
        except Exception as e:
            attempt += 1
            if attempt > max_retries:
                logger.error(f"Failed to send data from {device.device_id} after {attempt} attempts, Error: {e}")
                return
            else:
                logger.warning(f"Attempt {attempt}/{max_retries} failed. Retrying in {retry_interval} seconds. Error: {e}")
                time.sleep(retry_interval)
                retry_interval *= 2  # Exponential backoff


# Simulate multiple IoT devices for a single patient
def simulate_iot_devices(patient: Patient, topic, interval=1, abnormal_interval=10):
    iteration = 0
    while True:
        # Simulate abnormal vitals every `abnormal_interval` iterations
        simulate_abnormal = iteration % abnormal_interval == 0

        for device in patient.devices:
            send_data_to_kafka(device, topic, simulate_abnormal)
        time.sleep(interval)  # Sleep for `interval` seconds before sending next batch of data
        iteration += 1


# Create a patient and multiple devices
if __name__ == "__main__":
    patient = Patient()
    num_devices = 10  # Number of devices for the patient
    for i in range(num_devices):
        device_id = f'device_{i+1:03d}'
        device = Device(device_id, patient.id, failure_rate=0.1)
        patient.add_device(device)

    print(f"Patient {patient.name} (ID: {patient.id}) has devices: {[d.device_id for d in patient.devices]}")
    
    # Start the simulation with the created patient and devices
    simulate_iot_devices(patient, 'patient_vitals', interval=5, abnormal_interval=3)
