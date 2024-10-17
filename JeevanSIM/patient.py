from faker import Faker
import random

fake = Faker()

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