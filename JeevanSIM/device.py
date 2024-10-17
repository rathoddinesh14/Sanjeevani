import random
import time

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