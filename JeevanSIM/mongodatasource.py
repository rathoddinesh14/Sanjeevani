from datasource import DataSourceDecorator;

class MongoDataSource(DataSourceDecorator):
    def save(self, data):
        super().save(data)
        print(f"Data saved to MongoDB: {data}")