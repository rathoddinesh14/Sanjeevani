from datasource import DataSourceDecorator;
from pymongo import MongoClient

class MongoDataSource(DataSourceDecorator):
    def __init__(self, source=None):
        super().__init__(source)

        # Connect to MongoDB server at localhost:27017
        try:
            self.client = MongoClient("localhost", 27017)
            self.db = self.client['mydatabase']
            self.collection = self.db['mycollection']
            print("Connected to MongoDB server on localhost:27017")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")

    def save(self, data):
        super().save(data)
        try:
            # Insert data into MongoDB collection
            self.collection.insert_one(data.data)
            print(f"Data saved to MongoDB: {data.data}")
        except Exception as e:
            print(f"Failed to save data to MongoDB: {e}")