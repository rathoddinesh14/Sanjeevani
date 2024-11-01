import time
from patient import Patient
from device import Device
from kafkadatasource import KafkaDataSource
from mongodatasource import MongoDataSource
from dataobj import DataObj

# Function to send data to Kafka
def send_data_to_kafka(ds, device: Device, topic, simulate_abnormal):
    if device.device_failure():
        print(f"Device {device.device_id} is failing. Skipping data send.")
        return

    try:
        data = device.generate_vital_data(simulate_abnormal=simulate_abnormal)
        # TODO send data to kafka datasource
        dataObj = DataObj(topic, device.device_id, data)
        ds.save(data)
        print(f"Data sent from {device.device_id}: {data}")
    except Exception as e:
        print(f"Failed to send data from {device.device_id}: {e}")


# Simulate multiple IoT devices for a single patient
def simulate_iot_devices(ds, patient: Patient, topic, interval=1, abnormal_interval=10):
    iteration = 0
    while True:
        # Simulate abnormal vitals every `abnormal_interval` iterations
        simulate_abnormal = iteration % abnormal_interval == 0

        for device in patient.devices:
            send_data_to_kafka(ds, device, topic, simulate_abnormal)
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
    
    kds = KafkaDataSource()
    mds = MongoDataSource(kds)

    # Start the simulation with the created patient and devices
    simulate_iot_devices(mds, patient, 'patient_vitals', interval=5, abnormal_interval=3)
