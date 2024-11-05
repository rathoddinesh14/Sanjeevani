from datasource import DataSourceDecorator;
from kafka import KafkaProducer
import json

class KafkaDataSource(DataSourceDecorator):
    def __init__(self):
        super().__init__()
        try:
            # Initialize Kafka Producer
            self._producer = KafkaProducer(
                bootstrap_servers='localhost:9092',  # Adjust this to your Kafka broker address
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # Serialize data to JSON
                key_serializer=lambda k: k.encode('utf-8')  # Serialize keys to UTF-8 strings
            )
        except Exception as e:
            print(f"Failed to initialize Kafka Producer: {e}")
            self._producer = None

    def save(self, dataObj):
        if super() is not None:
            super().save(dataObj)
        if self._producer is None:
            print("Kafka Producer is not initialized. Skipping data save.")
            return
        self._producer.send(dataObj.topic, key=dataObj.device_id, value=dataObj.data)
        self._producer.flush()  # Send the message immediately
        print(f"Data saved to Kafka: {dataObj.data}")