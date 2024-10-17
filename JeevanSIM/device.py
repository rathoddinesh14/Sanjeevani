import random
import time

class Device:
    def __init__(self, device_id, patient_id):
        self.device_id = device_id
        self.patient_id = patient_id

    def generate_vital_data(self, simulate_abnormal=False):
        
        # Normal vital ranges
        heart_rate = random.randint(60, 100)
        systolic_bp = random.randint(110, 140)
        diastolic_bp = random.randint(70, 90)
        oxygen_level = random.randint(95, 100)

        # Inject abnormal vitals if simulate_abnormal is True
        if simulate_abnormal:
            if random.random() < 0.5:  # 50% chance to simulate abnormal heart rate or oxygen level
                heart_rate = random.randint(121, 150)  # Abnormal heart rate (>120 bpm)
            if random.random() < 0.5:
                oxygen_level = random.randint(80, 89)  # Abnormal oxygen level (<90%)

        return {
            "device_id": self.device_id,
            "patient_id": self.patient_id,
            "heart_rate": heart_rate,
            "blood_pressure": {
                "systolic": systolic_bp,
                "diastolic": diastolic_bp
            },
            "oxygen_level": oxygen_level,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }