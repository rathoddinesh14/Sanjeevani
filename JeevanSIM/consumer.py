from kafka import KafkaConsumer
import json

# Initialize Kafka consumer
try:
    consumer = KafkaConsumer(
        'patient_vitals',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',  # Start reading from the beginning
        enable_auto_commit=True
    )
    print("Kafka Consumer initialized.")
except Exception as e:
    print(f"Error initializing Kafka Consumer: {e}")
    exit(1)

# Read and print messages from the topic
print("Reading data from Kafka topic:")
try:
    for message in consumer:
        data = message.value
        print(f'Received: {data}')
except Exception as e:
    print(f"Error consuming messages: {e}")
